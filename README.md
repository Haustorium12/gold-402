# gold-402

> The gold standard for x402 resources. **442 curated entries** — every one checked by hand before it was listed. No filler. No dead links.

[![GitHub stars](https://img.shields.io/github/stars/Haustorium12/gold-402?style=social)](https://github.com/Haustorium12/gold-402)
[![Last Commit](https://img.shields.io/github/last-commit/Haustorium12/gold-402)](https://github.com/Haustorium12/gold-402/commits/main)
[![Curated by 24K Labs](https://img.shields.io/badge/Curated_by-24K_Labs-gold)](https://24klabs.ai)

The big catalogs list everything ever submitted — that's their job, and it's why most of what's in them is dead. We measured it: **67–79% of the free-listing catalogs no longer answer.**

gold-402 is the other thing. Smaller on purpose. A person checked every entry, we publish what we checked and what we didn't, and in July 2026 we started **buying services and reporting what came back** — which as far as we can tell nobody else in this ecosystem does.

---

## The Directory

The product. 442 entries across 13 shelves, in [`directory/`](directory/).

| Shelf | What's on it |
|---|---|
| [APIs & Services](directory/apis.md) | Paid endpoints an agent can call. Every one probed for a live 402 before listing. |
| [MCP Servers](directory/mcp-servers.md) | Model Context Protocol servers — utility, crypto, security, identity, escrow, discovery. |
| [SDKs & Libraries](directory/sdks.md) | Client and server libraries across languages. |
| [Facilitators](directory/facilitators.md) | Payment verification and settlement services. |
| [Frameworks](directory/frameworks.md) | Agent frameworks with x402 support. |
| [Tools](directory/tools.md) | CLIs, CI, monitoring, spend controls, testing, discovery. |
| [Security](directory/security.md) | Audit, risk scoring, pre-execution gates, compliance. |
| [Ecosystem](directory/ecosystem.md) | Protocol, infrastructure, wallets, orchestration, marketplaces. |
| [Aggregators & Proxies](directory/aggregators.md) | One integration, many upstreams — services that unify or resell access to other providers' APIs and data. |
| [**The Global Agent Economy**](directory/global.md) | **China, India, Korea — infrastructure no English-language directory indexes.** |
| [Learning](directory/learning.md) | Quickstarts, tutorials, reference docs, news. |
| [Community](directory/community.md) | Channels, newsletters, jobs, events. |
| [Market Data](directory/market-data.md) | On-chain analytics, dashboards, adoption. |

---

## What "verified" means here

One tier: **listed = verified.** No bronze, silver, gold.

If an entry is on the list, a maintainer confirmed the endpoint was live and answered an x402 request correctly at review, and we re-check periodically. That is the whole claim.

**It is not** an audit of the provider, a guarantee of uptime, or a promise any given call will succeed.

**Some entries carry more.** Where we have paid for a service and confirmed what came back, we say so and keep the receipt — what we sent, what it cost, the transaction hash, what arrived. That's a stronger claim and we only make it about services we actually bought. Most of the list hasn't been through that yet, and we'd rather say so than imply otherwise.

---

## Ecosystem Data

Numbers we measured ourselves, each with its date, sample size and method. Where measurements disagree, both are shown — they were taken on different days by different methods, and blending them into one tidy figure would be the kind of thing this directory exists to argue against.

### How much of the ecosystem is alive

| Measured | Population | Live | Dead | Method |
|---|---|---|---|---|
| 2026-07 | 22,545 CDP Bazaar services | 5,792 | **74%** | full probe crawl, valid 402 required |
| 2026-07-10 | 25,614 catalog services | 5,344 | **79%** | catalog snapshot, verify-state carried forward |
| 2026-07-29 | 24,583 catalog services | — | **~67%** | earlier full crawl, cited in the liveness study |

Three runs, three numbers, one direction: **the large free-listing catalogs are majority dead, and have been all month.** Anyone quoting a single decimal-point figure for this is quoting a moment, not a fact.

### Liveness is predicted by listing friction

Across four independent registries — 204,500 registered agents and services — the dead share tracks one variable: what it costs to get listed.

| Registry | Entry cost | Dead |
|---|---|---|
| CDP Bazaar | free | ~67–79% |
| ERC-8004 on-chain identity | gas only | 85–97% |
| Glama MCP registry | curation + scoring | 47% unhealthy _(their own published figure)_ |

**Free entry selects for abandonment.** Full method, limits, and an open invitation to refute it: [The Liveness Law →](articles/2026-07-the-liveness-law.md)

### Buying is harder than finding

In July 2026 we ran the first paid delivery check across our own shelf — actually buying services and recording what came back.

- **16** of 126 listed services were purchasable by a machine at a discoverable address
- **8** delivered exactly what they advertised
- **0** took payment and returned nothing
- **$0.054** spent, every transaction reconciled on-chain

The friction in this economy sits **before** the payment, not after it. Most services are fine; most front doors are not. A larger sample is in progress before we make a claim of it.

### Coverage beyond the West

x402 is a US-governed rail. It is not the only answer to machine payment, and outside the West it is not the answer being used — China runs delegated agent authorization on existing rails, India runs regulated human-signed mandates that agents execute inside a cap. Both were operating at scale before the x402 Foundation was a month old.

We index that world too, including surfaces no English-language directory carries: [The Global Agent Economy →](directory/global.md)

_All figures above are ours and reproducible. Where we could not reach something, we say so rather than leaving the gap invisible._

---

---

## Featured This Month

[![24K Featured](https://img.shields.io/badge/24K_Featured-2026--08-C0C0C0?style=plastic)](FEATURED.md)

**August 2026 — one pick per shelf.** Each shelf opens with its pick and the write-up. Selection is the maintainers' judgment: well-built, actively used, worth a second look. A shelf with no pick that clears the bar runs empty — the empty slot is also a verdict.

| Shelf | August pick |
|---|---|
| APIs & Services | [The Bot Wire](https://thebotwire.com) |
| MCP Servers | [Razorpay MCP Server](https://github.com/razorpay/razorpay-mcp-server) |
| SDKs & Libraries | [ra2a](https://github.com/qntx/ra2a) |
| Facilitators | [Primev FastRPC](https://facilitator.primev.xyz) |
| Frameworks | [machi](https://github.com/qntx/machi) |
| Tools | [portal-tunnel](https://github.com/gosuda/portal-tunnel) |
| Security | [Hermes Plant Action Safety](https://hermesplant.com/api/agent-services/action-safety/quick) |
| Ecosystem | [Glama](https://glama.ai/mcp/servers) |
| The Global Agent Economy | [ONDC](https://ondc.org) |
| Learning | [Tangle Network: x402 Production Runway](https://dev.to/tangle_network/series/37294) |
| Community | [WorkProtocol](https://workprotocol.ai) |
| Market Data | [Valoria](https://x402.valoria.net) |
| Aggregators & Proxies | — |

[Past features →](FEATURED.md)

---

## This Week in x402

The weekly wire now lives at **[24klabs.ai/news](https://24klabs.ai/news)** — dated editions with permanent links, every claim cited. [Latest edition →](https://24klabs.ai/news/2026-07-27/)

---

<!-- NEW-THIS-WEEK:START -->
## New This Week

**This week** (Aug 10—16)

_No new listings yet._

**Last week** (Aug 3—9)

- **[ScoutScore](https://scoutscore.ai)** — Trust scoring for x402 services. Monitors 1,700+ services with continuous health checks and fidelity probes.
- **[x402 Trust](https://x402.fuchss.app)** — Autonomous trust and reliability scoring for every publicly listed x402 endpoint, derived from continuous live probing and on-chain USDC settlement. Live report via POST /v1/x402-trust, free preview via GET /v1/x402-trust-preview.
- **[Viridis MCP Security Preflight](https://mcp.viridisconservation.com/x402/security-preflight/security_preflight?agent_id=viridis-probe&manifest=%7B%7D)** — Deterministic static preflight for caller-supplied MCP manifests that checks endpoint and authentication declarations, closed tool schemas, approval-policy conflicts, and prompt-injection indicators, returning an input-redacted signed receipt after x402 USDC settlement on Base.
- **[Minneapolis Rental Compliance](https://x402-mcp.onrender.com/mn/property-check)** — Rental-license status, tier, licensed unit count and expiration for any Minneapolis street address, plus violation and code-enforcement case history and condemned/boarded status. Live City of Minneapolis open data. For tenant screening and landlord or property-manager due diligence. $0.01 USDC on Base. ([OpenAPI](https://x402-mcp.onrender.com/openapi.json)) ([llms.txt](https://x402-mcp.onrender.com/llms.txt))
- **[ECB FX Reference](https://official-fx-reference.vercel.app/api/v1/convert)** — Converts amounts across ECB-supported currencies from the European Central Bank's daily euro reference observations, returning source rates, publication date, cross-rate math, and attribution for $0.0015 USDC per call on Base. ([OpenAPI](https://official-fx-reference.vercel.app/openapi.json)) ([GitHub](https://github.com/ArgonautWorks/ecb-fx-reference))
- **[BridgeNode](https://bridgenode.cc)** — OpenAI-compatible LLM inference bridge: chat completions with SSE streaming, pay per call via x402 with Solana USDC. From $0.002 per call. ([OpenAPI](https://bridgenode.cc/openapi.json)) ([llms.txt](https://bridgenode.cc/llms.txt)) ([GitHub](https://github.com/applefanaimail-blip/bridgenode-skill))
- **[BridgeNode MCP](https://www.npmjs.com/package/@bridgenode/mcp)** — x402-gated AI inference MCP server: chat completions + model listing, automatic USDC payments on Solana. Remote streamable-http at [bridgenode.cc/mcp](https://bridgenode.cc/mcp) or stdio via `npx @bridgenode/mcp`. ([GitHub](https://github.com/applefanaimail-blip/bridgenode-skill))
- **[IBANforge](https://ibanforge.com)** — Pre-payout IBAN screening: validation + issuing-bank identification against 6 national bank registers (CH/LI, DE, AT, BE, FI), Swiss clearing incl. QR-IID resolution, bank-level sanctions, SEPA + VoP reachability. 121k+ BICs, 89 IBAN countries. $0.002-$0.02 USDC on Base (CDP facilitator). MCP: `npx -y ibanforge-mcp`. ([OpenAPI](https://api.ibanforge.com/openapi.json), [x402 discovery](https://api.ibanforge.com/.well-known/x402))
- **[US City Open-Data Compliance Network](https://x402-mcp.onrender.com/us/cities)** — Multi-jurisdiction property compliance for AI agents: free catalog at /us/cities, free fixed-address samples at /us/{code}/property-check/sample, paid joins at /us/{code}/property-check ($0.01 USDC on Base). Fourteen live open-data markets (Minneapolis, Seattle, NYC, Chicago, Denver, San Francisco, Los Angeles, Boston, Philadelphia, Orlando, New Orleans, Montgomery County MD, Gainesville, Kansas City) covering rental registration/license and code-violation feeds. ([OpenAPI](https://x402-mcp.onrender.com/openapi.json)) ([llms.txt](https://x402-mcp.onrender.com/llms.txt)) ([GitHub](https://github.com/kwizzlesurp10-ctrl/x402-mcp))
- **[x402 Manifest Check](https://github.com/ruizmr/x402-api-readiness-review)** — Zero-dependency Python CLI and live x402-paid API for static manifest checks covering network, recipient, asset, and amount bindings; neither validates runtime enforcement or settlement.
- **[OyaPicks](https://oyapicks.app)** — Cross-venue prediction market data for AI agents: 10 endpoints covering keyword market search, single-market lookup, probability movers, 24h volume spikes, cross-venue arbitrage gaps between Polymarket and Alpha Arcade, markets closing within 48 hours, newly listed markets, resolutions with winning outcomes, and price history. $0.01–$0.25 USDC on Base via the CDP facilitator and Algorand via GoPlausible. Example: `GET /api/x402/single-market?q=fed`. ([Manifest](https://oyapicks.app/.well-known/x402)) ([OpenAPI](https://oyapicks.app/openapi.json)) ([llms.txt](https://oyapicks.app/llms.txt))
- **[Data Quality Gate](https://www.aidatatools.dev/api)** — Deterministic dataset-quality verdict (RELIABLE/USABLE_WITH_CLEANING/UNRELIABLE) with per-check facts on completeness, nulls, types, impossible values, duplicates, and outliers, plus optional cross-source price-divergence detection for financial/trading data, for $0.01 USDC per call on Base or Solana.
- **[Rue Render API](https://rue.mossgate.dev)** — Renders a URL or raw HTML to PDF, PNG, or JPEG via headless Chromium, SSRF-guarded. $0.003 USDC on Base via x402.
- **[Mossgate Trust API](https://api.mossgate.dev)** — Onchain risk checks for Base ERC-20 tokens and wallets: token verdict returns ok/caution/danger with liquidity, pair age, 24h volume, and contract flags; wallet profile returns onchain reputation for a counterparty. $0.01-$0.25 USDC on Base. ([llms.txt](https://api.mossgate.dev/llms.txt))
- **[Decision Anchor](https://api.decision-anchor.com)** — External anchoring layer for accountability before x402 payment execution. Records what was authorized, when, and at what scope. Content-blind. Non-judgmental.
<!-- NEW-THIS-WEEK:END -->

---

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

## Need More?

This README is the front door. The full curated directory — every shelf, every entry — is in [`directory/`](directory/).

**Other lists worth knowing:** the community [awesome-x402](https://github.com/x402-foundation/awesome-x402) accepts everything and is the right place for exhaustive coverage. [Glama](https://glama.ai/mcp/servers) indexes MCP servers at enormous scale and publishes its own health data, which is rarer than it should be. Different jobs. Use all three.

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
  <a href="https://24klabs.ai">24klabs.ai</a> •
  <a href="https://x402.org">x402.org</a> •
  <a href="https://github.com/coinbase/x402">Protocol Spec</a> •
  <a href="https://docs.cdp.coinbase.com/x402">Coinbase Docs</a> •
  <a href="https://discord.gg/x402">Discord</a> •
  <a href="https://agenteconomy.to">Live Dashboard</a>
</p>
