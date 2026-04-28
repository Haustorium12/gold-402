# SDKs & Client Libraries

Client and server-side libraries for building with x402. Start with the official Coinbase SDKs, then layer in community libraries as your stack demands.

---

## TypeScript / JavaScript

### Official
- [x402-typescript](https://github.com/coinbase/x402/tree/main/typescript) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Official TypeScript implementation. Core protocol types, payment verification and settlement logic, multi-chain support (Base, Base Sepolia, Ethereum, Solana).

### HTTP Clients
- [cipher-x402-client](https://github.com/cryptomotifs/cipher-x402-client) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/cryptomotifs/cipher-x402-client) — Lightweight TS/JS x402 v2 client. Zero runtime deps, native fetch, ESM + CJS dual build. 34 tests, 89% coverage. Node 18+ / browsers. Optional `ethers` peer dep for signing.
- [x402-got](https://www.npmjs.com/package/x402-got) — Got HTTP client integration for x402.

### AI Agent SDKs
- [x402-mcp](https://www.npmjs.com/package/x402-mcp) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Vercel's library for adding x402 paywalls to MCP servers via the AI SDK. The `paidTool` primitive — declare a price on any MCP tool, require payment before execution. ([Blog](https://vercel.com/blog/introducing-x402-mcp-open-protocol-payments-for-mcp-tools))
- [PayBot SDK](https://github.com/RBKunnela/paybot-sdk) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/RBKunnela/paybot-sdk) — TypeScript SDK for integrating x402 into AI agents and bots. Automatic 402 detection, wallet management, USDC on Base. ([npm](https://www.npmjs.com/package/paybot-sdk))
- [ClawPay MCP](https://www.npmjs.com/package/clawpay-mcp) — Non-custodial x402 payment layer for AI agents. Agents sign locally with their own keys. USDC on Base.
- [Azeth SDK](https://github.com/azeth-protocol/sdk) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/azeth-protocol/sdk) [![ERC-8004](https://img.shields.io/badge/ERC--8004-registered-E36209?style=plastic)](https://github.com/azeth-protocol/sdk) — TypeScript SDK with x402 client (`fetch402`), ERC-4337 smart accounts, on-chain reputation feedback, and ERC-8004 service discovery. ([npm](https://www.npmjs.com/package/@azeth/sdk))
- [MoltsPay](https://github.com/Yaqing2023/moltspay) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-5+-blue?style=flat-square)](https://github.com/Yaqing2023/moltspay) — Payment infrastructure for AI agents. CLI, TypeScript SDK, LangChain/CrewAI integrations. Gasless payments on Base, Polygon, Solana, BNB, Tempo. ([npm](https://www.npmjs.com/package/moltspay))

### Privacy
- [PRXVT Privacy SDK](https://github.com/prxvt/sdk) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/prxvt/sdk) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-2+-0366D6?style=plastic)](https://github.com/prxvt/sdk) — Privacy layer for x402. Fresh burner wallet per payment (unlinkable), Groth16 zero-knowledge proofs, AES-256-GCM encrypted notes, cross-chain deposits (Base to Polygon). ([Website](https://www.prxvt.com/))

### Wallet Integration
- [Agent Wallet SDK](https://www.npmjs.com/package/agentwallet-sdk) — Non-custodial smart contract wallets for AI agents. On-chain spend limits, operator model. Base L2.
- [viem](https://viem.sh/) — TypeScript library used for signing x402 payments.
- [ethers.js](https://docs.ethers.org/) — Alternative Ethereum library for signing.

---

## Python

### Official
- [x402](https://pypi.org/project/x402/) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Official Python SDK. FastAPI middleware, `requests` session with auto-payments, payment requirement generation.

### Community
- [ag402](https://github.com/AetherCore-Dev/ag402) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/AetherCore-Dev/ag402) — Payment layer for AI agents using x402. Wrap any API or MCP server with a USDC paywall (`ag402 serve`), or let agents auto-pay (`ag402 run`). Solana USDC, ~0.5s settlement, non-custodial, 648+ tests.
- [open402](https://pypi.org/project/open402/) — Wire-compatible protocol layer of the ag402 project. Standalone protocol parsing or full engine with `ag402-core`.
- [primer-x402](https://pypi.org/project/primer-x402/) — Python SDK for x402 payments — pay and charge for APIs with stablecoins.
- [x402-pay](https://pypi.org/project/x402-pay/) — Call any x402 API with one API key. Routes through a broker that handles on-chain payment. httpx-based with optional wallet mode. ([GitHub](https://github.com/bartonguestier1725-collab/x402-pay))
- [MoltsPay Python](https://github.com/Yaqing2023/moltspay-python) [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-4+-blue?style=flat-square)](https://github.com/Yaqing2023/moltspay-python) — Python SDK for x402 agent payments. LangChain compatible. Auto-creates wallets, discovers services, pays via x402. Base, Polygon, Solana, BNB. ([PyPI](https://pypi.org/project/moltspay/))
- [x402 Payment Harness](https://github.com/rplryan/x402-payment-harness) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/rplryan/x402-payment-harness) — Python library + CLI for x402 without Coinbase CDP wallet. Works with any Ethereum EOA. Full HTTP 402 -> EIP-712 sign -> X-PAYMENT header flow. `pip install x402-payment-harness`.
- [x402-mock](https://pypi.org/project/x402-mock/) — Test/mock implementation of x402 for EVM blockchains. Useful for dev/testing without live payments.

### XRPL
- [xrpl-x402-core](https://pypi.org/project/xrpl-x402-core/) — Wire-level validation with CAIP-2 XRPL identifiers.
- [xrpl-x402-client](https://pypi.org/project/xrpl-x402-client/) — Buyer-side Python SDK with `wrap_httpx_with_xrpl_payment`.
- [xrpl-x402-middleware](https://pypi.org/project/xrpl-x402-middleware/) — Server-side middleware with `require_payment()`. Optional Coinbase x402 interop.

---

## Rust

- [x402-rs](https://github.com/x402-rs/x402-rs) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/x402-rs/x402-rs) — Production-grade Rust implementation. Axum middleware, reqwest client wrapper, self-hostable facilitator, multi-chain support.
- [x402-kit](https://github.com/bitrouter/x402-kit) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/bitrouter/x402-kit) — Fully modular, framework-agnostic Rust SDK. Composable buyer (signer) and seller (server) primitives. ([crates.io](https://crates.io/crates/x402-paywall))
- [alloy](https://github.com/alloy-rs/alloy) — High-performance Ethereum library used for Rust x402 signing.

---

## Go

- [coinbase/x402 (Go)](https://github.com/coinbase/x402/tree/main/go) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Official Go implementation. Core protocol types, multi-chain support.
- [x402-go](https://github.com/mark3labs/x402-go) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/mark3labs/x402-go) — Community Go implementation by Mark III Labs.
- [mcp-go-x402](https://github.com/mark3labs/mcp-go-x402) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/mark3labs/mcp-go-x402) — x402 payment transport for MCP-Go clients and servers. Drop-in replacement compatible with mcp-go transport interface. Automatic 402 handling, multi-chain (EVM + Solana), mock signers for testing. ([Go Package](https://pkg.go.dev/github.com/mark3labs/mcp-go-x402))

---

## Other Languages

- [genlayer-x402](https://github.com/habiiyt31/genlayer-x402) — x402 for GenLayer Intelligent Contracts. 4 production-ready on-chain contracts gating real-time web data and AI services behind trustless payments. No server, no API key, no middleman.
- [Spillway](https://github.com/openledger-labs/Spillway) — Subscription payment channels on Stellar using x402. Stream payments, not transactions — 1,000 requests = only 2 on-chain transactions.
