#!/usr/bin/env python3
"""
extract_url.py -- decide WHICH url in a submission's description is the door.

WHY THIS IS A FILE AND NOT TWO LINES OF grep (2026-09-05)

The gate has now probed the wrong URL twice in three days, and both times it told a
stranger their service failed when their service was never touched:

  #183  a `Contact URL:` line matched on `url:`, so the gate probed the submitter's
        social profile.  Fixed the same day by anchoring the label to the start of
        the line.
  #185  no labelled line at all, so the fallback took the FIRST url anywhere in the
        body -- an inline markdown link to an npm package -- trailing `),` included.
        It probed `https://www.npmjs.com/package/@fractalai/x402-pqc-witness),`,
        got 403, and posted FAILED against a manifest that answers 402 on all seven
        of its endpoints.

Second sighting in the same place is a bug, not bad luck.  The real defect is that
"first url in the text" is not a rule -- it is a coin flip that happens to be right
when the description is short.  So the choice is ordered, and the log says which
tier fired, because a verdict that cannot say why it probed that address is not a
verdict.

THE ORDER
  1. a line that STARTS with `URL:` / `Endpoint:` / `Service:` / `Manifest:` / `API:`
     -- the submitter said it plainly, take them at their word
  2. any url containing `/.well-known/x402` -- CONTRIBUTING asks for exactly this:
     "the endpoint itself, or a /.well-known/x402 manifest that points at it"
  3. the first url that is not a package registry, code host or social profile --
     those are things ABOUT a service, never the payable door
  4. the first url, whatever it is -- a library or learning submission legitimately
     has nothing but a repo link, and tier 3 must not starve it

`Contact:` lines are never candidates at any tier.

Trailing punctuation is stripped, because a url written inside a sentence or a
markdown link carries the sentence home with it.

USAGE
    PR_BODY="..." python3 scripts/extract_url.py
prints the url on stdout, writes `url=` and `tier=` to $GITHUB_OUTPUT when set.
Exit 0 with empty output when there is no url at all -- the workflow decides what
that means, not this script.
"""

import os
import re
import sys

LABELS = r"(?:url|endpoint|service|manifest|api)"
LABEL_RE = re.compile(rf"(?im)^[ \t]*{LABELS}[ \t]*:[ \t]*(https?://\S+)")
URL_RE = re.compile(r"https?://[^\s\"'<>`\\]+")
CONTACT_LINE_RE = re.compile(r"(?i)^[ \t]*contact[ \t]*:")

# Hosts that describe a service but are never the thing an agent pays.
OFFSITE = (
    "npmjs.com", "pypi.org", "crates.io", "rubygems.org", "packagist.org",
    "hub.docker.com", "github.com", "gitlab.com", "bitbucket.org",
    "x.com", "twitter.com", "t.me", "discord.gg", "discord.com",
    "linkedin.com", "medium.com", "youtube.com", "youtu.be",
    "reddit.com", "notion.site", "docs.google.com",
)

TRAILING = ".,;:!?*_\"'`"


def trim(url: str) -> str:
    """Strip the sentence off the end of a url without eating a real path."""
    while url:
        last = url[-1]
        if last in TRAILING:
            url = url[:-1]
        elif last in ")]}":
            opener = {")": "(", "]": "[", "}": "{"}[last]
            # Keep it only if this url opened one itself -- markdown link
            # closers never do, real parenthesised paths do.
            if url.count(opener) >= url.count(last):
                break
            url = url[:-1]
        else:
            break
    return url


def host(url: str) -> str:
    h = url.split("://", 1)[-1].split("/", 1)[0].split("@")[-1].split(":")[0]
    return h.lower()


def is_offsite(url: str) -> bool:
    h = host(url)
    return any(h == d or h.endswith("." + d) for d in OFFSITE)


def pick(body: str):
    """Return (url, tier, why). Empty url when the body has none."""
    if not body:
        return "", 0, "PR body is empty"

    m = LABEL_RE.search(body)
    if m:
        return trim(m.group(1)), 1, "labelled line in the description"

    lines = [ln for ln in body.splitlines() if not CONTACT_LINE_RE.match(ln)]
    urls = [trim(u) for u in URL_RE.findall("\n".join(lines))]
    urls = [u for u in urls if u]
    if not urls:
        return "", 0, "no url found in the description"

    for u in urls:
        if "/.well-known/x402" in u:
            return u, 2, "x402 discovery manifest named in the description"

    for u in urls:
        if not is_offsite(u):
            return u, 3, "first url that is not a package, repo or social link"

    return urls[0], 4, "first url in the description"


def main() -> int:
    url, tier, why = pick(os.environ.get("PR_BODY", ""))
    print(f"[extract_url] tier {tier}: {why}")
    print(f"[extract_url] url: {url or '(none)'}")
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as fh:
            fh.write(f"url={url}\n")
            fh.write(f"tier={tier}\n")
            fh.write(f"why={why}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
