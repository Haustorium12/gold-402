# Server Frameworks & Middleware

Server-side integrations for accepting x402 payments, and agent frameworks with x402 support. Drop into your existing stack with minimal changes.

---

> ★ **Featured — October 2026: [x402-rails](https://github.com/quiknode-labs/x402-rails)**
> QuickNode Labs' official Rails integration. If your API already lives in a Rails app, this is the shortest path to answering with a 402 — no new service to stand up beside it.

## Node.js / TypeScript

### Multi-Framework
- [machi](https://github.com/qntx/machi) — Agent behavior that compiles. x402-native agent execution framework with payment primitives baked in. 562★
- [aixyz](https://github.com/agentlyhq/aixyz) — Next.js-like framework for building payment-native AI agents. Bootstrap agents that pay and receive via x402 out of the box. 81★
- [x402-gateway-template](https://github.com/azep-ninja/x402-gateway-template) — Production-ready x402 gateway template. Widely referenced starting point for new x402 server deployments. 94★
- [monapi](https://monapi.dev) — One-line API monetization SDK. Wraps x402 setup into a single function call. Express, Next.js, and MCP support. Per-route pricing, Base/Arbitrum/Polygon, gas-free agent payments via EIP-3009. ([npm](https://www.npmjs.com/package/@monapi/sdk)) ([GitHub](https://github.com/DenisTheM/monapi))

### Express / Hono
- [@moltrust/x402](https://www.npmjs.com/package/@moltrust/x402) — Trust score middleware for x402 endpoints. One line: `app.use(requireScore({ minScore: 60 }))`. Extracts paying wallet from X-Payment header, looks up MolTrust trust score, blocks agents below threshold with 403. Zero dependencies. ([GitHub](https://github.com/MoltyCel/moltrust-x402))
- [Azeth Provider](https://github.com/azeth-protocol/provider) — Hono middleware for gating endpoints behind x402 with payment-agreement support for recurring agent-to-agent billing. ([npm](https://www.npmjs.com/package/@azeth/provider))

### Next.js
- [x402-next](https://www.npmjs.com/package/x402-next) — App Router middleware for Next.js.
- [Next.js route protection](https://github.com/x402-foundation/x402/tree/main/examples/typescript/fullstack/next) — Official complete Next.js app example with x402 payment gates.

### API Gateways
- [Zuplo x402](https://zuplo.com/blog/mcp-api-payments-with-x402) — API gateway with x402 paywalls. Add pay-per-request monetization to any API or MCP server. Sub-cent transaction fees on Base and Solana. ([Docs](https://zuplo.com/docs/articles/monetization))

---

## Python

### FastAPI
- [FastAPI example](https://github.com/x402-foundation/x402/tree/main/examples/python) — Official complete FastAPI implementation with x402 payment middleware.

---

## Rust

### Axum
- [x402-axum](https://crates.io/crates/x402-axum) — Axum web framework integration (part of [x402-rs](https://github.com/x402-rs/x402-rs)).
- [x402-reqwest](https://crates.io/crates/x402-reqwest) — Reqwest HTTP client wrapper (part of x402-rs).

---

## Ruby / Rails

- [x402-rails](https://github.com/quiknode-labs/x402-rails) — Accept instant blockchain micropayments in Rails applications using x402. QuickNode Labs official Rails integration. 36★

---

## Astro

- [astro-x402](https://github.com/morinokami/astro-x402) — Astro middleware integration for the x402 Payment Protocol. Drop into any Astro project to gate routes behind USDC micropayments. 2★

---

## Java / Spring Boot

- [x402-spring-boot-starter](https://github.com/mogami-tech/x402-spring-boot-starter) — Protect Java APIs with pay-per-call logic using a single Spring Boot annotation. Fills the Java framework gap in the official x402 ecosystem. 10★

---

## EVM / Account Abstraction

- [nero-x402](https://github.com/nerochain/nero-x402) — First Account Abstraction-native x402 stack on NERO Chain. Facilitator, SDK, and audited AA contracts for gasless agent payments. 47★

---

## Cloudflare Workers

- [Cloudflare Agents SDK v0.4.0](https://developers.cloudflare.com/agents/) — x402 v2 migration support: `ClientEvmSigner` type, auto-selection from payment requirements, dual-header support (v2 `PAYMENT-SIGNATURE` + v1 `X-PAYMENT`), lazy facilitator initialization.

---

## Agent Frameworks

- [Franklin](https://github.com/blockrunai/franklin) — The AI agent with a wallet — spends USDC autonomously to get real work done. Agentic payment-native framework by BlockRun. 636★
- [Lucid Agents](https://github.com/daydreamsai/lucid-agents) — Commerce SDK by Daydreams. Bootstrap AI agents in 60 seconds that can pay, sell, and transact autonomously via x402. 188★
- [Agenti](https://github.com/nirholas/agenti) — Give any AI agent a crypto wallet. Agents pay x402 APIs with USDC on Base. Simple drop-in wallet integration. 68★
- [mcpay](https://github.com/microchipgnu/mcpay) — Open-source infrastructure for MCP and x402. Payment primitives for building monetized MCP servers. 90★
- [use-agently](https://github.com/agentlyhq/use-agently) — Routing and settlement layer for AI agents. x402-native payment coordination for multi-agent workflows. 69★
- [Vault-0](https://github.com/0-Vault/Vault-0) — Encrypted secret vault, agent monitor, and x402 wallet for OpenClaw. Handles 402 detection, EIP-3009 signing, policy-gated auto-settlement.
- [Nevermined](https://nevermined.ai/blog/building-agentic-payments-with-nevermined-x402-a2a-and-ap2) — Integrated Visa Intelligent Commerce + x402 for autonomous AI agent commerce (April 9, 2026). Agents get delegated credit card spending authority with budget limits, per-purchase caps, merchant restrictions, time windows.
- [Phidata Agents](https://github.com/phidatahq/phidata) — Multi-modal agents with x402 integration.
- [NEAR AI](https://near.ai) — Cross-chain agent settlements.
- [World AgentKit](https://www.coindesk.com/tech/2026/03/17/sam-altman-s-world-teams-up-with-coinbase-to-prove-there-is-a-real-person-behind-every-ai-transaction) — Integrates World's WorldID biometric identity with x402. AI agents prove they act on behalf of a verified unique human during x402 transactions. 18M+ verified humans.

---
