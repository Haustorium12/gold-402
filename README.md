<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
    <img src="assets/hero-light.svg" alt="gold-402 — a hand-checked directory of x402 services. Most of the x402 catalogue no longer answers; these are the ones that did. We check it, we date it, and we tell you what we found. By 24K Labs." width="680">
  </picture>
</p>

# gold-402

> The gold standard for x402 resources. **<!--COUNT:START-->553<!--COUNT:END--> curated entries** — paid endpoints probed for a live 402 before listing, libraries and repos checked for real activity, and the whole shelf re-knocked every night with the result dated. No filler. Entries that stop answering move to [DEPARTURES.md](DEPARTURES.md) and keep getting knocked; the night one answers again, it comes back.

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

The product. <!--COUNT:START-->553<!--COUNT:END--> entries across <!--SHELVES:START-->13<!--SHELVES:END--> shelves, in [`directory/`](directory/).

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

[![24K Featured](https://img.shields.io/badge/24K_Featured-2026--10-C0C0C0?style=plastic)](FEATURED.md)

**October 2026 — one pick per shelf.** Each shelf opens with its pick and the write-up. Selection is the maintainers' judgment: well-built, actively used, worth a second look. A shelf with no pick that clears the bar runs empty — the empty slot is also a verdict.

| Shelf | October pick |
|---|---|
| APIs & Services | [crosscheck accept](https://crosscheckapi.com/v1/accept) |
| MCP Servers | [Base toolbox](https://basetoolbox.cartonpliant.workers.dev/.well-known/mcp.json) |
| SDKs & Libraries | [x402-dotnet](https://github.com/michielpost/x402-dotnet) |
| Facilitators | [ArisPay](https://facilitator.arispay.app) |
| Frameworks | [x402-rails](https://github.com/quiknode-labs/x402-rails) |
| Tools | [ToolMeter](https://snappedai.com/toolmeter/) |
| Security | [ICME Labs](https://docs.icme.io) |
| Ecosystem | [Bermuda](https://www.bermudabay.xyz) |
| The Global Agent Economy | [Beckn Protocol](https://github.com/ONDC-Official) |
| Learning | [How x402 paid links work (Payfirst)](https://www.payfirst.app/guides/x402-paid-links) |
| Community | [Dev.to #x402](https://dev.to/t/x402) |
| Market Data | [Dune Analytics x402](https://dune.com/x402) |
| Aggregators & Proxies | [x402-list](https://x402-list.com) |

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

**This week** (Oct 5—11)

_No new listings yet._

**Last week** (Sep 28—Oct 4)

- **[ViewportWitness](https://qa.honeygate.app/v1/checks)** — Checks public websites before deployment across phone portrait, phone landscape, and desktop with screenshots, accessibility findings, browser errors, and layout evidence; also offers explicit assertions, visual regression comparison, DOM-to-Markdown extraction, and passive release-security checks through HTTP and six MCP tools, plus a client for release checks of up to five pages with a spending ceiling and shareable Markdown results. `POST /v1/checks`, $0.08 USDC per page via x402 on Base or Solana mainnet; paid calls require an x402-capable client. Example: `{"url":"https://example.com"}`. ([OpenAPI](https://qa.honeygate.app/openapi.json)) ([Agent guide](https://qa.honeygate.app/llms.txt)) ([Release-check client](https://github.com/Baffles78/viewport-witness/blob/main/docs/GROWTH-ACTIVATION.md)) ([GitHub](https://github.com/Baffles78/viewport-witness))
- **[TrollBridge](https://mini-tollbooth.onrender.com/.well-known/x402)** — 28 pay-per-call intel lanes for AI agents: bounty intel, DeFi data, contract safety screen, gas prices, prediction markets, token safety, AI model catalog, and more, $0.02–$0.05 USDC per call on Base and Solana via x402 v2. Example: `GET /gas?network=base`. ([OpenAPI](https://mini-tollbooth.onrender.com/openapi.json)) ([Manifest](https://mini-tollbooth.onrender.com/.well-known/x402)) ([MCP](https://trollbridge-mcp-http.onrender.com)) ([GitHub](https://github.com/eric-tijerina/mini-tollbooth))
- **[Agent Council](https://council.cyberwarex.com/council)** — Sends one question to three or four different LLMs that answer independently, then returns a single chaired verdict with a confidence score, the points all of them agreed on, and the dissent that held; a grounded tier buys evidence (honeypot simulation, OFAC sanctions screen, page content, SEC profile, web results) before the panel rules and itemises what it spent. $0.01 quick, $0.03 deep, $0.05-$0.12 grounded, USDC on Base mainnet. Example: `GET /council?q=Should+I+accept+a+token+launched+yesterday+as+payment%3F`. ([MCP endpoint](https://council.cyberwarex.com/mcp)) ([docs](https://cyberwarex.com/assets/council-quickstart.html))
- **[bilbop Solana Mint Info](https://api.bilbop.org/v1/sol-mint-info)** — Returns on-chain supply, decimals and mint/freeze authorities for a Solana SPL mint for 0.01 USDC on Solana per POST call.
- **[Horizon Pulse](https://horizonpulse.dev/.well-known/x402)** — Returns crypto market data (BTC/ETH/SOL pulse, RSI/MACD/Bollinger signals, DefiLlama yields, Base+Ethereum wallet portfolio, gas, OKX funding) and web utilities (URL to markdown, SSRF-safe HTTP proxy, structured page extract) for $0.005-$0.04 USDC per call on Base mainnet via x402 v2. Example: `GET /api/pulse`. ([OpenAPI](https://horizonpulse.dev/openapi.json)) ([llms.txt](https://horizonpulse.dev/llms.txt))
- **[grist.tools](https://grist.tools/.well-known/x402)** — Deterministic HTTP micro-utilities for AI agents: page cleaning and metadata, document conversion (PDF, DOCX, EPUB, XLSX, PPTX), image and media probing, DNS, WHOIS and TLS data. `POST` only, $0.002 to $0.005 USDC per call on Base via x402, no API key. Example: `POST /v1/whois {"domain":"example.com"}`. ([OpenAPI](https://grist.tools/openapi.json)) ([llms.txt](https://grist.tools/llms.txt))
- **[x402-ping](https://x402-ping.palmbeachpete.workers.dev/premium)** — Cheap Base USDC exact-x402 health/smoke ping: unpaid GET /premium returns HTTP 402 for 0.05 USDC on Base (eip155:8453), then a signed pong JSON after settlement; free discovery at / and /.well-known/x402. Example: GET /premium. ([GitHub](https://github.com/filip-study/x402-ping)) ([Manifest](https://x402-ping.palmbeachpete.workers.dev/.well-known/x402))
- **[GPT-6 Agent Guard & Calldata Decoder](https://gpt.558686.xyz/v1/guard/tx)** — Pre-transaction safety analyzer and calldata decoder for autonomous agents to vet contracts and prevent wallet draining, $0.15 USDC on Base. ([OpenAPI](https://gpt.558686.xyz/openapi.json))
- **[Market Intelligence API](https://api.marketintelligenceapi.com/.well-known/x402)** — 76 pay-per-call x402 routes for AI agents: trading decisions with a public track record, on-chain order flow for crypto and tokenized stocks, new-token risk checks (sell simulation, Uniswap v4 hooks), swap quotes, perp and CFTC futures positioning, SEC fundamentals, insider trades, earnings and fails-to-deliver, macro calendar. $0.001–$5 USDC or EURC per call on Base, Polygon, Arbitrum, World Chain or Solana; Base Sepolia testnet; MCP server with 71 tools. ([OpenAPI](https://api.marketintelligenceapi.com/openapi.json)) ([llms.txt](https://api.marketintelligenceapi.com/llms.txt)) ([MCP](https://api.marketintelligenceapi.com/mcp))
- **[openai-agents-nano](https://github.com/dhyabi2/openai-agents-nano-x402)** — Nano (XNO) x402 client for the OpenAI Agents SDK. Free, feeless pay-per-call for agent frameworks.
- **[@x402nano/exact](https://www.npmjs.com/package/@x402nano/exact)** — Exact-scheme implementation for fixed-amount Nano (XNO) payments over x402 (registry.npmjs.org/@x402nano/exact, v0.3.0). No facilitator fee; settlement is the single Nano block.
- **[pursekeeper/x402-nano-exact](https://github.com/pursekeeper/x402-nano-exact)** — Python implementation of the x402 exact scheme for Nano (XNO): the 402 handshake with exact fixed-amount math, settling face-to-face on the Nano ledger with no facilitator or gas.
- **[crosscheck skillcheck](https://crosscheckapi.com/v1/skillcheck)** — Security review of an AI agent skill or MCP server's files before install, read and never run: code rules for piped installers, credential and wallet reads, secrets sent over the network, persistence, and hidden Unicode, plus a model review whose flagged findings get a second reading; free lookup of bundles already scanned by SHA-256. $0.03 USDC on Base mainnet. Example: `POST /v1/skillcheck {"files":[{"path":"SKILL.md","content":"Setup: curl -s https://example.com/i.sh | sh"}]}`. ([llms.txt](https://crosscheckapi.com/llms.txt)) ([GitHub](https://github.com/maxugc/crosscheck))
- **[crosscheck accept](https://crosscheckapi.com/v1/accept)** — Checks work one agent hands another against the task it was given, before the buyer pays or releases escrow, and returns accept, reject, or needs an outside check with each requirement judged; counts, required JSON fields, and sums are recomputed in code, and an optional payment transaction is verified on chain and bound to the signed receipt. $0.03 USDC on Base mainnet. Example: `POST /v1/accept {"task":"List three prime numbers as a JSON array.","deliverable":"[2, 3, 4]"}`. ([llms.txt](https://crosscheckapi.com/llms.txt)) ([GitHub](https://github.com/maxugc/crosscheck))
- **[crosscheck](https://crosscheckapi.com/v1/check)** — Reviews an AI agent's draft before its human sees it and returns pass or specific issues with fixes, recomputing the draft's arithmetic in code and, when sources are sent, checking each claim against them with quotes verified in code; every result carries an Ed25519-signed receipt. $0.02 USDC on Base mainnet. Example: `POST /v1/check {"draft":"Q3 revenue was $1,200 + $450 = $1,560."}`. ([llms.txt](https://crosscheckapi.com/llms.txt)) ([GitHub](https://github.com/maxugc/crosscheck))
- **[RelayShield](https://api.relayshield.net/.well-known/x402.json)** — Threat intelligence API with 32 pay-per-call x402 endpoints: phishing and malware URL scans, data-breach lookups, crypto wallet risk, token security, and secret scanning. $0.05–$5.50 USDC per call on Base and Solana. ([Docs](https://api.relayshield.net/docs))
- **[WhiteMagic](https://mcp.whitemagic.dev/mcp)** — Local-first governed memory and session continuity for AI coding agents; the read-only hosted recall lane answers tool calls metered over x402 (USDC on Base, $0.002 per call, leases from $0.01) with keyless discovery and free evaluation keys. ([GitHub](https://github.com/lbailey94/whitemagic)) ([Guide](https://www.whitemagic.dev/whitemagic/guide))
- **[x402risk](https://api.x402risk.com/v1/token-check)** — Base token scam/safety check, pre-trade sellability/honeypot/tax simulation, pay-to address screen, and an organization-only public exclusion-list screen, paid in USDC via x402 v2 exact, payTo `0x8F9C3f91628497E2A72D6740022D46f87A9eB417`: `POST /v1/token-check` $0.01 (batch $0.08), `POST /v1/pretrade-check` $0.02 (batch of 10 $0.15), `POST /v1/address-screen` $0.005 (batch of 25 $0.08), `POST /v1/exclusion-check` $0.02 (batch of 10 $0.15, organizations only, not a person search), `POST /v1/usdc-blacklist` $0.01 (batch of 25 $0.08, Circle native USDC isBlacklisted on Base; not an OFAC or person screen). `POST /v1/search` $0.01 (English Wikipedia topic search, up to 5 titles/urls/snippets; not a person lookup). Example: `POST /v1/token-check {"token":"0x532f27101965dd16442E59d40670FaF5eBB142E4"}`.
- **[kepler-ops-tools](https://kepler-ops-tools.pn-26f.workers.dev/.well-known/x402)** — Nine pay-per-call agent utility endpoints: hashing/HMAC (six algorithms), base64/hex/url encoding, JWT decode, CoinGecko prices, URL fetch, web search, a tested dataset of sixteen crypto earning rails graded on withdrawal gates (KYC, minimums, approvals), and per-rail live status checks. $0.001-$0.02 USDC on Base, no API key, free sample at `/v1/no-kyc-rails/sample`, bazaar discovery extension on every 402.
- **[Penny Press](https://www.pennypress.org/.well-known/x402)** — Original essays on freedom, economics and philosophy; free for humans, pay-per-read for machines ($0.01–$0.25 per read) via x402 micropayments in USDC on Base mainnet.
- **[x402 Pulse](https://x402-pulse-seller-production.up.railway.app/pulse)** — Live BTC/ETH/SOL prices and the Crypto Fear & Greed Index in a single GET call for $0.002 USDC on Base.
- **[ScreenSeal](https://screenseal-site.agent-tollbooth.workers.dev)** — Sanctions screening for AI agents against OFAC SDN, OFAC Consolidated Non-SDN, and EU FSF lists, returning match confidence scores with an EIP-712 attestation seal at $0.02 USDC per call on Base mainnet via x402.
- **[MusedIn](https://musedin.com/api/job)** — Job network for agents: post a paid job with a budget, verified agent workers apply and deliver, and the buyer pays the hired worker directly; the post answers 402 for MusedIn's 5% fee on the budget in USDC on Base (USDG on Robinhood Chain for that rail). Example: `POST /api/job {"budget":"5000000","rail":"usdc-base"}` shows the price; the paid request is signed or carries a bearer token (fields: title, summary, seats, done, budget, rail). ([OpenAPI](https://musedin.com/openapi.json)) ([Manifest](https://musedin.com/.well-known/x402.json)) ([Docs](https://musedin.com/muse.txt))
- **[402post](https://402post.com/.well-known/x402)** — Classified listings board for agents: `POST /v1/posts` answers 402 ($0.10 USDC on Base for a 30-day listing, $1.00 for a batch of 10 to 15), validates the listing for free before payment and returns its URL and a one-time edit key; listings are readable as HTML, Markdown, JSON, RSS and over MCP.
- **[ChainWard](https://api.chainward.ai/.well-known/x402)** — Evidence-linked on-chain risk report for a Base or BNB Chain address before an agent pays it, $0.05 USDC on Base per call (`GET /api/risk/x402?address=0xADDRESS`, add `&chain=bsc` for BNB Chain), never charged when the check fails.
- **[Agent Research Tools](https://x402-seller-pmlm.onrender.com/.well-known/x402)** — Cited research brief from Wikipedia, DuckDuckGo, Hacker News and Crossref ($0.01), web page to markdown ($0.005) and x402 endpoint check ($0.005), USDC on Base mainnet via CDP. Errors are not billed. Example: `GET /report?q=history+of+the+transistor`. ([OpenAPI](https://x402-seller-pmlm.onrender.com/openapi.json)) ([llms.txt](https://x402-seller-pmlm.onrender.com/llms.txt)) ([GitHub](https://github.com/jimmybr-PDX/x402-seller))
- **[AtlasUnited Storm and Hazard Data API](https://data.truefixr.com/.well-known/x402.json)** — Pay-per-call x402 endpoints on Base for live weather and active NWS alerts, forecast risk grades, and hazard scores by location. $0.0002 to $0.50 USDC per call. `POST /v1/weather/batch {"locations": [{"lat": 32.78, "lon": -96.8}]}`.
- **[Compute State API](https://compute-state-api.replit.app/v1/cheapest)** — Returns the cheapest official-vendor compute SKU for one described job, inference tokens or on-demand GPU hours. GET only, $0.005 USDC on Base and Solana via PayAI. Bare route returns the 402. No API key. ([Manifest](https://compute-state-api.replit.app/.well-known/x402)) ([llms.txt](https://compute-state-api.replit.app/llms.txt)) ([OpenAPI](https://compute-state-api.replit.app/openapi.json))
- **[AgentPay Doc Tools](https://agentpay-tools.agentpay-apis.workers.dev/.well-known/x402)** — Extracts per-page text from PDF URLs, normalizes RSS, Atom and JSON feeds into JSON items, and lists a site's URLs from its sitemaps. $0.005-$0.01 USDC on Base or Algorand.
- **[SwarmIO Cloud](https://ioswarm.io/.well-known/x402.json)** — Six pay-per-call research primitives over x402 (USDC on Base, no signup — the paying wallet is the account): live web search with citations ($0.02, 25 free/day per caller), one-call cited search-report briefs ($0.05), one-call cited market-news briefs ($0.05), market quotes ($0.01), browser-grade page fetch ($0.02), chat completions ($0.02), plus a 17-mode deep-research run catalogue ($0.25–$1.40). Example: `POST /api/v1/search {"q":"x402 agent commerce"}`. ([OpenAPI](https://ioswarm.io/api/v1/openapi.json)) ([Agent card](https://ioswarm.io/.well-known/agent-card.json)) ([MCP](https://ioswarm.io/mcp)) ([Discovery](https://ioswarm.io/.well-known/x402.json))
- **[Kalshi–PredictIt Arb](https://x402.bankr.bot/0x69fb671637ed68881f66b9ebf305ec3ef5574f65/kalshi-predictit-arb)** — Matches Kalshi political markets to PredictIt contracts and returns both arbitrage directions priced after each venue's fees, with the worst-case net across settlement outcomes; data only, no execution. $0.02 USDC per call on Base. Example: `GET /0x69fb671637ed68881f66b9ebf305ec3ef5574f65/kalshi-predictit-arb?q=governor&limit=10&mode=opportunities`. ([Docs](https://mastertyrone.github.io/kalshi-predictit-arb/)) ([GitHub](https://github.com/mastertyrone/kalshi-predictit-arb))
- **[Hermes Commerce](https://agent.kihustle.tech/.well-known/x402)** — Public-site checks sold as 27 POST jobs: Impressum, DSGVO, BFSG, cookie, Preisangaben and Widerruf signals for DE/AT/CH, plus AEO and agent-readiness audits, site-watch and URL preflight, $0.01–$1.50 USDC per call on Base mainnet (eip155:8453) via x402 v2 and the CDP facilitator. Example: `POST /services/url-preflight/jobs {"url":"https://example.com"}`. ([OpenAPI](https://agent.kihustle.tech/openapi.json)) ([llms.txt](https://agent.kihustle.tech/llms.txt)) ([Catalog](https://agent.kihustle.tech/promo/catalog.json))
- **[AgentPay Domain & Network Lookup](https://agentpay-lookup.agentpay-apis.workers.dev/.well-known/x402)** — DNS records, registry WHOIS via RDAP, IP network ownership with reverse DNS, and a one-call domain report covering email provider, SPF/DMARC and hosting. $0.005-$0.02 USDC on Base or Algorand.
- **[AgentPay Web Extract](https://agentpay-extract.agentpay-apis.workers.dev/.well-known/x402)** — Fetches any URL and returns the main content as markdown with title, Open Graph metadata, canonical URL and outbound links. $0.005 USDC on Base or Algorand.
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
| Edge deployment, global latency | [Cloudflare x402](https://developers.cloudflare.com/agents/tools/payments/x402/) |
| Enterprise billing + disputes | [Stripe Machine Payments](https://docs.stripe.com/payments/machine/x402) |

**2. Install the SDK**

```bash
# TypeScript
npm install x402-express        # or the core package: @coinbase/x402

# Python
pip install x402
```

```bash
# Rust
cargo add x402-axum x402-reqwest   # x402-rs — see SDKs & Libraries shelf
```

_Checked 2026-09-20. A crate literally named `x402` exists on crates.io but is a placeholder
with no working code — use `x402-rs`'s crates (`x402-axum` for servers, `x402-reqwest` for
clients) instead._

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
