# MCP Servers

x402-enabled MCP servers. AI agents (Claude, Cursor, any MCP client) can call these tools and pay automatically per invocation via USDC micropayments. No API keys. No accounts. Wallet is authentication.

> **gold-402 note:** The MCP + x402 intersection is the fastest-growing part of the ecosystem. This list grows weekly.

---

> ★ **Featured — August 2026: [Razorpay MCP Server](https://github.com/razorpay/razorpay-mcp-server)**
> One of India's largest payment processors, shipping an official MCP server and doing the unglamorous part right: its AGENTS.md sets explicit conventions for agent-authored tools, including a money-unit safety rule. Worth reading even if you never route a payment through it.

## General Utility

- [Andreax](https://pagos.andreax.dev/tienda) — Remote MCP server with 54 pay-per-call AI tools: prompt compression, inference, web/PDF read, OCR, vision, embeddings, semantic search, translation, FX, and market data. $0.001-$0.50 USDC on Base. ([MCP](https://pagos.andreax.dev/mcp)) ([Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=andreax))
- [Fry x402 MCP](https://github.com/Fry-Foundation/fry-x402-mcp) — MCP server for the fry.farm x402 API. Repo live 2026-07-30; storefront at [fry.farm/x402](https://fry.farm/x402/).
- [blockrun-mcp](https://blockrun.ai) — Live data MCP for AI agents: search, research, markets, crypto, X/Twitter. Pay-per-use USDC on Base and Solana via x402. 31+ AI models, 600+ services indexed. 471★
- [MetaMask MCP x402](https://github.com/metamask/mcp-x402) — Official MetaMask MCP server with x402 payment integration. Creates x402 payment headers using MetaMask wallet. 4★
- [x402-mcp](https://www.npmjs.com/package/x402-mcp) — Vercel's `paidTool` primitive — add an x402 paywall to any MCP tool with one wrapper. The foundational MCP payment SDK. ([Blog](https://vercel.com/blog/introducing-x402-mcp-open-protocol-payments-for-mcp-tools)) ([Starter Template](https://vercel.com/templates/next.js/x402-ai-starter))
- [agentsvc.io MCP](https://agentsvc.io/mcp-server.mjs) — 20 pay-per-call utility tools: screenshots (Playwright), OCR (Tesseract), PDF generation, webpage reader, web/news search, weather, forex/crypto/stock prices, DNS, IP geolocation, geocoding, translation, QR codes, email/phone/SSL validation, WHOIS. $0.001-$0.008 USDC on Base. ([GitHub](https://github.com/jakobautomation/agentsvc-mcp))
- [Spraay MCP](https://docs.spraay.app) — 60+ tool MCP server for multi-chain DeFi payments: batch sends, payroll, token swaps, bridge, escrow, AI inference, Robot Task Protocol (RTP). 76+ x402 endpoints across 13 chains. $0.005-$0.25 USDC. ([GitHub](https://github.com/plagtech)) ([Smithery](https://smithery.ai/server/@plagtech/spraay-x402-mcp))
- [EntRoute MCP](https://www.npmjs.com/package/@entroute/mcp-server) — Discover and call 350+ verified x402 API endpoints across 110+ capabilities. Natural language intent discovery, quality ranking (success rate, latency, price), automatic payments. `npx @entroute/mcp-server`. ([GitHub](https://github.com/entroute/mcp-server))
- [Pylon MCP](https://www.npmjs.com/package/@pylonapi/mcp) — 20-tool MCP server: web extraction, search, translation, code execution, image generation, email, and more. `npx @pylonapi/mcp`. ([GitHub](https://github.com/pylon-apis/pylon-mcp))
- [Apollo Intelligence MCP](https://www.npmjs.com/package/@apollo_ai/mcp-proxy) — 26-tool MCP server: intelligence feeds, crypto, OSINT, DeFi, proxy, and search. `npx @apollo_ai/mcp-proxy`. ([GitHub](https://github.com/bnmbnmai/mcp-proxy))
- [APIbase.pro](https://apibase.pro) — MCP gateway with 263+ tools from 74 providers, x402 USDC micropayments on Base.
- [x402engine MCP](https://www.npmjs.com/package/x402engine-mcp) — 74 pay-per-call API tools: 44 LLMs, image/video generation, crypto data, web search, code execution, TTS, travel, IPFS. Multi-chain USDC. `npx x402engine-mcp`. ([GitHub](https://github.com/agentc22/x402-engine))
- [APIMesh MCP](https://www.npmjs.com/package/@mbeato/apimesh-mcp-server) — 16-tool MCP server for web analysis: SEO, security headers, Core Web Vitals, domain availability, email security, tech stack detection, wallet spend tracking. x402 on Base. `npx @mbeato/apimesh-mcp-server`. ([GitHub](https://github.com/mbeato/conway))
- [AskClaude MCP](https://www.npmjs.com/package/askclaude-mcp) — Pay-per-query Claude AI. 9 x402 endpoints: Haiku/Sonnet/Opus chat, streaming, summarization, code review, translation, sentiment, crypto analysis. $0.01-$0.10 USDC on Base. `npx askclaude-mcp`. ([GitHub](https://github.com/pvega23/askclaude-mcp))
- [JubJub MCP](https://api.jubjubapp.com/v2/mcp) — 65-tool MCP server for media publishing, cross-platform analytics, automated on-chain royalty splits.
- [Human Pages MCP](https://github.com/human-pages-ai/humanpages) — 31-tool MCP for the open directory AI agents use to hire humans for real-world tasks. x402 pay-per-use on Base.
- [vindex-mcp](https://www.npmjs.com/package/vindex-mcp) — Vehicle data over x402: VIN decode with warranty terms, recalls, reliability, and US/Canada purchase-cost estimates. USDC on Base. `npx vindex-mcp`.
- [Apiosk](https://apiosk.com) — MCP gateway to discover, pay for, execute, and publish x402 APIs. Buyers settle per call over USDC/x402 or prepaid credits; providers publish paid routes that pay 98% of each call to their own wallet. Hosted at mcp.apiosk.com/mcp and listed in the official MCP Registry as io.github.obcraft/apiosk-mcp. USDC on Base. `npx @apiosk/mcp`. ([npm](https://www.npmjs.com/package/@apiosk/mcp)) ([PyPI](https://pypi.org/project/apiosk-mcp/)) ([GitHub](https://github.com/obcraft/apiosk-mcp))
- [402Found](https://402found.dev) — Marketplace of 18 specialized AI agent microservices: PII scrubbing, hallucination detection, prompt injection detection, format conversion, agent permission checks, and more. Each service is independently pay-per-request via x402 in USDC on Base.
- [BridgeNode MCP](https://www.npmjs.com/package/@bridgenode/mcp) — x402-gated AI inference MCP server: chat completions + model listing, automatic USDC payments on Solana. Remote streamable-http at [bridgenode.cc/mcp](https://bridgenode.cc/mcp) or stdio via `npx @bridgenode/mcp`. Example tool call: `chat_completions {"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}]}`. ([GitHub](https://github.com/applefanaimail-blip/bridgenode-skill))

---
- [botwire-mcp](https://www.npmjs.com/package/botwire-mcp) — The Bot Wire as MCP tools: 57 real-time primary-source wires (SEC EDGAR, Federal Register, federal courts, DOJ, FDA, Fed/ECB, BLS/BEA, CISA, NWS, USGS, arXiv) paid per call in USDC on Base. Free preview tier works with no wallet configured. Remote endpoint at [thebotwire.com/mcp](https://thebotwire.com/mcp) or `npx botwire-mcp`. ([GitHub](https://github.com/ArasPasha/botwire-mcp))
- [AgentFund US Economic, SEC & On-Chain Data](https://x402.agentfund.net/mcp) — 21 tools over US government data and public chain state: Treasury yield curve, CPI, PCE, jobs, GDP, retail sales, housing starts, EIA energy, release calendar; SEC EDGAR insider Form 4, XBRL financials, 13F holdings, filing feeds, full-text search; EVM token balances, portfolios, cross-chain balances, Chainlink oracle prices, gas. $0.001–$0.03 USDC on Base. Each tool also has its own HTTP route; example: `POST https://x402.agentfund.net/x402/edgar_financials {"ticker":"AAPL"}`. A call that fails upstream is returned unsettled rather than billed. ([OpenAPI](https://x402.agentfund.net/openapi.json)) ([GitHub](https://github.com/ktcod/x402-json-repair-mcp))

## Crypto & DeFi Intelligence

- [Cerebrus Pulse MCP](https://cerebruspulse.xyz) — Real-time crypto intelligence: technical analysis (RSI, EMAs, Bollinger Bands), sentiment, funding rates for 30+ Hyperliquid perpetuals. x402 USDC on Base.
- [BotIndex MCP](https://github.com/Cyberweasel777/botindex-mcp-server) — 17-tool signal intelligence: sports odds, crypto correlations, token graduations (Zora/Hyperliquid/Metaplex Genesis), DFS optimization, arbitrage detection. 50 free requests/wallet then x402 on Base. `npx botindex-mcp-server`. ([npm](https://npmjs.com/package/botindex-mcp-server))
- [Harvey Intel](https://agents.rugslayer.com) — Solana token rug pull detection (DrainBrain ML ensemble), trading signals, social intelligence. 8 tools, $0.005-$0.05 USDC on Solana. ([npm](https://www.npmjs.com/package/@meltingpixels/harvey-intel))
- [Harvey Tools](https://tools.rugslayer.com) — Web scraping, screenshots, structured data extraction, code review, content generation, sentiment analysis. 8 tools on Solana. ([npm](https://www.npmjs.com/package/@meltingpixels/harvey-tools))
- [Harvey Verify](https://verify.rugslayer.com) — Post-transaction outcome verification using LLM-as-judge. Aggregated service quality scores. 5 tools on Solana.
- [Harvey Budget](https://budget.rugslayer.com) — Agent spending management: budget tracking, ROI analysis, spend approval. 6 tools on Solana.
- [SolSigs MCP](https://solsigs.com) — 16-tool Solana blockchain intelligence MCP server: DEX prices, arbitrage, wallet scoring, token launches, NFT intel, whale tracking, smart money, staking, Polymarket predictions, social sentiment, RPC relay, price feeds, dev activity, alerts, on-chain summarizer, trending tokens. $0.001-$0.010 USDC on Solana.
- [isocast-mcp](https://www.npmjs.com/package/isocast-mcp) — Per-signal Polymarket weather-market data across 37 cities, with market URLs and live bucket odds. USDC on Base. `npx isocast-mcp`.
- [moltalyzer-mcp](https://www.npmjs.com/package/moltalyzer-mcp) — Polymarket and AI-agent-community intelligence: order-book microstructure movers, whale hold-to-resolution calibration, and multi-source digests. USDC on Base. `npx moltalyzer-mcp`.

---

## Security

- [ShieldAPI MCP](https://www.npmjs.com/package/shieldapi-mcp) — 9-tool security MCP: password breach, email breach, domain/IP reputation, URL safety, full security scan, prompt injection detection, skill security scanning. x402 USDC on Base or free demo mode. `npx shieldapi-mcp`.
- [MCP Security Snapshot Server](https://github.com/Seiya-wasabi/mcp-server-security-snapshot) — Pay-per-call HTTP security header scanning. $0.05 USDC on Base.
- [lso-mcp](https://mcp.lonestaroracle.xyz) — 46 LoneStarOracle data tools: token and wallet risk, contract audits, whale tracking, DeFi and stablecoin risk, market and macro data, weather. x402-metered USDC on Base. ([GitHub](https://github.com/Homie4570/lso-mcp))

---

## Code & Development

- [24K Labs MCP](https://api.24klabs.ai) — 6 AI code analysis tools: explain, debug, review, security audit, automation scripts, MCP blueprints. $0.50-$50.00 USDC on Base.
- [Stack AI x402](https://x402.stacks-ai.app) — Platform for monetizing MCP servers. Tool calls execute inline with payment prompts.
- [PYTHIA Oracle](https://github.com/eyloni/pythia-oracle) — Oracle MCP server. One tool (`consult_oracle`), one reading. 3 free per agent, then $0.025 USDC on Base via x402. [Smithery](https://smithery.ai/servers/dexigo/pythia)

---

## Identity & Trust

- [ALTER MCP](https://mcp.truealter.com/api/v1/mcp) — Identity infrastructure MCP for the AI economy. Verified human identity via 33-trait psychometric engine. Identity Income via x402 USDC. 16 tools free. ([Docs](https://truealter.com)) ([SDK](https://github.com/true-alter/alter-identity))
- [Azeth MCP](https://github.com/azeth-protocol/mcp-server) — x402 payment tool (`azeth_pay`), ERC-8004 trust registry discovery, on-chain reputation scoring, payment agreements for recurring billing. ([npm](https://www.npmjs.com/package/@azeth/mcp-server))
- [MoltGuard](https://api.moltrust.ch/guard/) — Agent trust scoring (0-100), Sybil detection, Polymarket integrity, Ed25519 Verifiable Credentials. 7 MCP tools. $0.005-$0.05 USDC on Base. ([GitHub](https://github.com/moltrust/moltguard))

---

## Escrow & Payments

- [Razorpay MCP Server](https://github.com/razorpay/razorpay-mcp-server) — Official MCP server from one of India's largest payment processors. Its `AGENTS.md` is worth reading on its own — an explicit convention set for agent-authored tools, including a money-unit safety rule.
- [PayCrow](https://github.com/michu5696/paycrow) — Escrow protection for autonomous agent payments. Trust scoring from 4 on-chain sources + USDC escrow with dispute resolution on Base. 10 MCP tools: `safe_pay` (trust-informed escrow) and `trust_gate` (go/no-go before payment). ([npm](https://www.npmjs.com/package/paycrow))
- [Arbitova](https://arbitova.com) — Escrow + transparent AI arbitration (N=3 LLM majority vote). Sub-task chained escrow for agent swarms. 0.5% success fee, 2% dispute only. 8 MCP tools. ([npm SDK](https://www.npmjs.com/package/@arbitova/sdk)) ([MCP](https://www.npmjs.com/package/@arbitova/mcp-server))
- [PayBot MCP](https://github.com/RBKunnela/paybot-mcp) — Claude and AI agents make autonomous x402 payments. Wallet management, transaction history, configurable spending limits. ([npm](https://www.npmjs.com/package/paybot-mcp))
- [agentpay-mcp](https://github.com/up2itnow0822/agentpay-mcp) — Native x402 client-side payment execution inside the agent loop. Detects 402 responses and completes transactions with no human handoff. ([npm](https://www.npmjs.com/package/agentpay-mcp))
- [402-mcp](https://github.com/forgesworn/402-mcp) — Payment-rail-agnostic x402 MCP client. No Lightning node required, multi-wallet support, encrypted credentials.

---

## Discovery

- [x402search MCP](https://github.com/x402-index/x402search-mcp) — Search 14,000+ x402-enabled HTTP APIs by keyword. The largest x402 API index. $0.01 USDC per search on Base. ([npm](https://www.npmjs.com/package/x402search-mcp)) ([PyPI](https://pypi.org/project/x402search-mcp/))
- [x402 Service Discovery MCP](https://github.com/rplryan/x402-discovery-mcp) — MCP for discovering 251+ x402-payable services with quality signals (uptime, latency, trust scores). 6 tools. Smithery 100/100.
- [Intelligence Aeternum](https://github.com/codex-curator/intelligence-aeternum-mcp) — Monetized MCP server marketplace. 2M+ museum artworks. 16 MCP tools for search, enrichment, delivery. [Live](https://data-portal-172867820131.us-west1.run.app/mcp)
- [ToolOracle](https://tooloracle.io) — x402 entitlement gateway with 10 intelligence products and 90+ MCP tools: RankOracle (SEO), ShopOracle, MemeOracle, SmartMoneyOracle (whale flows), YieldOracle (DeFi), FlightOracle, HotelOracle, NewsOracle, JobOracle, MacroOracle. Unit-based pricing ($0.01/unit, 2-15 units per call). USDC on Base.

---

## Domain & Web

- [InstaDomain](https://instadomain.fly.dev) — Domain registration accepting x402. AI agents search, check availability, buy domains autonomously.
- [Recall Kitchen](https://recallkitchen.com/docs/#mcp) — Search food/product/vehicle recalls. $0.025 USDC on Base per request. [Examples](https://github.com/Recall-Kitchen/rk-mcp/tree/master/examples/go)
- [x402 Wallet for Claude Desktop](https://github.com/402md/x402-wallet-for-claude-desktop) — Native Claude Desktop extension (.mcpb one-click install). USDC wallet on Stellar and Base. Three tools: check_balance, pay, x402_fetch. Configurable budget limits.
- [Scout MCP](https://scout.hugen.tokyo) — Multi-source search across code, academic, social, community platforms. From $0.01 USDC on Base. ([Source](https://github.com/bartonguestier1725-collab/scout-mcp))
- [TweetClaw](https://xquik.com/mcp) — Real-time X (Twitter) data. 7 pay-per-use endpoints via x402. ([GitHub](https://github.com/Xquik-dev/tweetclaw)) ([npm](https://www.npmjs.com/package/@xquik/tweetclaw))

---

## Media & Content

- [Stockfilm MCP](https://api.stockfilm.com/mcp) — 217,000+ authentic vintage 8mm home movie clips (1930s-1980s) restored in 4K. AI agents search, preview, license archival footage via x402. $10 USDC per clip. 6 tools. ([Docs](https://stockfilm.com/for-ai-agents))
