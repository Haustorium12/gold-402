# scripts/submit_check.py
# Gold-402: submission gate
# Called by the submit.yml GitHub Action when a PR is opened.
# Usage: python scripts/submit_check.py <url> [<example_request_body>]
# Exit 0 = pass (auto-merge). Exit 1 = fail (auto-close with reason).
# SSRF protection baked in -- private IPs are rejected before any request.
#
# Example request body (optional, single-line JSON): endpoints that validate
# request parameters BEFORE issuing the 402 challenge (e.g. OpenAI-compatible
# APIs) cannot answer an empty-body probe with 402. When the PR body includes
# an `Example: {...}` line, this script probes with that body instead of `{}`.

import ipaddress
import json
import os
import re
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT    = "Gold-402-Verifier/1.0 (https://24klabs.ai/gold-402)"
PROBE_TIMEOUT = 10

PRIVATE_RANGES = [
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("169.254.0.0/16"),
    ipaddress.ip_network("0.0.0.0/8"),
    ipaddress.ip_network("::1/128"),
    ipaddress.ip_network("fc00::/7"),
    ipaddress.ip_network("fe80::/10"),
]


def fail(reason):
    print(f"FAIL: {reason}")
    # Write result for GitHub Actions to pick up
    with open("submit_result.json", "w") as f:
        json.dump({"result": "fail", "reason": reason}, f)
    sys.exit(1)


def ok(reason):
    print(f"PASS: {reason}")
    with open("submit_result.json", "w") as f:
        json.dump({"result": "pass", "reason": reason}, f)
    sys.exit(0)


def is_private_ip(hostname):
    try:
        addr_info = socket.getaddrinfo(hostname, None)
        for _, _, _, _, sockaddr in addr_info:
            ip_str = sockaddr[0]
            ip_obj = ipaddress.ip_address(ip_str)
            for net in PRIVATE_RANGES:
                if ip_obj in net:
                    return True, ip_str
        return False, None
    except Exception as e:
        return True, str(e)


def check_already_listed(resource_url):
    """Return True if this exact endpoint URL is already in the curated
    directory (directory/*.md). Matches on host+path, not just host --
    same host with a different path = different service = not a duplicate.
    """
    try:
        parsed = urllib.parse.urlparse(resource_url)
        low_host = parsed.netloc.lower().lstrip("www.")
        low_path = parsed.path.lower().rstrip("/")
        md_url_re = re.compile(r"\((https?://[^)\s]+)\)")
        for name in os.listdir("directory"):
            if not name.endswith(".md"):
                continue
            with open(os.path.join("directory", name), "r", encoding="utf-8") as f:
                for m in md_url_re.finditer(f.read()):
                    sp = urllib.parse.urlparse(m.group(1))
                    if sp.netloc.lower().lstrip("www.") == low_host and \
                       sp.path.lower().rstrip("/") == low_path:
                        return True, name
        return False, None
    except Exception:
        return False, None


def main():
    if len(sys.argv) < 2:
        fail("no URL provided -- usage: python submit_check.py <url> [<example_request_body>]")

    url = sys.argv[1].strip()
    example_body = sys.argv[2].strip() if len(sys.argv) > 2 else ""
    print(f"[submit_check] Checking: {url}")

    # 1. URL format validation
    try:
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme not in ("http", "https"):
            fail(f"invalid scheme '{parsed.scheme}' -- only http/https allowed")
        if not parsed.netloc:
            fail("URL has no hostname")
        hostname = parsed.hostname
        if not hostname:
            fail("could not extract hostname from URL")
    except Exception as e:
        fail(f"URL parse error: {e}")

    # 2. SSRF check -- resolve hostname before any network request
    private, ip_addr = is_private_ip(hostname)
    if private:
        fail(f"SSRF blocked: {hostname} resolves to private/reserved IP ({ip_addr})")

    print(f"[submit_check] Hostname {hostname} resolves to public IP -- safe to probe")

    # 3. Check if already in CDP Bazaar (fast-track)
    listed, source = check_already_listed(url)
    if listed and source == "cdp-bazaar":
        print(f"[submit_check] Already in CDP Bazaar -- fast-track")
        # Still probe to confirm it's still live
    elif listed:
        fail(f"already listed in Gold-402 (source: {source})")

    # 4. Probe for 402
    probe_body = b"{}"
    if example_body:
        try:
            json.loads(example_body)
        except Exception as e:
            fail(f"invalid example request body in PR (must be valid JSON): {e}")
        probe_body = example_body.encode()
        print(f"[submit_check] Probing {url} with example request body...")
    else:
        print(f"[submit_check] Probing {url} for HTTP 402...")
    try:
        req = urllib.request.Request(
            url,
            data=probe_body,
            method="POST",
            headers={
                "User-Agent":   USER_AGENT,
                "Content-Type": "application/json",
                "Accept":       "application/json",
            },
        )
        try:
            urllib.request.urlopen(req, timeout=PROBE_TIMEOUT)
            fail("endpoint did not return HTTP 402 -- got 2xx response. "
                 "x402 endpoints must return 402 Payment Required on unauthenticated requests.")
        except urllib.error.HTTPError as e:
            if e.code == 402:
                ok("endpoint returned HTTP 402 -- x402 compliant")
            else:
                hint = ""
                if e.code in (400, 422):
                    hint = (" If your endpoint requires request parameters, add an "
                            "`Example: {...}` line to the PR body so the gate can "
                            "probe with a valid request.")
                fail(f"endpoint returned HTTP {e.code} instead of 402. "
                     f"x402 endpoints must return 402 on unauthenticated requests.{hint}")
    except urllib.error.URLError as e:
        fail(f"could not reach endpoint: {e.reason}")
    except Exception as e:
        if "timed out" in str(e).lower():
            fail(f"endpoint timed out after {PROBE_TIMEOUT}s -- "
                 f"ensure your service is reachable and returns 402 promptly")
        fail(f"probe error: {e}")


if __name__ == "__main__":
    main()
