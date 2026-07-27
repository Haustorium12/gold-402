# gold-402

> The gold standard for x402 resources. Facilitators, SDKs, APIs, MCP servers, tools, and ecosystem data — curated by 24K Labs. No filler. No dead links. Updated weekly.

[![GitHub stars](https://img.shields.io/github/stars/Haustorium12/gold-402?style=social)](https://github.com/Haustorium12/gold-402)
[![Last Commit](https://img.shields.io/github/last-commit/Haustorium12/gold-402)](https://github.com/Haustorium12/gold-402/commits/main)
[![Curated by 24K Labs](https://img.shields.io/badge/Curated_by-24K_Labs-gold)](https://24klabs.ai)

The x402 ecosystem passed 50M transactions in March 2026. 300+ projects across 8 chains. 10,000%+ year-over-year growth. The community awesome-list accepts everything — that's its job.

gold-402 doesn't. Every entry in the README earned its place. The full catalog lives in [`directory/`](directory/).

This is the editorial layer: curated picks with context, backed by an exhaustive reference directory. Two layers, one repo.

---

## Featured This Month

> ★ **July 2026** — [**24K Labs Verification Report: Three-Quarters of the x402 Bazaar Is Dead**](articles/2026-07-verification-findings.md) by [24K Labs](https://24klabs.ai)

[![24K Featured](https://img.shields.io/badge/24K_Featured-2026--07-C0C0C0?style=plastic)](FEATURED.md)

We probed all 22,545 x402 services in the CDP Bazaar. 5,792 returned a valid 402 Payment Required response. The other 16,753 were gone, misconfigured, or unreachable — a 74% dead rate.

That number is the whole argument for a verified catalog. The Bazaar reflects everything ever listed; it cannot tell you what is running right now. This report can: the headline finding, a reproducible methodology, and the verified services framed as "the ones that actually work" — including real payer counts that no listing can fake. It is the most direct statement of what gold-402 is for.

[Read the full report →](articles/2026-07-verification-findings.md) · [Past features →](FEATURED.md)

---

## This Week in x402

_Week of July 20–26, 2026_

- **The x402 Foundation is live.** The Linux Foundation announced its operational launch on July 14, with 40 members and Coinbase's contribution of the protocol complete — 17 of them premier, including Adyen, AWS, American Express, Circle, Cloudflare, Coinbase, Fiserv, Google, Mastercard, MoonPay, Ripple, Shopify, the Solana and Stellar foundations, Stripe, and Visa. The standard now sits under open governance rather than one company's roadmap, and an executive-director search and a technical steering committee are underway. [[Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications)]
- **Ripple and MoonPay buy in.** Ripple joined with production data, not a pitch — more than 1M agentic transactions on the XRP Ledger and a June-shipped XRPL AI Starter Kit; MoonPay took a board seat. [[Genfinity](https://genfinity.io/2026/07/14/x402-foundation-launch-ripple-stellar-solana-quant-premier-members/)]
- **The numbers, unvarnished.** x402 moved about $24M across 75M transactions in the last 30 days — roughly 94k buyers, 22k sellers, an average payment near 32¢. That's the whole thesis: charges too small for a card network to touch, working as designed. It's also a fraction of what any premier member clears in a day. Both true. [[CoinDesk](https://www.coindesk.com/tech/2026/07/15/visa-mastercard-and-ripple-join-the-standard-letting-ai-agents-pay-in-stablecoins)]

---

<!-- NEW-THIS-WEEK:START -->
## New This Week

**This week** (Jul 27—Aug 2)

_No new listings yet._

**Last week** (Jul 20—26)

- **[Fabler Labs x402 Storefront](https://fablerlabs.com/x402/)** — Security and utility APIs for AI agents on Base, USDC per call, no signup: secret scan ($0.005), agent-config audit ($0.05), diff security gate ($0.10), pre-deploy evidence gate ($0.08), URL security evidence ($0.08), plus data and rendering endpoints and digital-product downloads; free machine-readable catalog at GET https://x402.fablerlabs.com/. Built and operated end-to-end by an autonomous AI agent.
- **[x402-seller](https://x402-seller-m8nx.onrender.com)** — Token rug/honeypot scoring combining GoPlus static analysis with live Honeypot.is sell simulation, liquidity-drain detection from a self-collected reserve time-series, and market data. EVM + Solana. $0.001-$0.05 USDC on Base. ([Track record](https://x402-seller-m8nx.onrender.com/track-record))
- **[Groundcheck](https://groundcheck.seiche.info)** — Claim grounding and delivery attestation for AI agents: machine-verified verdicts (supported/refuted/unverified) with confidence scores and cited sources, plus signed offline-verifiable receipts binding an x402 payment to what was delivered. Free single-claim tier; paid endpoints $0.005–$0.05 USDC on Base. ([OpenAPI](https://groundcheck.seiche.info/openapi.json)) ([npm](https://www.npmjs.com/package/groundcheck-mcp))
- **[Mart402](https://mart402.com)** — Web and PDF extraction for AI agents: URL-to-Markdown extraction, PDF parsing with dual-engine OCR consensus (hallucination detection, calibrated confidence, Japanese-strong), invoice field verification, schema-driven structured extraction, and JP company profiles. $0.001–$0.02 USDC on Base; free Sepolia sandbox at mart402.dev. ([Docs](https://mart402.com/agents.md)) ([GitHub](https://github.com/tanaka-77/mart402-agent-kit))
- **[Apiosk](https://apiosk.com)** — MCP gateway to discover, pay for, execute, and publish x402 APIs. Buyers settle per call over USDC/x402 or prepaid credits; providers publish paid routes that pay 98% of each call to their own wallet. Hosted at mcp.apiosk.com/mcp and listed in the official MCP Registry as io.github.obcraft/apiosk-mcp. USDC on Base. `npx @apiosk/mcp`. ([npm](https://www.npmjs.com/package/@apiosk/mcp)) ([PyPI](https://pypi.org/project/apiosk-mcp/)) ([GitHub](https://github.com/obcraft/apiosk-mcp))
- **[VirtualSMS](https://virtualsms.io/api/v1/x402/sms-verify)** — SMS verification and OTP receiving for AI agents: real carrier numbers across 145+ countries and 2500+ services, no account or API key. Also number rentals, matching-country proxies, and a hosted MCP server at mcp.virtualsms.io. USDC on Base, BNB Chain, and Solana.
- **[402Found](https://402found.dev)** — Marketplace of 18 specialized AI agent microservices: PII scrubbing, hallucination detection, prompt injection detection, format conversion, agent permission checks, and more. Each service is independently pay-per-request via x402 in USDC on Base.
- **[token-risk](https://token-risk.com)** — Deterministic structural risk reports for ERC-20 tokens and wallet addresses on Base via x402 USDC per request.
- **[Zugabot Code Agent](https://zugabot.ai/x402)** — AI developer services: code review, bug fix, test generation, docs, refactor, security audit, architecture review, full-repo audit. USDC on Base.
- **[Macro Pulse](https://macro-pulse-x402.onrender.com)** — Pay-per-call macroeconomic indicator API sourced from the World Bank (GDP growth, inflation, unemployment trend). Single-country lookup $0.02, 8-country flat-priced batch endpoint $0.05, 6-hour response caching. USDC on Base.
- **[Stelar Digital](https://api.stelardigital.com)** — Live crypto grid-trading telemetry (real P&L, not simulated), grid-parameter recommendations, market-regime classification, and sentiment scoring. 8 endpoints, $0.005-$2.50 USDC on Base. ([x402](https://api.stelardigital.com/.well-known/x402))
<!-- NEW-THIS-WEEK:END -->

---

## Contents

- [Featured This Month](#featured-this-month)
- [This Week in x402](#this-week-in-x402)
- [New This Week](#new-this-week)
- [Quick Start](#quick-start)
- [How x402 Works](#how-x402-works)
- [Facilitators](#facilitators)
- [SDKs & Libraries](#sdks--libraries)
- [MCP Servers](#mcp-servers)
- [APIs & Services](#apis--services)
- [Tools & Monitoring](#tools--monitoring)
- [Security & Compliance](#security--compliance)
- [Ecosystem & Wallets](#ecosystem--wallets)
- [Learning & Community](#learning--community)
- [Market Data](#market-data)
- [Need More?](#need-more)
- [Contributing](#contributing)

---

## Quick Start

> **New to x402?** Three steps to your first payment.

**1. Pick a facilitator**

| Use case | Facilitator |
|----------|-------------|
| Most chains, full SDK support | [Coinbase CDP](https://docs.cdp.coinbase.com/x402) |
| Edge deployment, global latency | [Cloudflare x402](https://developers.cloudflare.com/workers/examples/x402) |
| Enterprise billing + disputes | [Stripe Machine Payments](https://docs.stripe.com/payments/machine/x402) |

**2. Install the SDK**

```bash
# TypeScript
npm install @coinbase/x402-express

# Python
pip install x402

# Rust
cargo add x402
```

**3. Add payment middleware**

```typescript
import { paymentMiddleware } from '@coinbase/x402-express';

app.use(paymentMiddleware(wallet, {
  '/api/data': { price: '$0.01', network: 'base-mainnet' }
}));
```

That's it. The middleware returns 402 with payment details, verifies the client's payment header, and lets the request through.

[Full quickstart →](https://docs.cdp.coinbase.com/x402/quickstart-for-sellers) · [Testnet setup →](https://docs.cdp.coinbase.com/x402/network-support)

---

## How x402 Works

```
1. Client  →  GET /api/data                              (initial request)
2. Server  ←  402 Payment Required                       (payment details in header)
               X-Payment-Required: {amount, address, network}
3. Client  →  EIP-3009 gasless USDC transfer             (client signs + submits)
4. Client  →  GET /api/data  +  X-Payment: {signed tx}  (retry with payment)
5. Facilitator  →  verify + settle on-chain              (~2 seconds)
6. Server  ←  200 OK  +  X-Payment-Response              (resource returned)
```

No gas for the sender. No subscription. No API key. Payment IS authentication.

[Protocol spec →](https://github.com/coinbase/x402) · [EIP-3009 →](https://eips.ethereum.org/EIPS/eip-3009)

---

## Facilitators

Facilitators verify payment headers and settle transactions on-chain. Production deployments require one. Choose based on chains needed and where you're deploying.

| Facilitator | Chains | Description |
|-------------|--------|-------------|
| [Coinbase CDP](https://docs.cdp.coinbase.com/x402/facilitators) | Base, ETH, SOL, POL, XRPL, XLM, + | Official facilitator. Most chains, deepest SDK integration. Primary choice for production. |
| [Cloudflare x402](https://developers.cloudflare.com/workers/examples/x402) | Base, ETH | Edge-native. Zero cold start, global CDN distribution. Best for latency-sensitive APIs. |
| [Stripe Machine Payments](https://docs.stripe.com/payments/machine/x402) [![24K Featured](https://img.shields.io/badge/24K_Featured-2026--04-C0C0C0?style=plastic)](FEATURED.md) | Base | Enterprise billing infrastructure: dispute resolution, fraud detection, compliance tooling. |
| [Polygon x402](https://polygon.technology/payments/agentic-payments) | Polygon | Now leading Base in daily transaction count. MATIC fee subsidies for agentic payments. |
| [Stellar x402](https://docs.stellar.org/x402) | XLM | Fastest finality in the ecosystem. Added March 2026. |
| [AsterPay](https://asterpay.io) | Base, ETH | EU/MiCA-compliant facilitator for European enterprise deployments. |
| [Dexter DAO](https://github.com/Dexter-DAO/dexter-x402-sdk) | Base, ETH, SOL, + | Largest x402 facilitator by volume. Handles ~50% of daily transactions. Chain-agnostic v2 SDK with client, server, React hooks, and Express middleware. |
| [Ultravioleta DAO](https://facilitator.ultravioletadao.xyz) | EVM, SOL, NEAR, XLM, ALGO, SUI, + | Broadest multi-chain coverage in the ecosystem. 33+ networks including non-EVM chains. REST API with chain-specific settlement routing. |

[Full facilitator directory →](directory/facilitators.md)

---

## SDKs & Libraries

| SDK | Language | Description |
|-----|----------|-------------|
| [x402-typescript](https://github.com/coinbase/x402/tree/main/typescript) | TypeScript | Official SDK. Express, Hono, Next.js, Fastify middleware + `x402-fetch` client. The default choice. |
| [x402 Python](https://pypi.org/project/x402/) | Python | Official SDK. FastAPI middleware + async requests client. |
| [x402-rs](https://github.com/x402-rs/x402-rs) | Rust | Axum middleware + async runtime. Full EIP-3009 signing. |
| [ag402](https://github.com/AetherCore-Dev/ag402) | Go/Python | Multi-language. Wrap any API with `ag402 serve`, auto-pay with `ag402 run`. Solana USDC. |
| [x402-mcp](https://vercel.com/blog/introducing-x402-mcp-open-protocol-payments-for-mcp-tools) | TypeScript | Vercel AI SDK `paidTool` primitive. The cleanest path for AI SDK builders. |
| [MoltsPay](https://github.com/moltspay/molts-pay) | TypeScript | Multi-framework (Express, Hono, Fastify, Next.js). Base + Solana + ETH. Drop-in replacement. |
| [Mogami](https://mogami.tech) | Java | Production-ready Java x402 stack with SDK, server, console, and bundled MCP server. Fills the Java gap in the official ecosystem. |
| [Solana Foundation Pay](https://github.com/solana-foundation/pay) | TypeScript | Official Solana Foundation library for handling x402 and MPP payment challenges with user-authorized stablecoin signing. Updated May 2026. |

[Full SDK directory →](directory/sdks.md) · [Framework middleware →](directory/frameworks.md)

---

## MCP Servers

x402-native Model Context Protocol servers — AI agents pay per tool call, no API keys.

| MCP Server | Category | Description |
|-----------|----------|-------------|
| [agentsvc.io MCP](https://agentsvc.io/mcp) | General | 100+ curated MCP tools, x402-gated. The hub for AI agent tooling. |
| [x402-mcp](https://vercel.com/blog/introducing-x402-mcp-open-protocol-payments-for-mcp-tools) | SDK | Vercel AI SDK `paidTool` primitive — for building MCP tools that monetize via x402. |
| [IteraTools MCP](https://iteratools.ai/mcp) | Automation | Task automation via x402. Sequential and parallel workflow execution. |
| [EntRoute MCP](https://entroute.ai/mcp) | Data/Intelligence | Data intelligence and routing. Multi-chain analytics. |
| [ShieldAPI MCP](https://www.npmjs.com/package/shieldapi-mcp) | Security | 9 endpoints: breach check (900M+ HIBP hashes), URL safety, prompt injection detection. |
| [MoltGuard](https://api.moltrust.ch/guard/) | Trust | Agent trust scoring (0-100), Sybil detection, Ed25519 Verifiable Credentials. 7 MCP tools. |
| [ToolOracle](https://tooloracle.ai) | Discovery | Real-time discovery of x402-enabled tools across the ecosystem. Agents find tools, tools get paid. |
| [24K Labs Code Review MCP](https://24klabs.ai/mcp) | Dev Tools | AI code review + security audit via MCP. Pay per PR. Runs in CI or interactively. |
| [vindex-mcp](https://www.npmjs.com/package/vindex-mcp) | Data/Intelligence | Vehicle data over x402: VIN decode with warranty terms, recalls, reliability, and US/Canada purchase-cost estimates. USDC on Base. |
| [isocast-mcp](https://www.npmjs.com/package/isocast-mcp) | Data/Intelligence | Per-signal Polymarket weather-market data across 37 cities, with market URLs and live bucket odds. USDC on Base. |
| [moltalyzer-mcp](https://www.npmjs.com/package/moltalyzer-mcp) | Data/Intelligence | Polymarket and AI-agent-community intelligence: order-book movers, whale calibration, and multi-source digests. USDC on Base. |
| [fry-x402-mcp](https://github.com/Fry-Foundation/fry-x402-mcp) | DeFi | Catalog-generated MCP tools for fry.farm's 15 x402 endpoints: DeFi/DePIN data feeds plus unsigned-group builders signed by the agent's own wallet. USDC on Algorand. |

[Full MCP server directory →](directory/mcp-servers.md)

---

## APIs & Services

x402-payable APIs — pay per request, no subscriptions.

| Service | Pricing | Description |
|---------|---------|-------------|
| [24K Labs Code Review API](https://24klabs.ai/code-review) | $0.01-$3.00 | 6 AI code services: explain, debug, review, security audit, automation, MCP blueprint. USDC on Base. |
| [agentsvc.io](https://agentsvc.io) | Per-call | 100+ AI tools via a single x402-gated endpoint. One integration, full ecosystem access. |
| [Strale](https://strale.ai) | Per-token | LLM inference via x402. Pay per token, no subscription, no API key. |
| [AIsa](https://aisa.ai) | Per-call | AI + crypto data fusion. Highest x402 transaction count of any API service in the ecosystem. |
| [QuickNode RPC](https://quicknode.com) | Per-request | Pay-per-request RPC access to 130+ chains. No node management. |
| [Arch Tools](https://archtools.io) | Per-call | 27 on-chain tools. Portfolio analysis, NFT data, market intelligence on Base. |
| [ShieldAPI](https://shield.vainplex.dev) | $0.002–$0.05 | Security intelligence: breach check, domain reputation, URL safety, prompt injection detection. |
| [Valoria](https://x402.valoria.net) | — | Market intelligence: 90K+ indexed services, $148M+ tracked on-chain volume, revenue rankings. |
| [Firecrawl x402](https://api.firecrawl.dev/v1/x402/search) | Per-request | Web scraping and search API with x402-gated endpoints and automatic on-chain USDC settlement. Coinbase CDP case study service. |
| [JMT x402 Agent Tools](https://jmt-x402-proxy.jmthomasofficial.workers.dev) | $0.001-$0.15 | 25 endpoints: web search, AI analysis, crypto/stock data, SEC filings, company intel, news, sentiment, macro dashboard. USDC on Base. Local LLM-powered. |
| [Vindex](https://api.vindexapi.dev) | $0.01 | Vehicle-data API: VIN decode with factory warranty terms, recalls, known-issues/reliability, and US & Canada purchase-cost estimates. NHTSA and Transport Canada sources. USDC on Base. |
| [Isocast](https://api.isocast.dev) | From $0.01 | Per-signal Polymarket weather-market data across 37 cities. Fires when a city's daily-high temperature crosses into a new Polymarket bucket, returning the market URL and live bucket odds. USDC on Base. |
| [Moltalyzer](https://api.moltalyzer.xyz) | $0.01–$0.05 | Polymarket and AI-agent-community intelligence: order-book microstructure movers, whale hold-to-resolution calibration, and multi-source digests. USDC on Base. |
| [_done](https://underscoredone.com) | $0.01–$0.05 | Suite of x402 micropayment-gated utility APIs for AI agents (Web lookups, site analysis, data and more). Pay-per-call, no API keys or subscriptions — agents discover and pay per request via x402. Base + Solana mainnet payment support. |
| [Zugabot Code Agent](https://zugabot.ai/x402) | $0.10–$5.00 | AI developer services: code review, bug fix, test generation, docs, refactor, security audit, architecture review, full-repo audit. USDC on Base. |
| [fry.farm x402 Agentic Actions](https://fry.farm/x402/) | $0.001–$0.01 | DeFi/DePIN data and non-custodial transaction builders on Algorand mainnet: staking, LP farming, NFT mint, P2P offers. Builders return unsigned atomic groups signed by the agent's own wallet. USDC on Algorand. |
| [VirtualSMS](https://virtualsms.io/api/v1/x402/sms-verify) | From $0.05 | SMS verification and OTP receiving for AI agents: real carrier numbers across 145+ countries and 2500+ services, no account or API key. Also number rentals, matching-country proxies, and a hosted MCP server at mcp.virtualsms.io. USDC on Base, BNB Chain, and Solana. |

[Full API directory →](directory/apis.md)

---

## Tools & Monitoring

| Tool | Description |
|------|-------------|
| [x402-proxy](https://www.npmjs.com/package/x402-proxy) | `npx x402-proxy` — cURL for x402 APIs. Auto-pays 402 with USDC on Base and Solana. MCP stdio proxy. |
| [Paybound](https://github.com/pando-b/paybound) | Open-source governance proxy. Per-agent budgets, circuit breakers, SQLite audit trail. Drop-in `@x402/fetch` replacement. |
| [Sentinel/Valeo](https://sentinel.valeocash.com) | Enterprise audit layer. Budget enforcement, structured trails, real-time dashboard, public payment explorer. |
| [ScoutScore](https://scoutscore.ai) | Trust scoring for x402 services. Monitors 1,700+ services with continuous health checks. |
| [x402scan](https://x402scan.com) | Block explorer for x402 payments. Transaction search, payment requirement inspection, settlement status. |
| [24K Labs GitHub Action](https://github.com/Haustorium12/24klabs-action) | AI code review + security audit on every PR via x402 micropayments. Drop into any GitHub Actions workflow. |
| [Agent Forensics](https://www.npmjs.com/package/agent-forensics) | Claude Code cost observability. Analyzes JSONL session logs: per-model cost breakdown, cache efficiency, waste patterns. Free CLI. |
| [x402station](https://x402station.com) | Real-time monitoring and discovery for 20,000+ x402 endpoints. Continuous health probes every 10 minutes. MCP server for agent access included. |
| [AWS CloudFront x402 sample](https://github.com/aws-samples/sample-x402-content-monetization-with-cloudfront-and-waf) | AWS-published reference implementation for monetizing content behind CloudFront and WAF with x402 and USDC payments. |
| [LemonCake](https://lemoncake.xyz) | x402 gateway + agent funding rail. 402 challenge returns `accepts[]` with `buyUrl` (human) and `mintUrl` (machine). Off-session top-ups via Buyer Key (hard-capped per-mint/daily/monthly). Stripe Connect Direct Charge — custody-free. MCP server on npm. |
| [Agent Café](https://api.402.coffee/docs) | The trust layer for agent payments on Base. One live x402 endpoint, three services in real USDC: **certify** a paying agent (public certificate + badge that it pays correctly, refuses over-priced scams, and checks the recipient), **score** any wallet's payment risk 0–100 before you transact (`POST /score`; free `GET /verify`), and **escrow** x402 sales with automated on-chain arbitration. Every result is a fact observed on-chain. |

[Full tools directory →](directory/tools.md)

---

## Security & Compliance

| Service | Description |
|---------|-------------|
| [ShieldAPI](https://shield.vainplex.dev) | x402-native security API. Breach check (900M+ HIBP hashes), domain/IP reputation, prompt injection detection. |
| [KaelAi](https://kaelai.io) | Wallet trust scoring 0-100 across 10 chains. Vet incoming/outgoing payment wallets before serving requests. |
| [MoltGuard](https://api.moltrust.ch/guard/) | Agent trust scoring, Sybil detection with funding cluster analysis, Ed25519 Verifiable Credentials. |
| [Paybound](https://github.com/pando-b/paybound) | Governance proxy with circuit breakers and per-agent spending limits. MIT licensed. |
| [SENTINEL](https://mru-oracle.com) | AML/CFT compliance. 77K+ sanctions entities (OFAC, UN, EU, PEP, Interpol), 159-country jurisdiction risk scoring. |
| [PolicyLayer](https://policylayer.com) | Non-custodial spending controls. Daily limits, per-transaction caps, recipient whitelists — no private key custody. |

[Full security directory →](directory/security.md)

---

## Ecosystem & Wallets

| Project | Description |
|---------|-------------|
| [Coinbase Agentic Wallets](https://docs.cdp.coinbase.com/agentic-wallets) | Native CDP wallets purpose-built for AI agents. Launched April 2, 2026. The reference implementation. |
| [Cloudflare Agents SDK](https://developers.cloudflare.com/agents) | Edge-native agent deployment with x402 built in. v0.4.0 adds x402 v2 migration (March 2026). |
| [Agent.market](https://agent.market) | Official app store for AI agents. x402-powered transactions. Launched April 20, 2026. |
| [WorkProtocol](https://workprotocol.ai) | Structured work marketplace for agents and builders. Escrow-backed jobs, on-chain reputation. |
| [Nevermined + Visa](https://pinionnewswire.com/press-release/nevermineds-visa-intelligent-commerce-x402-integration-unlocks-agentic-commerce/) | AI agents get delegated credit card spending authority via Visa Intelligent Commerce + x402 (April 2026). |
| [World AgentKit](https://www.coindesk.com/tech/2026/03/17/sam-altman-s-world-teams-up-with-coinbase-to-prove-there-is-a-real-person-behind-every-ai-transaction) | WorldID biometric identity + x402. Prove a verified human is behind every agent transaction. 18M+ verified humans. |

[Full ecosystem directory →](directory/ecosystem.md)

---

## Learning & Community

### Get Started

- [5-Minute Quickstart](https://docs.cdp.coinbase.com/x402/quickstart-for-sellers) — Accept your first x402 payment.
- [x402 Protocol Spec](https://github.com/coinbase/x402) — Official open-source protocol by Coinbase.
- [Coinbase Developer Platform Docs](https://docs.cdp.coinbase.com/x402) — Complete implementation guide and API reference.
- [LearnAI x402 Course](https://www.uselearnai.com/course/x402-protocol) — Free, interactive, AI-guided. Covers the full payment flow, facilitator setup, and agent-to-agent payments.

### Essential Reading

- [24K Labs: x402 Explained](https://24klabs.ai/blog/x402-explained) — History and technical breakdown of HTTP 402.
- [AWS: x402 and Agentic Commerce](https://aws.amazon.com/blogs/industries/x402-and-agentic-commerce-redefining-autonomous-payments-in-financial-services/) — Full x402 stack with AgentCore + CloudFront + Lambda@Edge.
- [WorkOS: x402 vs Stripe MPP](https://workos.com/blog/x402-vs-stripe-mpp-how-to-choose-payment-infrastructure-for-ai-agents-and-mcp-tools-in-2026) — How to choose in 2026.
- [CoinDesk: Demand Still Unproven](https://www.coindesk.com/markets/2026/03/11/coinbase-backed-ai-payments-protocol-wants-to-fix-micropayment-but-demand-is-just-not-there-yet) — Honest March 2026 assessment. Worth reading.

### Community

- [x402 Foundation Discord](https://discord.gg/x402) — Official community. Protocol questions and announcements.
- [x402 Builders Telegram](https://t.me/x402builders) — Active developer chat.
- [GitHub Issues — coinbase/x402](https://github.com/coinbase/x402/issues) — Technical Q&A and bug reports.
- [Agent Economy Digest](https://agenteconomy.substack.com) — Weekly newsletter covering x402, MPP, A2A, and agentic commerce.

[Full learning directory →](directory/learning.md) · [Full community directory →](directory/community.md)

---

## Market Data

> April 2026 snapshot.

| Metric | Value |
|--------|-------|
| Cumulative Transactions | 50M+ |
| Annualized Volume | ~$600M |
| Ecosystem Market Cap | $815M |
| Total Projects | 300+ |
| Supported Chains | 8+ |
| Transaction Growth (YoY) | 10,000%+ |
| Foundation Members | 22+ |
| Settlement Speed | 2 seconds avg |

**Chain leaders:** Solana commanded up to 88% of transaction count by volume. Polygon now leads Base in daily transaction count. Base leads in cumulative value transferred (~$21.5M).

[Full market data →](directory/market-data.md) · [Live dashboard →](https://agenteconomy.to) · [On-chain analytics →](https://dune.com/x402)

---

## Need More?

The README is the curated magazine — handpicked entries with context and tags. The [`directory/`](directory/) folder is the exhaustive reference, with everything we know about across the x402 ecosystem.

- [Facilitators](directory/facilitators.md) — all hosted and self-hosted facilitators, hosted and self-hosted coverage tables.
- [SDKs & Libraries](directory/sdks.md) — all SDKs by language: TypeScript, Python, Rust, Go, and more.
- [Frameworks & Middleware](directory/frameworks.md) — server middleware for Express, Hono, Next.js, FastAPI, Axum, and Cloudflare Workers.
- [MCP Servers](directory/mcp-servers.md) — the full MCP ecosystem, organized by category.
- [APIs & Services](directory/apis.md) — all x402-payable API services: AI, data, infrastructure, and production deployments.
- [Tools & Utilities](directory/tools.md) — CLI tools, monitoring, analytics, spending controls, testing, and discovery.
- [Security & Compliance](directory/security.md) — audits, security tools, spending controls, trust scoring, and compliance.
- [Ecosystem & Wallets](directory/ecosystem.md) — agent wallets, frameworks, marketplaces, and infrastructure.
- [Learning Resources](directory/learning.md) — quickstarts, tutorials, articles, news, and migration guides.
- [Community](directory/community.md) — channels, newsletters, jobs, and events.
- [Market Data](directory/market-data.md) — on-chain analytics, dashboards, enterprise adoption, and growth timeline.

---

## Contributing

gold-402 is curated, not exhaustive. Every entry earns its place.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the curation standard, badge system, acceptance criteria, and submission process.

**Quick rules:**
- Entry must use the x402 protocol (HTTP 402 + X-Payment), not just USDC or general crypto payments.
- Live URL or public GitHub repo. Link must work.
- Last activity within 12 months (for libraries and resources without a live endpoint).
- One entry per pull request. Format: `[Name](url) — Description starting uppercase, ending with period.`
- Descriptions are factual. No marketing language.

---

<p align="center">
  <b>Curated by <a href="https://24klabs.ai">24K Labs</a></b><br>
  <sub>If this saved you time, star the repo.</sub><br><br>
  <a href="https://x402.org">x402.org</a> •
  <a href="https://github.com/coinbase/x402">Protocol Spec</a> •
  <a href="https://docs.cdp.coinbase.com/x402">Coinbase Docs</a> •
  <a href="https://discord.gg/x402">Discord</a> •
  <a href="https://agenteconomy.to">Live Dashboard</a>
</p>
