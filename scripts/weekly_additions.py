#!/usr/bin/env python3
# weekly_additions.py -- maintains the "New This Week" block in README.md.
#
# Two rolling lists only: entries merged in the current ISO week (Mon-Sun) and
# the previous ISO week. Nothing older, no archive, no separate posts.
#
# Stateless and self-rolling: recomputes both weeks from merge history every
# run, so the Monday roll needs no special logic -- the week math just moves.
#
# Source of truth: merged PRs that ADD a directory entry (a list item in
# directory/*.md or a table row in README.md). Merge date = PR merged_at (UTC).
#
# Usage:
#   GITHUB_TOKEN=... python scripts/weekly_additions.py [--print]
#     --print : render the block to stdout, do NOT touch README (dry run)
import argparse, datetime, glob, json, os, re, sys, urllib.request

EM = "\u2014"
REPO = os.environ.get("WEEKLY_REPO", "Haustorium12/gold-402")
START, END = "<!-- NEW-THIS-WEEK:START -->", "<!-- NEW-THIS-WEEK:END -->"
BADGE = re.compile(r"\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)")
LINK = re.compile(r"\[([^\]]+)\]\((\S+?)\)")

def api(path, token):
    req = urllib.request.Request("https://api.github.com" + path,
        headers={"User-Agent": "24KLabs-weekly/1.0",
                 "Accept": "application/vnd.github+json",
                 "Authorization": "Bearer " + token})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def parse_added(line):
    t = BADGE.sub("", line.lstrip("+").strip())
    m = LINK.search(t)
    if not m:
        return None
    name, url = m.group(1).strip(), m.group(2).strip()
    rest = t[m.end():]
    desc = ""
    if t.startswith("-"):
        d = rest.split(EM, 1)
        desc = d[1] if len(d) > 1 else ""
    elif t.startswith("|"):
        cells = [c.strip() for c in t.strip().strip("|").split("|")]
        cand = [c for c in cells if url not in c and c]
        if cand:
            desc = max(cand, key=len)
            if EM in desc:
                desc = desc.split(EM, 1)[-1]
        else:
            d = rest.split(EM, 1)
            desc = d[1] if len(d) > 1 else ""
    else:
        return None
    desc = re.sub(r"\s+", " ", desc).strip().strip("|").strip()
    return name, url, desc

def shelf_now():
    """The shelf as it stands, keyed by URL.

    WHY: entries_for_pr() reads the PR's *patch* -- the line as submitted. Any
    editorial correction made after the merge never reaches this block, so the
    README can quote one number while the shelf beside it quotes another.
    Happened 2026-09-03 with RGX: merged saying "19k+ entries", corrected to
    "16k+" (the submitter's own manifest) thirty seconds later, and the New
    This Week block went on saying 19k+ because it was reading the patch.
    Same class as the bug it sits next to: report live state, not a snapshot.
    """
    live = {}
    for f in sorted(glob.glob("directory/*.md")):
        for ln in open(f, encoding="utf-8"):
            if ln.startswith("- ["):
                e = parse_added(ln)
                if e:
                    live[e[1]] = e
    return live

def entries_for_pr(num, token):
    out = []
    for f in api("/repos/%s/pulls/%d/files" % (REPO, num), token):
        fn = f["filename"]
        if fn.startswith("directory/") or fn == "README.md":
            for ln in (f.get("patch") or "").splitlines():
                if ln.startswith("+") and not ln.startswith("+++"):
                    e = parse_added(ln)
                    if e:
                        out.append(e)
    return out

def monday_of(d):
    return d - datetime.timedelta(days=d.weekday())

def label(mon):
    sun = mon + datetime.timedelta(days=6)
    if mon.month == sun.month:
        return "%s%s%s" % (mon.strftime("%b %-d"), EM, sun.strftime("%-d"))
    return "%s%s%s" % (mon.strftime("%b %-d"), EM, sun.strftime("%b %-d"))

def build_block(token, today):
    cur_mon = monday_of(today)
    prev_mon = cur_mon - datetime.timedelta(days=7)
    buckets = {cur_mon: [], prev_mon: []}
    seen = set()
    live = shelf_now()
    closed = api("/repos/%s/pulls?state=closed&sort=updated&direction=desc&per_page=100" % REPO, token)
    merged = sorted([p for p in closed if p.get("merged_at")], key=lambda p: p["merged_at"])
    for p in merged:
        md = datetime.date.fromisoformat(p["merged_at"][:10])
        mon = monday_of(md)
        if mon not in buckets:
            continue
        for name, url, desc in entries_for_pr(p["number"], token):
            if url in seen:
                continue
            seen.add(url)
            # prefer the line as it stands on the shelf over the line as merged
            buckets[mon].append(live.get(url, (name, url, desc)))

    def render(mon, heading):
        rows = buckets[mon]
        head = "**%s** (%s)" % (heading, label(mon))
        if not rows:
            return head + "\n\n_No new listings yet._"
        lines = ["- **[%s](%s)**%s" % (n, u, (" " + EM + " " + d) if d else "") for n, u, d in rows]
        return head + "\n\n" + "\n".join(lines)

    body = "## New This Week\n\n" + render(cur_mon, "This week") + "\n\n" + render(prev_mon, "Last week") + "\n"
    return body

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--print", action="store_true", dest="dry")
    ap.add_argument("--readme", default="README.md")
    args = ap.parse_args()
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GHT")
    if not token:
        sys.exit("no token in GITHUB_TOKEN/GHT")
    today = datetime.date.today()
    block = build_block(token, today)
    if args.dry:
        sys.stdout.write(block + "\n")
        return
    txt = open(args.readme, encoding="utf-8").read()
    if START not in txt or END not in txt:
        sys.exit("markers not found in %s; place %s ... %s once, then this maintains it" % (args.readme, START, END))
    pre = txt.split(START)[0]
    post = txt.split(END, 1)[1]
    new = pre + START + "\n" + block + END + post
    if new != txt:
        open(args.readme, "w", encoding="utf-8").write(new)
        print("README updated")
    else:
        print("no change")

if __name__ == "__main__":
    main()
