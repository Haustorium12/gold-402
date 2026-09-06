# scripts/submit_check.py
# Gold-402: submission gate
# Called by the submit.yml GitHub Action when a PR is opened.
# Usage: python scripts/submit_check.py <url> [<example_request_body>] [<mode>]
# Exit 0 = pass. Exit 1 = fail (labelled needs-work; never auto-closed).
#
# TWO MODES, because CONTRIBUTING.md has always had two acceptance rules and
# this script only ever implemented one (fixed 2026-09-05, found on PR #183):
#
#   service  (default) -- an API, MCP server, facilitator, anything with a live
#                         payable endpoint. Must answer HTTP 402. POST probe.
#   resource            -- a library, framework, or learning/community resource
#                         with no payable endpoint of its own. Must be publicly
#                         reachable. GET probe, 2xx/3xx passes, 402 is NOT
#                         required and is not expected.
#
# A MANIFEST IS A DOOR TOO (added 2026-09-05, found on PR #185)
# CONTRIBUTING.md says it twice -- acceptance is "a valid HTTP 402 challenge ...
# or serves a valid x402 manifest", and the ask is "the endpoint itself, or a
# /.well-known/x402 manifest that points at it". This script only implemented the
# first half, so a submitter who gave us the manifest we asked for was told their
# service returned 2xx instead of 402. Service mode now follows a manifest to the
# resources it declares and knocks one of THOSE for 402 -- the manifest is never
# taken on trust, it is only a map to the door.
#
# Mode is chosen by the workflow from the shelf files the PR touches, never by
# anything the submitter writes -- a submitter cannot talk their way into the
# looser mode, they can only put their entry on a shelf a human then reads.
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


def probe_for_402(url, probe_body=b"{}"):
    """POST once. Returns (status, note). status is an int code or None if the
    request never completed."""
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
        resp = urllib.request.urlopen(req, timeout=PROBE_TIMEOUT)
        return resp.getcode(), "2xx"
    except urllib.error.HTTPError as e:
        return e.code, "http error"
    except urllib.error.URLError as e:
        return None, str(e.reason)
    except Exception as e:
        return None, str(e)


def looks_like_manifest(url):
    return "/.well-known/x402" in urllib.parse.urlparse(url).path.lower()


def manifest_resources(url):
    """Fetch an x402 manifest and return the endpoint URLs it declares.
    Returns (urls, error). Never raises."""
    try:
        req = urllib.request.Request(
            url, method="GET",
            headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
        )
        raw = urllib.request.urlopen(req, timeout=PROBE_TIMEOUT).read()
    except urllib.error.HTTPError as e:
        return [], f"manifest returned HTTP {e.code}"
    except Exception as e:
        return [], f"could not fetch manifest: {e}"
    try:
        doc = json.loads(raw)
    except Exception as e:
        return [], f"manifest is not valid JSON: {e}"
    if not isinstance(doc, dict):
        return [], "manifest is not a JSON object"
    # EVERY SHAPE THAT IS ACTUALLY OUT THERE (widened 2026-09-05, same day it shipped).
    # The first version of this read only `resources: [{resource|url}]`. Knocking 329 live
    # x402 manifests that afternoon found that shape is a minority: the wild also uses
    # `resources: ["https://..."]`, `resources: ["POST /ask/haiku"]`, `endpoints:`,
    # `services:`, and a `baseUrl` that relative paths hang off. The narrow reader found a
    # door on 22 of them; this one finds 94 on the same set. Shipping the narrow version
    # would have failed a submitter whose manifest is perfectly valid and just not shaped
    # the way ours is -- which is the exact bug this whole function was added to fix.
    # Relative refs hang off the ORIGIN, not off the manifest's own path -- joining them
    # to ".../.well-known/x402" produces ".../.well-known/x402/ask/haiku", which 404s.
    _p = urllib.parse.urlparse(url)
    base = doc.get("baseUrl") or doc.get("base_url") or f"{_p.scheme}://{_p.netloc}"
    urls = []

    def add(ref):
        if not isinstance(ref, str) or not ref.strip():
            return
        ref = ref.strip()
        if " " in ref:                      # "POST /ask/haiku"
            verb, _, rest = ref.partition(" ")
            if verb.upper() in ("GET", "POST", "PUT", "PATCH", "DELETE"):
                ref = rest.strip()
        if ref.startswith(("http://", "https://")):
            urls.append(ref)
        else:
            urls.append(urllib.parse.urljoin(base.rstrip("/") + "/", ref.lstrip("/")))

    for key in ("resources", "endpoints", "services", "paths", "apis", "routes"):
        val = doc.get(key)
        if isinstance(val, list):
            for item in val:
                if isinstance(item, str):
                    add(item)
                elif isinstance(item, dict):
                    add(item.get("resource") or item.get("url")
                        or item.get("path") or item.get("endpoint"))
        elif isinstance(val, dict):
            for k, v in val.items():
                if isinstance(v, str):
                    add(v)
                elif isinstance(v, dict):
                    add(v.get("resource") or v.get("url") or v.get("path") or k)
    if isinstance(doc.get("resource"), str):
        add(doc["resource"])

    seen, uniq = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            uniq.append(u)
    if not uniq:
        return [], "manifest declares no resources"
    return uniq, None



