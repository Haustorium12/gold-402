# APIs & Pay-Per-Call Services

x402-enabled APIs and production services. No API keys. No accounts. Pay USDC per call via x402 and get the data. Wallet is authentication.

> Sorted by category. For discovery tooling that indexes these services, see [ecosystem.md](ecosystem.md).

---

## AI Services

- [24K Labs](https://24klabs.ai) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/Haustorium12/24klabs-mcp) — 6 AI code analysis services: explain, debug, review, security audit, automation scripts, MCP blueprints. $0.50-$50.00 per request. USDC on Base. [Live API](https://api.24klabs.ai)
- [tx402.ai](https://tx402.ai) — Agent-native LLM inference gateway. 20+ EU-hosted models (DeepSeek, Qwen, Llama, Mixtral) via x402 USDC on Base. OpenAI-compatible, SSE streaming, GDPR-compliant, zero data retention. No API keys — wallet is auth. [Models](https://tx402.ai/v1/models)
- [AskClaude](https://askclaude.shop) — Pay-per-query Claude API. 9 endpoints: Haiku ($0.01), Sonnet ($0.03), Opus ($0.10), plus summarization, code review, translation, sentiment, crypto analysis. USDC on Base.
- [x402engine](https://x402engine.app) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-3+-0366D6?style=plastic)](https://x402engine.app) — 74 pay-per-call API tools: 44 LLMs, image/video generation, crypto data, web search, code execution, TTS, travel, IPFS. Multi-chain: Base, MegaETH, Solana. ([GitHub](https://github.com/agentc22/x402-engine))
- [x402 AI API — zeroreader](https://api.zeroreader.com) — 29 Cloudflare Workers AI models (LLM, Embeddings, Image Generation, Audio, Translation) via x402. $0.001-$0.015 per request, USDC on Base. OpenAI-compatible format.
- [GPU-Bridge](https://gpubridge.xyz) — 30-service GPU inference: LLM, image generation, embeddings, STT, TTS, PDF processing in one API. USDC on Base L2. ([Docs](https://docs.gpubridge.xyz)) ([GitHub](https://github.com/fjnunezn75/gpu-bridge))
- [MOSS Agent](https://moss.chobon.top) [![A2A Ready](https://img.shields.io/badge/A2A-ready-8250DF?style=plastic)](https://moss.chobon.top/.well-known/agent.json) — AI-powered coding services: code review ($0.005), translation ($0.003), code explanation ($0.003). A2A protocol compatible.
- [SkillMint](https://skillmint.sagasu.art) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/s87343472/skillmint) — 51 AI skills across 7 categories (dev tools, creative design, research, writing, docs). $0.01-$0.50 USDC on Base. No subscriptions.
- [Obol](https://obol.sh) — AI code generation via x402. $5 USDC per call on Base — forks your GitHub repo, generates production-ready code, opens a PR. 7 endpoints: Next.js cloning, Farcaster mini apps, OpenAPI + Hono servers, Vitest tests, MDX docs, GitHub Actions, TypeScript refactoring.

---

## Data & Research

- [agentsvc.io](https://agentsvc.io) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — 20 utility tools for AI agents: `ip-lookup`, `dns-lookup`, `qr-code`, `exchange-rates`, `email-validate`, `ssl-check`, `weather`, `translate`, `whois`, `crypto-prices`, `stock-prices`, `geocode`, `web-search`, `news-search`, `pdf-extract`, `screenshot`, `webpage-reader`, `html-to-pdf`, `ocr`. $0.001-$0.008 USDC per call on Base. ([GitHub](https://github.com/jakobautomation/agentsvc-mcp))
- [DevDrops](https://devdrops.run) — 22 pay-per-query data APIs: prediction markets (Polymarket + Manifold), property intelligence, sports odds, regulatory filings, FX rates, weather, IP geolocation, academic papers, document summarisation, and more. $0.001-$0.10 USDC on Base. ([OpenAPI](https://api.devdrops.run/openapi.json))
- [Aigregator](https://x402.aigregator.com) — Structured data on 5,336+ AI tools via REST API and MCP server. Search, compare, retrieve tool profiles. USDC on Base.
- [Xquik](https://xquik.com) — Real-time X (Twitter) data API. 7 x402 endpoints: tweet lookup, tweet search, user lookup, follower check, article extraction, media download, trends. ([npm](https://www.npmjs.com/package/@xquik/tweetclaw))
- [Content Intelligence API](https://content.hugen.tokyo) — AI-powered web content extraction and analysis. Clean text extraction (F1=0.909), metadata/OG tags, link classification, AI summarization, entity extraction. 5 endpoints from $0.003 USDC on Base.
- [panevin-x402-api](https://api.panevin.net) — Web content extraction and AI processing. 8 endpoints: text extraction, link extraction, metadata, markdown conversion, AI summarization, translation, structured data extraction. $0.001-$0.008 USDC on Base.
- [Scout MCP](https://scout.hugen.tokyo) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/bartonguestier1725-collab/scout-mcp) — Multi-source search across code, academic, social, community platforms. From $0.01 USDC on Base.
- [AnyBrowse](https://anybrowse.dev) — Autonomous web browsing agent. Converts URLs to LLM-ready Markdown via real Chrome browsers. USDC on Base.
- [Fly Labs Agentic Market](https://flylabs.fun/agents) — YouTube data APIs for AI agents. Transcribe ($0.03) and engagement analytics ($0.02) with structured JSON payloads. USDC on Base.
- [GigSoul AI Research Agent](https://gig-x402-api.jayson-be1.workers.dev) — 23-endpoint AI research API: SEC filings, earnings calls, competitor analysis, market research, document intelligence. $0.01 USDC per call on Base.

---

## Crypto & DeFi Data

- [AgentData API](https://agentdata-api.com) [![ERC-8004](https://img.shields.io/badge/ERC--8004-registered-E36209?style=plastic)](https://agentdata-api.com/discovery) — Real-time crypto market data. 16 pay-per-request endpoints: prices, funding rates, volatility, liquidation levels, DeFi yields, cross-exchange arbitrage, technical indicators (RSI/MACD/BB/ATR), support/resistance, sentiment, stablecoin health, historical OHLCV. Self-hosted facilitator.
- [Polybot Arb Intelligence](https://github.com/packrvnner/polybot-arb-api) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/packrvnner/polybot-arb-api) — Real-time cross-platform prediction market arb data (Polymarket + Kalshi + Myriad). x402 USDC on Base.
- [Tick Aggregator API](https://tick.hugen.tokyo) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-2+-0366D6?style=plastic)](https://tick.hugen.tokyo) — Multi-source aggregated FX Best Bid/Ask from 3 institutional liquidity providers. 62-88% tighter spreads than single source. 15 pairs including EURUSD, USDJPY, XAUUSD. $0.005 USDC per call on Base and Solana.
- [DeFi Intelligence API](https://defi.hugen.tokyo) — Unified DeFi security, bridging, analytics. 26 endpoints: GoPlus Security, LI.FI bridge quotes, DeFi Llama TVL. $0.005-$0.01 USDC on Base.
- [MoonMaker API](https://api.moonmaker.cc) — AI-native crypto intelligence. 11 endpoints: signals, market context, DeFi regime, institutions, ETF flows, DeFi yields, DEX alpha. $0.02-$0.10/call USDC on Base.
- [DeepBlue Trading API](https://api.deepbluebase.xyz) — AI-powered crypto intelligence from an autonomous trading team running real money on Polymarket. 21 endpoints. $0.01-$0.05 USDC on Base.
- [MoltGuard](https://api.moltrust.ch/guard/) [![ERC-8004](https://img.shields.io/badge/ERC--8004-registered-E36209?style=plastic)](https://api.moltrust.ch) — Agent trust scoring, Sybil detection, Polymarket integrity, Ed25519 Verifiable Credentials. 7 MCP tools. $0.005-$0.05 USDC on Base.
- [Hodler DeFi Intelligence](https://x402.hodle.com.br) — Stablecoin monitoring, redeem arbitrage, cross-chain pair discovery across 10 EVM chains. 6 paid endpoints at $0.01 USDC via xpay.sh on Base.
- [Rug Munch Intelligence](https://cryptorugmunch.app) — AI-powered crypto risk intelligence. 19 x402 endpoints: rug pull detection, honeypot scoring, deployer tracking, holder deep-dive, KOL shill detection, social OSINT, LLM forensic analysis. $0.02-$2.00 USDC on Base.
- [AlphaClaw](https://github.com/diassique/alphaclaw) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/diassique/alphaclaw) — Autonomous alpha hunting on Polymarket and DeFi. 6 data stream microservices via x402 micropayments.
- [SolSignal API](https://solsignal-api.onrender.com) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/cryptomotifs/solsignal-api) — Solana token safety scanner. DexScreener, RugCheck, GoPlus, Jupiter simulation in one SAFE/CAUTION/AVOID/RUG verdict. 10 free scans/day, $0.01 USDC on Solana.
- [Automaton Oracle](https://automaton-oracle.xyz) — Sovereign crypto intelligence: real-time prices, global macro intelligence, pump.fun graduation radar, trading signals, meme generation. Self-hosted facilitator (no Coinbase CDP dependency). $0.005-$0.05 USDC on Base.
- [SignalFuse](https://api.signalfuse.co) — Trading intelligence + x402 API gateway. Crypto signals fusing sentiment, macro regime, market structure. Gateway proxies: web search via Tavily and Brave, code execution via E2B. USDC on Base.
- [Sentinel](https://sentinel-awms.onrender.com) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/nbsickler-ux/Sentinel) — x402-gated trust verification for autonomous agents. Protocol trust scoring, token safety, DeFi risk assessment, OFAC screening. 5 endpoints on Base.
- [x402-api](https://x402-api.fly.dev) [![ERC-8004](https://img.shields.io/badge/ERC--8004-Agent_%2318763-orange?style=flat-square)](https://x402-api.fly.dev) — Pay-per-call DeFi & crypto data. 8 endpoints: price feeds, whale tracking, gas tracker, DEX quotes, token scanner, yield scanner, funding rates, wallet profiler. USDC on Base.
- [CryptoSignalBot](https://frog03-20494.wykr.es) — x402-gated crypto volume anomaly scanner. Tokens with unusual trading volume vs 30-day average. $0.01 USDC on Ethereum via Primev facilitator.
- [SIBYL](https://sibylcap.com) [![ERC-8004](https://img.shields.io/badge/ERC--8004-Agent_%2320880-orange?style=flat-square)](https://sibylcap.com/8004.json) — Crypto intelligence agent on Base. Token scoring ($0.05), rug/honeypot detection ($0.02), builder shipping velocity vs market cap ($0.10).
- [Crysha Price Oracle](https://api.crysha.com) — Aggregated crypto prices (multi-source BTC/others). $0.001/call on Base USDC.
- [Polymarket Liquidity API](https://polymarket-liquidity-api.tatsu77.workers.dev) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/TKtokyo/polymarket-liquidity-api) — Real-time Polymarket liquidity data. Order book depth, spread analysis, market efficiency scoring. $0.005 USDC on Base.
- [Polymarket Scan API](https://github.com/TKtokyo/polymarket-scan-api) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/TKtokyo/polymarket-scan-api) — Automated Polymarket scanner detecting liquidity anomalies. Scans all active markets every 60s. `/scan/liquidity-anomaly` ($0.018 USDC) and `/scan/history` ($0.005 USDC). Cloudflare Workers.
- [Moltalyzer](https://moltalyzer.xyz) — Four AI intelligence feeds: hourly Moltbook community digests, daily GitHub trending repos, Polymarket predetermined outcome detection, real-time token intelligence. x402 micropayments on Base.

---

## Finance & FX

- [Mercury402](https://mercury402.uk) — Pay-per-call U.S. Treasury and macro data API. FRED indicators, yield curves, GDP data with USDC micropayments on Base.
- [Gotobi Calendar API](https://gotobi.hugen.tokyo) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-2+-0366D6?style=plastic)](https://gotobi.hugen.tokyo) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/bartonguestier1725-collab/x402-gotobi-api) — Japanese FX gotobi date intelligence for trading agents. Holiday-aware USD settlement day detection. $0.01 USDC on Base and Solana.
- [PreReason](https://www.prereason.com) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/PreReason/mcp) — Financial context API. 17 pre-analyzed market briefings: BTC, macro, cross-asset regime signals. $0.01-$0.03 USDC on Base. Dual facilitator (Coinbase CDP + Dexter).
- [KR Crypto Intelligence](https://api.printmoneylab.com) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/bakyang2/kr-crypto-intelligence) — Korean crypto market data. 6 endpoints: Kimchi Premium, Upbit/Bithumb prices, USD/KRW FX rate. First verified Korean market data on x402. $0.001 USDC on Base.
- [CrossFin](https://crossfin.dev) — 15 paid Korean market data APIs (Kimchi Premium, KOSPI, Bithumb, Upbit, Coinone, FX, headlines, trading signals). First Korean financial data on x402. MCP server included.
- [Cross-Asset Intelligence API](https://x402.bankr.bot/0x98ee945dfa6bb8e9ed9f9b6ae56eb82bcc82f0aa/) — AI-powered cross-market financial analysis (crypto × traditional finance). 10 x402 endpoints on Base. BTC-equity correlation, risk scores, macro reports, daily briefings. Powered by Claude Haiku.

---

## Web & Geospatial

- [Visual API](https://visual.hugen.tokyo) — Screenshot and PDF capture API. Full-page scroll capture, CSS element targeting, mobile device emulation (iPhone 15, Pixel 7, iPad Pro), dark mode, ad/cookie banner blocking. $0.01 USDC on Base.
- [geo-gateway](https://nj4epne560.execute-api.us-west-2.amazonaws.com) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/sun-jay-ea/geo-gateway) — Pay-per-call Mapbox geospatial proxy. 6 endpoints: directions, isochrones, geocoding (forward + reverse), map matching, route optimization, distance matrices. $0.002-$0.0635 USDC on Base.
- [PortsideLabs Places API](https://portsidelabs-x402-places-536698811508.us-west1.run.app) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-2+-0366D6?style=plastic)](https://portsidelabs-x402-places-536698811508.us-west1.run.app) — Google Places API v1 proxy. Place detail lookup and full-text search. $0.001 USDC on Base and Solana.
- [Domain Intelligence API](https://domain.hugen.tokyo) — 8-endpoint domain analysis: WHOIS, multi-resolver DNS, SSL/TLS grading, Wappalyzer tech stack detection, security headers, CT log subdomains, redirect chains. $0.001-$0.02 USDC on Base.
- [Micro Data API Factory — Weather](https://weather-data-api.kasanegi123.workers.dev) — Cloudflare Workers edge weather for AI agents. Current conditions + 1-7 day forecasts worldwide by city name. $0.001 USDC on Base. Open-Meteo (CC BY 4.0).
- [Weather API](https://weather.hugen.tokyo) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/bartonguestier1725-collab/x402-weather-api) — Global weather data for AI agents. Real-time conditions and 7-day forecasts. $0.01 USDC on Base.
- [Bloomfilter](https://bloomfilter.xyz) — x402-powered domain registration API for AI agents. Register ICANN domains and manage DNS, paying with USDC on Base.
- [Find Domain](https://finddomain.io) — Domain research API. Generates candidates from keywords with stemming, IDN normalization, geo/registrar filtering, then checks availability via DNS or registry lookup. $0.002-$0.01 USDC on Base.
- [Mailcheck API](https://mailcheck.hugen.tokyo) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/bartonguestier1725-collab/x402-mailcheck-api) — Email validation: syntax, MX records, disposable domain detection, free provider check, role-based address detection, typo suggestion. $0.01 USDC on Base.

---

## Security

- [ShieldAPI](https://shield.vainplex.dev) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/alberthild/shieldapi-mcp) — Security intelligence for AI agents. Password breach (900M+ HIBP hashes), email breach, domain/IP reputation, URL safety, prompt injection detection, skill security analysis. $0.001-$0.02 USDC on Base. [MCP Server](https://www.npmjs.com/package/shieldapi-mcp)
- [Rug Scanner](https://rug-scanner-production.up.railway.app) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/LucianoLupo/rug-scanner) — On-chain token risk analysis. 7 parallel checks (bytecode, holders, liquidity, deployer, trading, verification, market), deterministic scoring. $0.05 USDC on Base.
- [Daizyx402 Security Research API](http://daizyx402.com:5402) — AI-powered smart contract security analysis. $0.05 USDC per query, $0.50 USDC deep analysis on Base. No signup.
- [AEO Scanner (Convrgent)](https://scan.convrgent.ai) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-2+-0366D6?style=plastic)](https://scan.convrgent.ai/.well-known/x402) — AI search visibility audit for any website. Triple scoring: AEO, GEO, Agent Readiness. 55+ checks across 12 categories. Free scan via SIWX, full audit $1, fix code $5 USDC on Base & Solana.
- [CYBERA Compliance API](https://compliance-api-ruddy.vercel.app) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/tedddb-ai/compliance-api) — Crypto compliance suite. VASP address identification (20,468 addresses, 29 chains), risk scoring, sanctions/mixer screening. $0.01 USDC on Base.

---

## Business Intelligence

- [Strale](https://strale.dev) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Trust layer for AI agents with 250+ independently tested business data and compliance capabilities: IBAN validation, VAT checks, sanctions screening, company lookups, SSL checks, and more. Quality-scored (SQS). $0.02-$1.00 USDC. [MCP](https://api.strale.io/mcp)
- [Intel API](https://intel.hugen.tokyo) — AI-synthesized token due diligence. Aggregates 4 GoPlus security checks + CoinGecko market data into risk-scored verdicts. One call replaces 5+ separate APIs. $0.50 USDC on Base.
- [PayAPI Market](https://payapi.market) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/chetparker/x402-marketplace) — First marketplace for x402-powered APIs. 65 endpoints: UK property data, email verification, company enrichment, postcode lookup, currency/crypto rates, screenshots, DNS intelligence, web scraping, IP geolocation, QR codes. $0.001-$0.01 USDC on Base.
- [EnrichAPI](http://72.62.52.171:8000) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/cognoco/enrichapi) — B2B lead intelligence. POST a company URL, get tech stack, growth signals, ICP fit score, pain hypothesis, and personalized outreach angle. $0.01 USDC/call.
- [DeFi Signal Agent](https://defi-signal-agent-production.up.railway.app) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/dislovelhl/defi-signal-agent) — Real-time DeFi intelligence. New pool risk scoring (0-10) on Base + Ethereum, Solana whale alerts (>$100K), Dune Analytics enrichment. 4 endpoints from $0.01-$0.10 USDC on Base Sepolia.
- [Kerdos Market Intelligence](https://nonvisceral-eloisa-mousily.ngrok-free.dev) — AI market intelligence for agents and traders. 8 endpoints: live crypto sentiment, BTC/ETH regime direction, Hyperliquid funding rates, gold/oil signals, whale alerts, liquidation cascade risk. $0.01-$0.05 USDC on Base.

---

## Infrastructure APIs

- [Arch Tools](https://archtools.dev) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-15+-blue?style=flat-square)](https://archtools.dev) — 58 production API tools for AI agents. Web scraping, AI generation, crypto data, OCR, browser automation. Patent-pending agent auth. 15+ chains. ([GitHub](https://github.com/Deesmo/Arch-AI-Tools))
- [dTelecom STT](https://x402stt.dtelecom.org) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-DePIN-blue?style=flat-square)](https://x402stt.dtelecom.org) — Real-time speech-to-text API. Dual-engine (Parakeet-TDT + Whisper), 99+ languages, hallucination filtering. $0.005/min. Built on dTelecom DePIN.
- [Coinnect](https://coinnect.bot) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/coinnect-dev/coinnect) — Money transfer routing API. Finds cheapest multi-hop paths across 45+ live sources (crypto exchanges, remittance providers, P2P markets). $0.002 USDC on Base. Non-profit, MIT licensed.
- [OpSpawn Screenshot API](https://github.com/opspawn/screenshot-api) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/opspawn/screenshot-api) — Pay-per-request screenshot and document generation. $0.01/screenshot, $0.005/markdown conversion. USDC on Base.
- [Micro Data API Factory — Broker](https://broker-entry-api.kasanegi123.workers.dev) — Wallet-free entry layer. Issues trial API key instantly, meters calls against credit, hands off to x402 when exhausted. Factory primitive — new products added by DB insert.

---

## Niche & Specialty

- [Banking Bodyguard](https://bodyguard.finance) — Real-time cbBTC whale movement signals on Base. Scored sentiment (1-10), HOLD/TIGHTEN_STOP/EXIT recommendations. ~500K signals indexed. $0.10 USDC on Base.
- [mornin-agentee](https://api.mornin-agentee.cc) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/Minnanthu/mornin-agentee) — Daily Tokyo morning briefing. Top 5 Japanese news, weather, 3 focus proposals — refreshed daily 07:30 JST. $0.05 USDC on Base.
- [Product Reputation API](https://x402-reputation-api-production.up.railway.app) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/andichen0420/x402-reputation-api) — AI-powered product reputation intelligence from Reddit, HN & YouTube. Structured scores, dimensional analysis, competitor comparisons. $0.03-$0.08 USDC.
- [Know Your Human (Convrgent)](https://convrgent.ai/kyh) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-2+-0366D6?style=plastic)](https://convrgent.ai/.well-known/x402) [![A2A Ready](https://img.shields.io/badge/A2A-ready-8250DF?style=plastic)](https://convrgent.ai/.well-known/agent.json) — Personality intelligence API. 36 endpoints across 11 personality frameworks (Socionics, Enneagram, Human Design, Vedic, BaZi, more). $0.10-$25 USDC on Base & Solana.
- [PROWL](https://prowldata.dev) — 47 real-world data feeds (prediction markets, economics, weather, geopolitics, narrative, crypto) for AI agents. MCP server for Claude included.
- [KnowMint](https://knowmint.shop) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/Sou0327/knowmint) — Open-source knowledge marketplace. AI agents discover and purchase human expertise via MCP with autonomous x402 payment flow. Solana.
- [Stockfilm](https://stockfilm.com) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-2+-0366D6?style=plastic)](https://stockfilm.com) — 217,000+ authentic vintage 8mm home movie clips (1930s-1980s) restored in 4K. AI agents search, preview, license archival footage. $10 USDC per clip on Solana and Base.
- [AgentPay](https://www.x402-agent-pay.com) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-8+-blue?style=flat-square)](https://www.x402-agent-pay.com) — Real-world service booking via x402 + Stripe. AI agents find, book, and pay for local businesses (salons, HVAC, restaurants, auto shops, medical) worldwide. 7 EVM chains + Solana.
- [CentRake](https://centrake.biz) — Universal calculator with 3-layer self-correcting verification. 5-tier dynamic pricing: $0.01 basic solve to $0.15 AI action plans. 438+ problem categories. Free for humans, paid for AI agents.

---

## Production Deployments (High Volume)

- [AIsa](https://aisa.network) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Leading x402 payment processor. **10.5M+ cumulative transactions** on the x402 network. The benchmark for production scale.
- [Coinbase Developer Platform](https://coinbase.com/developer-platform) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Official CDP implementation processing hundreds of thousands of transactions weekly. Enterprise-grade, 2-second settlement.
- [Cloudflare Workers](https://workers.cloudflare.com) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Edge payment verification at scale across 300+ data centers globally.
