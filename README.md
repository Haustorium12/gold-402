# gold-402

> The gold standard for x402 resources. **459 curated entries** — every one checked by hand before it was listed. No filler. No dead links.

[![GitHub stars](https://img.shields.io/github/stars/Haustorium12/gold-402?style=social)](https://github.com/Haustorium12/gold-402)
[![Last Commit](https://img.shields.io/github/last-commit/Haustorium12/gold-402)](https://github.com/Haustorium12/gold-402/commits/main)
[![Curated by 24K Labs](https://img.shields.io/badge/Curated_by-24K_Labs-gold)](https://24klabs.ai)

The big catalogs list everything ever submitted — that's their job, and it's why most of what's in them is dead. We measured it: **67–79% of the free-listing catalogs no longer answer.**

gold-402 is the other thing. Smaller on purpose. A person checked every entry, we publish what we checked and what we didn't, and in July 2026 we started **buying services and reporting what came back**. Automated monitors now do the machine half of that continuously and do it well; what they do not do — by their own published scope — is judge whether the thing that came back was any good. That judgement is what this list is.

---

## The Directory

The product. 459 entries across 13 shelves, in [`directory/`](directory/).

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

In July 2026 we ran a paid delivery check across our own shelf — actually buying services and recording what came back.

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

The weekly wire now lives at **[24klabs.ai/news](https://24klabs.ai/news)** — dated editions with permanent links, every claim cited. [Latest edition →](https://24klabs.ai/news/2026-08-10/)

---

<!-- NEW-THIS-WEEK:START -->
## New This Week

**This week** (Aug 24—30)

- **[TaskMarket Data API](https://site-wine-nu-93.vercel.app/api/tm_list_tasks)** — Read-only TaskMarket bounty-market data for AI agents: list open tasks (rewards, deadlines, submission demand), full task details by ID, per-task submissions. $0.001/call USDC on Base via x402 v1 exact scheme (EIP-3009) — real on-chain enforcement through the non-custodial xpay facilitator, no CDP key needed. Unpaid requests get a spec-compliant 402 with payment terms. Built by Autonomy Labs, an autonomous AI agent. ([Discovery](https://site-wine-nu-93.vercel.app/.well-known/x402)) ([llms.txt](https://site-wine-nu-93.vercel.app/llms.txt)) ([GitHub](https://github.com/Autonomy-Labs-Tech/taskmarket-mcp))
- **[Animica Research](https://animica.dev/x402/research)** — One call that searches the web, fetches the top pages and returns their readable text with every requested URL accounted for; $0.02 USDC on Base or ANM natively at a 25% discount, free trial per client per day. Example: `POST /x402/research {"query":"post-quantum blockchain signatures","pages":4}`. ([Manifest](https://animica.dev/.well-known/x402)) ([OpenAPI](https://animica.dev/openapi.json)) ([llms.txt](https://animica.dev/llms.txt))
- **[Animica x402 Index](https://animica.dev/x402/index)** — Full-text search over ~18,000 machine-payable services indexed from their own 402 challenges (descriptions, input schemas, parameter names, prices, settlement networks), refreshed hourly; ~$0.006 USDC per query, free trial. Example: `POST /x402/index {"query":"wallet balance eip155:8453"}`. Free human-readable directory of ANM-settling services at [animica.dev/x402/scan](https://animica.dev/x402/scan). ([Manifest](https://animica.dev/.well-known/x402))
- **[Animica Agent Job Network](https://x402.animica.dev)** — Agents post tasks with a USDC budget and other agents perform them for payment; escrow holds the budget until the buyer's chosen verification passes, rejected jobs refund in full, receipts are ML-DSA-65 signed. Example: `POST /api/v1/jobs/quote {"capability":"summarise","budget_usd":1}`. ([OpenAPI](https://x402.animica.dev/openapi.json))
- **[Frantic](https://gofrantic.com)** — Bounty board where AI agents claim funded work, deliver artifacts in the open, and are paid in USDC on Base only when a delivery is accepted, with x402 pay-per-post at `POST /v1/vendor-postings/x402`, a manifest at `/.well-known/x402`, and every claim, judgment, and payout sealed to a public receipt ledger.
- **[BlockLabs Catalog](https://shop.blocklabs.nl)** — Dropshipping storefront selling physical products to agents: 300,000+ item catalog, paid full-text search at $0.001/query, order quotes (items + shipping + taxes) returned on the 402, ships to EU countries only. USDC on Base and Solana. ([llms.txt](https://shop.blocklabs.nl/llms.txt)) ([MCP](https://www.npmjs.com/package/@blocklabs/shop-mcp))
- **[BlockLabs Shop MCP](https://www.npmjs.com/package/@blocklabs/shop-mcp)** — Mounts the BlockLabs physical-goods shop as MCP tools: paid product search, free order quotes, order placement with a spend cap the agent cannot exceed, tracking. USDC on Base via x402; runs with npx, no build step. ([llms.txt](https://shop.blocklabs.nl/llms.txt))
- **[MCPFax Public-Data Utility](https://mcpfax-utility.bowling-anthony.workers.dev)** — 31 keyless public-data endpoints for AI agents: geocoding, weather, air quality, VIN decode, FX, stock quotes, SEC company facts, holidays, LEI, DNS. $0.001–$0.004 USDC per call on Base (x402 v1+v2); errors are free — a call that returns no data settles nothing. ([llms.txt](https://mcpfax-utility.bowling-anthony.workers.dev/llms.txt)) ([MCP](https://mcpfax-utility.bowling-anthony.workers.dev/mcp))
- **[MCP Scores](https://mcpscores.com)** — Reliability register + x402 money-flow observatory over 36K+ MCP/x402 listings: observed USDC inflow, seller rankings, payer breadth, wash-risk flags, with published methodology. Free register; paid intelligence via x402 ($0.003–$0.50) at [MCPFax Intel](https://mcpfax-intel.bowling-anthony.workers.dev/llms.txt).
- **[Feeless402](https://feeless402.com/premium)** — Reference pay-per-call endpoint settling in Nano (XNO): GET /premium answers a v2 402 at 0.0001 XNO per call with sub-second on-chain settlement and no gas; the 402 carries the rail-hint extension pointing at an on-site faucet so a new agent can fund itself and pay in one session. ([llms.txt](https://feeless402.com/llms.txt)) ([Manifest](https://feeless402.com/.well-known/x402))
- **[feeless402](https://pypi.org/project/feeless402/)** — Client and merchant server for x402 over the Nano (XNO) rail: CLI pays any x402 v2 endpoint, FastAPI merchant verifies and self-settles without a facilitator (Nano has no gas), includes a read-only remote MCP server. ([GitHub](https://github.com/Feeless402/feeless402))
- **[Cheapest Grocery Basket](https://grocery-basket.bowling-anthony.workers.dev/)** — Whole-list grocery optimization: send a shopping list and a ZIP, get what it costs at each nearby store and which store — or split of stores — is cheapest. Package sizes are normalized before anything is compared, so a $3.55 gallon correctly beats a $2.15 half gallon. Live prices from ALDI, Publix, Kroger banners, Walmart, Target and Ingles across US metros, with stock, sale prices, purchase links and when each price was last read. $0.01–$0.20 USDC on Base (x402 v1+v2); an uncovered ZIP or unknown product returns an error and is never charged. ([llms.txt](https://grocery-basket.bowling-anthony.workers.dev/llms.txt)) ([OpenAPI](https://grocery-basket.bowling-anthony.workers.dev/openapi.json)) ([MCP](https://grocery-basket.bowling-anthony.workers.dev/mcp))
- **[Black Label Continuum Audit](https://continuum.blacklabelbots.com/api/x402/cdp/audit)** — Scores eight self-declared AI-agent continuity capabilities and returns a deterministic 0–100 score with ranked gaps for 0.01 USDC on Base through Coinbase CDP x402; the same deterministic audit remains free at `POST /api/audit`, while the paid call adds x402 execution and a settlement receipt and does not commission Continuum.

**Last week** (Aug 17—23)

- **[apix402](https://api402x.com)** — Sixteen paid endpoints for agents, each answering against the source that decides rather than a summary of it: DAO proposal execution, Safe owner/threshold/module drift, oracle staleness per feed, Aave wstETH depeg exposure, token vesting and insider early-sale checks, plus package, advisory, MCP-server, RPC and x402-listing checks read from the registry or the endpoint itself; $0.001-$0.05 USDC per call on Base, free preview on every route, no signup. ([x402](https://api402x.com/.well-known/x402)) ([OpenAPI](https://api402x.com/openapi.json))
- **[fetchx402](https://api.fetchx402.com)** — Network utilities for agents: DNS, SSL, WHOIS (RDAP), HTTP headers, redirect tracing, host-intel and uptime bundles at $0.005–$0.015 USDC on Base. Example: `GET /v1/tools/dns?domain=example.com`. ([Docs](https://api.fetchx402.com/docs)) ([OpenAPI](https://api.fetchx402.com/openapi.json)) ([llms.txt](https://api.fetchx402.com/llms.txt))
- **[TaskMarket Trust Score](https://95-217-164-43.sslip.io)** — Requester reputation scoring for TaskMarket (taskmarket.dev): given a requester wallet address, returns a 0-100 trust score from on-platform payment history (completed tasks, cancellations-after-submission, expirations, self-awards). $0.001 USDC per call on Base, self-facilitated EIP-3009 exact scheme. Example: `GET /trust/0xADDRESS`. Discovery: `GET /.well-known/x402`.
- **[Forge Attestation](https://forgesignals.org/.well-known/forge-attestation)** — Signed third-party evidence records for x402 transactions, where every claim is labelled `witnessed` or `asserted`: witnessed means Forge observed it directly, either probing what the endpoint advertised at that moment or checking a Base settlement transaction against that advertised price and payee; asserted means a party stated it and Forge only notarised the statement. A response hash submitted after the call is classed asserted and the spec states it is not proof of delivery; consistency and conformance are declared supported, correctness not supported by any third-party witness including this one. Ed25519, verifiable offline from the published key, every claim carrying a `falsifiable_by` field; response bodies are never transmitted or stored, hashes only. $0.02 USDC per attestation on Base via the Coinbase CDP facilitator; retrieval, hosted verification and the spec are free. Example: `POST /attest {"url":"https://example.com/paid-api"}` with optional `settlement_tx`, `response_sha256`, `request_nonce`. Free: `POST /attestations/verify`, `GET /attestations/:id`.
- **[BridgeNode Solana x402 Quickstart](https://github.com/bridgenode-ai/bridgenode-skill/blob/main/examples/README.md)** — Step-by-step walkthrough that teaches the x402 payment flow on Solana: trigger the 402, sign a USDC transfer (fee-sponsored, no SOL needed), retry with PAYMENT-SIGNATURE, get the 200. Curl + TypeScript + Python examples, from first payment to SDK usage.
- **[Andreax](https://pagos.andreax.dev/tienda)** — Remote MCP server with 54 pay-per-call AI tools: prompt compression, inference, web/PDF read, OCR, vision, embeddings, semantic search, translation, FX, and market data. $0.001-$0.50 USDC on Base. ([MCP](https://pagos.andreax.dev/mcp)) ([Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=andreax))
- **[Cleared Index](https://clearedindex.com)** — Trust provider and verification index with a conformant trust-evaluation endpoint: `POST /api/cleared/trust/evaluate` (`x402-trust-evaluation-v0.1`), Ed25519 signed attestations, and public JWKS at `GET /api/cleared/jwks`. Discovery manifest: `/.well-known/x402.json`.
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
