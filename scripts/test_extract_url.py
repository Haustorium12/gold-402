#!/usr/bin/env python3
"""
test_extract_url.py -- the four real submissions that shaped extract_url.py.

Every fixture is a body a stranger actually sent us. Two of them are the ones the
gate got wrong. Run it before touching the picker:  python3 scripts/test_extract_url.py
"""

import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from extract_url import pick  # noqa: E402

CASES = [
    (
        "#183 Payfirst -- labelled line wins, and a Contact URL: line must not",
        "URL: https://www.payfirst.app/guides/x402-paid-links\n"
        "Category: Free learning resource (HTTP 200 expected).\n"
        "Contact URL: https://x.com/payfirst\n",
        "https://www.payfirst.app/guides/x402-paid-links",
        1,
    ),
    (
        "#175 x402-list -- lowercase label, Contact: line ignored",
        "Add x402-list to directory/aggregators.md.\n\n"
        "endpoint: https://x402-list.com/api/v1/suggestions\n"
        'Example: {"text":"x402-list directory submission"}\n\n'
        "Contact: inbox@cosimomiccol.is\n",
        "https://x402-list.com/api/v1/suggestions",
        1,
    ),
    (
        "#180 Preflight -- query string with & and %, kept whole",
        "## Verification\n\n"
        "URL: https://x402.chikocorp.com/api/x402/preflight/audit?resource_url=https%3A%2F%2Fx402.chikocorp.com&method=GET\n",
        "https://x402.chikocorp.com/api/x402/preflight/audit?resource_url=https%3A%2F%2Fx402.chikocorp.com&method=GET",
        1,
    ),
    (
        "#185 FractalAI -- no label; manifest beats the inline npm link",
        "Seven pay-per-call proof endpoints on Base (x402 v2).\n\n"
        "Also shipping [`@fractalai/x402-pqc-witness`](https://www.npmjs.com/package/@fractalai/x402-pqc-witness), "
        "which adds attestation to any resource server.\n\n"
        "Live discovery manifest: https://fractalai.net.co/.well-known/x402.json\n",
        "https://fractalai.net.co/.well-known/x402.json",
        2,
    ),
    (
        "no manifest, no label -- skip the npm link, take the service",
        "Ships as [pkg](https://www.npmjs.com/package/thing) and runs at https://pay.example.com/api/quote\n",
        "https://pay.example.com/api/quote",
        3,
    ),
    (
        "library submission -- a repo link is all there is, and that is fine",
        "An x402 middleware for Axum. Source: https://github.com/someone/axum-x402\n",
        "https://github.com/someone/axum-x402",
        4,
    ),
    (
        "empty body -- no url, no crash",
        "",
        "",
        0,
    ),
]


def main() -> int:
    failures = 0
    for name, body, want_url, want_tier in CASES:
        url, tier, why = pick(body)
        ok = url == want_url and tier == want_tier
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        if not ok:
            failures += 1
            print(f"      want tier {want_tier} {want_url!r}")
            print(f"      got  tier {tier} {url!r}  ({why})")
    print(f"\n{len(CASES) - failures}/{len(CASES)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
