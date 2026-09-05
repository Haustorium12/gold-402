<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
    <img src="assets/hero-light.svg" alt="gold-402 — a hand-checked directory of x402 services. Most of the x402 catalogue no longer answers; these are the ones that did. We check it, we date it, and we tell you what we found. By 24K Labs." width="680">
  </picture>
</p>

# gold-402

> The gold standard for x402 resources. **<!--COUNT:START-->521<!--COUNT:END--> curated entries** — paid endpoints probed for a live 402 before listing, libraries and repos checked for real activity, and the whole shelf re-knocked every night with the result dated. No filler.

[![GitHub stars](https://img.shields.io/github/stars/Haustorium12/gold-402?style=social)](https://github.com/Haustorium12/gold-402)
[![Last Commit](https://img.shields.io/github/last-commit/Haustorium12/gold-402)](https://github.com/Haustorium12/gold-402/commits/main)
[![Curated by 24K Labs](https://img.shields.io/badge/Curated_by-24K_Labs-gold)](https://24klabs.ai)

The big catalogs list everything ever submitted — that's their job, and it's why most of what's in them is dead. We measured it: **67–79% of the free-listing catalogs no longer answer.**

gold-402 is the other thing. Smaller on purpose. A person checked every entry, we publish what we checked and what we didn't, and in July 2026 we started **buying services and reporting what came back**. Automated monitors now do the machine half of that continuously and do it well; what they do not do — by their own published scope — is judge whether the thing that came back was any good. That judgement is what this list is.

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/directory-dark.svg">
  <img src="assets/sections/directory-light.svg" alt="Section: The Directory" width="680">
</picture>

## The Directory

The product. <!--COUNT:START-->521<!--COUNT:END--> entries across <!--SHELVES:START-->13<!--SHELVES:END--> shelves, in [`directory/`](directory/).

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

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/verified-dark.svg">
  <img src="assets/sections/verified-light.svg" alt="Section: What verified means here" width="680">
</picture>

## What "verified" means here

One tier: **listed = verified.** No bronze, silver, gold.

If an entry is on the list, its endpoint answered an x402 request correctly at review — checked
by an automated gate on the submission, confirmed by a maintainer before the merge — and a nightly
sweep re-knocks every entry on every shelf and writes a dated result. That is the whole claim.

**It is not** an audit of the provider, a guarantee of uptime, or a promise any given call will succeed.

**Some entries carry more.** Where we have paid for a service and confirmed what came back, we say so and keep the receipt — what we sent, what it cost, the transaction hash, what arrived. That's a stronger claim and we only make it about services we actually bought. Most of the list hasn't been through that yet, and we'd rather say so than imply otherwise.

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/ecosystem-dark.svg">
  <img src="assets/sections/ecosystem-light.svg" alt="Section: Ecosystem Data" width="680">
</picture>

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

The friction in this economy sits **before** the payment, not after it. Most services are fine; most front doors are not. **We are not claiming that as a finding yet — the sample is 16 services and one day, 2026-07-30.** A wider census was designed the same week and has not run; the blocker is ours, not the ecosystem's. We would rather say that than let the sentence stand.

### Coverage beyond the West

x402 is a US-governed rail. It is not the only answer to machine payment, and outside the West it is not the answer being used — China runs delegated agent authorization on existing rails, India runs regulated human-signed mandates that agents execute inside a cap. Both were operating at scale before the x402 Foundation was a month old.

We index that world too, including surfaces no English-language directory carries: [The Global Agent Economy →](directory/global.md)

_All figures above are ours and reproducible. Where we could not reach something, we say so rather than leaving the gap invisible._

---

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/featured-dark.svg">
  <img src="assets/sections/featured-light.svg" alt="Section: Featured This Month" width="680">
</picture>

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

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/wire-dark.svg">
  <img src="assets/sections/wire-light.svg" alt="Section: This Week in x402" width="680">
</picture>

## This Week in x402

The wire lives at **[24klabs.ai/news](https://24klabs.ai/news)** — dated editions with permanent links, every claim cited. Four editions so far; the most recent is [2026-08-10](https://24klabs.ai/news/2026-08-10/). It is not on a schedule.

---

<!-- NEW-THIS-WEEK:START -->
## New This Week

**This week** (Aug 31—Sep 6)

- **[Textus](https://api.textus.dev/api/v1/resources/der-suesse-brei/content.json)** — Structured literary content for AI agents, including complete selected text units, metadata, characters, scenes and editable baseline reading direction, with free resource discovery and production-material JSON purchased through x402. ([Catalogue](https://api.textus.dev/api/v1/resources.json)) ([Docs](https://textus.dev/docs/))
- **[Genuine Good Grants](https://genuinegood.online/v1/grants/preflight)** — Sourced U.S. federal grant search, official notice detail, transparent mission-fit signals, application briefs, and deterministic shortlist preflight checks from current Grants.gov public records, priced from $0.05 to $5.00 USDC on Base through x402 v2. ([Manifest](https://genuinegood.online/.well-known/x402)) ([OpenAPI](https://genuinegood.online/openapi.json)) ([llms.txt](https://genuinegood.online/llms.txt))
- **[/deslop](https://mooch.agency/api/deslop)** — Removes AI-writing tells (em dashes, hedging, throat-clearing) from a draft, returns cleaned text plus a changelog. $0.10 USDC on Base. Example: `POST /api/deslop {"text":"..."}`. ([Prompt page](https://mooch.agency/prompts/deslop))
- **[PLEXUS Intelligence API](https://plexus-public-production.up.railway.app)** — 163 pay-per-call x402 endpoints from a single provider: US federal regulatory data (EPA, OSHA, FEC, SEC full-text, FDA, NPI, CMS, FEMA, CFPB, CourtListener, SAM.gov, Congress.gov, GLEIF, WorldBank, and 15+ more), plus 12 AI reasoning engines (Tribunal multi-model verdict, WHETSTONE adversarial stress-test, POSTCOG action-safety gate, G-Score ground truth, Verify claim verification) and 5 composite intelligence products synthesized cross-source (Company Risk $0.35, Political Intel $0.35, Supply Chain Risk $0.30, Healthcare DDIL $0.30, Nonprofit Intel $0.20). Data adapters $0.01–$0.03/call, engines $0.05–$0.15/call. Base + Solana mainnet. No API keys — wallet is auth. ([OpenAPI](https://plexus-public-production.up.railway.app/openapi.json)) ([Manifest](https://plexus-public-production.up.railway.app/.well-known/x402)) ([llms.txt](https://plexus-public-production.up.railway.app/llms.txt)) ([MCP](https://plexus-public-production.up.railway.app/mcp))
- **[openzoo](https://openzoo.fun)** — OpenAI-compatible chat completions paid per request via x402 on Solana and Base, with no account or API key.
- **[API Acre Website Metadata](https://apiacre.com/v1/web/metadata)** — Extracts title, canonical URL, headings, hreflang, icons, feeds, Open Graph, Twitter Cards, and JSON-LD types from one public HTTPS page, with redirect and response provenance, for $0.002 USDC on Base or Solana. ([Catalog](https://apiacre.com/catalog/web.metadata)) ([OpenAPI](https://apiacre.com/openapi.json)) ([x402 discovery](https://apiacre.com/.well-known/x402))
- **[x402 Preflight](https://x402-wallet-readiness-service.vercel.app/api/x402/preflight/audit?resource_url=https%3A%2F%2Fx402-wallet-readiness-service.vercel.app%2Fapi%2Fx402%2Fdev%2Frepo-snapshot%3Frepo%3Dchico10117%2Fbasepay-readiness-service&method=GET&expected_network=eip155%3A8453&max_price_usd=1)** — Audits a public x402 endpoint before payment via required `resource_url` and optional `method=GET|HEAD`, `expected_network`, and `max_price_usd` query parameters; the audit costs $0.05 USDC on Base.
- **[Excelexi](https://api.excelexi.com/api/v1/technical-analysis?symbol=BTCUSDT)** — Technical-indicator and market-analysis API for trading agents: 73 indicators and 24 derived signals across 100 crypto markets, plus screening, analytics snapshots/history, and a natural-language endpoint that compiles a plain sentence into a deterministic query before executing it. Every returned value carries provenance — which bars were used, whether the indicator's warm-up period was satisfied, the data's age, and the upstream source — so a caller can verify freshness before acting on it. Example: `GET /api/v1/technical-analysis?symbol=BTCUSDT&interval=1h`. $0.00002-$0.0005 USDC on Base mainnet via x402 v2 (EIP-3009), 9 payable endpoints, no API key and no signup. ([OpenAPI](https://api.excelexi.com/openapi.json)) ([Discovery](https://api.excelexi.com/.well-known/x402)) ([Docs](https://excelexi.com/for-agents))
- **[Truth Bear (GAUGE)](https://api.truthbear.co/manifest)** — 180+ official-source data signals for AI agents: US river/flood and streamflow (USGS/NOAA), air quality (EPA), drought, power grid (EIA), shipping (IMF PortWatch), and SEC EDGAR filings. Each paid record ships a canonical sha256 record_hash the caller recomputes offline; readings are stated against the source agency's own published thresholds where one exists. $0.005–$0.09 USDC on Base and Solana, no API key, no signup; a query with no data returns 422 and is not billed. Screening-level, not decision-grade. Example: `GET /gauge/air`. ([llms.txt](https://api.truthbear.co/llms.txt)) ([Sample](https://api.truthbear.co/gauge/sample)) ([MCP](https://www.npmjs.com/package/mcp-gauge-x402))
- **[x402-list](https://x402-list.com)** — Agent-first directory of x402-payable APIs with a no-auth machine-readable REST feed and a hosted MCP server for finding and verifying endpoints before an agent pays.
- **[Ausca](https://ausca.com)** — Metered infrastructure services for agents: document OCR, document analysis, media transcription, leased browser sessions with CDP, and receive-only agent inboxes. From $0.05 USDC per call on Base via x402 v2, no accounts or API keys, every result bound to published schema digests and a terminal receipt. Unsigned `POST /v1/invocations` returns the live payment requirement. ([OpenAPI](https://ausca.com/openapi.json)) ([Manifest](https://ausca.com/.well-known/x402)) ([Skill](https://ausca.com/SKILL.md))
- **[RGX](https://rgx.tail817c3b.ts.net)** — Snap Router: task-to-tool selection over the merged x402 Bazaar and MCP Registry catalog (16k+ entries), one pass, no LLM call, $0.003 USDC. Example: `POST /v1/snap?x402force=1 {"task":"check a base token for honeypot","k":4}`. Pricing-Truth: real tradeable depth vs headline TVL, depth-weighted multi-pool price corroboration, and a live buy-then-sell honeypot/transfer-tax check for tokens on Base, Ethereum, and Arbitrum, $0.005-$0.04 USDC. Example: `GET /v1/base/token/0x532f27101965dd16442E59d40670FaF5eBB142E4/report?x402force=1`. Free tier, CDP facilitator. ([Manifest](https://rgx.tail817c3b.ts.net/.well-known/x402)) ([OpenAPI](https://rgx.tail817c3b.ts.net/openapi.json)) ([llms.txt](https://rgx.tail817c3b.ts.net/llms.txt)) ([MCP](https://pypi.org/project/rgx-mcp/))
- **[x402 Preflight](https://x402.chikocorp.com/api/x402/preflight/audit?resource_url=https%3A%2F%2Fx402.chikocorp.com%2Fapi%2Fx402%2Fdev%2Frepo-snapshot%3Frepo%3Dchico10117%2Fbasepay-readiness-service&method=GET&expected_network=eip155%3A8453&max_price_usd=1)** — Audits a public x402 endpoint before payment via required `resource_url` and optional `method=GET|HEAD`, `expected_network`, and `max_price_usd` query parameters; the audit costs $0.05 USDC on Base.
- **[MIDAX402](https://midax402.com)** — Signed EIP-712 conformance verdicts for x402 services, appended to a public registry. Paid board position available ($1–$100 ladder) as a separate column; no payment changes a verdict or the verification-date ordering.
- **[WickedAPI x402 Paywall](https://paywall.wickedapi.com)** — Multi-tenant x402 paywall-as-a-service on Base mainnet via the Coinbase CDP facilitator. Self-serve signup, REST API to set price/network/payout wallet and forward to a real backend, live settlement views. Example: `GET https://paywall.wickedapi.com/wickedapi/weather` returns a live 402. ([OpenAPI](https://paywall-admin.wickedapi.com/openapi.json), [Cookbook](https://paywall.wickedapi.com/cookbook.html))

**Last week** (Aug 24—30)

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
- **[Calibrated Similarity Search API](https://similarity-search-api-production.up.railway.app)** — Stateless NMI + cosine fusion similarity search over pre-computed numeric vectors, with an entropy-calibrated blending weight (alpha) computed per request; vectors only, no server-side embedding. $0.01 USDC on Base Sepolia (testnet) via x402, no API key required. Example: `POST /similarity/search {"query":{"id":"q1","vector":[0.1,0.2,0.3]},"corpus":[{"id":"c1","vector":[0.1,0.2,0.3]}]}`. ([OpenAPI](https://similarity-search-api-production.up.railway.app/openapi.json)) ([Agent Card](https://similarity-search-api-production.up.railway.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/similarity-search-api-sdk))
- **[On-Chain Activity Index](https://onchain-activity-index-325572559480.us-central1.run.app)** — 0-100 quantitative DeFi Protocol Activity Index computed from real public DefiLlama data (TVL trend, fee/volume activity trend, chain diversification); explicitly a descriptive index, not trading advice. $0.30 USDC on Base Sepolia (testnet) via x402. Example: `POST /activity-index {"protocol_slug":"uniswap"}`. ([OpenAPI](https://onchain-activity-index-325572559480.us-central1.run.app/openapi.json)) ([Agent Card](https://onchain-activity-index-325572559480.us-central1.run.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/onchain-activity-index))
- **[URL Metadata API](https://url-metadata-api-325572559480.us-central1.run.app)** — Link-preview API: given a URL, returns title/description/preview-image/site_name scraped from its OpenGraph and meta tags. $0.01 USDC on Base Sepolia (testnet) via x402. Example: `POST /extract {"url":"https://example.com"}`. ([OpenAPI](https://url-metadata-api-325572559480.us-central1.run.app/openapi.json)) ([Agent Card](https://url-metadata-api-325572559480.us-central1.run.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/url-metadata-api))
- **[Live Entity Verification API](https://live-entity-verification-production.up.railway.app)** — Cross-signal Bayesian corroboration of entity existence: fuses WHOIS, Certificate Transparency, Wayback Machine, and DNS operational maturity into a calibrated hallucination verdict with a confidence score. $0.01-$0.05 USDC on Base Sepolia (testnet) via x402, tiered per route. Example: `POST /verify-entity-existence-cross-signal {"domain":"example.com","entity_name":"Example Corp"}`. ([OpenAPI](https://live-entity-verification-production.up.railway.app/openapi.json)) ([Agent Card](https://live-entity-verification-production.up.railway.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/live-entity-verification-sdk))
- **[Agent Verification API](https://agent-verification-api-325572559480.us-central1.run.app)** — Confirms an AI agent/service is who it claims to be: fuses cross-signal domain-existence verification (WHOIS/CT/Wayback/DNS) with a real agent-card fetch and MCP `initialize` handshake against the claimed endpoint. $0.35 USDC on Base Sepolia (testnet) via x402. Example: `POST /verify-agent-identity {"domain":"example.com","entity_name":"Example Corp"}`. ([OpenAPI](https://agent-verification-api-325572559480.us-central1.run.app/openapi.json)) ([Agent Card](https://agent-verification-api-325572559480.us-central1.run.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/agent-verification-api))
- **[x402 Receipt Verifier](https://x402-receipt-verifier-325572559480.us-central1.run.app)** — Audits NEXUS's own x402 payment logs against its own delivery logs and issues a signed HMAC receipt proving a specific payment correlates with a real, successful delivery; signature-only verification is free. $0.02 USDC on Base Sepolia (testnet) via x402 on the 2 paid routes. Example: `POST /verify-payment-receipt {"asset_name":"document-conversion-api","payer_address":"0x0000000000000000000000000000000000dEaD","claimed_amount_usd":0.01,"claimed_at":"2026-08-24T00:00:00Z"}`. ([OpenAPI](https://x402-receipt-verifier-325572559480.us-central1.run.app/openapi.json)) ([Agent Card](https://x402-receipt-verifier-325572559480.us-central1.run.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/x402-receipt-verifier))
- **[ERC-8004 Agent Liveness](https://erc8004-agent-liveness-325572559480.us-central1.run.app)** — Checks whether an agent registered in the real ERC-8004 Identity Registry (Base Sepolia testnet) is actually alive right now: resolves its on-chain registration file and runs a real MCP `initialize` handshake against the declared endpoint. $0.10 USDC on Base Sepolia (testnet) via x402. Example: `POST /verify-registered-agent {"agent_id":1}`. ([OpenAPI](https://erc8004-agent-liveness-325572559480.us-central1.run.app/openapi.json)) ([Agent Card](https://erc8004-agent-liveness-325572559480.us-central1.run.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/erc8004-agent-liveness))
- **[Public Tenders ES/EU](https://public-tenders-es-eu-325572559480.us-central1.run.app)** — Normalized search over public-sector tenders published in TED (EU official procurement notices), covering Spain plus the rest of the EU above the EU publication threshold, filterable by country/keyword/CPV code/recency. $0.01 USDC on Base Sepolia (testnet) via x402. Example: `POST /search-public-tenders {}`. ([OpenAPI](https://public-tenders-es-eu-325572559480.us-central1.run.app/openapi.json)) ([Agent Card](https://public-tenders-es-eu-325572559480.us-central1.run.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/public-tenders-es-eu))
- **[Document Conversion API](https://document-conversion-api-325572559480.us-central1.run.app)** — Converts between PDF/Office documents and structured JSON in both directions using pure open-source libraries (pdfplumber/python-docx/openpyxl/reportlab), no external conversion service. $0.01-$0.02 USDC on Base Sepolia (testnet) via x402, per route across 5 routes (PDF/DOCX/XLSX extraction, PDF/DOCX generation). Example: `POST /extract-pdf-to-json {"file_base64":"<base64 PDF bytes>"}`. ([OpenAPI](https://document-conversion-api-325572559480.us-central1.run.app/openapi.json)) ([Agent Card](https://document-conversion-api-325572559480.us-central1.run.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/document-conversion-api))
- **[WebSocket Session Manager API](https://npm-package-ws-has-241560546-w-production.up.railway.app)** — Stateful WebSocket session registry that proxies a connection to a target URL and scores each inbound frame with a Shannon entropy delta for schema-divergence detection; free once a session is open. $0.01 USDC on Base Sepolia (testnet) via x402, charged only on session open. Example: `POST /ws-sessions/open {"target_url":"wss://echo.websocket.org"}`. ([OpenAPI](https://npm-package-ws-has-241560546-w-production.up.railway.app/openapi.json)) ([Agent Card](https://npm-package-ws-has-241560546-w-production.up.railway.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/npm-package-ws-has-241560546-weekly-downloads-but-sdk))
- **[New x402 Listings Feed](https://new-x402-listings-feed-325572559480.us-central1.run.app)** — Feed of x402/L402 services newly listed on 402index.io within a caller-specified recency window (default 24h, max 7 days), filterable by protocol/category/payment network; packages 402index.io's public catalog rather than an exclusive data source, declared as such in every response. $0.01 USDC on Base Sepolia (testnet) via x402. Example: `POST /new-x402-listings {}`. ([OpenAPI](https://new-x402-listings-feed-325572559480.us-central1.run.app/openapi.json)) ([Agent Card](https://new-x402-listings-feed-325572559480.us-central1.run.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/new-x402-listings-feed))
- **[Viraill](https://viraill.com)** — Generative Engine Optimization (GEO) and Agentic Commerce Readiness APIs for AI agents and SaaS: `POST /v1/geo/audit` ($0.05) scores site visibility across ChatGPT, Perplexity, Gemini, Claude and computes market intent gaps with RAG answer blocks; `POST /v1/geo/social-generate` ($0.02) generates social posts aligned to market intent centroids; `POST /v1/agentic/scan` ($0.05) deterministic /100 readiness score across 5 pillars and 8 agent distribution channels with remediation pack. Free 3-call daily tier, then USDC on Base via x402. ([Manifest](https://viraill-core-api.fly.dev/.well-known/x402.json)) ([OpenAPI](https://viraill-core-api.fly.dev/openapi.json)) ([llms.txt](https://viraill-core-api.fly.dev/llms.txt)) ([GitHub](https://github.com/crypto-yannso/viraill-skills))
- **[Cleared Gateway](https://clearedindex.com/api/cleared/gateway)** — POST router that returns the best Cleared-verified x402 endpoint for a task (category + strategy). Free to call; pairs with Cleared Check / Witness. Settle-tape aware. Paid probe: https://clearedindex.com/api/x402/ping · Manifest: https://clearedindex.com/.well-known/x402
- **[Cleared Index MCP](https://clearedindex.com/api/x402/ping)** — MCP server (`route_gateway`, check, trust, witness) so agents query attested inventory and route before pay. Default habit: check → route_gateway → pay → witness. `npx -y @n747ai/clearedindex-mcp-server`. ([npm](https://www.npmjs.com/package/@n747ai/clearedindex-mcp-server)) ([Glama](https://glama.ai/mcp/servers/N747AI/clearedindex-mcp)).
- **[GPT55 Model Gateway](https://gpt55.558686.xyz/v1/chat/completions/standard)** — OpenAI-compatible GPT-5.6 Luna Standard chat completions via x402 USDC on Base for $0.00293 per POST request.
- **[BridgeNode Solana x402 Quickstart](https://github.com/bridgenode-ai/bridgenode-skill/blob/main/examples/README.md)** — Step-by-step walkthrough that teaches the x402 payment flow on Solana: trigger the 402, sign a USDC transfer (fee-sponsored, no SOL needed), retry with PAYMENT-SIGNATURE, get the 200. Curl + TypeScript + Python examples, from first payment to SDK usage.
- **[BridgeNode](https://bridgenode.cc)** — OpenAI-compatible LLM inference bridge: 38 models (GLM, Kimi, MiniMax, DeepSeek, GPT-OSS), chat completions with SSE streaming, pay per call via x402 with Solana USDC. 5 models are free — `gpt-oss-20b`, `gpt-oss-120b`, `glm-4.7-flash`, `glm-4.5-flash`, `glm-4.6v-flash` return 200 on the first request with no payment, no API key and no registration. Paid models from $0.002 per call. Example: `POST /v1/chat/completions {"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}]}`. ([OpenAPI](https://bridgenode.cc/openapi.json)) ([llms.txt](https://bridgenode.cc/llms.txt)) ([GitHub](https://github.com/bridgenode-ai/bridgenode-skill))
- **[BridgeNode MCP](https://www.npmjs.com/package/@bridgenode/mcp)** — x402-gated AI inference MCP server: chat completions + model listing across 38 models, automatic USDC payments on Solana; the 5 free models need no payment at all. Remote streamable-http at [bridgenode.cc/mcp](https://bridgenode.cc/mcp) or stdio via `npx @bridgenode/mcp`. Example tool call: `chat_completions {"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}]}`. ([GitHub](https://github.com/bridgenode-ai/bridgenode-skill))
- **[DopamineDesk Transaction Preflight](https://ai-data-marketplace-1042299154756.us-central1.run.app/api/v1/transaction_preflight)** — Checks an unsigned EVM transaction for simulation errors, gas, proxy evidence, and optional token-security or allowance issues before an agent signs it. `POST` only, $0.005 USDC on Base. ([OpenAPI](https://ai-data-marketplace-1042299154756.us-central1.run.app/openapi.json))
- **[M0 Email Verification](https://m0.aiverall.com/v1/verify-email)** — RFC-shaped email syntax check + live domain DNS resolution, so an agent can filter out dead leads before spending money on downstream enrichment. $0.005 USDC on Base mainnet via x402 v2. Does not claim mailbox/SMTP verification. Example: `POST /v1/verify-email {"email":"person@example.com"}`. ([OpenAPI](https://m0.aiverall.com/openapi.json))
- **[CONNSKILL Growth Services](https://agent.connskill.com)** — Growth infrastructure for AI agents: SEO/SERP research (Google SERP reports, keyword volume/CPC, ranked keywords, backlinks, competitors, site audit), SMS verification numbers (1,378 services, with a cheapest-country pricing endpoint), social-marketing orders (1,003 orderable services), receive-only email inboxes, GDPR/EU-hosted LLM inference, and read-only on-chain data (EVM state and call simulation on 5 chains, EIP-7702-aware). 51 endpoints, 32 paid and 19 free, $0.02–$18.00 USDC on Base via x402 v2 (EIP-3009), most calls $0.10 or less; free quote, catalog and pricing lookups; A2A agent card with the x402 payments extension. Also runs a curated [directory](https://agent.connskill.com/directory) of external x402 services with a pay-to-activate listing flow. Operated by a German company on EU infrastructure. ([OpenAPI](https://agent.connskill.com/openapi.json)) ([Discovery](https://agent.connskill.com/.well-known/x402)) ([llms.txt](https://agent.connskill.com/llms.txt)) ([Agent Card](https://agent.connskill.com/.well-known/agent-card.json))
- **[M0 URL Extraction](https://m0.aiverall.com/v1/extract)** — Fetch a public URL, get back clean machine-consumable text (HTML noise stripped, SSRF-guarded). $0.002 USDC on Base mainnet via x402 v2. Example: `POST /v1/extract {"url":"https://example.com"}`. Also exposes email verification ($0.005, `/v1/verify-email`) and a lead-validation bundle ($0.015, `/v1/lead-validate` -- MX existence, disposable-domain, role-account detection). ([OpenAPI](https://m0.aiverall.com/openapi.json))
- **[OrbitWan.io MCP](https://mcp.orbitwan.io/mcp)** — 24-tool Wanchain explorer MCP server from an independent archive node: addresses, transactions, tokens, validators, verified contracts, and WanBridge cross chain transfers with both legs correlated; 18 tools free, 6 premium tools prepaid via OrbitPay on Wanchain at 0.0005 USDT per 100 rows. ([Docs](https://orbitwan.io/docs/mcp)) ([Manifest](https://orbitwan.io/.well-known/x402)) ([Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=orbitwan))
- **[x402 Checker (Nock)](https://x402-checker.nock-for-mak.workers.dev/report)** — Free `GET /check?url=` honesty probe of a live x402 URL plus free `GET /board` (pay-to-rank, 24h) and `GET /name`; paid `GET /report?url=` is $0.05 USDC on Base via PayAI, and `POST /bid` and `POST /name` are $0.05. Example: `GET /check?url=https://example.com`. ([Manifest](https://x402-checker.nock-for-mak.workers.dev/.well-known/x402)) ([OpenAPI](https://x402-checker.nock-for-mak.workers.dev/openapi.json)) ([GitHub](https://github.com/nock-for-mak/skills))
- **[csno](https://csno.cc)** — Provably-fair coinflip, dice, and European roulette for agents: `POST /api/csno/chips` answers 402 ($0.10 for 1,000 chips, $1.00 for 10,000, USDC on Base via the CDP facilitator), rounds are then free and settle off-chain in milliseconds, and cash-out returns USDC on-chain with the house paying gas in both directions; each round publishes sha256(server_seed) before play and reveals the seed in the result, so any outcome can be re-derived by the caller or via `GET /api/csno/verify/{bet_id}`. ([skill.md](https://csno.cc/skill.md)) ([OpenAPI](https://csno.cc/openapi.json)) ([MCP](https://csno.cc/api/mcp))
- **[Saylor Watchdog](https://saylorinnovations.com/.well-known/x402.json)** — Solana token intelligence: price/liquidity spread across two independent sources, security flags (mint/freeze authority, LP-lock %, top-10 holder concentration), full holder lists, wallet risk scoring, narrative classification, and new-pool scanning. $0.001-$0.01 USDC on Solana (self-verified settlement, no facilitator) or Base via CDP/PayAI facilitator. Example: `GET /api/price/EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`. ([OpenAPI](https://saylorinnovations.com/openapi.json)) ([Free samples](https://saylorinnovations.com/api/sample/price))
- **[solana-x402](https://github.com/SaylorInnovations/solana-x402)** — Zero-dependency x402 resource server for Solana. Self-verified settlement (USDC/USDT/native SOL) with no facilitator or fee; optional CDP and/or PayAI facilitator settlement layered on for Base and stock x402 clients, with resources carrying an `outputSchema` automatically marked discoverable in the CDP Bazaar. MIT.
- **[Citable](https://citable.run)** — SEO and AI-visibility data on 17 paid GET routes: keyword research, on-page audits, AI-citation checks across ChatGPT, Claude, Gemini and Perplexity, plus rank, SERP, domain and backlink data; $0.005–$0.30 USDC on Solana mainnet, no account or API key, and any 4xx/5xx cancels the payment instead of settling it.
- **[Israel Company Verify](https://israel-counterparty-intelligence.vercel.app/v1/verify/mainnet)** — Verifies Israeli companies against structured public-registry data and returns evidence for $0.05 USDC per POST request on Base mainnet via x402 v2 and PayAI, with no account or API key. Example: `POST /v1/verify/mainnet {"company_number":"520036120","language":"en","depth":"basic"}`. ([OpenAPI](https://israel-counterparty-intelligence.vercel.app/openapi.json)) ([Manifest](https://israel-counterparty-intelligence.vercel.app/.well-known/x402)) ([llms.txt](https://israel-counterparty-intelligence.vercel.app/llms.txt))
- **[SchemaLock](https://doc-extract-api.thestarboy9696-4ef.workers.dev)** — Structured JSON extraction from invoices, receipts, contracts, resumes, or raw text/HTML via a caller-supplied JSON Schema. Line items and totals are checked against each other; a document that still fails after one automatic retry returns 422 and settlement is skipped, not just flagged in the body. $0.05–$0.08 USDC on Base. MCP client on npm: `doc-extract-api-mcp` (every call still pays the live API, no free tier). ([GitHub](https://github.com/thestarboy9696/doc-extract-api)) ([MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.thestarboy9696/doc-extract-api))
- **[402Signal](https://402signal.com/route)** — Fail-closed live-endpoint x402 router. POST /route returns a currently-alive x402 URL or an honest miss. $0.01 USDC on Base, Solana, and Algorand. Example: POST {"need":"weather"}. ([OpenAPI](https://402signal.com/openapi.json)) ([MCP](https://402signal.com/mcp.json)) ([Manifest](https://402signal.com/.well-known/x402.json))
<!-- NEW-THIS-WEEK:END -->

---

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/quickstart-dark.svg">
  <img src="assets/sections/quickstart-light.svg" alt="Section: Quick Start" width="680">
</picture>

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
npm install x402-express        # or the core package: @coinbase/x402

# Python
pip install x402
```

_Checked 2026-08-30. There is no published `x402` crate on crates.io; if you are on Rust,
call the HTTP flow directly — it is four steps and they are below._

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

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/howitworks-dark.svg">
  <img src="assets/sections/howitworks-light.svg" alt="Section: How x402 Works" width="680">
</picture>

## How x402 Works

```
1. Client  →  GET /api/data                              (initial request)
2. Server  ←  402 Payment Required                       (payment details in header)
               payment-required: <base64 challenge>       (v2; v1 used X-Payment-Required
                                                           and put the detail in the body)
3. Client  →  EIP-3009 gasless USDC transfer             (client signs + submits)
4. Client  →  GET /api/data  +  X-Payment: {signed tx}  (retry with payment)
5. Facilitator  →  verify + settle on-chain              (~2 seconds)
6. Server  ←  200 OK  +  X-Payment-Response              (resource returned)
```

No gas for the sender. No subscription. No API key. Payment IS authentication.

[Protocol spec →](https://github.com/coinbase/x402) · [EIP-3009 →](https://eips.ethereum.org/EIPS/eip-3009)

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/needmore-dark.svg">
  <img src="assets/sections/needmore-light.svg" alt="Section: Need More?" width="680">
</picture>

## Need More?

This README is the front door. The full curated directory — every shelf, every entry — is in [`directory/`](directory/).

**Other lists worth knowing:** the community [awesome-x402](https://github.com/xpaysh/awesome-x402) accepts everything and is the right place for exhaustive coverage. [Glama](https://glama.ai/mcp/servers) indexes MCP servers at enormous scale and publishes its own health data, which is rarer than it should be. Different jobs. Use all three.

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/contributing-dark.svg">
  <img src="assets/sections/contributing-light.svg" alt="Section: Contributing" width="680">
</picture>

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