def main():
    if len(sys.argv) < 2:
        fail("no URL provided -- usage: python submit_check.py <url> [<example_request_body>]")

    url = sys.argv[1].strip()
    example_body = sys.argv[2].strip() if len(sys.argv) > 2 else ""
    mode = (sys.argv[3].strip() if len(sys.argv) > 3 else "") or \
           os.environ.get("SUBMIT_MODE", "") or "service"
    if mode not in ("service", "resource"):
        fail(f"internal: unknown mode '{mode}' -- expected 'service' or 'resource'")
    print(f"[submit_check] Checking: {url}")
    print(f"[submit_check] Mode: {mode}")

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

    # 4a. Resource mode -- reachability, not payment.
    if mode == "resource":
        print(f"[submit_check] Probing {url} for a live public response (GET)...")
        try:
            req = urllib.request.Request(
                url,
                method="GET",
                headers={"User-Agent": USER_AGENT, "Accept": "*/*"},
            )
            try:
                resp = urllib.request.urlopen(req, timeout=PROBE_TIMEOUT)
                ok(f"resource is publicly reachable -- HTTP {resp.getcode()}. "
                   f"No 402 required for this shelf.")
            except urllib.error.HTTPError as e:
                if 300 <= e.code < 400:
                    ok(f"resource is publicly reachable -- HTTP {e.code} redirect. "
                       f"No 402 required for this shelf.")
                if e.code in (401, 403):
                    fail(f"resource returned HTTP {e.code} -- it is behind a login or "
                         f"otherwise not publicly accessible. CONTRIBUTING.md requires "
                         f"a resource to be reachable without an account.")
                fail(f"resource returned HTTP {e.code} -- not a live public page.")
        except urllib.error.URLError as e:
            fail(f"could not reach resource: {e.reason}")
        except Exception as e:
            if "timed out" in str(e).lower():
                fail(f"resource timed out after {PROBE_TIMEOUT}s")
            fail(f"probe error: {e}")

    # 4b0. Service mode, manifest form -- the URL we were given is a map, not the
    # door. Read it, then knock the doors it names. Each one gets its own SSRF
    # check: the manifest is a document a stranger controls.
    if looks_like_manifest(url):
        print(f"[submit_check] {url} is an x402 manifest -- reading the resources it declares")
        resources, err = manifest_resources(url)
        if err:
            fail(f"{err}. A manifest at /.well-known/x402 must be valid JSON "
                 f"declaring the endpoints it sells.")
        print(f"[submit_check] manifest declares {len(resources)} resource(s)")
        tried = []
        for r in resources[:5]:
            r_host = urllib.parse.urlparse(r).hostname
            if not r_host:
                continue
            private, ip_addr = is_private_ip(r_host)
            if private:
                print(f"[submit_check] skipping {r} -- resolves to private/reserved IP ({ip_addr})")
                continue
            print(f"[submit_check] knocking {r} for HTTP 402...")
            code, note = probe_for_402(r)
            tried.append(f"{r} -> {code if code else note}")
            if code == 402:
                ok(f"manifest at {url} declares {len(resources)} resource(s); "
                   f"{r} answered HTTP 402 -- x402 compliant")
        detail = "; ".join(tried) if tried else "no publicly resolvable resource in the manifest"
        fail(f"manifest at {url} is readable, but none of the endpoints it declares "
             f"answered HTTP 402 ({detail}).")

    # 4b. Service mode -- probe for 402
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
