# Aggregators & Proxies

One integration, many upstreams — services that unify or resell access to other providers' APIs and data.

Every entry is live-probed like the rest of the directory: a maintainer confirmed the endpoint answered an x402 request correctly at review.

---

> ★ **Featured — October 2026: [x402-list](https://x402-list.com)**
> A directory built for the machine reading it: a no-auth REST feed and a hosted MCP server for finding and checking an endpoint before an agent pays, not after.

---

- [Cleared Gateway](https://clearedindex.com/.well-known/x402.json) — POST router that returns the best Cleared-verified x402 endpoint for a task (category + strategy). Free to call; pairs with Cleared Check / Witness. Settle-tape aware. Paid probe: https://clearedindex.com/api/x402/ping · Manifest: https://clearedindex.com/.well-known/x402


- [x402-list](https://x402-list.com) — Agent-first directory of x402-payable APIs with a no-auth machine-readable REST feed and a hosted MCP server for finding and verifying endpoints before an agent pays.

- [Multi-ATS Jobs Feed](https://assetfactory-jobs-x402.sigrunner.workers.dev/) — Normalized job postings, per-company hiring-intent signals and compensation data unified across 10 applicant-tracking systems (Greenhouse, Lever, Ashby, SmartRecruiters, Workday, Recruitee, Workable, BambooHR, Breezy, Personio) from one integration with company-domain auto-detection; GET /jobs/search ($0.004), /hiring/signal ($0.003), /jobs/comp ($0.005), free /jobs/preview teaser, USDC on Base. Manifest: https://assetfactory-jobs-x402.sigrunner.workers.dev/.well-known/x402
