#!/usr/bin/env python3
"""Post one notice in the Departures discussion category for each listing that moves to
DEPARTURES.md, and one reply when it moves back to its shelf.

    python scripts/departures_board.py --before <sha> --after <sha> [--dry-run] [--allow-many]

Forward-only: it reads the change between two commits and never looks at older lines.
Safe to re-run: a listing that already has a notice gets nothing new.
Refuses (exit 1) to post more than MAX_POSTS notices in one run unless --allow-many.
Needs GITHUB_TOKEN with discussions: write. Exit 0 = every post it owed was made.
"""
import argparse, json, os, re, subprocess, sys, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone

CATEGORY = "Departures"
MAX_POSTS = 10
OWNER_LOGINS = {"haustorium12"}          # lines we added ourselves get no @
UA = "gold-402-departures (+https://github.com/Haustorium12/gold-402)"
ENTRY = re.compile(r"^- \[([^\]]+)\]\((https?://[^)\s]+)\)")
API = "https://api.github.com"


def git(*args):
    """Fails loudly: a git read that silently returned "" once meant 'every listing departed'."""
    r = subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        sys.exit(f"REFUSED: git {' '.join(args[:2])} failed ({r.stderr.strip()[:200]}). Nothing posted.")
    return r.stdout


def listings(text):
    """url -> name for every listing line in a markdown file."""
    out = {}
    for line in (text or "").splitlines():
        m = ENTRY.match(line.strip())
        if m:
            out[m.group(2)] = m.group(1)
    return out


def shelf_urls(sha):
    urls = set()
    for path in git("ls-tree", "--name-only", sha, "directory/").split():
        if path.endswith(".md"):
            urls |= set(listings(git("show", f"{sha}:{path}")))
    return urls


def changes(before, after):
    """(departed, returned): lists of (name, url) newly in / newly out of DEPARTURES.md."""
    old = listings(git("show", f"{before}:DEPARTURES.md"))
    new = listings(git("show", f"{after}:DEPARTURES.md"))
    departed = [(n, u) for u, n in new.items() if u not in old]
    back = shelf_urls(after)
    returned = [(n, u) for u, n in old.items() if u not in new and u in back]
    return departed, returned


