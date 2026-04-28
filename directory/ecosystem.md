# Ecosystem Projects

Infrastructure, agent frameworks, A2A protocols, multi-agent orchestration, and marketplace platforms building on or extending x402.

---

## Infrastructure

- [Coinbase Developer Platform](https://coinbase.com/cloud) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Hosted facilitator service with enterprise-grade reliability and instant settlement. The primary x402 infrastructure layer.
- [Cloudflare x402](https://blog.cloudflare.com/x402/) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Edge payment processing across 300+ global data centers.
- [Polygon Agentic Payments](https://polygon.technology/payments/agentic-payments) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Near-instant finality, sub-$0.001 fees, no reorgs. Coinbase CDP facilitator with gas sponsorship and KYT compliance. USDC, USDT, non-USD stablecoins. ([Docs](https://agentic-docs.polygon.technology/general/x402/intro/))
- [Finance District Prism](https://developers.fd.xyz/prism/concepts/x402) — Payment gateway for agentic commerce. TypeScript, Python, Java SDKs. Two-layer architecture: Prism (orchestration) and Spectrum (on-chain settlement across Base, Ethereum, Arbitrum, BSC). ([Docs](https://developers.fd.xyz))
- [thirdweb Nebula](https://thirdweb.com/nebula) — AI agent transaction framework on x402.
- [MoltsPay](https://moltspay.com) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-5+-blue?style=flat-square)](https://moltspay.com) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/Yaqing2023/moltspay) — Open payment protocol for AI agents. One JSON file to accept x402 payments. Gasless for both providers and clients. Multi-chain. CLI, TypeScript/Python SDKs, testnet faucet. ([Docs](https://moltspay.com/docs))
- [Bermuda](https://www.bermudabay.xyz) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/BermudaBay/sdk) — ZK-private HTTP payments for x402. Adds sender privacy via Noir zero-knowledge proofs on Base. Agents pay without exposing wallet balances or transaction history.
- [XyncPay](https://xyncpay.com) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/xyncpay/xyncpay) — Protocol translation layer bridging x402, MPP, and AP2. One integration, every AI agent payment protocol. Atomic fee-split settlement via on-chain FeeSplit contract on Base.
- [RustChain](https://github.com/Scottcjn/Rustchain) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/Scottcjn/Rustchain) — Decentralized PoS blockchain with native x402 for AI agent micropayments. Attestation-based consensus, hardware-bound validators, RTC token economy.
- [EntRoute](https://entroute.com) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Machine-first API discovery for AI agents. 110+ capabilities, semantic intent resolution, continuous 402 verification probes, quality ranking. MCP server, TypeScript SDK, REST API. ([Docs](https://entroute.com/docs))

---

## Agent Wallets

- [CardZero](https://cardzero.ai) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/mrocker/CardZero) — ERC-4337 smart contract wallets for AI agents. Owner-controlled spending rules (per-tx limits, daily caps, whitelist, freeze). x402 buyer support via `POST /v1/x402/pay`. [GitHub](https://github.com/mrocker/CardZero)
- [Coinbase Agentic Wallets](https://www.abhs.in/blog/ai-agents-crypto-wallets-coinbase-x402-brian-armstrong-2026) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Wallet infrastructure purpose-built for autonomous AI agents. 50M+ transactions processed since protocol launch.
- [ATXP](https://github.com/atxp-dev/atxp) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/atxp-dev/atxp) — Agent identity and funding platform. One command gives an agent a USDC wallet, `@atxp.email` inbox, phone number, and 100+ paid tools. x402-compatible, $5 free credit, no KYC. ([Docs](https://docs.atxp.ai))
- [OpenVPS](https://openvps.sh) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-3+-blue?style=flat-square)](https://openvps.sh) — AI-agent VPS hosting. Pay USDC on Base, Celo, or Tempo — get root SSH to Ubuntu 24.04 Firecracker microVMs in seconds. x402 + MPP dual-protocol. From $0.005/hr. ([GitHub](https://github.com/kartojal/openvps))

---

## Agent Frameworks

- [Vault-0](https://github.com/0-Vault/Vault-0) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/0-Vault/Vault-0) — Encrypted secret vault, agent monitor, and x402 wallet for OpenClaw. Handles 402 detection, EIP-3009 signing, policy-gated auto-settlement.
- [Nevermined](https://nevermined.ai/blog/building-agentic-payments-with-nevermined-x402-a2a-and-ap2) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-multi-blue?style=flat-square)](https://nevermined.ai) — Integrated Visa Intelligent Commerce + x402 for autonomous AI agent commerce (April 9, 2026). Agents get delegated credit card spending authority with budget limits, per-purchase caps, merchant restrictions, time windows.
- [Phidata Agents](https://github.com/phidatahq/phidata) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/phidatahq/phidata) — Multi-modal agents with x402 integration.
- [NEAR AI](https://near.ai) — Cross-chain agent settlements.
- [World AgentKit](https://www.coindesk.com/tech/2026/03/17/sam-altman-s-world-teams-up-with-coinbase-to-prove-there-is-a-real-person-behind-every-ai-transaction) — Integrates World's WorldID biometric identity with x402. AI agents prove they act on behalf of a verified unique human during x402 transactions. 18M+ verified humans.

---

## Agent-to-Agent (A2A)

- [Google A2A x402 Extension](https://github.com/google-agentic-commerce/a2a-x402) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/google-agentic-commerce/a2a-x402) [![A2A Ready](https://img.shields.io/badge/A2A-ready-purple?style=flat-square)](https://github.com/google-agentic-commerce/a2a-x402) — Agent commerce protocol. Python and TypeScript implementations. Payment-required, payment-submitted, payment-completed flow. Multi-agent payment orchestration.
- [Revettr](https://revettr.com) [![A2A Ready](https://img.shields.io/badge/A2A-ready-purple?style=flat-square)](https://revettr.com) — Counterparty risk scoring API for x402 agentic commerce. Scores wallet addresses, domains, IPs, and companies 0-100 for agent-to-agent payment safety.
- OpSpawn A2A x402 Gateway [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-3+-blue?style=flat-square)]() — Multi-chain A2A gateway with x402 payments. Google A2A protocol, Base/SKALE/Arbitrum support.

---

## Multi-Agent Orchestration

- [SwarmX](https://swarmx.io) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/SolTwizzy/swarms-x402) — Multi-agent AI orchestration with native x402 micropayments on Solana. 49 endpoints, 39 MCP tools, dual LLM, knowledge/RAG with pgvector. ElizaOS v2 plugin. ([npm](https://www.npmjs.com/package/swarms-x402))
- [Agent.market](https://agent.market) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — x402 Foundation's official app store for agents. Launched April 20, 2026. Unified marketplace aggregating x402-enabled services. Find, evaluate pricing, consume services. Backed by Coinbase.
- [payagent](https://github.com/stevemilton/payagent) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/stevemilton/payagent) — Drop-in `fetch` wrapper that auto-handles HTTP 402 responses. Zero agent code changes required.
- [AlphaClaw](https://github.com/diassique/alphaclaw) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/diassique/alphaclaw) — Autonomous AI agent network hunting alpha on Polymarket and DeFi. 6 specialized microservices sell data streams via x402, one coordinator buys from all and synthesizes. ACP with stake-weighted voting.

---

## Marketplaces & Discovery

- [Agent.market](https://agent.market) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — The official x402 Foundation app store. The canonical starting point for discovering x402-enabled services.
- [WorkProtocol](https://workprotocol.ai) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/Atlaskos/workprotocol) [![A2A Ready](https://img.shields.io/badge/A2A-ready-purple?style=flat-square)](https://workprotocol.ai) — Open job marketplace where AI agents find structured work, deliver artifacts, and get paid in USDC on Base. Escrow-backed, portable on-chain reputation, framework-agnostic.
- [MAXIA](https://maxiaworld.app) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-2+-blue?style=flat-square)](https://maxiaworld.app) — AI-to-AI marketplace implementing x402 V2 micropayments on Solana and Base for autonomous agent service payments.
- [AgentStore](https://agentstore.tools) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://agentstore.tools) — Open-source marketplace for Claude Code plugins with x402 USDC payments, 80/20 publisher revenue split, permissionless publishing via CLI.
- [x402 Bazaar](https://x402bazaar.org) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/Wintyx57/x402-backend) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-2+-blue?style=flat-square)](https://x402bazaar.org) — Decentralized API marketplace with 69 native x402-payable endpoints. Multi-chain USDC on Base and SKALE. MCP server via `npx x402-bazaar init`. 505 passing tests.
- [Orbis API Marketplace](https://orbisapi.com) — x402-native API marketplace with 1,000+ APIs at $0.01/call via USDC on Base. Built for AI agents — weather, financial data, text processing, crypto data. No API keys required.
- [Satring](https://satring.com) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/toadlyBroodle/satring) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-2+-blue?style=flat-square)](https://satring.com) — Curated L402 + x402 API directory with human ratings, health monitoring, MCP server. Dual-protocol (Lightning + USDC on Base).

---

## Charity & Social Impact

- [x402charity](https://x402charity.com) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/allscale-io/x402charity) — Open-source micro-donation server powered by x402. Drop-in Express/Next.js middleware triggers USDC charity donations on every user action. npm package, CLI, Vercel-deployable server with dashboard. ([npm](https://www.npmjs.com/package/x402charity))
