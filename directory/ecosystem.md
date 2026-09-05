# Ecosystem Projects

Infrastructure, agent frameworks, A2A protocols, multi-agent orchestration, and marketplace platforms building on or extending x402.

---

> ★ **Featured — August 2026: [Glama](https://glama.ai/mcp/servers)**
> An MCP registry indexing 64,000+ servers — and the only one publishing both its scoring rubric and its health data. In a space full of unexplained ranks, you can see what it checked and how it decided.

## Foundation & Protocol

- [x402](https://github.com/x402-foundation/x402) — The canonical x402 protocol repository maintained by the x402 Foundation under the Linux Foundation. Reference implementations, official SDKs, spec documentation. The source of truth for the protocol. 6,147★
- [x402scan](https://x402scan.com) — x402 Ecosystem Explorer by Merit Systems. Browse, search, and monitor the x402 service landscape. 346★
- [Awesome Agentic Commerce](https://github.com/merit-systems/awesome-agentic-commerce) — Curated resources for the x402 ecosystem by Merit Systems. Comprehensive listing of protocols, SDKs, and projects. 127★

---

## Infrastructure

- [Coinbase Developer Platform](https://coinbase.com/cloud) — Hosted facilitator service with enterprise-grade reliability and instant settlement. The primary x402 infrastructure layer.
- [Cloudflare x402](https://blog.cloudflare.com/x402/) — Edge payment processing across 300+ global data centers.
- [Polygon Agentic Payments](https://polygon.technology/payments/agentic-payments) — Near-instant finality, sub-$0.001 fees, no reorgs. Coinbase CDP facilitator with gas sponsorship and KYT compliance. USDC, USDT, non-USD stablecoins. ([Docs](https://agentic-docs.polygon.technology/general/x402/intro/))
- [Finance District Prism](https://developers.fd.xyz/prism/concepts/x402) — Payment gateway for agentic commerce. TypeScript, Python, Java SDKs. Two-layer architecture: Prism (orchestration) and Spectrum (on-chain settlement across Base, Ethereum, Arbitrum, BSC). ([Docs](https://developers.fd.xyz))
- [thirdweb Nebula](https://thirdweb.com/nebula) — AI agent transaction framework on x402.
- [MoltsPay](https://moltspay.com) — Open payment protocol for AI agents. One JSON file to accept x402 payments. Gasless for both providers and clients. Multi-chain. CLI, TypeScript/Python SDKs, testnet faucet. ([Docs](https://moltspay.com/docs))
- [Bermuda](https://www.bermudabay.xyz) — ZK-private HTTP payments for x402. Adds sender privacy via Noir zero-knowledge proofs on Base. Agents pay without exposing wallet balances or transaction history.
- [XyncPay](https://xyncpay.com) — Protocol translation layer bridging x402, MPP, and AP2. One integration, every AI agent payment protocol. Atomic fee-split settlement via on-chain FeeSplit contract on Base.
- [RustChain](https://github.com/Scottcjn/Rustchain) — Decentralized PoS blockchain with native x402 for AI agent micropayments. Attestation-based consensus, hardware-bound validators, RTC token economy.
- [EntRoute](https://entroute.com) — Machine-first API discovery for AI agents. 110+ capabilities, semantic intent resolution, continuous 402 verification probes, quality ranking. MCP server, TypeScript SDK, REST API. ([Docs](https://entroute.com/docs))
- [WickedAPI x402 Paywall](https://paywall.wickedapi.com) — Multi-tenant x402 paywall-as-a-service on Base mainnet via the Coinbase CDP facilitator. Self-serve signup, REST API to set price/network/payout wallet and forward to a real backend, live settlement views. Example: `GET https://paywall.wickedapi.com/wickedapi/weather` returns a live 402. ([OpenAPI](https://paywall-admin.wickedapi.com/openapi.json), [Cookbook](https://paywall.wickedapi.com/cookbook.html))

---

## Agent Wallets

- [CardZero](https://cardzero.ai) — ERC-4337 smart contract wallets for AI agents. Owner-controlled spending rules (per-tx limits, daily caps, whitelist, freeze). x402 buyer support via `POST /v1/x402/pay`. [GitHub](https://github.com/mrocker/CardZero)
- [Coinbase Agentic Wallets](https://www.abhs.in/blog/ai-agents-crypto-wallets-coinbase-x402-brian-armstrong-2026) — Wallet infrastructure purpose-built for autonomous AI agents. 50M+ transactions processed since protocol launch.
- [ATXP](https://github.com/atxp-dev/atxp) — Agent identity and funding platform. One command gives an agent a USDC wallet, `@atxp.email` inbox, phone number, and 100+ paid tools. x402-compatible, $5 free credit, no KYC. ([Docs](https://docs.atxp.ai))
- [OpenVPS](https://openvps.sh) — AI-agent VPS hosting. Pay USDC on Base, Celo, or Tempo — get root SSH to Ubuntu 24.04 Firecracker microVMs in seconds. x402 + MPP dual-protocol. From $0.005/hr. ([GitHub](https://github.com/kartojal/openvps))

---

## Agent Frameworks

- [Franklin](https://github.com/blockrunai/franklin) — The AI agent with a wallet — spends USDC autonomously to get real work done. Agentic payment-native framework by BlockRun. 636★
- [Lucid Agents](https://github.com/daydreamsai/lucid-agents) — Commerce SDK by Daydreams. Bootstrap AI agents in 60 seconds that can pay, sell, and transact autonomously via x402. 188★
- [Agenti](https://github.com/nirholas/agenti) — Give any AI agent a crypto wallet. Agents pay x402 APIs with USDC on Base. Simple drop-in wallet integration. 68★
- [Faremeter](https://faremeter.io) — Universal framework for transparent API cost integration into agent workflows. Agents discover, negotiate, and pay for services via x402. 66★
- [mcpay](https://github.com/microchipgnu/mcpay) — Open-source infrastructure for MCP and x402. Payment primitives for building monetized MCP servers. 90★
- [use-agently](https://github.com/agentlyhq/use-agently) — Routing and settlement layer for AI agents. x402-native payment coordination for multi-agent workflows. 69★
- [Vault-0](https://github.com/0-Vault/Vault-0) — Encrypted secret vault, agent monitor, and x402 wallet for OpenClaw. Handles 402 detection, EIP-3009 signing, policy-gated auto-settlement.
- [Nevermined](https://nevermined.ai/blog/building-agentic-payments-with-nevermined-x402-a2a-and-ap2) — Integrated Visa Intelligent Commerce + x402 for autonomous AI agent commerce (April 9, 2026). Agents get delegated credit card spending authority with budget limits, per-purchase caps, merchant restrictions, time windows.
- [Phidata Agents](https://github.com/phidatahq/phidata) — Multi-modal agents with x402 integration.
- [NEAR AI](https://near.ai) — Cross-chain agent settlements.
- [World AgentKit](https://www.coindesk.com/tech/2026/03/17/sam-altman-s-world-teams-up-with-coinbase-to-prove-there-is-a-real-person-behind-every-ai-transaction) — Integrates World's WorldID biometric identity with x402. AI agents prove they act on behalf of a verified unique human during x402 transactions. 18M+ verified humans.

---

## Agent-to-Agent (A2A)

- [AP2 — Agent Payments Protocol](https://ap2-protocol.org) — Apache-2.0 authorization layer sitting above payment rails, built on signed user mandates. Notable for what it concedes: its Trusted Surface must be non-agentic UI, which puts a human screen at the trust anchor of an agent-payments protocol.
- [Agent Commerce Kit (ACK)](https://github.com/agentcommercekit/ack) — MIT-licensed DID and verifiable-credential toolkit for agent identity. Builds owner-accountable delegation chains — the opposite design pole from ERC-8004's pseudonymous on-chain identity.
- [Skyfire](https://docs.skyfire.xyz) — Agent identity and payment credentials as ES256 JWTs with a public JWKS endpoint. The rare pattern in this space that a stranger can verify without contacting the issuer — worth studying if you're designing receipts.
- [Google A2A x402 Extension](https://github.com/google-agentic-commerce/a2a-x402) — Agent commerce protocol. Python and TypeScript implementations. Payment-required, payment-submitted, payment-completed flow. Multi-agent payment orchestration.
- [Revettr](https://revettr.com) — Counterparty risk scoring API for x402 agentic commerce. Scores wallet addresses, domains, IPs, and companies 0-100 for agent-to-agent payment safety.
- [Animica Agent Job Network](https://x402.animica.dev) — Agents post tasks with a USDC budget and other agents perform them for payment; escrow holds the budget until the buyer's chosen verification passes, rejected jobs refund in full, receipts are ML-DSA-65 signed. Example: `POST /api/v1/jobs/quote {"capability":"summarise","budget_usd":1}`. ([OpenAPI](https://x402.animica.dev/openapi.json))

---

## Multi-Agent Orchestration

- [SwarmX](https://swarmx.io) — Multi-agent AI orchestration with native x402 micropayments on Solana. 49 endpoints, 39 MCP tools, dual LLM, knowledge/RAG with pgvector. ElizaOS v2 plugin. ([npm](https://www.npmjs.com/package/swarms-x402))
- [payagent](https://github.com/stevemilton/payagent) — Drop-in `fetch` wrapper that auto-handles HTTP 402 responses. Zero agent code changes required.
- [AlphaClaw](https://github.com/diassique/alphaclaw) — Autonomous AI agent network hunting alpha on Polymarket and DeFi. 6 specialized microservices sell data streams via x402, one coordinator buys from all and synthesizes. ACP with stake-weighted voting.

---

## Marketplaces & Discovery

- [Official MCP Registry](https://registry.modelcontextprotocol.io) — The canonical registry for the Model Context Protocol. The upstream source that Glama, PulseMCP and other aggregators pull from. Namespace authentication via GitHub — the closest thing the MCP world has to a name you can trust.
- [Glama](https://glama.ai/mcp/servers) — MCP registry indexing 64,239 servers, and the only one that publishes both its scoring rubric and its health data. Rare in this space: you can see what it checked and how it decided.
- [Agent.market](https://agent.market) — x402 Foundation's official app store for agents. Launched April 20, 2026. Unified marketplace aggregating x402-enabled services. Find, evaluate pricing, consume services. Backed by Coinbase.
- [WorkProtocol](https://workprotocol.ai) — Open job marketplace where AI agents find structured work, deliver artifacts, and get paid in USDC on Base. Escrow-backed, portable on-chain reputation, framework-agnostic.
- [MAXIA](https://maxiaworld.app) — AI-to-AI marketplace implementing x402 V2 micropayments on Solana and Base for autonomous agent service payments.
- [AgentStore](https://agentstore.tools) — Open-source marketplace for Claude Code plugins with x402 USDC payments, 80/20 publisher revenue split, permissionless publishing via CLI.
- [x402 Bazaar](https://x402bazaar.org) — Decentralized API marketplace with 69 native x402-payable endpoints. Multi-chain USDC on Base and SKALE. MCP server via `npx x402-bazaar init`. 505 passing tests.
- [Satring](https://satring.com) — Curated L402 + x402 API directory with human ratings, health monitoring, MCP server. Dual-protocol (Lightning + USDC on Base).
- [minia2a.uk](https://minia2a.uk) — Open M2M micropayment marketplace. 173 x402-payable services across 50+ categories (crypto data, web scraping, email verification, token security, agent toolkits). 34 registered agents. 5% fee, USDC settlement on Base. MCP registry, CLI, and 5-minute hands-on tutorial.
- [Frantic](https://gofrantic.com) — Bounty board where AI agents claim funded work, deliver artifacts in the open, and are paid in USDC on Base only when a delivery is accepted, with x402 pay-per-post at `POST /v1/vendor-postings/x402`, a manifest at `/.well-known/x402`, and every claim, judgment, and payout sealed to a public receipt ledger.

## Notable Implementations

- [x402-audio-to-audio](https://github.com/eversmile12/x402-audio-to-audio) — Transmits signed USDC payments over sound using a custom OOK audio modem with Goertzel DSP. A creative demonstration of x402's protocol flexibility. 35★

---

## Charity & Social Impact

- [x402charity](https://x402charity.com) — Open-source micro-donation server powered by x402. Drop-in Express/Next.js middleware triggers USDC charity donations on every user action. npm package, CLI, Vercel-deployable server with dashboard. ([npm](https://www.npmjs.com/package/x402charity))
