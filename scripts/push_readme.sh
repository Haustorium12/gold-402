#!/usr/bin/env bash
# Push README.md when two workflows write it at once.
#
# WHY THIS EXISTS. README.md has two independent writers — weekly-additions (the
# "New This Week" block) and readme-numbers (the count between the fence markers).
# They deliberately do NOT share a concurrency group: that was tried on 2026-09-03
# and was worse, because GitHub keeps one pending run per group and cancels the
# rest, and a cancelled run reports no failure while leaving the number stale.
# So the race is handled here, at the push, instead.
#
# THE DEFECT THIS REPLACES (2026-09-06). The old loop was:
#
#     for i in 1 2 3; do
#       git pull --rebase --autostash origin main && git push && exit 0
#       ...
#
# When the rebase CONFLICTS — which is what happens when both writers touch
# README.md — git stops mid-rebase and leaves unmerged files in the tree. The next
# iteration calls `git pull --rebase` again and git refuses instantly: "Pulling is
# not possible because you have unmerged files." Attempts 2 and 3 could never do
# anything. The loop advertised three retries and had one. Four merges landing
# inside thirty seconds on 2026-09-06 was enough to spend it, and Weekly Additions
# failed with the New This Week block a day stale.
#
# WHAT THIS DOES INSTEAD. It never rebases a stale diff. On a rejected push it
# throws its own commit away, resets to whatever origin/main now holds, and RE-RUNS
# THE GENERATOR against that new head. Both generators are deterministic functions
# of the shelf, so regenerating is the correct conflict resolution — the second
# answer is computed from the same source of truth the first one was, just newer.
# If the regenerated file is identical to what is already on origin, the other
# writer got there with the same answer and there is nothing left to do: exit 0,
# quietly, rather than inventing a failure.
#
# Proven against two staged races before shipping: one where both writers collide on
# the same line, one where they own different blocks. The old loop fails both; this
# one lands the block in the first and exits quietly in the second. It still fails
# closed — a generator that errors or an origin it cannot fetch exits 1 rather than
# reporting a push it did not make.
#
# Usage:  scripts/push_readme.sh "<generator command>" "<commit message>"
set -u

GEN="${1:?usage: push_readme.sh '<generator command>' '<commit message>'}"
MSG="${2:?usage: push_readme.sh '<generator command>' '<commit message>'}"
ATTEMPTS="${PUSH_README_ATTEMPTS:-5}"

for i in $(seq 1 "$ATTEMPTS"); do
  if git push; then
    exit 0
  fi
  echo "push rejected (attempt $i) -- rebuilding on top of origin/main"

  # A conflicted rebase left behind by anything earlier would poison every retry.
  git rebase --abort >/dev/null 2>&1 || true
  git merge --abort  >/dev/null 2>&1 || true

  git fetch origin main || { echo "::error::could not fetch origin/main"; exit 1; }
  git reset --hard origin/main

  eval "$GEN" || { echo "::error::generator failed while resolving the push race"; exit 1; }

  if git diff --quiet -- README.md; then
    echo "the other README writer already wrote this same answer -- nothing left to push"
    exit 0
  fi

  git add README.md
  git commit -m "$MSG"
  sleep $((i * 5))
done

echo "::error::could not push README after $ATTEMPTS attempts against a moving origin/main"
exit 1
