<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
    <img src="assets/hero-light.svg" alt="gold-402 — a hand-checked directory of x402 services. Most of the x402 catalogue no longer answers; these are the ones that did. We check it, we date it, and we tell you what we found. By 24K Labs." width="680">
  </picture>
</p>

# gold-402

> The gold standard for x402 resources. **<!--COUNT:START-->544<!--COUNT:END--> curated entries** — paid endpoints probed for a live 402 before listing, libraries and repos checked for real activity, and the whole shelf re-knocked every night with the result dated. No filler.

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

The product. <!--COUNT:START-->544<!--COUNT:END--> entries across <!--SHELVES:START-->13<!--SHELVES:END--> shelves, in [`directory/`](directory/).

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
  <img src="assets/sections/verified-light.svg" alt="Section: What being on this list means" width="680">
</picture>

## What being on this list means

There is no stamp. There was one — "Gold402 Verified," one tier, a gold tick — and it was
retired on 2026-09-06 because it said the identical thing about a paid API we knocked last
Tuesday, a community wiki with no endpoint to knock at all, and an entry we hold no dated
receipt for. A mark that everything wears certifies nothing. We have made that criticism of
other people's badges and it was true of ours.

What every entry now carries instead is the finding, per entry:

- **A date** — *this endpoint answered an HTTP 402 when we knocked it, on this day.* An
  automated gate checks the submission, a maintainer confirms it before merge, and a sweep
  re-knocks and writes a dated result. A date is checkable. A tick is not.
- **Or "listed — no knock receipt"** — a human read it and it is on the list. We hold no
  dated knock, and we will not backfill a date we cannot show.
- **Or "listed — no endpoint to knock"** — libraries, guides, wallets, clients and
  community resources. Nothing here answers a 402 because that is not what these things
  do. We read them, and we checked they were publicly reachable.

**None of it is a delivery test.** We have not paid these services and graded what came
back. Read any of it as "we checked what is stated above," never as "this is worth the
money."

**Some entries carry more.** Where we have paid for a service and confirmed what came back,
we say so and keep the receipt — what we sent, what it cost, the transaction hash, what
arrived. That is a stronger claim and we only make it about services we actually bought.
Most of the list has not been through that, and we would rather say so than imply otherwise.

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

**This week** (Sep 7—13)

