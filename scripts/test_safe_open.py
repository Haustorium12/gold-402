#!/usr/bin/env python3
"""
test_safe_open.py -- the gate never connects to a private address, including by redirect.

submit_check.safe_open is the one door every probe goes through. It resolves a host once,
refuses unless every address is public, connects to the address it checked, and does the
same on each redirect hop. These tests prove that without touching anyone else's server:
two loopback addresses stand in for "a public host" and "somewhere private".

Needs 127.0.0.1 and 127.0.0.2 to both be loopback (Linux). Run:
    python3 scripts/test_safe_open.py
"""

import http.server
import sys
import threading
import urllib.error
import urllib.request

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import submit_check  # noqa: E402

P1, P2 = 8941, 8942
REAL_BLOCKED = submit_check._blocked_ip
HITS = {"second": 0, "loop": 0}


class _First(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        if self.path == "/to-second":
            self.send_response(302)
            self.send_header("Location", f"http://127.0.0.2:{P2}/secret")
        elif self.path == "/to-ftp":
            self.send_response(302)
            self.send_header("Location", "ftp://127.0.0.1/x")
        elif self.path == "/loop":
            HITS["loop"] += 1
            self.send_response(302)
            self.send_header("Location", "/loop")
        else:
            self.send_response(200)
        self.end_headers()


class _Second(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        HITS["second"] += 1
        self.send_response(200)
        self.end_headers()


def _open(url):
    return submit_check.safe_open(urllib.request.Request(url, method="GET"), timeout=5)


def _raises(url):
    try:
        _open(url)
    except (urllib.error.URLError, urllib.error.HTTPError, OSError) as e:
        return e
    return None


def main() -> int:
    s1 = http.server.HTTPServer(("127.0.0.1", P1), _First)
    try:
        s2 = http.server.HTTPServer(("127.0.0.2", P2), _Second)
    except OSError as e:
        print(f"SKIP  cannot bind 127.0.0.2 here ({e})")
        return 0
    for s in (s1, s2):
        threading.Thread(target=s.serve_forever, daemon=True).start()
    results = []

    def check(name, ok, detail=""):
        results.append(ok)
        print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"\n      {detail}" if detail and not ok else ""))

    try:
        # --- the real guard, unpatched ----------------------------------------
        submit_check._blocked_ip = REAL_BLOCKED
        e = _raises(f"http://127.0.0.1:{P1}/")
        check("a loopback address is refused outright", e is not None and "refused" in str(e), repr(e))
        e = _raises(f"http://localhost:{P1}/")
        check("a hostname that resolves to loopback is refused", e is not None and "refused" in str(e), repr(e))
        cases = [("::ffff:127.0.0.1", True), ("::1", True), ("169.254.169.254", True),
                 ("10.1.2.3", True), ("100.64.0.1", True), ("0.0.0.0", True),
                 ("8.8.8.8", False), ("2606:4700:4700::1111", False)]
        bad = [(ip, want) for ip, want in cases if REAL_BLOCKED(ip) != want]
        check("address classes: private/reserved/mapped blocked, public allowed", not bad, str(bad))

        # --- a redirect to somewhere private is not followed -------------------
        # 127.0.0.1 plays "the public host"; 127.0.0.2 plays "somewhere private".
        HITS["second"] = 0
        submit_check._blocked_ip = lambda ip: ip != "127.0.0.1"
        e = _raises(f"http://127.0.0.1:{P1}/to-second")
        check("redirect from an allowed host to a blocked address is refused",
              e is not None and "refused" in str(e), repr(e))
        check("...and the blocked server never saw a request", HITS["second"] == 0, f"hits={HITS['second']}")

        # --- control: the same redirect IS followed when both are allowed ------
        HITS["second"] = 0
        submit_check._blocked_ip = lambda ip: False
        try:
            code = _open(f"http://127.0.0.1:{P1}/to-second").getcode()
        except Exception as ex:
            code = repr(ex)
        check("control: with both allowed the redirect is followed (so the test can see it)",
              code == 200 and HITS["second"] == 1, f"code={code} hits={HITS['second']}")

        # --- other redirect limits --------------------------------------------
        e = _raises(f"http://127.0.0.1:{P1}/to-ftp")
        check("redirect to a non-http scheme is refused", e is not None, repr(e))
        HITS["loop"] = 0
        e = _raises(f"http://127.0.0.1:{P1}/loop")
        check("a redirect loop stops after a few hops", e is not None and HITS["loop"] <= 7,
              f"hits={HITS['loop']} err={e!r}")
        try:
            code = _open(f"http://127.0.0.1:{P1}/ok").getcode()
        except Exception as ex:
            code = repr(ex)
        check("an ordinary request still works", code == 200, str(code))
    finally:
        submit_check._blocked_ip = REAL_BLOCKED
        s1.shutdown()
        s2.shutdown()

    failures = results.count(False)
    print(f"\n{len(results) - failures}/{len(results)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