def gh(method, path, body=None):
    req = urllib.request.Request(API + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
                                          "Accept": "application/vnd.github+json", "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def gql(query, **variables):
    r = gh("POST", "/graphql", {"query": query, "variables": variables})
    if r.get("errors"):
        raise RuntimeError(r["errors"])
    return r["data"]


def first_pr(repo, needle):
    """(pr_dict or None, date) for the first commit that put `needle` on a shelf."""
    shas = git("log", "--reverse", "--format=%H %cs", "-S", needle, "--", "directory/").split("\n")
    if not shas or not shas[0].strip():
        return None, None
    sha, date = shas[0].split()
    try:
        prs = gh("GET", f"/repos/{repo}/commits/{sha}/pulls")
    except urllib.error.HTTPError:
        prs = []
    merged = [p for p in prs if p.get("merged_at")] or prs
    return (merged[0] if merged else None), date


def submitter(repo, name, url):
    """(pr_number, login, listed_date) of the PR that first listed this entry. By URL first;
    if that finds no PR (the URL was rebound later by a direct commit), by name AND host, so
    two listings that share a name on different hosts can never borrow each other's @."""
    p, date = first_pr(repo, url)
    if not p:
        u = urllib.parse.urlsplit(url)
        p2, date2 = first_pr(repo, f"[{name}]({u.scheme}://{u.netloc}")
        if p2:
            p, date = p2, date2
    if not p:
        return None, None, date
    login = p["user"]["login"]
    if login.lower() in OWNER_LOGINS or login.endswith("[bot]"):
        login = None
    return p["number"], login, (p.get("merged_at") or date)[:10]


class _NoFollow(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def look(url):
    """One plain check of the listed URL, GET then POST. Returns a short phrase."""
    seen = []
    for method in ("GET", "POST"):
        req = urllib.request.Request(url, method=method, data=b"{}" if method == "POST" else None,
                                     headers={"User-Agent": UA, "Content-Type": "application/json"})
        try:
            with urllib.request.build_opener(_NoFollow).open(req, timeout=10) as r:
                seen.append(str(r.status))
        except urllib.error.HTTPError as e:
            seen.append(str(e.code))
        except Exception as e:
            reason = str(getattr(e, "reason", e)).lower()
            if "timed out" in reason or isinstance(e, TimeoutError):
                return "the URL did not answer within 10 seconds"
            if "name or service" in reason or "nodename" in reason or "getaddrinfo" in reason:
                return "the address did not resolve"
            return "the connection to the URL failed"
    if seen[0] == seen[1]:
        return f"the URL answered {seen[0]} to GET and POST"
    return f"the URL answered {seen[0]} to GET and {seen[1]} to POST"


def board(repo):
    """(repo_id, category_id, {(title, url): (discussion_id, last_comment_body)})."""
    owner, name = repo.split("/")
    d = gql("""query($o:String!,$n:String!){repository(owner:$o,name:$n){id
      discussionCategories(first:50){nodes{id name}}}}""", o=owner, n=name)["repository"]
    cat = next((c["id"] for c in d["discussionCategories"]["nodes"] if c["name"] == CATEGORY), None)
    if not cat:
        sys.exit(f"REFUSED: no '{CATEGORY}' discussion category on {repo}. Nothing posted.")
    posts, after = {}, None
    while True:
        page = gql("""query($o:String!,$n:String!,$c:ID!,$a:String){repository(owner:$o,name:$n){
          discussions(first:100,after:$a,categoryId:$c){pageInfo{hasNextPage endCursor}
          nodes{id title body comments(last:1){nodes{body}}}}}}""",
                   o=owner, n=name, c=cat, a=after)["repository"]["discussions"]
        for x in page["nodes"]:
            m = re.search(r"`(https?://[^`\s]+)`", x["body"])
            last = (x["comments"]["nodes"] or [{"body": ""}])[0]["body"]
            posts[(x["title"], m.group(1) if m else "")] = (x["id"], last)
        if not page["pageInfo"]["hasNextPage"]:
            return d["id"], cat, posts
        after = page["pageInfo"]["endCursor"]


def notice(name, url, pr, login, listed, departed, saw):
    who = ", ".join(x for x in (f"#{pr}" if pr else None, f"@{login}" if login else None) if x)
    listed_line = f"Listed {listed}" + (f" ({who})" if who else "") if listed else "Listed"
    return (f"**{name}**\n`{url}`\n{listed_line}. Departed {departed}: {saw}.\n"
            f"It comes back the night it answers a 402 again.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--before", required=True)
    ap.add_argument("--after", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--allow-many", action="store_true")
    a = ap.parse_args()
    repo = os.environ.get("GITHUB_REPOSITORY", "Haustorium12/gold-402")
    if not re.fullmatch(r"[0-9a-f]{7,40}", a.before) or set(a.before) == {"0"}:
        sys.exit(f"REFUSED: no usable 'before' commit ({a.before!r}); forward-only, nothing posted.")
    departed, returned = changes(a.before, a.after)
    today = git("show", "-s", "--format=%cs", a.after).strip() or datetime.now(timezone.utc).date().isoformat()
    print(f"{len(departed)} departed, {len(returned)} returned between {a.before[:7]} and {a.after[:7]}")
    if not departed and not returned:
        return
    repo_id, cat, posts = board(repo)
    owed = []
    for name, url in departed:                    # idempotency first, so a re-run owes nothing
        old = posts.get((name, url))
        if old and not old[1].startswith("Back on the shelf"):
            print(f"skip (notice exists): {name}")
        else:
            owed.append((name, url, old))
    if len(owed) > MAX_POSTS and not a.allow_many:
        sys.exit(f"REFUSED: {len(owed)} departure notices owed in one change (limit {MAX_POSTS}). "
                 "A person re-runs with allow_many if this is real. Nothing posted.")
    made = []
    for name, url, old in owed:
        saw = look(url)
        if old:                                   # it came back once and left again
            body, act = f"Departed again {today}: {saw}.", "reply"
        else:
            pr, login, listed = submitter(repo, name, url)
            body, act = notice(name, url, pr, login, listed, today, saw), "post"
        made.append((act, name, body))
        if a.dry_run:
            continue
        if act == "post":
            gql("""mutation($r:ID!,$c:ID!,$t:String!,$b:String!){createDiscussion(input:
              {repositoryId:$r,categoryId:$c,title:$t,body:$b}){discussion{url}}}""",
                r=repo_id, c=cat, t=name, b=body)
        else:
            gql("""mutation($d:ID!,$b:String!){addDiscussionComment(input:{discussionId:$d,body:$b})
              {comment{url}}}""", d=old[0], b=body)
    for name, url in returned:
        old = posts.get((name, url))
        if not old or old[1].startswith("Back on the shelf"):
            print(f"skip (no notice, or already marked back): {name}")
            continue
        body = f"Back on the shelf {today}."
        made.append(("reply", name, body))
        if not a.dry_run:
            gql("""mutation($d:ID!,$b:String!){addDiscussionComment(input:{discussionId:$d,body:$b})
              {comment{url}}}""", d=old[0], b=body)
    for act, name, body in made:
        print(f"--- {'WOULD ' if a.dry_run else ''}{act}: {name}\n{body}")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(f"Departures board: {len(made)} action(s)\n\n" +
                     "".join(f"- {act}: {name}\n" for act, name, _ in made))


if __name__ == "__main__":
    main()