- **[Gardenpatch Growth Coaches](https://gardenpatch.xyz/.well-known/x402)** — Seven growth coaches (strategy, sales, marketing, operations, retention, technology, people) answering a mode plus messages with a typed JSON deliverable, USDC on Base at $0.18 to $0.45 per call. Example: `POST /api/v1/agents/mary/call {"mode":"diagnose_growth","messages":[{"role":"user","content":"Revenue is flat at $40k/mo. Where are we stuck?"}]}`. ([OpenAPI](https://gardenpatch.xyz/openapi.json)) ([Catalog](https://gardenpatch.xyz/api/v1/agents)) ([Skill](https://gardenpatch.xyz/skills/gardenpatch-x402/SKILL.md))
- **[webcap](https://nickname-trident-driveway.ngrok-free.dev/.well-known/x402)** — Web capture API with five pay-per-call routes: page screenshots, structured content extraction, SEO audits, site mapping, and scroll-capture video, $0.001-$0.01 USDC on Base via x402 with no API keys. Example: `POST /v1/x402/capture {"url":"https://example.com"}`.
- **[Council of AI](https://councilof.ai/api/eunomia-data?feed=1)** — Independent AI-behaviour measurement packs and EU AI Act evidence over x402 on Base; GET /api/gspc is free, paid doors answer 402 with catalog query params. Example: `GET /api/eunomia-data?feed=1`. ([OpenAPI](https://councilof.ai/openapi.json)) ([Manifest](https://councilof.ai/.well-known/x402.json)) ([MCP](https://councilof.ai/mcp)).
- **[Council of AI GSPC MCP](https://councilof.ai/mcp)** — Measurement MCP (not certification). Free board tools; paid tools over x402 (`art50_marking_evidence`, `rwa_evidence`, `receipts_batch`, `commission_card`). Remote `https://councilof.ai/mcp`. npm `csoai-gspc-mcp`. ([OpenAPI](https://councilof.ai/openapi.json)) ([Manifest](https://councilof.ai/.well-known/x402.json)) ([x402scan](https://www.x402scan.com/server/9b8bcb34-6c9f-45d6-b881-9a6afe7bf6b5)).
- **[Base toolbox](https://basetoolbox.cartonpliant.workers.dev/.well-known/x402.json)** — Base Uniswap v3 swap preflight, leftover allowances, tx explain, and transfer check at $0.10 USDC on Base via x402, plus $0.01 price/gas/ENS. Example: `POST /v1/preflight {"from":"0xYourWallet","tokenIn":"USDC","tokenOut":"WETH","amountIn":"1000000"}`. ([Skill](https://basetoolbox.cartonpliant.workers.dev/SKILL.md)) ([OpenAPI](https://basetoolbox.cartonpliant.workers.dev/openapi.json)) ([Constants](https://basetoolbox.cartonpliant.workers.dev/v1/constants)).
- **[Base toolbox](https://basetoolbox.cartonpliant.workers.dev/.well-known/mcp.json)** — Remote MCP for Base before you sign: Uniswap v3 swap preflight, leftover allowances, tx explain, transfer check ($0.10 USDC), plus $0.01 price/gas/ENS. GET /v1/constants free. ([MCP](https://basetoolbox.cartonpliant.workers.dev/mcp)) ([OpenAPI](https://basetoolbox.cartonpliant.workers.dev/openapi.json)) ([Skill](https://clawhub.ai/cartonpliant/skills/basetoolbox))
- **[Veriton HTML→JSON](https://veriton-html-json-api.netlify.app/v1/html-to-json)** — Metered HTML to structured JSON for agents (title/meta/links/headings/images); $0.02 body / $0.05 fetch USDC on Base; prepaid credits or HTTP 402. Example: `POST /v1/html-to-json {"html":"<html><title>Hi</title><h1>X</h1></html>","selector":"h1"}` . ([Docs](https://veriton-dev.github.io/veriton-micro-dev/api/)) ([OpenAPI](https://veriton-html-json-api.netlify.app/v1/openapi.json)) ([Manifest](https://veriton-html-json-api.netlify.app/.well-known/x402)) ([MCP](https://veriton-html-json-api.netlify.app/mcp)) ([GitHub](https://github.com/veriton-dev/veriton-micro-dev))
- **[url2md](https://url2md.io/v1/md?url=https%3A%2F%2Fexample.com)** — Converts one public URL to clean Markdown through a single conversion engine for static pages, JavaScript-rendered pages (headless browser) and PDFs, honours robots.txt per RFC 9309, and pays an upstream x402 toll on the caller's behalf when the target page charges one (quoted at toll + 25%, cap $0.05 per toll); $0.005 USDC on Base via the Coinbase CDP facilitator. Example: `GET /v1/md?url=https://example.com` or `POST /v1/md {"url":"https://example.com"}`. ([OpenAPI](https://url2md.io/openapi.json)) ([MCP server](https://www.npmjs.com/package/@url2md-io/mcp)) ([llms.txt](https://url2md.io/llms.txt))
- **[Video Download AI](https://video-download.ai/.well-known/x402)** — Downloads authorized public media URLs as MP4 video or MP3 audio with duration-based pricing from $0.0005 per started minute, paid in USDC on Base via x402 v2. ([OpenAPI](https://video-download.ai/openapi.json)) ([llms.txt](https://video-download.ai/llms.txt))
- **[Nano CSV service](https://nano-csv-service.onrender.com/clean)** — Deduplicates up to 5,000 CSV records by exact composite string keys, preserving the first row, for 0.1 XNO per request over x402 v2 on Nano mainnet ([source and usage](https://github.com/Reeyenn/nano-csv-service)).
- **[Torquantis](https://torquantis.com/x402)** — Order-book exchange where AI agents buy and sell units of work (research briefs, code tasks, agent hours, GPU hours, inference, transcription, web fetching, human checks) from each other in USDC on Base, with escrow, three AI judges for disputes, an MCP server at `/mcp`, and an x402 door on every market at `POST /x402/buy/<market>` that answers 402 whenever a seller has a standing ask.
- **[Kael Ecosystem Pulse](https://kael-ecosystem-pulse.onrender.com/.well-known/x402)** — Paid 24h Solana ecosystem digest for agents via x402 Exact SVM USDC on Solana mainnet (PayAI facilitator): full pulse $0.10, headlines $0.02, delta $0.08, evidence $0.05; free sample and tip-jar metadata. Informational synthesis only — not financial advice or trading signals. Example: `GET /v1/pulse?ecosystem=solana&window=24h`. ([llms.txt](https://kael-ecosystem-pulse.onrender.com/llms.txt) | [Sample](https://kael-ecosystem-pulse.onrender.com/v1/pulse/sample) | [Tip](https://kael-ecosystem-pulse.onrender.com/tip))
- **[Vega URL Extractor](https://extract.kramsg1online.com/extract)** — Extract clean text from any web page URL. x402 on Base mainnet, $0.05 USDC per call. `POST /extract {"url": "..."}`. (OpenAPI: https://extract.kramsg1online.com/openapi.json)
- **[Vega PDF Extractor](https://pdf.kramsg1online.com/extract)** — Extract text from PDF files. x402 on Base mainnet, $0.05 USDC per call. `POST /extract multipart/form-data file`. (OpenAPI: https://pdf.kramsg1online.com/openapi.json)
- **[Vega Article Summarizer](https://summarize.kramsg1online.com/summarize)** — Summarize articles and URLs into key points. x402 on Base mainnet, $0.02 USDC per call. `POST /summarize {"url": "..."}`. (OpenAPI: https://summarize.kramsg1online.com/openapi.json)
- **[Basalt](https://basalt-n6lt.onrender.com/.well-known/x402.json)** — 8 pay-per-call utility tools for AI agents: URL metadata extraction, domain availability via RDAP, email/MX validation, HTML-to-Markdown, QR code generation, PDF text extraction, TLS certificate checks, and language detection (186 languages). $0.002-$0.01 USDC on Base. Example: `POST /domain-check {"domain":"example.com"}`. ([OpenAPI](https://basalt-n6lt.onrender.com/openapi.json))
- **[gravee](https://engine-production-3a58.up.railway.app)** — 23 pay-per-call business lead generation and market intelligence endpoints: scored leads by vertical and location, business scoring, contact extraction, competitor analysis, multi-source verification, digital health audits, WHOIS, social presence, tech stack detection, formation data, hiring signals, review aggregation, market saturation, gap analysis, growth trajectory, website status, email and phone verification, competitive pricing. $0.005–$0.75 USDC per call on Base and Solana. No API keys — wallet is auth. ([Manifest](https://engine-production-3a58.up.railway.app/.well-known/x402.json)) ([llms.txt](https://engine-production-3a58.up.railway.app/llms.txt))

**Last week** (Aug 31—Sep 6)

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
- **[How x402 paid links work (Payfirst)](https://www.payfirst.app/guides/x402-paid-links)** — Guide to x402 V2 payment headers, URL delivery, buyer-client requirements, and retry handling when settlement is uncertain.
- **[FractalAI x402 Proofs](https://fractalai.net.co/.well-known/x402.json)** — Seven pay-per-call endpoints on Base (x402 v2, USDC via EIP-3009 gasless settlement) signing with ML-DSA-65/Dilithium-3 (NIST FIPS 204): message signing and verification, AI-decision attestation, and provenance/CBOM sealing, each response independently verifiable offline against the exact signed bytes returned; a companion `@x402/core` extension, [`@fractalai/x402-pqc-witness`](https://www.npmjs.com/package/@fractalai/x402-pqc-witness), adds the same post-quantum settlement attestation to any resource server.
- **[DNS Doctor](https://dnsdoctor.dev/.well-known/x402.json)** — Email-authentication and DNS diagnostics for agents: SPF, DMARC, DKIM, MX, blacklists, domain/SSL expiry and six-vantage propagation, returning deterministic copy-paste fix records. Bulk scans $0.005 per domain, 24h propagation and HTTP-ping watches $0.10–$0.25, USDC on Base (x402 v1+v2). Example: `POST https://dnsdoctor.dev/api/v1/bulk-scan {"domains":["example.com","example.org"]}` ([OpenAPI](https://dnsdoctor.dev/openapi.json), [docs](https://dnsdoctor.dev/learn/x402-agent-payments))
- **[Israel Invoice Payment Gate](https://israel-counterparty-intelligence.vercel.app/v1/invoice-gate/mainnet)** — Pre-payment gate for Israeli tax invoices and accounts-payable agents. Checks VAT arithmetic and totals, applies Israel Invoices allocation-number rules using date, amount, VAT and buyer-attested conditions, resolves the supplier against public-registry evidence, and returns deterministic PAY, HOLD, or BLOCK reason codes. $0.25 USDC per POST on Base mainnet via x402 v2, with no account or API key. It does not verify bank-account ownership or independently authenticate buyer-supplied Tax Authority results. Example: `POST /v1/invoice-gate/mainnet {"supplier_company_number":"514744887","invoice_number":"INV-2026-001","invoice_date":"2026-09-04","amount_before_vat":6000,"vat_amount":1080,"total_amount":7080}`. ([Free preview](https://israel-counterparty-intelligence.vercel.app/v1/invoice-gate/preview)) ([OpenAPI](https://israel-counterparty-intelligence.vercel.app/openapi.json)) ([Manifest](https://israel-counterparty-intelligence.vercel.app/.well-known/x402))
- **[aiworker-data](https://aiworker.duckdns.org/openapi.json)** — DeFi yield pools and single-protocol snapshots from DefiLlama (refreshed every 5 minutes), plus clean-Markdown and LLM-summary fetch of any public page. Four endpoints, $0.01–$0.04 USDC per call on Base and Solana via PayAI, settled only after a successful response. Example: `GET /v1/defi/protocol/aave-v3`; `POST /v1/scrape/markdown {"url":"https://example.com"}`. ([OpenAPI](https://aiworker.duckdns.org/openapi.json)) ([MCP](https://aiworker.duckdns.org/mcp)) ([Site](https://aiworker.duckdns.org/))
- **[aiworker-data MCP](https://aiworker.duckdns.org/mcp)** — Remote streamable-http MCP with four paid tools: `defi_yields` and `defi_protocol` (DefiLlama data, refreshed every 5 minutes), `scrape_markdown` and `scrape_summary` (public page to clean Markdown, optionally LLM-summarised). $0.01–$0.04 USDC per call on Base and Solana via x402, settled only after a successful response; listed in the official MCP Registry as `org.duckdns.aiworker/aiworker-data`. Example tool call: `defi_protocol {"slug":"aave-v3"}`. ([OpenAPI](https://aiworker.duckdns.org/openapi.json)) ([Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=aiworker-data))
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
