# Aggregators & Proxies

One integration, many upstreams — services that unify or resell access to other providers' APIs and data.

Every entry is live-probed like the rest of the directory: a maintainer confirmed the endpoint answered an x402 request correctly at review.

---

> ★ **Featured — October 2026: [x402-list](https://x402-list.com)**
> A directory built for the machine reading it: a no-auth REST feed and a hosted MCP server for finding and checking an endpoint before an agent pays, not after.

---

- [Cleared Gateway](https://clearedindex.com/.well-known/x402.json) — POST router that returns the best Cleared-verified x402 endpoint for a task (category + strategy). Free to call; pairs with Cleared Check / Witness. Settle-tape aware. Paid probe: https://clearedindex.com/api/x402/ping · Manifest: https://clearedindex.com/.well-known/x402

- [402Signal](https://402signal.com/route) — Fail-closed live-endpoint x402 router. POST /route returns a currently-alive x402 URL or an honest miss. Authorizes $0.003 USDC on Base, Solana, and Algorand; settles only when a live eligible route is found, so a typed miss is not charged. Example: POST {"need":"weather"}. ([OpenAPI](https://402signal.com/openapi.json)) ([MCP](https://402signal.com/mcp.json)) ([Manifest](https://402signal.com/.well-known/x402.json))

- [x402-list](https://x402-list.com) — Agent-first directory of x402-payable APIs with a no-auth machine-readable REST feed and a hosted MCP server for finding and verifying endpoints before an agent pays.
