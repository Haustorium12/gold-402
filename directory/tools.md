# Tools & Utilities

Development tools, CLI utilities, monitoring, analytics, and CI/CD integrations for x402 builders.

---

## CLI Tools

- [mcpc](https://github.com/apify/mcpc) — Universal CLI client for MCP by Apify. Supports persistent sessions, stdio/HTTP, OAuth, and x402 micropayments. The `curl` for MCP. 679★
- [portal-tunnel](https://github.com/gosuda/portal-tunnel) — Publishes localhost services to the agentic web through self-hostable, trustless tunnels with x402 payment gating. 260★
- [x402-payment-link](https://github.com/second-state/x402-payment-link) — Generate shareable x402 payment links. Pay-per-access URLs for content, APIs, and digital goods. 201★
- [tweazy](https://github.com/aaronjmars/tweazy) — Monetize AI applications and MCP servers using x402, CDP Smart Wallets, and Coinbase AgentKit. Quick scaffolding for payment-gated tools. 47★
- [x402-proxy](https://github.com/cascade-protocol/x402-proxy) — `curl` for x402 paid APIs. Auto-pays HTTP 402 with USDC on Base and Solana. MCP stdio proxy for AI agents. `npx x402-proxy`. ([npm](https://www.npmjs.com/package/x402-proxy))
- [ClawRouter](https://github.com/BlockRunAI/ClawRouter) — Agent-native LLM router. 41+ models, <1ms routing, USDC payments on Base and Solana via x402. "Payment IS authentication." Part of the OpenClaw ecosystem.
- [key0](https://github.com/key0ai/key0) — Commercial gateway for AI agents. Discover, pay for, and access APIs autonomously via x402. Exposes `/discover`, `/x402/access`, `/.well-known/agent.json`, `/.well-known/mcp.json`, `/llms.txt`.
- [World AgentKit](https://www.coindesk.com/tech/2026/03/17/sam-altman-s-world-teams-up-with-coinbase-to-prove-there-is-a-real-person-behind-every-ai-transaction) — Developer toolkit integrating World's WorldID biometric identity with x402. AI agents prove they act on behalf of a verified unique human. 18M+ verified humans.
- [Red Team Blue Team Agent Fabric](https://github.com/msaleme/red-team-blue-team-agent-fabric) — Security testing harness for autonomous AI agents with dedicated x402 endpoint testing. MCP, A2A, x402/L402 support. 342-test suite.

---

## GitHub Actions & CI/CD

- [24K Labs GitHub Action](https://github.com/Haustorium12/24klabs-action) — Automated AI code review on every PR. Runs explain, debug, review, and security audit via x402 micropayments. Drop into any GitHub Actions workflow.
- [Obol GitHub Actions CI/CD](https://api.obol.sh) — Obol generates GitHub Actions CI/CD pipelines via x402. $5 USDC per call on Base.

---

## Monitoring & Analytics

- [Sentinel/Valeo](https://sentinel.valeocash.com) — Enterprise audit and compliance layer for x402 payments. Budget enforcement (per-call, hourly, daily), structured audit trails, real-time dashboard, public payment explorer. SDK: [`@x402sentinel/x402`](https://npmjs.com/package/@x402sentinel/x402).
- [ScoutScore](https://scoutscore.ai) — Trust scoring infrastructure for x402 services. Monitors 1,700+ services with continuous health checks and fidelity probes. 4-pillar model: Contract Clarity, Availability, Response Fidelity, Identity & Safety. [npm SDK](https://www.npmjs.com/package/@scoutscore/sdk) [MCP Server](https://www.npmjs.com/package/@scoutscore/mcp-server)
- [x402scan Explorer](https://x402scan.com) — Blockchain explorer for x402 payments. Transaction search and verification, payment requirement inspection, settlement status tracking.
- [Agent Forensics](https://www.npmjs.com/package/agent-forensics) — Agent cost observability for Claude Code. Analyzes JSONL session logs: per-model cost breakdown, cache efficiency, waste patterns (model misallocation, debug loops, sub-agent sprawl). Free CLI: `npx agent-forensics analyze`. x402 API at $5/$15 tiers on Base.
- [Valoria](https://x402.valoria.net) — x402 market intelligence with revenue rankings, service analysis, pricing data across 90K+ indexed services and $148M+ in tracked on-chain volume.
- [x402station](https://x402station.com) — Real-time monitoring and discovery platform for 20,000+ x402 endpoints. Probes every 10 minutes, tracks health scores, uptime, and latency. MCP server for agent access included.
- [ToolMeter](https://snappedai.com/toolmeter/) — MCP/x402 seller-readiness tool with pricing metadata, `.well-known/x402`, OpenAPI, agent metadata, listing kit, and buyer-safety checks for paid endpoint launches.
- [agenteconomy.to](https://agenteconomy.to) — Real-time dashboard tracking agentic economy across x402, ERC-8004, ERC-8183, and MPP protocols on 8 chains. Refreshes every 6 hours.
- [Dune Analytics x402](https://dune.com/x402) — On-chain metrics: transaction volumes, chain-by-chain analytics, facilitator comparison, revenue/fee metrics.

---

## Spending Controls & Policy

- [Paybound](https://github.com/pando-b/paybound) — Open-source governance proxy for x402 agent payments. Per-agent budgets, circuit breakers, SQLite audit trail. Drop-in `@x402/fetch` replacement. MIT licensed.
- [PolicyLayer](https://policylayer.com) — Non-custodial spending controls for AI agents. Daily spending limits, per-transaction caps, recipient whitelists, rate limiting — without holding private keys.
- [ICME Labs](https://docs.icme.io) — Formal verification for AI agent actions. Natural language policies compile to SMT-LIB formal logic, checked by SMT solver. Wrapped in zero knowledge proofs for sub-1s verification. $0.10 USDC on Base.
- [PaySentry](https://github.com/mkmkkkkk/paysentry) — Control plane for AI agent payments. Spending limits, circuit breakers, anomaly detection, audit trails for x402. npm: `@paysentry/x402`.
- [x402 Notary](https://github.com/x402notary/notary) — Enterprise-grade audit and compliance platform for x402. Full visibility into agent spending, policy enforcement, cryptographic audit trails.
- [Decision Anchor](https://api.decision-anchor.com) — External accountability proof for agent payments and delegation. Records what was authorized, when, at what scope — before x402 payment execution.

---

## Testing & Development

- [x402-mock](https://pypi.org/project/x402-mock/) — Test/mock implementation of x402 for EVM blockchains. Dev/testing without live payments.
- [AWS CloudFront x402 content monetization sample](https://github.com/aws-samples/sample-x402-content-monetization-with-cloudfront-and-waf) — AWS-published reference implementation for monetizing content behind CloudFront and WAF using x402 and USDC payments. Published March 2026.
- [Base Sepolia Testnet](https://docs.base.org/docs/network-information) — Primary testnet for x402 development.
- [Base Sepolia USDC Faucet](https://faucet.circle.com/) — Get test USDC for development.
- [Base Sepolia Bridge](https://bridge.base.org/) — Bridge test ETH to Base Sepolia.
- [x402 FixSpec](https://github.com/am5188/x402-fixspec) — Deterministic endpoint conformance and remediation tool that inspects unpaid challenges, validates Base USDC requirements, probes discovery documents, and returns OpenAPI, Bazaar, and agent-instruction templates. [Live x402 offer](https://fixspec.am518.uk/buy/fixspec).

---

## Discovery & Search

- [x402 Service Discovery API](https://x402-discovery-api.onrender.com) — Enriched directory of 251+ x402-payable services. Trust signals, uptime, latency, health scores. Auto-scans x402.org/ecosystem every 6h. 6-tool MCP server.
- [x402 RouteNet](https://x402-routenet.onrender.com) — Smart routing layer for x402-enabled services. Selects optimal endpoint from 251+ services based on price, latency, health, or composite trust. Four strategies: `best`, `cheapest`, `fastest`, `most_trusted`.
- [OpenClaw Discovery Index](https://x402search.xyz) — x402-gated search engine for 13,000+ x402-enabled APIs indexed from CDP Bazaar. $0.01 USDC per search on Base.
- [AgentIndex](https://agentndx-production.up.railway.app) — Unified search across 15,000+ MCP services, A2A agents, and x402 APIs from 5 registries (Smithery, official MCP, GitHub, Bazaar, A2A). x402 paid search ($0.005), analyze ($0.05), trending ($0.10).
- [Cinderwright Discovery Hub](https://api.ideafactorylab.org) — x402 service search engine. 152+ services across 9 categories with daily crawling and health checks. Paid search, free submission, free stats. Built by a production autonomous AI agent.
- [BlockRun](https://blockrun.ai) — AI Gateway + Service Directory. 600+ x402 services indexed, trust scores, 31+ AI models via pay-per-use USDC.
- [x402search MCP](https://github.com/x402-index/x402search-mcp) — Search 14,000+ x402-enabled HTTP APIs. Also live as ACP agent on Virtuals Protocol (ID 22531). ([npm](https://www.npmjs.com/package/x402search-mcp)) ([PyPI](https://pypi.org/project/x402search-mcp/))
