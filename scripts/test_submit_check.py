#!/usr/bin/env python3
"""
test_submit_check.py -- probe_for_402's GET retry on a 405 or a 404.

PR #224 (MadeOnSol, 2026-09-19): a GET-only manifest, every declared endpoint
402-compliant on GET, failed this gate with 405 on every one, because the
probe only ever tried POST.

Issue #217 (Obol, 2026-09-23): a GET-only endpoint whose router answers a
wrong-verb POST with a plain 404, not 405 -- the 2026-09-19 fix didn't cover
it, so the submitter routed around the gate through an issue instead of a PR.
Extended the retry to 404 as well; see probe_for_402's own docstring for why
that can't turn a genuinely dead URL into a false pass.

Run before touching probe_for_402:
    python3 scripts/test_submit_check.py
"""

import http.server
import sys
import threading

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from submit_check import probe_for_402  # noqa: E402

PORT = 8931


class _Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_POST(self):
        if self.path == "/get-only-405":
            self.send_response(405)
        elif self.path in ("/get-only-404", "/dead"):
            self.send_response(404)
        elif self.path == "/post-normal":
            self.send_response(402)
        else:
            self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path in ("/get-only-405", "/get-only-404"):
            self.send_response(402)
        elif self.path == "/dead":
            self.send_response(404)
        else:
            self.send_response(405)
        self.end_headers()


CASES = [
    ("#224 MadeOnSol shape -- POST 405, GET 402: retry finds it", "/get-only-405", 402),
    ("#217 Obol shape -- POST 404, GET 402: retry finds it", "/get-only-404", 402),
    ("ordinary POST-only service -- 402 on first try, no retry needed", "/post-normal", 402),
    ("neither verb works -- POST 200 is not a 404/405, must NOT retry into a false pass",
     "/nothing", 200),
    ("genuinely dead URL -- POST 404 triggers the retry, GET is 404 too: still fails, no false pass",
     "/dead", 404),
]


def main() -> int:
    srv = http.server.HTTPServer(("127.0.0.1", PORT), _Handler)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        failures = 0
        for name, path, want_code in CASES:
            code, note = probe_for_402(f"http://127.0.0.1:{PORT}{path}")
            ok = code == want_code
            print(f"{'PASS' if ok else 'FAIL'}  {name}")
            if not ok:
                failures += 1
                print(f"      want {want_code}, got {code} ({note})")
        print(f"\n{len(CASES) - failures}/{len(CASES)} passed")
        return 1 if failures else 0
    finally:
        srv.shutdown()


if __name__ == "__main__":
    sys.exit(main())
