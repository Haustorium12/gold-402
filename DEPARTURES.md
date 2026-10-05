# Departures

Thank you for staying with us.

Every entry below was listed on a gold-402 shelf and stopped answering our nightly knock. It moved here so the shelf files list only entries that answered their last knock. Each line is kept exactly as it was listed, under the shelf and section it came from.

This is a record, not a verdict. A departure date says an endpoint stopped answering us. It does not say why, and it says nothing about the business behind it. Every entry here is still knocked every night. The night one answers again, its line goes back to its shelf.

Dates for every entry (first failed knock, last answer, returns) are in [24klabs.ai/graveyard.json](https://24klabs.ai/graveyard.json). The page is [24klabs.ai/graveyard](https://24klabs.ai/graveyard).

## aggregators

### Unfiled

- [Orders of Magnitude](https://x402-api-production-5133.up.railway.app/x402.json) — Unified pay-per-call access to 1,100+ public and utility API endpoints through one wallet. $0.003–$0.10 per call, machine-readable manifest at `/x402.json` (mirrored at `/.well-known/x402`). x402 v2, USDC on Base.

## apis

### AI Services

- [MOSS Agent](https://moss.chobon.top) — AI-powered coding services: code review ($0.005), translation ($0.003), code explanation ($0.003). A2A protocol compatible.
- [RGX](https://rgx.tail817c3b.ts.net) — Snap Router: task-to-tool selection over the merged x402 Bazaar and MCP Registry catalog (16k+ entries), one pass, no LLM call, $0.003 USDC. Example: `POST /v1/snap?x402force=1 {"task":"check a base token for honeypot","k":4}`. Pricing-Truth: real tradeable depth vs headline TVL, depth-weighted multi-pool price corroboration, and a live buy-then-sell honeypot/transfer-tax check for tokens on Base, Ethereum, and Arbitrum, $0.005-$0.04 USDC. Example: `GET /v1/base/token/0x532f27101965dd16442E59d40670FaF5eBB142E4/report?x402force=1`. Free tier, CDP facilitator. ([Manifest](https://rgx.tail817c3b.ts.net/.well-known/x402)) ([OpenAPI](https://rgx.tail817c3b.ts.net/openapi.json)) ([llms.txt](https://rgx.tail817c3b.ts.net/llms.txt)) ([MCP](https://pypi.org/project/rgx-mcp/))

### Business Intelligence

- [Kerdos Market Intelligence](https://nonvisceral-eloisa-mousily.ngrok-free.dev) — AI market intelligence for agents and traders. 8 endpoints: live crypto sentiment, BTC/ETH regime direction, Hyperliquid funding rates, gold/oil signals, whale alerts, liquidation cascade risk. $0.01-$0.05 USDC on Base.
- [Public Tenders ES/EU](https://public-tenders-es-eu-325572559480.us-central1.run.app) — Normalized search over public-sector tenders published in TED (EU official procurement notices), covering Spain plus the rest of the EU above the EU publication threshold, filterable by country/keyword/CPV code/recency. $0.01 USDC on Base Sepolia (testnet) via x402. Example: `POST /search-public-tenders {}`. ([OpenAPI](https://public-tenders-es-eu-325572559480.us-central1.run.app/openapi.json)) ([Agent Card](https://public-tenders-es-eu-325572559480.us-central1.run.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/public-tenders-es-eu))

### Crypto & DeFi Data

- [apix402](https://api402x.com/.well-known/x402.json) — Sixteen paid endpoints for agents, each answering against the source that decides rather than a summary of it: DAO proposal execution, Safe owner/threshold/module drift, oracle staleness per feed, Aave wstETH depeg exposure, token vesting and insider early-sale checks, plus package, advisory, MCP-server, RPC and x402-listing checks read from the registry or the endpoint itself; $0.001-$0.05 USDC per call on Base, no signup; every route also has a `/preview` path that returns the response shape and a worked example rather than running the check. ([x402](https://api402x.com/.well-known/x402)) ([OpenAPI](https://api402x.com/openapi.json))
- [Automaton Oracle](https://automaton-oracle.xyz) — Sovereign crypto intelligence: real-time prices, global macro intelligence, pump.fun graduation radar, trading signals, meme generation. Self-hosted facilitator (no Coinbase CDP dependency). $0.005-$0.05 USDC on Base.
- [CapGain safety and work artifacts](https://5-9-107-124.nip.io) — EVM token risk and Base swap preflights from $0.01, plus machine-buyable invariant tests ($0.03), repository reviews ($0.05), and protocol research ($0.03), paid in Base USDC via x402. ([x402](https://5-9-107-124.nip.io/.well-known/x402.json))
- [Crysha Price Oracle](https://api.crysha.com) — Aggregated crypto prices (multi-source BTC/others). $0.001/call on Base USDC.
- [DeepBlue Trading API](https://api.deepbluebase.xyz) — AI-powered crypto intelligence from an autonomous trading team running real money on Polymarket. 21 endpoints. $0.01-$0.05 USDC on Base.
- [Excelexi](https://api.excelexi.com/api/v1/technical-analysis?symbol=BTCUSDT) — Technical-indicator and market-analysis API for trading agents: 73 indicators and 24 derived signals across 100 crypto markets, plus screening, analytics snapshots/history, and a natural-language endpoint that compiles a plain sentence into a deterministic query before executing it. Every returned value carries provenance — which bars were used, whether the indicator's warm-up period was satisfied, the data's age, and the upstream source — so a caller can verify freshness before acting on it. Example: `GET /api/v1/technical-analysis?symbol=BTCUSDT&interval=1h`. $0.00002-$0.0005 USDC on Base mainnet via x402 v2 (EIP-3009), 9 payable endpoints, no API key and no signup. ([OpenAPI](https://api.excelexi.com/openapi.json)) ([Discovery](https://api.excelexi.com/.well-known/x402)) ([Docs](https://excelexi.com/for-agents))
- [Hodler DeFi Intelligence](https://x402.hodle.com.br) — Stablecoin monitoring, redeem arbitrage, cross-chain pair discovery across 10 EVM chains. 6 paid endpoints at $0.01 USDC via xpay.sh on Base.
- [On-Chain Activity Index](https://onchain-activity-index-325572559480.us-central1.run.app) — 0-100 quantitative DeFi Protocol Activity Index computed from real public DefiLlama data (TVL trend, fee/volume activity trend, chain diversification); explicitly a descriptive index, not trading advice. $0.30 USDC on Base Sepolia (testnet) via x402. Example: `POST /activity-index {"protocol_slug":"uniswap"}`. ([OpenAPI](https://onchain-activity-index-325572559480.us-central1.run.app/openapi.json)) ([Agent Card](https://onchain-activity-index-325572559480.us-central1.run.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/onchain-activity-index))
- [x402 Crypto Research API](https://x402-crypto-research-api-production.up.railway.app/research) — Generates current, source-linked cryptocurrency ecosystem research reports for 0.01 USDC per POST request on Base mainnet. Example: `{"topic":"Give a concise current status update on the Base ecosystem."}`. ([GitHub](https://github.com/stgzwpzy8w-eng/x402-crypto-research-api))

### Data & Research

- [Animica Research](https://animica.dev/x402/research) — One call that searches the web, fetches the top pages and returns their readable text with every requested URL accounted for; $0.02 USDC on Base or ANM natively at a 25% discount, free trial per client per day. Example: `POST /x402/research {"query":"post-quantum blockchain signatures","pages":4}`. ([Manifest](https://animica.dev/.well-known/x402)) ([OpenAPI](https://animica.dev/openapi.json)) ([llms.txt](https://animica.dev/llms.txt))
- [AnyBrowse](https://anybrowse.dev) — Autonomous web browsing agent. Converts URLs to LLM-ready Markdown via real Chrome browsers. USDC on Base.
- [Calibrated Similarity Search API](https://similarity-search-api-production.up.railway.app) — Stateless NMI + cosine fusion similarity search over pre-computed numeric vectors, with an entropy-calibrated blending weight (alpha) computed per request; vectors only, no server-side embedding. $0.01 USDC on Base Sepolia (testnet) via x402, no API key required. Example: `POST /similarity/search {"query":{"id":"q1","vector":[0.1,0.2,0.3]},"corpus":[{"id":"c1","vector":[0.1,0.2,0.3]}]}`. ([OpenAPI](https://similarity-search-api-production.up.railway.app/openapi.json)) ([Agent Card](https://similarity-search-api-production.up.railway.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/similarity-search-api-sdk))
- [Nano CSV service](https://nano-csv-service.onrender.com/clean) — Deduplicates up to 5,000 CSV records by exact composite string keys, preserving the first row, for 0.1 XNO per request over x402 v2 on Nano mainnet ([source and usage](https://github.com/Reeyenn/nano-csv-service)).
- [panevin-x402-api](https://api.panevin.net) — Web content extraction and AI processing. 8 endpoints: text extraction, link extraction, metadata, markdown conversion, AI summarization, translation, structured data extraction. $0.001-$0.008 USDC on Base.
- [TaskMarket Data API](https://site-wine-nu-93.vercel.app/api/tm_list_tasks) — Read-only TaskMarket bounty-market data for AI agents: list open tasks (rewards, deadlines, submission demand), full task details by ID, per-task submissions. $0.001/call USDC on Base via x402 v1 exact scheme (EIP-3009) — real on-chain enforcement through the non-custodial xpay facilitator, no CDP key needed. Unpaid requests get a spec-compliant 402 with payment terms. Built by Autonomy Labs, an autonomous AI agent. ([Discovery](https://site-wine-nu-93.vercel.app/.well-known/x402)) ([llms.txt](https://site-wine-nu-93.vercel.app/llms.txt)) ([GitHub](https://github.com/Autonomy-Labs-Tech/taskmarket-mcp))
- [The Bot Wire](https://thebotwire.com) — 57 primary-source data wires for AI agents: SEC EDGAR, Federal Register, federal court opinions, congressional bills, DOJ, FDA, Federal Reserve and ECB, BLS/BEA releases, CISA CVEs, cloud outages, NWS alerts, USGS quakes, arXiv, WHO/CDC, European Commission, GOV.UK, NASA, EIA, plus 40 curated news sources. $0.005–$0.01 USDC on Base, free 3-result preview on every wire. Example: `GET /fed/latest?src=fomc&since=30d`. ([Manifest](https://thebotwire.com/.well-known/x402)) ([OpenAPI](https://thebotwire.com/openapi.json)) ([Routing table](https://thebotwire.com/llms-full.txt))
- [Veriton HTML→JSON](https://veriton-html-json-api.netlify.app/v1/html-to-json) — Metered HTML to structured JSON for agents (title/meta/links/headings/images); $0.02 body / $0.05 fetch USDC on Base; prepaid credits or HTTP 402. Example: `POST /v1/html-to-json {"html":"<html><title>Hi</title><h1>X</h1></html>","selector":"h1"}` . ([Docs](https://veriton-dev.github.io/veriton-micro-dev/api/)) ([OpenAPI](https://veriton-html-json-api.netlify.app/v1/openapi.json)) ([Manifest](https://veriton-html-json-api.netlify.app/.well-known/x402)) ([MCP](https://veriton-html-json-api.netlify.app/mcp)) ([GitHub](https://github.com/veriton-dev/veriton-micro-dev))

### Finance & FX

- [Colombia TRM](https://x402.lagaceta.net/trm) — Official Superintendencia Financiera daily USD/COP TRM as prepaid x402 at $0.005 USDC on Base. ([OpenAPI](https://x402.lagaceta.net/openapi.json)) ([llms.txt](https://x402.lagaceta.net/llms.txt))

### Infrastructure APIs

- [dTelecom STT](https://x402stt.dtelecom.org) — Real-time speech-to-text API. Dual-engine (Parakeet-TDT + Whisper), 99+ languages, hallucination filtering. $0.005/min. Built on dTelecom DePIN.
- [WebSocket Session Manager API](https://npm-package-ws-has-241560546-w-production.up.railway.app) — Stateful WebSocket session registry that proxies a connection to a target URL and scores each inbound frame with a Shannon entropy delta for schema-divergence detection; free once a session is open. $0.01 USDC on Base Sepolia (testnet) via x402, charged only on session open. Example: `POST /ws-sessions/open {"target_url":"wss://echo.websocket.org"}`. ([OpenAPI](https://npm-package-ws-has-241560546-w-production.up.railway.app/openapi.json)) ([Agent Card](https://npm-package-ws-has-241560546-w-production.up.railway.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/npm-package-ws-has-241560546-weekly-downloads-but-sdk))

### Niche & Specialty

- [CentRake](https://centrake.biz) — Universal calculator with 3-layer self-correcting verification. 5-tier dynamic pricing: $0.01 basic solve to $0.15 AI action plans. 438+ problem categories. Free for humans, paid for AI agents.
- [New x402 Listings Feed](https://new-x402-listings-feed-325572559480.us-central1.run.app) — Feed of x402/L402 services newly listed on 402index.io within a caller-specified recency window (default 24h, max 7 days), filterable by protocol/category/payment network; packages 402index.io's public catalog rather than an exclusive data source, declared as such in every response. $0.01 USDC on Base Sepolia (testnet) via x402. Example: `POST /new-x402-listings {}`. ([OpenAPI](https://new-x402-listings-feed-325572559480.us-central1.run.app/openapi.json)) ([Agent Card](https://new-x402-listings-feed-325572559480.us-central1.run.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/new-x402-listings-feed))
- [Smart Event Scraper](https://smart-event-scraper-agent.onrender.com/.well-known/x402) — Aggregates events from Eventbrite, Meetup, AllEvents, District, EventsEye, and ConferenceAlerts into one standardized dataset. `POST /api/scrape-events {"search_query":"developer conference","category":"tech","location":"New York","limit":5}` — $0.01-$2.00 USDC on Base, price scales with requested result volume. ([OpenAPI](https://smart-event-scraper-agent.onrender.com/openapi.json)) ([llms.txt](https://smart-event-scraper-agent.onrender.com/llms.txt))
- [Video Download AI](https://video-download.ai/.well-known/x402) — Downloads authorized public media URLs as MP4 video or MP3 audio with duration-based pricing from $0.0005 per started minute, paid in USDC on Base via x402 v2. ([OpenAPI](https://video-download.ai/openapi.json)) ([llms.txt](https://video-download.ai/llms.txt))

### Production Deployments (High Volume)

- [Visibility AI Audit API](https://visibility.gleefulai.com) — AI-visibility and AEO audit for websites: agent-readiness scoring (llms.txt, schema, bot access, FAQ), generated fixes, and competitor gap analysis. Pay-per-call USDC on Base via x402, no API keys. ([OpenAPI](https://visibility.gleefulai.com/openapi.json)) ([Docs](https://visibility.gleefulai.com/docs))

### Security

- [ERC-8004 Agent Liveness](https://erc8004-agent-liveness-325572559480.us-central1.run.app) — Checks whether an agent registered in the real ERC-8004 Identity Registry (Base Sepolia testnet) is actually alive right now: resolves its on-chain registration file and runs a real MCP `initialize` handshake against the declared endpoint. $0.10 USDC on Base Sepolia (testnet) via x402. Example: `POST /verify-registered-agent {"agent_id":1}`. ([OpenAPI](https://erc8004-agent-liveness-325572559480.us-central1.run.app/openapi.json)) ([Agent Card](https://erc8004-agent-liveness-325572559480.us-central1.run.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/erc8004-agent-liveness))
- [Live Entity Verification API](https://live-entity-verification-production.up.railway.app) — Cross-signal Bayesian corroboration of entity existence: fuses WHOIS, Certificate Transparency, Wayback Machine, and DNS operational maturity into a calibrated hallucination verdict with a confidence score. $0.01-$0.05 USDC on Base Sepolia (testnet) via x402, tiered per route. Example: `POST /verify-entity-existence-cross-signal {"domain":"example.com","entity_name":"Example Corp"}`. ([OpenAPI](https://live-entity-verification-production.up.railway.app/openapi.json)) ([Agent Card](https://live-entity-verification-production.up.railway.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/live-entity-verification-sdk))
- [Mossgate Trust API](https://api.mossgate.dev) — Onchain risk checks for Base ERC-20 tokens and wallets: token verdict returns ok/caution/danger with liquidity, pair age, 24h volume, and contract flags; wallet profile returns onchain reputation for a counterparty. $0.01-$0.25 USDC on Base. ([llms.txt](https://api.mossgate.dev/llms.txt))
- [x402 Receipt Verifier](https://x402-receipt-verifier-325572559480.us-central1.run.app) — Audits NEXUS's own x402 payment logs against its own delivery logs and issues a signed HMAC receipt proving a specific payment correlates with a real, successful delivery; signature-only verification is free. $0.02 USDC on Base Sepolia (testnet) via x402 on the 2 paid routes. Example: `POST /verify-payment-receipt {"asset_name":"document-conversion-api","payer_address":"0x0000000000000000000000000000000000dEaD","claimed_amount_usd":0.01,"claimed_at":"2026-08-24T00:00:00Z"}`. ([OpenAPI](https://x402-receipt-verifier-325572559480.us-central1.run.app/openapi.json)) ([Agent Card](https://x402-receipt-verifier-325572559480.us-central1.run.app/.well-known/agent-card.json)) ([GitHub](https://github.com/nexus-mcp-infra/x402-receipt-verifier))

### Web & Geospatial

- [PortsideLabs Places API](https://portsidelabs-x402-places-536698811508.us-west1.run.app) — Google Places API v1 proxy. Place detail lookup and full-text search. $0.001 USDC on Base and Solana.
- [Rue Render API](https://rue.mossgate.dev) — Renders a URL or raw HTML to PDF, PNG, or JPEG via headless Chromium, SSRF-guarded. $0.003 USDC on Base via x402.
- [Venture Reader](https://api.venturebot.party/extract) — Extracts one public web page to clean Markdown for LLM pipelines using Mozilla Readability and Turndown with GFM tables, $0.01 USDC per call on Base verified on-chain with no facilitator, and no charge for failed extracts; operated as a disclosed autonomous AI-agent business. Example: `GET /extract?url=https://example.com`. ([Manifest](https://api.venturebot.party/.well-known/x402.json)) ([OpenAPI](https://api.venturebot.party/openapi.json))

## community

### Events

- [ETHDenver x402 Workshop](https://www.youtube.com/watch?v=ethdenver-x402) — Hands-on workshop from ETHDenver 2025.

## ecosystem

### Agent Frameworks

- [Faremeter](https://faremeter.io) — Universal framework for transparent API cost integration into agent workflows. Agents discover, negotiate, and pay for services via x402. 66★

### Agent Wallets

- [CardZero](https://cardzero.ai) — ERC-4337 smart contract wallets for AI agents. Owner-controlled spending rules (per-tx limits, daily caps, whitelist, freeze). x402 buyer support via `POST /v1/x402/pay`. [GitHub](https://github.com/mrocker/CardZero)
- [OpenVPS](https://openvps.sh) — AI-agent VPS hosting. Pay USDC on Base, Celo, or Tempo — get root SSH to Ubuntu 24.04 Firecracker microVMs in seconds. x402 + MPP dual-protocol. From $0.005/hr. ([GitHub](https://github.com/kartojal/openvps))

## learning

### Blog Posts & Articles

- [Calmops: x402 Protocol Complete Guide 2026](https://calmops.com/web3/x402-protocol-programmable-payments-ai-agents-2026/) — Programmable payments for AI agents guide.
- [Lushbinary: x402 & EmDash Content Monetization](https://lushbinary.com/blog/x402-emdash-content-monetization-ai-agent-era-2026/) — x402 + Cloudflare EmDash as the content monetization stack for the AI era.

## market-data

### Analytics Dashboards

- [MCP Scores](https://mcpscores.com) — Reliability register + x402 money-flow observatory over 36K+ MCP/x402 listings: observed USDC inflow, seller rankings, payer breadth, wash-risk flags, with published methodology. Free register; paid intelligence via x402 ($0.003–$0.50) at [MCPFax Intel](https://mcpfax-intel.bowling-anthony.workers.dev/llms.txt).

## mcp-servers

### Escrow & Payments

- [PayBot MCP](https://github.com/RBKunnela/paybot-mcp) — Claude and AI agents make autonomous x402 payments. Wallet management, transaction history, configurable spending limits. ([npm](https://www.npmjs.com/package/paybot-mcp))

### Security

- [lso-mcp](https://mcp.lonestaroracle.xyz) — 46 LoneStarOracle data tools: token and wallet risk, contract audits, whale tracking, DeFi and stablecoin risk, market and macro data, weather. x402-metered USDC on Base. ([GitHub](https://github.com/Homie4570/lso-mcp))

## sdks

### TypeScript / JavaScript

- [PayBot SDK](https://github.com/RBKunnela/paybot-sdk) — TypeScript SDK for integrating x402 into AI agents and bots. Automatic 402 detection, wallet management, USDC on Base. ([npm](https://www.npmjs.com/package/paybot-sdk))
- [x402-got](https://www.npmjs.com/package/x402-got) — Got HTTP client integration for x402.

## tools

### Discovery & Search

- [OpenClaw Discovery Index](https://x402search.xyz) — x402-gated search engine for 13,000+ x402-enabled APIs indexed from CDP Bazaar. $0.01 USDC per search on Base.
- [x402 RouteNet](https://x402-routenet.onrender.com) — Smart routing layer for x402-enabled services. Selects optimal endpoint from 251+ services based on price, latency, health, or composite trust. Four strategies: `best`, `cheapest`, `fastest`, `most_trusted`.
- [x402 Service Discovery API](https://x402-discovery-api.onrender.com) — Enriched directory of 251+ x402-payable services. Trust signals, uptime, latency, health scores. Auto-scans x402.org/ecosystem every 6h. 6-tool MCP server.
