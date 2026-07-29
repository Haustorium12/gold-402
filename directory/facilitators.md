# Facilitators

Payment verification and settlement services for x402. A facilitator verifies payment signatures and settles USDC on-chain so your server doesn't have to run blockchain infrastructure.

> **gold-402 note:** For most builders, start with Coinbase CDP. For European deployments, AsterPay is the only MiCA-compliant option. For edge/global scale, Cloudflare. This is the shelf where trust actually settles — every x402 payment clears through one of these.
>
> **This month (July 2026):** the first NEAR facilitator landed ([NEAR x402 Facilitator](https://x402.mikedotexe.com/), open source, with published paid-flow evidence for both NEAR and Base). Chain breadth keeps widening — XRPL, Bitcoin relays, and Solana settlement all now have working facilitators on this shelf.

---

## Hosted Facilitators

- [Coinbase CDP](https://docs.cdp.coinbase.com/x402) — Official facilitator on Base and Base Sepolia. Instant settlement, supports all ERC-20 tokens (not just USDC). Most widely used in the ecosystem.
- [Stripe x402](https://docs.stripe.com/payments/machine/x402) [![24K Featured](https://img.shields.io/badge/24K_Featured-2026--04-C0C0C0?style=plastic)](../FEATURED.md) — Stripe's Machine Payments infrastructure. Deposit addresses, automatic PaymentIntent capture on settlement, dashboard monitoring, webhooks. USDC on Base. ([Quickstart](https://docs.stripe.com/payments/machine/x402/quickstart))
- [Cloudflare x402](https://developers.cloudflare.com/agents/tools/payments/x402/) — Edge computing facilitator on Base and Ethereum. Deferred settlement. Global distribution via 300+ data centers.
- [Polygon x402 Facilitator](https://docs.polygon.technology/payment-services/agentic-payments/x402/intro) — Coinbase CDP on Polygon with gas sponsorship, automated KYT compliance screening, 1,000 free transactions/month. USDC on Polygon.
- [Stellar x402](https://developers.stellar.org/docs/build/agentic-payments/x402) — Official Stellar Foundation integration. Middleware for Stellar payment addresses, browser wallet support.
- [AsterPay](https://asterpay.io) — European x402 facilitator with EUR off-ramp via SEPA Instant. First European-focused x402 infrastructure. ElizaOS plugin available.
- [Primev FastRPC](https://facilitator.primev.xyz) — Fee-free facilitator on Ethereum mainnet with sub-200ms settlement via [mev-commit](https://mev-commit.xyz) preconfirmations.
- [Bankr x402 Cloud](https://bankr.bot/x402) — Hosted platform for deploying USDC-monetized pay-per-request APIs. Includes hosting, payment processing, and agent discovery indexing. Freemium (5% revenue cut). Built on Base. Launched April 2, 2026.
- [Dexter DAO](https://github.com/Dexter-DAO/dexter-x402-sdk) — Open-source x402 facilitator and SDK. Chain-agnostic v2 with client, server, React hooks, and Express middleware.
- [Ultravioleta DAO](https://facilitator.ultravioletadao.xyz) — Multi-chain hosted facilitator supporting 33+ networks including EVM, Solana, NEAR, Stellar, Algorand, and Sui. REST API with chain-specific settlement routing.
- [BNB Chain Pieverse](https://www.pieverse.io) — BNB Chain x402 facilitator using pieUSD (a 1:1 USDT wrapper) to enable EIP-3009 gasless payments on BNB. Generates jurisdiction-compliant receipts immutably stored on BNB Greenfield for audit purposes. ([x402b GitHub](https://github.com/Pieverse-Eng/x402b))
- [MERX x402 for TRON](https://x402.merx.exchange) — First TRON facilitator. USDT, USDC, USDD on TRON mainnet. Sub-3-second confirmation. [Express middleware](https://npmjs.com/package/merx-x402).
- [XRPL / t54.ai Facilitator](https://xrpl-x402.t54.ai/) — x402 facilitator for XRP Ledger by t54.ai, supporting native XRP and RLUSD payments. Handles on-chain verification and settlement for autonomous agent transactions without requiring API keys or custodial wallets.
- [x402 Sponsor Relay](https://github.com/aibtcdev/x402-sponsor-relay) — x402 sponsor relay for AI on Bitcoin (aibtcdev). Agents access gated endpoints without managing their own wallets — relay sponsors on their behalf. ([aibtc.dev](https://aibtc.dev))
- [Satoshi Facilitator](https://bitcoinsapi.com/docs) — Independent facilitator for Bitcoin-focused pay-per-call services. Base, Base Sepolia, Solana Mainnet, Solana Devnet. [Supported networks](https://facilitator.bitcoinsapi.com/supported)
- [NEAR x402 Facilitator](https://x402.mikedotexe.com/) — Open-source, API-key-gated facilitator for exact Circle USDC payments on NEAR and Base. It sponsors relayer gas and persists settlements for recovery. [Source](https://github.com/fastnear/x402-near-facilitator) and sanitized paid-flow evidence for [NEAR](https://github.com/fastnear/x402-near-facilitator/blob/main/docs/evidence/2026-07-26-v041-near-mainnet-canary.md) and [Base](https://github.com/fastnear/x402-near-facilitator/blob/main/docs/evidence/2026-07-26-v041-base-mainnet-canary.md).
- [ArisPay](https://facilitator.arispay.app) — Free, public x402 facilitator on Base mainnet with USDC and EURC settlement. Open /verify and /settle, no API key or signup. Machine-readable fee policy and discovery at [/supported](https://facilitator.arispay.app/supported) and [/facilitator](https://facilitator.arispay.app/facilitator).

---

## Self-Hosted Facilitators

- [x402-sovereign](https://github.com/dhaiwat10/x402-sovereign) — Self-hosted x402 facilitator. Full control over payment verification and settlement. 63★
- [qntx/facilitator](https://github.com/qntx/facilitator) — Production-ready x402 facilitator server by qntx. Docker-deployable, multi-chain. 148★
- [OpenZeppelin Relayer x402 Plugin](https://github.com/openzeppelin/relayer-plugin-x402-facilitator) — x402 facilitator plugin for OpenZeppelin Relayer. Enterprise-grade access control and gas management. 3★
- [x402-rs Facilitator](https://github.com/x402-rs/x402-rs#facilitator) — Production-grade Rust self-hosted facilitator. Docker deployment, multi-chain config, REST API (`/verify`, `/settle`).
- [@facilitator/eip7702](https://github.com/melonask/facilitator) — Supports all EVM blockchains (BNB, Polygon, etc.), all tokens (USDT, DAI, WBTC, etc.), and native coins (POL, AVAX, etc.).

---

## Multi-Chain Coverage

| Chain        | Status     | Facilitators                     | Settlement    |
|--------------|------------|----------------------------------|---------------|
| Base         | Production | Coinbase CDP, Cloudflare, Stripe | 2s instant    |
| Polygon      | Production | Coinbase CDP (gas sponsored)     | <1s           |
| Ethereum     | Production | Cloudflare, Primev               | Deferred      |
| Solana       | Production | Community                        | <1s           |
| Stellar      | Production | Stellar Foundation               | Instant       |
| BNB Chain    | Production | Pieverse                         | 2s instant    |
| TRON         | Production | MERX                             | <3s           |
| XRPL         | Production | t54.ai / Virtuals                | Instant       |
| Base Sepolia | Testnet    | Coinbase CDP                     | 2s instant    |
| 33+ chains   | Production | Ultravioleta DAO                 | Varies        |
