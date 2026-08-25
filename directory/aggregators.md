# Aggregators & Proxies

One integration, many upstreams — services that unify or resell access to other providers' APIs and data.

Every entry is live-probed like the rest of the directory: a maintainer confirmed the endpoint answered an x402 request correctly at review.

---

- [Orders of Magnitude](https://x402-api-production-5133.up.railway.app/x402.json) — Unified pay-per-call access to 1,100+ public and utility API endpoints through one wallet. $0.003–$0.10 per call, machine-readable manifest at `/x402.json` (mirrored at `/.well-known/x402`). x402 v2, USDC on Base.

- [Cleared Gateway](https://clearedindex.com/api/cleared/gateway) — POST router that returns the best Cleared-verified x402 endpoint for a task (category + strategy). Free to call; pairs with Cleared Check / Witness. Settle-tape aware. Paid probe: https://clearedindex.com/api/x402/ping · Manifest: https://clearedindex.com/.well-known/x402
