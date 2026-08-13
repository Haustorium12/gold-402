# APIs & Pay-Per-Call Services

x402-enabled APIs and production services. No API keys. No accounts. Pay USDC per call via x402 and get the data. Wallet is authentication.

> Sorted by category. For discovery tooling that indexes these services, see [ecosystem.md](ecosystem.md).

> **gold-402 note:** The deepest shelf in the directory, and the one that answers the only question that matters: what can an agent actually buy today? Every entry was probed for a live 402 before it was listed. Prices here run from a tenth of a cent to a few dollars — the card-network-impossible range the protocol exists for.
>
> **This month (July 2026):** this shelf crossed a line — its first services built and operated end-to-end by autonomous AI agents ([Fabler Labs](https://fablerlabs.com/x402/), [Base tx-decision](https://x402-mcp.onrender.com/base/tx-decision)) arrived through the same intake as everyone else, probed and listed on the same bar. The buyers were always going to be machines; now some of the sellers are too.

---

> ★ **Featured — August 2026: [The Bot Wire](https://thebotwire.com)**
> Fifty-seven primary-source data wires — SEC EDGAR, Federal Register, federal courts, Fed and ECB, CISA, arXiv — behind one x402 gate at $0.005–$0.01 a call, with a free three-result preview on every wire. Agents get the source document, not a scrape of someone's summary of it. Manifest, OpenAPI, and a routing table published side by side.

## AI Services

- [Venice AI](https://venice.ai) — Official Venice AI client for x402 micropayments. Pay-per-request AI inference with privacy-first LLMs. No account required — wallet is auth. 8★
- [24K Labs Chronographer](https://24klabs.ai/products/chronographer) — Temporal context for AI agents: 15+ time systems (lunar, solar, market sessions, circadian, ISO/Julian) plus an AI temporal-reasoning endpoint. $0.001–$0.05 USDC per call on Base. [Live API](https://time.24klabs.ai)
- [tx402.ai](https://tx402.ai) — Agent-native LLM inference gateway. 20+ EU-hosted models (DeepSeek, Qwen, Llama, Mixtral) via x402 USDC on Base. OpenAI-compatible, SSE streaming, GDPR-compliant, zero data retention. No API keys — wallet is auth. [Models](https://tx402.ai/v1/models)
- [AskClaude](https://askclaude.shop) — Pay-per-query Claude API. 9 endpoints: Haiku ($0.01), Sonnet ($0.03), Opus ($0.10), plus summarization, code review, translation, sentiment, crypto analysis. USDC on Base.
- [x402engine](https://x402engine.app) — 74 pay-per-call API tools: 44 LLMs, image/video generation, crypto data, web search, code execution, TTS, travel, IPFS. Multi-chain: Base, MegaETH, Solana. ([GitHub](https://github.com/agentc22/x402-engine))
- [x402 AI API — zeroreader](https://api.zeroreader.com) — 29 Cloudflare Workers AI models (LLM, Embeddings, Image Generation, Audio, Translation) via x402. $0.001-$0.015 per request, USDC on Base. OpenAI-compatible format.
- [GPU-Bridge](https://gpubridge.xyz) — 30-service GPU inference: LLM, image generation, embeddings, STT, TTS, PDF processing in one API. USDC on Base L2. ([Docs](https://docs.gpubridge.xyz)) ([GitHub](https://github.com/fjnunezn75/gpu-bridge))
- [MOSS Agent](https://moss.chobon.top) — AI-powered coding services: code review ($0.005), translation ($0.003), code explanation ($0.003). A2A protocol compatible.
- [SkillMint](https://skillmint.sagasu.art) — 51 AI skills across 7 categories (dev tools, creative design, research, writing, docs). $0.01-$0.50 USDC on Base. No subscriptions.
- [Obol](https://obol.sh) — AI code generation via x402. $5 USDC per call on Base — forks your GitHub repo, generates production-ready code, opens a PR. 7 endpoints: Next.js cloning, Farcaster mini apps, OpenAPI + Hono servers, Vitest tests, MDX docs, GitHub Actions, TypeScript refactoring.
- [DeskCrew](https://deskcrew.io/agents) — Agent-native helpdesk. 16 tools: agents pay per call to draft customer-support replies grounded in a knowledge base and to work real tickets, while discovery tools (search_kb, list_issues, list_changelog) are free and need no signup. $0.02-$0.08 USDC on Base, Polygon, Avalanche, Sei, and Solana. A human approves before anything reaches a customer. ([Manifest](https://deskcrew.io/.well-known/x402))
- [Zugabot Code Agent](https://zugabot.ai/x402) — AI developer services via x402: code review ($0.25), bug fix ($0.25), security audit ($0.50), architecture review ($3.00), full-repo audit ($5.00), plus test generation, docs, refactor, PR review. USDC on Base.
- [Zugabot Image Generation](https://zugabot.ai/api/x402/agent/image-generate) — Text-to-image generation via x402: FLUX Schnell ($0.15) or FLUX 2 Pro ($0.50), returns image URL plus dimensions and seed. USDC on Base. `POST` to the endpoint; storefront at [zugabot.ai/x402](https://zugabot.ai/x402).
- [BridgeNode](https://bridgenode.cc) — OpenAI-compatible LLM inference bridge: chat completions with SSE streaming, pay per call via x402 with Solana USDC. From $0.002 per call. ([OpenAPI](https://bridgenode.cc/openapi.json)) ([llms.txt](https://bridgenode.cc/llms.txt)) ([GitHub](https://github.com/applefanaimail-blip/bridgenode-skill))

---

## Data & Research

- [agentsvc.io](https://agentsvc.io) — 20 utility tools for AI agents: `ip-lookup`, `dns-lookup`, `qr-code`, `exchange-rates`, `email-validate`, `ssl-check`, `weather`, `translate`, `whois`, `crypto-prices`, `stock-prices`, `geocode`, `web-search`, `news-search`, `pdf-extract`, `screenshot`, `webpage-reader`, `html-to-pdf`, `ocr`. $0.001-$0.008 USDC per call on Base. ([GitHub](https://github.com/jakobautomation/agentsvc-mcp))
- [DevDrops](https://devdrops.run) — 22 pay-per-query data APIs: prediction markets (Polymarket + Manifold), property intelligence, sports odds, regulatory filings, FX rates, weather, IP geolocation, academic papers, document summarisation, and more. $0.001-$0.10 USDC on Base. ([OpenAPI](https://api.devdrops.run/openapi.json))
- [Aigregator](https://x402.aigregator.com) — Structured data on 5,336+ AI tools via REST API and MCP server. Search, compare, retrieve tool profiles. USDC on Base.
- [Xquik](https://xquik.com) — Real-time X (Twitter) data API. 7 x402 endpoints: tweet lookup, tweet search, user lookup, follower check, article extraction, media download, trends. ([npm](https://www.npmjs.com/package/@xquik/tweetclaw))
- [Content Intelligence API](https://content.hugen.tokyo) — AI-powered web content extraction and analysis. Clean text extraction (F1=0.909), metadata/OG tags, link classification, AI summarization, entity extraction. 5 endpoints from $0.003 USDC on Base.
- [panevin-x402-api](https://api.panevin.net) — Web content extraction and AI processing. 8 endpoints: text extraction, link extraction, metadata, markdown conversion, AI summarization, translation, structured data extraction. $0.001-$0.008 USDC on Base.
- [Scout MCP](https://scout.hugen.tokyo) — Multi-source search across code, academic, social, community platforms. From $0.01 USDC on Base.
- [AnyBrowse](https://anybrowse.dev) — Autonomous web browsing agent. Converts URLs to LLM-ready Markdown via real Chrome browsers. USDC on Base.
- [Fly Labs Agentic Market](https://flylabs.fun/agents) — YouTube data APIs for AI agents. Transcribe ($0.03) and engagement analytics ($0.02) with structured JSON payloads. USDC on Base.
- [GigSoul AI Research Agent](https://gig-x402-api.jayson-be1.workers.dev) — 23-endpoint AI research API: SEC filings, earnings calls, competitor analysis, market research, document intelligence. $0.01 USDC per call on Base.
- [x402 Entity-ID Resolver](https://entityresolver.xyz) — Resolves a company or crypto name or ticker into ranked entities with verified canonical IDs across registries: SEC CIK + ticker, GLEIF LEI, Wikidata QID, CoinGecko slug. $0.005 USDC per call on Base. ([OpenAPI](https://entityresolver.xyz/openapi.json))
- [_done](https://underscoredone.com) — Suite of x402 micropayment-gated utility APIs for AI agents (web lookups, site analysis, data and more). 18 resources, $0.01–$0.05. Pay-per-call, no API keys or subscriptions. Base + Solana mainnet.
- [PulseNetwork](https://pulsenetwork.theaslangroupllc.com) — Federated catalog of 950+ pay-per-call intelligence endpoints across 76 origins: token safety (8 EVM chains + Solana memecoins), macro & economic primitives, OFAC/sanctions screening, geopolitical risk, clinical-trials intel, government spending, stablecoin/RWA monitors, sports data, prediction markets, doc-prep. $0.001–$2.00 USDC per call on Base + Solana, native USDG on Robinhood Chain, XRP/RLUSD on XRPL. ([Manifest](https://pulsenetwork.theaslangroupllc.com/.well-known/x402.json)) ([OpenAPI](https://pulsenetwork.theaslangroupllc.com/openapi.json)) ([llms.txt](https://pulsenetwork.theaslangroupllc.com/llms.txt))
- [modelprices.xyz](https://modelprices.xyz) — Normalized LLM market data: per-token prices, context windows, and capability limits for 2,000+ models across 70+ providers, cross-checked hourly against two upstreams. Single-model lookups $0.002, cheapest-model queries $0.005 (ranked by blended $/request), full tables $0.01, price-change feed $0.02. Provenance on every row: source URL, first-observed date, confidence tier. USDC on Base. ([OpenAPI](https://modelprices.xyz/openapi.json)) ([llms.txt](https://modelprices.xyz/llms.txt))
- [JMT x402 Agent Tools](https://jmt-x402-proxy.jmthomasofficial.workers.dev) — 25 endpoints: web search, AI analysis, crypto/stock data, SEC filings, company intel, news, sentiment, macro dashboard. Local LLM-powered. $0.001-$0.15 USDC on Base.
- [Vindex](https://api.vindexapi.dev) — Vehicle-data API: VIN decode with factory warranty terms, recalls, known-issues/reliability, and US & Canada purchase-cost estimates. NHTSA and Transport Canada sources. $0.01 USDC on Base.
- [US City Open-Data Compliance Network](https://x402-mcp.onrender.com/us/cities) — Multi-jurisdiction property compliance for AI agents: free catalog /us/cities, free samples /us/{code}/property-check/sample, paid /us/{code}/property-check ($0.01 USDC on Base). Fourteen live open-data markets covering rental registration/license and code-violation public feeds. ([OpenAPI](https://x402-mcp.onrender.com/openapi.json)) ([llms.txt](https://x402-mcp.onrender.com/llms.txt)) ([GitHub](https://github.com/kwizzlesurp10-ctrl/x402-mcp))
- [Grey Ridge Signals — x402 Data & Security APIs](https://x402-data-api.sigrunner.workers.dev) — 17 agent-native pay-per-call endpoints: blockchain queries (balance, gas, code, receipts, token balances), crypto funding rates & prices, DeFi yields, domain enrichment, tech-risk scoring, prediction market data, MCP scanning. $0.001–$0.05 USDC on Base. ([OpenAPI](https://x402-data-api.sigrunner.workers.dev/openapi.json))
- [Groundcheck](https://groundcheck.seiche.info) — Claim grounding and delivery attestation for AI agents: machine-verified verdicts (supported/refuted/unverified) with confidence scores and cited sources, plus signed offline-verifiable receipts binding an x402 payment to what was delivered. Free single-claim tier; paid endpoints $0.005–$0.05 USDC on Base. ([OpenAPI](https://groundcheck.seiche.info/openapi.json)) ([npm](https://www.npmjs.com/package/groundcheck-mcp))
- [Mart402](https://mart402.com) — Web and PDF extraction for AI agents: URL-to-Markdown extraction, PDF parsing with dual-engine OCR consensus (hallucination detection, calibrated confidence, Japanese-strong), invoice field verification, schema-driven structured extraction, and JP company profiles. $0.001–$0.02 USDC on Base; free Sepolia sandbox at mart402.dev. ([Docs](https://mart402.com/agents.md)) ([GitHub](https://github.com/tanaka-77/mart402-agent-kit))
- [OyaPicks](https://oyapicks.app) — Cross-venue prediction market data for AI agents: 11 endpoints covering keyword market search, single-market lookup, probability movers, 24h volume spikes, cross-venue arbitrage gaps between Polymarket and Alpha Arcade, markets closing within 48 hours, newly listed markets, resolutions with winning outcomes, price history, and the complete live Alpha Arcade catalog in one call with per-outcome prices and Algorand application IDs. $0.01–$0.25 USDC on Base via the CDP facilitator and Algorand via GoPlausible. Example: `GET /api/x402/single-market?q=fed`. ([Manifest](https://oyapicks.app/.well-known/x402)) ([OpenAPI](https://oyapicks.app/openapi.json)) ([llms.txt](https://oyapicks.app/llms.txt))

---
- [The Bot Wire](https://thebotwire.com) — 57 primary-source data wires for AI agents: SEC EDGAR, Federal Register, federal court opinions, congressional bills, DOJ, FDA, Federal Reserve and ECB, BLS/BEA releases, CISA CVEs, cloud outages, NWS alerts, USGS quakes, arXiv, WHO/CDC, European Commission, GOV.UK, NASA, EIA, plus 40 curated news sources. $0.005–$0.01 USDC on Base, free 3-result preview on every wire. Example: `GET /fed/latest?src=fomc&since=30d`. ([Manifest](https://thebotwire.com/.well-known/x402)) ([OpenAPI](https://thebotwire.com/openapi.json)) ([Routing table](https://thebotwire.com/llms-full.txt))
- [Data Quality Gate](https://www.aidatatools.dev/api) — Deterministic dataset-quality verdict (RELIABLE/USABLE_WITH_CLEANING/UNRELIABLE) with per-check facts on completeness, nulls, types, impossible values, duplicates, and outliers, plus optional cross-source price-divergence detection for financial/trading data, for $0.01 USDC per call on Base or Solana.

## Crypto & DeFi Data

- [AgentServices](https://agentservices.to) — Paid data APIs for AI agents: crypto prices, technical indicators, DeFi yields, IP geolocation, and URL metadata. $0.00-$0.02 USDC on Base. ([x402](https://agentservices.to/.well-known/x402))
- [AgentData API](https://agentdata-api.com) — Real-time crypto market data. 16 pay-per-request endpoints: prices, funding rates, volatility, liquidation levels, DeFi yields, cross-exchange arbitrage, technical indicators (RSI/MACD/BB/ATR), support/resistance, sentiment, stablecoin health, historical OHLCV. Self-hosted facilitator.
- [Polybot Arb Intelligence](https://github.com/packrvnner/polybot-arb-api) — Real-time cross-platform prediction market arb data (Polymarket + Kalshi + Myriad). x402 USDC on Base.
- [Isocast](https://api.isocast.dev) — Per-signal Polymarket weather-market data across 37 cities. Fires when a city's daily-high temperature crosses into a new Polymarket bucket, returning the market URL and live bucket odds. From $0.01 USDC on Base.
- [Tick Aggregator API](https://tick.hugen.tokyo) — Multi-source aggregated FX Best Bid/Ask from 3 institutional liquidity providers. 62-88% tighter spreads than single source. 15 pairs including EURUSD, USDJPY, XAUUSD. $0.005 USDC per call on Base and Solana.
- [DeFi Intelligence API](https://defi.hugen.tokyo) — Unified DeFi security, bridging, analytics. 26 endpoints: GoPlus Security, LI.FI bridge quotes, DeFi Llama TVL. $0.005-$0.01 USDC on Base.
- [MoonMaker API](https://api.moonmaker.cc) — AI-native crypto intelligence. 11 endpoints: signals, market context, DeFi regime, institutions, ETF flows, DeFi yields, DEX alpha. $0.02-$0.10/call USDC on Base.
- [x402-seller](https://x402-seller-m8nx.onrender.com) — Token rug/honeypot scoring combining GoPlus static analysis with live Honeypot.is sell simulation, liquidity-drain detection from a self-collected reserve time-series, and market data. EVM + Solana. $0.001-$0.05 USDC on Base. ([Track record](https://x402-seller-m8nx.onrender.com/track-record))
- [DeepBlue Trading API](https://api.deepbluebase.xyz) — AI-powered crypto intelligence from an autonomous trading team running real money on Polymarket. 21 endpoints. $0.01-$0.05 USDC on Base.
- [MoltGuard](https://api.moltrust.ch/guard/) — Agent trust scoring, Sybil detection, Polymarket integrity, Ed25519 Verifiable Credentials. 7 MCP tools. $0.005-$0.05 USDC on Base.
- [Hodler DeFi Intelligence](https://x402.hodle.com.br) — Stablecoin monitoring, redeem arbitrage, cross-chain pair discovery across 10 EVM chains. 6 paid endpoints at $0.01 USDC via xpay.sh on Base.
- [AlphaClaw](https://github.com/diassique/alphaclaw) — Autonomous alpha hunting on Polymarket and DeFi. 6 data stream microservices via x402 micropayments.
- [SolSignal API](https://solsignal-api.onrender.com) — Solana token safety scanner. DexScreener, RugCheck, GoPlus, Jupiter simulation in one SAFE/CAUTION/AVOID/RUG verdict. 10 free scans/day, $0.01 USDC on Solana.
- [Automaton Oracle](https://automaton-oracle.xyz) — Sovereign crypto intelligence: real-time prices, global macro intelligence, pump.fun graduation radar, trading signals, meme generation. Self-hosted facilitator (no Coinbase CDP dependency). $0.005-$0.05 USDC on Base.
- [SignalFuse](https://api.signalfuse.co) — Trading intelligence + x402 API gateway. Crypto signals fusing sentiment, macro regime, market structure. Gateway proxies: web search via Tavily and Brave, code execution via E2B. USDC on Base.
- [Sentinel](https://sentinel-awms.onrender.com) — x402-gated trust verification for autonomous agents. Protocol trust scoring, token safety, DeFi risk assessment, OFAC screening. 5 endpoints on Base.
- [x402-api](https://x402-api.fly.dev) — Pay-per-call DeFi & crypto data. 8 endpoints: price feeds, whale tracking, gas tracker, DEX quotes, token scanner, yield scanner, funding rates, wallet profiler. USDC on Base.
- [GenTech x402 Gateway](https://api.gentechlabs.net) — 15 pay-per-call endpoints for crypto intelligence, wallet analysis, token risk scoring, NFT search, game/movie deals, and agent scanning. $0.001-$0.10 USDC per call across 5 chains (Base, Solana, Avalanche, BNB, OKX). ([OpenAPI](https://api.gentechlabs.net/openapi.json)) ([Discovery](https://api.gentechlabs.net/.well-known/x402))
- [CryptoSignalBot](https://frog03-20494.wykr.es) — x402-gated crypto volume anomaly scanner. Tokens with unusual trading volume vs 30-day average. $0.01 USDC on Ethereum via Primev facilitator.
- [SIBYL](https://sibylcap.com) — Crypto intelligence agent on Base. Token scoring ($0.05), rug/honeypot detection ($0.02), builder shipping velocity vs market cap ($0.10).
- [Crysha Price Oracle](https://api.crysha.com) — Aggregated crypto prices (multi-source BTC/others). $0.001/call on Base USDC.
- [Polymarket Liquidity API](https://polymarket-liquidity-api.tatsu77.workers.dev) — Real-time Polymarket liquidity data. Order book depth, spread analysis, market efficiency scoring. $0.005 USDC on Base.
- [Polymarket Scan API](https://github.com/TKtokyo/polymarket-scan-api) — Automated Polymarket scanner detecting liquidity anomalies. Scans all active markets every 60s. `/scan/liquidity-anomaly` ($0.018 USDC) and `/scan/history` ($0.005 USDC). Cloudflare Workers.
- [Moltalyzer](https://moltalyzer.xyz) — Four AI intelligence feeds: hourly Moltbook community digests, daily GitHub trending repos, Polymarket predetermined outcome detection, real-time token intelligence. x402 micropayments on Base.
- [SolSigs](https://solsigs.com) — 20 pay-per-call Solana blockchain intelligence APIs: DEX prices, arbitrage scanner, wallet intelligence, token launch detection, Polymarket predictions, NFT analysis, whale tracking, smart money signals, social sentiment, staking APY, RPC relay, on-chain LLM summarizer, webhook alerts, dev activity, batch pricing, trending tokens, token safety, alpha feed, trust scoring, perps intelligence. $0.001-$0.010 USDC on Solana.
- [LoneStarOracle](https://lonestaroracle.xyz) — 43 pay-per-call data APIs: token and wallet risk scoring, smart-contract security audits, whale and bundle tracking, DeFi and stablecoin risk, plus equity, options, macro, and weather data. $0.02-$2.00 USDC on Base. No API keys — wallet is auth. ([MCP](https://mcp.lonestaroracle.xyz))
- [TokenGuard](https://eltociear-tokenguard.hf.space) — ERC-20 rug/safety scanner over public RPC on 6 chains (Base, Ethereum, Arbitrum, Optimism, Polygon, BSC): infinite-mint, blacklist/freeze, pausable transfers, mutable sell-tax, upgradeable proxy and ownership checks. Also wallet intelligence, token price, ENS, gas, DeFi yields, TVL and crypto news endpoints. $0.005-$0.01 USDC on Base.
- [Base tx-decision](https://x402-mcp.onrender.com/base/tx-decision) — Submit-now-or-wait decision plus EIP-1559 fee sizing for Base mainnet transactions, computed live from RPC blocks every call. Also serves a Base network-economics snapshot and an MCP server. $0.01 USDC on Base.
- [Stelar Digital](https://api.stelardigital.com) — Live crypto grid-trading telemetry (real P&L, not simulated), grid-parameter recommendations, market-regime classification, and sentiment scoring. 8 endpoints, $0.005-$2.50 USDC on Base. ([x402](https://api.stelardigital.com/.well-known/x402))
- [GBLIN Protocol](https://gblin.digital/agents) — Treasury and risk data for a NAV-backed basket token on Base (cbBTC/WETH/USDC) with an automated on-chain crash-response policy. 7 endpoints: NAV and basket state, market risk regime attestation, MEV-safe swap quotes, wallet treasury health, and just-in-time redemption calldata to convert holdings to USDC when an invoice arrives. $0.001-$0.005 USDC on Base via the Coinbase CDP facilitator. ([x402](https://gblin.digital/.well-known/x402)) ([MCP](https://www.npmjs.com/package/@gblin-protocol/mcp-server))
- [Node Scorecard API](https://nodescorecard.xyz/scorecard/nodes) — Scored directory of Sentinel dVPN network nodes: composite score per node, sorted best-first, active nodes by default with an optional full snapshot. $0.005 USDC per call on Base, Solana, Polygon, Arbitrum, and Avalanche.
- [CapGain safety and work artifacts](https://5-9-107-124.nip.io) — EVM token risk and Base swap preflights from $0.01, plus machine-buyable invariant tests ($0.03), repository reviews ($0.05), and protocol research ($0.03), paid in Base USDC via x402. ([x402](https://5-9-107-124.nip.io/.well-known/x402.json))

---

## Finance & FX

- [Mercury402](https://mercury402.uk) — Pay-per-call U.S. Treasury and macro data API. FRED indicators, yield curves, GDP data with USDC micropayments on Base.
- [Gotobi Calendar API](https://gotobi.hugen.tokyo) — Japanese FX gotobi date intelligence for trading agents. Holiday-aware USD settlement day detection. $0.01 USDC on Base and Solana.
- [PreReason](https://www.prereason.com) — Financial context API. 17 pre-analyzed market briefings: BTC, macro, cross-asset regime signals. $0.01-$0.03 USDC on Base. Dual facilitator (Coinbase CDP + Dexter).
- [KR Crypto Intelligence](https://api.printmoneylab.com) — Korean crypto market data. 6 endpoints: Kimchi Premium, Upbit/Bithumb prices, USD/KRW FX rate. First verified Korean market data on x402. $0.001 USDC on Base.
- [CrossFin](https://crossfin.dev) — 15 paid Korean market data APIs (Kimchi Premium, KOSPI, Bithumb, Upbit, Coinone, FX, headlines, trading signals). First Korean financial data on x402. MCP server included.
- [Tollbooth](https://x402toll.com) — 56 financial, tax, and legal calculators for AI agents (income tax, self-employment/estimated tax, capital gains, LLC/entity comparison, mortgage/loan, retirement/RMD/Social Security, crypto/DeFi, sales tax). Each response includes its 2026 IRS/SSA source, a formula trace, and a reproducible SHA-256 hash, plus a free golden-vector self-check endpoint. $0.02-$1.00 USDC on Base. MCP: `npx tollbooth-x402`. ([OpenAPI](https://x402toll.com/v1/openapi.json))
- [Macro Pulse](https://macro-pulse-x402.onrender.com) — Pay-per-call macroeconomic indicator API sourced from the World Bank (GDP growth, inflation, unemployment trend). Single-country lookup $0.02, 8-country flat-priced batch endpoint $0.05, 6-hour response caching. USDC on Base.
- [ECB FX Reference](https://official-fx-reference.vercel.app/api/v1/convert) — Converts amounts across ECB-supported currencies from the European Central Bank's daily euro reference observations, returning source rates, publication date, cross-rate math, and attribution for $0.0015 USDC per call on Base. ([OpenAPI](https://official-fx-reference.vercel.app/openapi.json)) ([GitHub](https://github.com/ArgonautWorks/ecb-fx-reference))

---
- [IBANforge](https://ibanforge.com) — Pre-payout IBAN screening: validation + issuing-bank identification against 6 national bank registers (CH/LI, DE, AT, BE, FI), Swiss clearing incl. QR-IID resolution, bank-level sanctions, SEPA + VoP reachability. 121k+ BICs, 89 IBAN countries. $0.002-$0.02 USDC on Base (CDP facilitator). MCP: `npx -y ibanforge-mcp`. ([OpenAPI](https://api.ibanforge.com/openapi.json), [x402 discovery](https://api.ibanforge.com/.well-known/x402))

## Web & Geospatial

- [Visual API](https://visual.hugen.tokyo) — Screenshot and PDF capture API. Full-page scroll capture, CSS element targeting, mobile device emulation (iPhone 15, Pixel 7, iPad Pro), dark mode, ad/cookie banner blocking. $0.01 USDC on Base.
- [geo-gateway](https://nj4epne560.execute-api.us-west-2.amazonaws.com) — Pay-per-call Mapbox geospatial proxy. 6 endpoints: directions, isochrones, geocoding (forward + reverse), map matching, route optimization, distance matrices. $0.002-$0.0635 USDC on Base.
- [PortsideLabs Places API](https://portsidelabs-x402-places-536698811508.us-west1.run.app) — Google Places API v1 proxy. Place detail lookup and full-text search. $0.001 USDC on Base and Solana.
- [Domain Intelligence API](https://domain.hugen.tokyo) — 8-endpoint domain analysis: WHOIS, multi-resolver DNS, SSL/TLS grading, Wappalyzer tech stack detection, security headers, CT log subdomains, redirect chains. $0.001-$0.02 USDC on Base.
- [Weather API](https://weather.hugen.tokyo) — Global weather data for AI agents. Real-time conditions and 7-day forecasts. $0.01 USDC on Base.
- [Bloomfilter](https://bloomfilter.xyz) — x402-powered domain registration API for AI agents. Register ICANN domains and manage DNS, paying with USDC on Base.
- [Find Domain](https://finddomain.io) — Domain research API. Generates candidates from keywords with stemming, IDN normalization, geo/registrar filtering, then checks availability via DNS or registry lookup. $0.002-$0.01 USDC on Base.
- [Mailcheck API](https://mailcheck.hugen.tokyo) — Email validation: syntax, MX records, disposable domain detection, free provider check, role-based address detection, typo suggestion. $0.01 USDC on Base.
- [Venture NL Open-Data](https://api.pogo-tb.nl) — Dutch open-government data: RDW vehicle registry, BAG addresses/buildings, postcode/geocoding, OV transit departures. CC0/CC-BY-4.0 sources. $0.001-$0.01 USDC on Base.
- [Rue Render API](https://rue.mossgate.dev) — Renders a URL or raw HTML to PDF, PNG, or JPEG via headless Chromium, SSRF-guarded. $0.003 USDC on Base via x402.

---

## Security

- [ShieldAPI](https://shield.vainplex.dev) — Security intelligence for AI agents. Password breach (900M+ HIBP hashes), email breach, domain/IP reputation, URL safety, prompt injection detection, skill security analysis. $0.001-$0.02 USDC on Base. [MCP Server](https://www.npmjs.com/package/shieldapi-mcp)
- [AEO Scanner (Convrgent)](https://scan.convrgent.ai) — AI search visibility audit for any website. Triple scoring: AEO, GEO, Agent Readiness. 55+ checks across 12 categories. Free scan via SIWX, full audit $1, fix code $5 USDC on Base & Solana.
- [CYBERA Compliance API](https://compliance-api-ruddy.vercel.app) — Crypto compliance suite. VASP address identification (20,468 addresses, 29 chains), risk scoring, sanctions/mixer screening. $0.01 USDC on Base.
- [DDG Agent-Payable Services](https://agents.daedalusdevelopmentgroup.com) — Machine-readable security and commerce primitives for AI agents. x402 checkout-conformance audits, MCP/tool security preflight, spend-authorization contracts, browser-agent completion proofs, bounded artifact/model orders. Identity-first (403→402→receipt), 5 settlement networks. $0.01-$5.00 USDC per call. [MCP](https://mcp.daedalusdevelopmentgroup.com/mcp)
- [Agent Ready](https://agent-ready.dev) — Website agent-readability scanner. Scores any URL against the Vercel Agent Readability Spec and llmstxt.org with per-check remediation. Pay-per-scan: $0.02 (25 pages) / $0.25 (250 pages) USDC on Base via x402.
- [Skill Audit](https://eltociear-skill-audit.hf.space) — Malicious-pattern detection for AI agent skills, plugins and prompts. 68 patterns: credential exfiltration, download-and-execute, prompt injection, seed-phrase harvesting, privilege escalation. $0.01-$0.03 USDC on Base.
- [Contract Guard](https://eltociear-contract-guard.hf.space) — Pre-interaction EVM contract risk signals: EOA/contract/self-destructed status, EIP-7702 delegated-EOA detection, upgradeable proxy detection, ERC-20 metadata and risk score. $0.005 USDC on Base.
- [Fabler Labs x402 Storefront](https://fablerlabs.com/x402/) — Security and utility APIs for AI agents on Base, USDC per call, no signup: secret scan ($0.005), agent-config audit ($0.05), diff security gate ($0.10), pre-deploy evidence gate ($0.08), URL security evidence ($0.08), plus data and rendering endpoints and digital-product downloads; free machine-readable catalog at GET https://x402.fablerlabs.com/. Built and operated end-to-end by an autonomous AI agent.
- [Mossgate Trust API](https://api.mossgate.dev) — Onchain risk checks for Base ERC-20 tokens and wallets: token verdict returns ok/caution/danger with liquidity, pair age, 24h volume, and contract flags; wallet profile returns onchain reputation for a counterparty. $0.01-$0.25 USDC on Base. ([llms.txt](https://api.mossgate.dev/llms.txt))

---

## Business Intelligence

- [Strale](https://strale.dev) — Trust layer for AI agents with 250+ independently tested business data and compliance capabilities: IBAN validation, VAT checks, sanctions screening, company lookups, SSL checks, and more. Quality-scored (SQS). $0.02-$1.00 USDC. [MCP](https://api.strale.io/mcp)
- [Intel API](https://intel.hugen.tokyo) — AI-synthesized token due diligence. Aggregates 4 GoPlus security checks + CoinGecko market data into risk-scored verdicts. One call replaces 5+ separate APIs. $0.50 USDC on Base.
- [PayAPI Market](https://payapi.market) — First marketplace for x402-powered APIs. 65 endpoints: UK property data, email verification, company enrichment, postcode lookup, currency/crypto rates, screenshots, DNS intelligence, web scraping, IP geolocation, QR codes. $0.001-$0.01 USDC on Base.
- [Kerdos Market Intelligence](https://nonvisceral-eloisa-mousily.ngrok-free.dev) — AI market intelligence for agents and traders. 8 endpoints: live crypto sentiment, BTC/ETH regime direction, Hyperliquid funding rates, gold/oil signals, whale alerts, liquidation cascade risk. $0.01-$0.05 USDC on Base.

---

## Infrastructure APIs

- [Arch Tools](https://archtools.dev) — 58 production API tools for AI agents. Web scraping, AI generation, crypto data, OCR, browser automation. Patent-pending agent auth. 15+ chains. ([GitHub](https://github.com/Deesmo/Arch-AI-Tools))
- [dTelecom STT](https://x402stt.dtelecom.org) — Real-time speech-to-text API. Dual-engine (Parakeet-TDT + Whisper), 99+ languages, hallucination filtering. $0.005/min. Built on dTelecom DePIN.
- [Coinnect](https://coinnect.bot) — Money transfer routing API. Finds cheapest multi-hop paths across 45+ live sources (crypto exchanges, remittance providers, P2P markets). $0.002 USDC on Base. Non-profit, MIT licensed.

---
- [WebberSites x402 Data API](https://x402.webbersites.com) — 41 pay-per-call endpoints for AI agents: web scraping, document extraction, whole-site SEO audits, brand-kit/logo/site generation, DNS and email intelligence, crypto data, wallet-owned persistent Agent Datastore, and a free machine message board. $0.001-$0.009 USDC on Base via CDP facilitator. MCP server: `npx webbersites-x402-mcp`. ([OpenAPI](https://api.webbersites.com/openapi.json)) ([GitHub](https://github.com/webberdesign/api.webbersites.com))
- [NodeFlare](https://nodeflare.app/docs/x402) — Pay-per-request JSON-RPC on 23 EVM chains (including Robinhood Chain, Plasma, Ink and Zircuit) served from self-operated bare-metal nodes in 5 regions, priced by compute units from $0.001 per call with eth_getLogs/trace/debug included, USDC on Base via the CDP facilitator.

## Niche & Specialty

- [Know Your Human (Convrgent)](https://convrgent.ai/kyh) — Personality intelligence API. 36 endpoints across 11 personality frameworks (Socionics, Enneagram, Human Design, Vedic, BaZi, more). $0.10-$25 USDC on Base & Solana.
- [KnowMint](https://knowmint.shop) — Open-source knowledge marketplace. AI agents discover and purchase human expertise via MCP with autonomous x402 payment flow. Solana.
- [Stockfilm](https://stockfilm.com) — 217,000+ authentic vintage 8mm home movie clips (1930s-1980s) restored in 4K. AI agents search, preview, license archival footage. $10 USDC per clip on Solana and Base.
- [AgentPay](https://www.x402-agent-pay.com) — Real-world service booking via x402 + Stripe. AI agents find, book, and pay for local businesses (salons, HVAC, restaurants, auto shops, medical) worldwide. 7 EVM chains + Solana.
- [CentRake](https://centrake.biz) — Universal calculator with 3-layer self-correcting verification. 5-tier dynamic pricing: $0.01 basic solve to $0.15 AI action plans. 438+ problem categories. Free for humans, paid for AI agents.
- [Dokimo Verify API](https://dokimo.augaster.com/verify-api-docs.html) — Pay-per-call x402 endpoint that independently verifies a Merkle evidence proof to its committed root and returns a signed attestation; part of Dokimo, a non-custodial ASC-606 subledger that turns x402/agent revenue into audit-ready books.
- [402PIXEL](https://402pixel.com) — AI-agent-only territory game on a shared 402-tile board. `POST /api/claim {"tile":0-401,"days":1-30,"name":"MyAgent","color":"#4DD2FF"}` — 0.01-1.00 USDC/day by tile tier on Base, days stack, top payers rank on a live Hall of Fame. ([Manifest](https://402pixel.com/api/manifest)) ([llms.txt](https://402pixel.com/llms.txt))

---

## Production Deployments (High Volume)

- [AIsa](https://aisa.network) — Leading x402 payment processor. **10.5M+ cumulative transactions** on the x402 network. The benchmark for production scale.
- [Coinbase Developer Platform](https://coinbase.com/developer-platform) — Official CDP implementation processing hundreds of thousands of transactions weekly. Enterprise-grade, 2-second settlement.
- [Cloudflare Workers](https://workers.cloudflare.com) — Edge payment verification at scale across 300+ data centers globally.
- [AVT x402 Data Services](https://api.aventtech.com) — 16 pay-per-call data and validation APIs: field-verified AV/IT device-integration knowledge base (curated by working systems integrators), IBAN / EU-VAT (VIES) / email / phone / card / GTIN validation, DNS and RDAP domain lookup, timezone and ECB currency conversion. $0.002–$0.03 USDC on Base; free catalog, llms.txt, and OpenAPI. ([llms.txt](https://api.aventtech.com/llms.txt)) ([MCP server](https://github.com/ttsempelis/avt-x402-mcp))
- [Visibility AI Audit API](https://visibility.gleefulai.com) — AI-visibility and AEO audit for websites: agent-readiness scoring (llms.txt, schema, bot access, FAQ), generated fixes, and competitor gap analysis. Pay-per-call USDC on Base via x402, no API keys. ([OpenAPI](https://visibility.gleefulai.com/openapi.json)) ([Docs](https://visibility.gleefulai.com/docs))
