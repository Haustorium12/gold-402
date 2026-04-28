# gold-402

> The gold standard for x402 resources. Facilitators, SDKs, APIs, MCP servers, tools, and ecosystem data — curated by 24K Labs. No filler. No dead links. Updated monthly.

[![GitHub stars](https://img.shields.io/github/stars/Haustorium12/gold-402?style=social)](https://github.com/Haustorium12/gold-402)
[![Last Commit](https://img.shields.io/github/last-commit/Haustorium12/gold-402)](https://github.com/Haustorium12/gold-402/commits/main)
[![x402 Projects](https://img.shields.io/badge/x402_projects-300%2B-D4AF37)](https://x402.org/ecosystem)
[![Curated by 24K Labs](https://img.shields.io/badge/Curated_by-24K_Labs-gold)](https://24klabs.ai)
[![Chains](https://img.shields.io/badge/Chains-8%2B-blue)](directory/facilitators.md)

The x402 ecosystem passed 50M transactions in March 2026. 300+ projects across 8 chains. 10,000%+ year-over-year growth. The community awesome-list accepts everything — that's its job.

gold-402 doesn't. Every entry in the README earned its place. The full catalog lives in [`directory/`](directory/).

This is the editorial layer: curated picks with context and badges, backed by an exhaustive reference directory. Two layers, one repo.

---

## Featured This Month

> ★ **April 2026** — [**Stripe x402 Machine Payments**](https://docs.stripe.com/payments/machine/x402) by [Stripe](https://stripe.com)

[![24K Featured](https://img.shields.io/badge/24K_Featured-2026--04-C0C0C0?style=plastic)](FEATURED.md) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier)

Stripe's Machine Payments launched in March 2026 on Base with USDC. No checkout UX, no redirects — an AI agent hits a 402, pays the signed EIP-3009 transfer, retries, and gets the resource. Stripe brings dispute resolution, fraud detection, and compliance tooling to the x402 primitive. Enterprise-grade infrastructure around a crypto-native payment rail.

[Read the full write-up →](FEATURED.md) · [Past features →](FEATURED.md)

---

## What's New

> **April 2026** — The month x402 became an open standard.

- [**Linux Foundation + 22 founding members**](https://www.prnewswire.com/news-releases/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol-302732803.html) — Coinbase contributed x402 to the Linux Foundation on April 2 ("4/02 Day") at the MCP Dev Summit in New York. Adyen, AWS, Cloudflare, Google, Mastercard, Microsoft, Shopify, Stripe, Visa among founding members.
- [**Coinbase Agentic Wallets**](https://docs.cdp.coinbase.com/agentic-wallets) — Native CDP wallets purpose-built for AI agents. Launched same day as Linux Foundation contribution.
- [**Cloudflare EmDash**](https://developers.cloudflare.com/emdash) — CMS with native x402 content monetization. Launched 4/02.
- [**Polygon overtakes Base**](https://etherworld.co/polygon-leads-base-in-x402-transactions/) — Polygon leads Base in daily x402 transaction count. Polygon Agentic Payments infrastructure now live.
- [**Nevermined + Visa Intelligent Commerce**](https://pinionnewswire.com/press-release/nevermineds-visa-intelligent-commerce-x402-integration-unlocks-agentic-commerce/) — AI agents can now spend delegated credit card authority via Visa + x402.
- [**KakaoPay joins Foundation**](https://cryptonews.net/news/blockchain/32658871/) — First South Korean payment processor in the x402 Foundation.
- [**Agent.market app store**](https://agent.market) — Official app store for AI agents launched April 20.

---

## Contents

- [Featured This Month](#featured-this-month)
- [What's New](#whats-new)
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
| [Coinbase CDP](https://docs.cdp.coinbase.com/x402/facilitators) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Base, ETH, SOL, POL, XRPL, XLM, + | Official facilitator. Most chains, deepest SDK integration. Primary choice for production. |
| [Cloudflare x402](https://developers.cloudflare.com/workers/examples/x402) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Base, ETH | Edge-native. Zero cold start, global CDN distribution. Best for latency-sensitive APIs. |
| [Stripe Machine Payments](https://docs.stripe.com/payments/machine/x402) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) [![24K Featured](https://img.shields.io/badge/24K_Featured-2026--04-C0C0C0?style=plastic)](FEATURED.md) | Base | Enterprise billing infrastructure: dispute resolution, fraud detection, compliance tooling. |
| [Polygon x402](https://polygon.technology/payments/agentic-payments) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Polygon | Now leading Base in daily transaction count. MATIC fee subsidies for agentic payments. |
| [Stellar x402](https://docs.stellar.org/x402) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | XLM | Fastest finality in the ecosystem. Added March 2026. |
| [AsterPay](https://asterpay.io) [![MiCA](https://img.shields.io/badge/MiCA-aware-blue?style=flat-square)](https://asterpay.io) [![ERC-8004](https://img.shields.io/badge/ERC--8004-registered-orange?style=flat-square)](https://asterpay.io) | Base, ETH | EU/MiCA-compliant facilitator for European enterprise deployments. |

[Full facilitator directory →](directory/facilitators.md)

---

## SDKs & Libraries

| SDK | Language | Description |
|-----|----------|-------------|
| [x402-typescript](https://github.com/coinbase/x402/tree/main/typescript) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | TypeScript | Official SDK. Express, Hono, Next.js, Fastify middleware + `x402-fetch` client. The default choice. |
| [x402 Python](https://pypi.org/project/x402/) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Python | Official SDK. FastAPI middleware + async requests client. |
| [x402-rs](https://github.com/x402-rs/x402-rs) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/x402-rs/x402-rs) | Rust | Axum middleware + async runtime. Full EIP-3009 signing. |
| [ag402](https://github.com/AetherCore-Dev/ag402) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/AetherCore-Dev/ag402) | Go/Python | Multi-language. Wrap any API with `ag402 serve`, auto-pay with `ag402 run`. Solana USDC. |
| [x402-mcp](https://vercel.com/blog/introducing-x402-mcp-open-protocol-payments-for-mcp-tools) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | TypeScript | Vercel AI SDK `paidTool` primitive. The cleanest path for AI SDK builders. |
| [MoltsPay](https://github.com/moltspay/molts-pay) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/moltspay/molts-pay) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-3+-blue?style=flat-square)](https://github.com/moltspay/molts-pay) | TypeScript | Multi-framework (Express, Hono, Fastify, Next.js). Base + Solana + ETH. Drop-in replacement. |

[Full SDK directory →](directory/sdks.md) · [Framework middleware →](directory/frameworks.md)

---

## MCP Servers

x402-native Model Context Protocol servers — AI agents pay per tool call, no API keys.

| MCP Server | Category | Description |
|-----------|----------|-------------|
| [agentsvc.io MCP](https://agentsvc.io/mcp) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | General | 100+ curated MCP tools, x402-gated. The hub for AI agent tooling. |
| [x402-mcp](https://vercel.com/blog/introducing-x402-mcp-open-protocol-payments-for-mcp-tools) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | SDK | Vercel AI SDK `paidTool` primitive — for building MCP tools that monetize via x402. |
| [IteraTools MCP](https://iteratools.ai/mcp) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Automation | Task automation via x402. Sequential and parallel workflow execution. |
| [EntRoute MCP](https://entroute.ai/mcp) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Data/Intelligence | Data intelligence and routing. Multi-chain analytics. |
| [ShieldAPI MCP](https://www.npmjs.com/package/shieldapi-mcp) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/alberthild/shieldapi-mcp) | Security | 9 endpoints: breach check (900M+ HIBP hashes), URL safety, prompt injection detection. |
| [MoltGuard](https://api.moltrust.ch/guard/) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/moltrust/moltguard) [![ERC-8004](https://img.shields.io/badge/ERC--8004-registered-orange?style=flat-square)](https://api.moltrust.ch) | Trust | Agent trust scoring (0-100), Sybil detection, Ed25519 Verifiable Credentials. 7 MCP tools. |
| [ToolOracle](https://tooloracle.ai) | Discovery | Real-time discovery of x402-enabled tools across the ecosystem. Agents find tools, tools get paid. |
| [24K Labs Code Review MCP](https://24klabs.ai/mcp) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Dev Tools | AI code review + security audit via MCP. Pay per PR. Runs in CI or interactively. |

[Full MCP server directory →](directory/mcp-servers.md)

---

## APIs & Services

x402-payable APIs — pay per request, no subscriptions.

| Service | Pricing | Description |
|---------|---------|-------------|
| [24K Labs Code Review API](https://24klabs.ai/code-review) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | $0.50/review | AI code review + security audit on Base. Explain, debug, review, security-scan. |
| [agentsvc.io](https://agentsvc.io) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Per-call | 100+ AI tools via a single x402-gated endpoint. One integration, full ecosystem access. |
| [Strale](https://strale.ai) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Per-token | LLM inference via x402. Pay per token, no subscription, no API key. |
| [AIsa](https://aisa.ai) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Per-call | AI + crypto data fusion. Highest x402 transaction count of any API service in the ecosystem. |
| [QuickNode RPC](https://quicknode.com) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-130+-blue?style=flat-square)](https://quicknode.com) | Per-request | Pay-per-request RPC access to 130+ chains. No node management. |
| [Arch Tools](https://archtools.io) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Per-call | 27 on-chain tools. Portfolio analysis, NFT data, market intelligence on Base. |
| [ShieldAPI](https://shield.vainplex.dev) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/alberthild/shieldapi-mcp) | $0.002–$0.05 | Security intelligence: breach check, domain reputation, URL safety, prompt injection detection. |
| [Valoria](https://x402.valoria.net) | — | Market intelligence: 90K+ indexed services, $148M+ tracked on-chain volume, revenue rankings. |

[Full API directory →](directory/apis.md)

---

## Tools & Monitoring

| Tool | Description |
|------|-------------|
| [x402-proxy](https://www.npmjs.com/package/x402-proxy) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/cascade-protocol/x402-proxy) | `npx x402-proxy` — cURL for x402 APIs. Auto-pays 402 with USDC on Base and Solana. MCP stdio proxy. |
| [Paybound](https://github.com/pando-b/paybound) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/pando-b/paybound) | Open-source governance proxy. Per-agent budgets, circuit breakers, SQLite audit trail. Drop-in `@x402/fetch` replacement. |
| [Sentinel/Valeo](https://sentinel.valeocash.com) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Enterprise audit layer. Budget enforcement, structured trails, real-time dashboard, public payment explorer. |
| [ScoutScore](https://scoutscore.ai) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Trust scoring for x402 services. Monitors 1,700+ services with continuous health checks. |
| [x402scan](https://x402scan.com) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Block explorer for x402 payments. Transaction search, payment requirement inspection, settlement status. |
| [24K Labs GitHub Action](https://github.com/Haustorium12/24klabs-action) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/Haustorium12/24klabs-action) | AI code review + security audit on every PR via x402 micropayments. Drop into any GitHub Actions workflow. |
| [Agent Forensics](https://www.npmjs.com/package/agent-forensics) | Claude Code cost observability. Analyzes JSONL session logs: per-model cost breakdown, cache efficiency, waste patterns. Free CLI. |

[Full tools directory →](directory/tools.md)

---

## Security & Compliance

| Service | Description |
|---------|-------------|
| [ShieldAPI](https://shield.vainplex.dev) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/alberthild/shieldapi-mcp) | x402-native security API. Breach check (900M+ HIBP hashes), domain/IP reputation, prompt injection detection. |
| [KaelAi](https://kaelai.io) | Wallet trust scoring 0-100 across 10 chains. Vet incoming/outgoing payment wallets before serving requests. |
| [MoltGuard](https://api.moltrust.ch/guard/) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/moltrust/moltguard) [![ERC-8004](https://img.shields.io/badge/ERC--8004-registered-orange?style=flat-square)](https://api.moltrust.ch) | Agent trust scoring, Sybil detection with funding cluster analysis, Ed25519 Verifiable Credentials. |
| [Paybound](https://github.com/pando-b/paybound) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/pando-b/paybound) | Governance proxy with circuit breakers and per-agent spending limits. MIT licensed. |
| [SENTINEL](https://mru-oracle.com) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/INJprotocol/mauritius-oracle-) | AML/CFT compliance. 77K+ sanctions entities (OFAC, UN, EU, PEP, Interpol), 159-country jurisdiction risk scoring. |
| [PolicyLayer](https://policylayer.com) | Non-custodial spending controls. Daily limits, per-transaction caps, recipient whitelists — no private key custody. |

[Full security directory →](directory/security.md)

---

## Ecosystem & Wallets

| Project | Description |
|---------|-------------|
| [Coinbase Agentic Wallets](https://docs.cdp.coinbase.com/agentic-wallets) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Native CDP wallets purpose-built for AI agents. Launched April 2, 2026. The reference implementation. |
| [Cloudflare Agents SDK](https://developers.cloudflare.com/agents) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Edge-native agent deployment with x402 built in. v0.4.0 adds x402 v2 migration (March 2026). |
| [Agent.market](https://agent.market) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) | Official app store for AI agents. x402-powered transactions. Launched April 20, 2026. |
| [WorkProtocol](https://workprotocol.ai) | Structured work marketplace for agents and builders. Escrow-backed jobs, on-chain reputation. |
| [Nevermined + Visa](https://pinionnewswire.com/press-release/nevermineds-visa-intelligent-commerce-x402-integration-unlocks-agentic-commerce/) | AI agents get delegated credit card spending authority via Visa Intelligent Commerce + x402 (April 2026). |
| [World AgentKit](https://www.coindesk.com/tech/2026/03/17/sam-altman-s-world-teams-up-with-coinbase-to-prove-there-is-a-real-person-behind-every-ai-transaction) | WorldID biometric identity + x402. Prove a verified human is behind every agent transaction. 18M+ verified humans. |

[Full ecosystem directory →](directory/ecosystem.md)

---

## Learning & Community

### Get Started

- [5-Minute Quickstart](https://docs.cdp.coinbase.com/x402/quickstart-for-sellers) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier) — Accept your first x402 payment.
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
- Last activity within 12 months, or carries a `24K Verified` tag.
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
