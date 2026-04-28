# Facilitators

Payment verification and settlement services for x402. A facilitator verifies payment signatures and settles USDC on-chain so your server doesn't have to run blockchain infrastructure.

> **gold-402 note:** For most builders, start with Coinbase CDP. For European deployments, AsterPay is the only MiCA-compliant option. For edge/global scale, Cloudflare.

---

## Hosted Facilitators

- [Coinbase CDP](https://docs.cdp.coinbase.com/x402) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Official facilitator on Base and Base Sepolia. Instant settlement, supports all ERC-20 tokens (not just USDC). Most widely used in the ecosystem.
- [Stripe x402](https://docs.stripe.com/payments/machine/x402) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) [![24K Featured](https://img.shields.io/badge/24K_Featured-2026--04-C0C0C0?style=plastic)](../FEATURED.md) — Stripe's Machine Payments infrastructure. Deposit addresses, automatic PaymentIntent capture on settlement, dashboard monitoring, webhooks. USDC on Base. ([Quickstart](https://docs.stripe.com/payments/machine/x402/quickstart))
- [Cloudflare x402](https://blog.cloudflare.com/x402/) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Edge computing facilitator on Base and Ethereum. Deferred settlement. Global distribution via 300+ data centers.
- [Polygon x402 Facilitator](https://www.coinbase.com/developer-platform/discover/launches/x402facilitator-polygon) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Coinbase CDP on Polygon with gas sponsorship, automated KYT compliance screening, 1,000 free transactions/month. USDC on Polygon. ([Polygon Docs](https://docs.polygon.technology/pos/payments/x402/quickstart-sellers/))
- [Stellar x402](https://stellar.org/blog/foundation-news/x402-on-stellar) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) — Official Stellar Foundation integration. Middleware for Stellar payment addresses, browser wallet support. ([Docs](https://developers.stellar.org/docs/build/agentic-payments/x402))
- [AsterPay](https://asterpay.io) [![MiCA](https://img.shields.io/badge/MiCA-compliant-blue?style=flat-square)](https://asterpay.io) [![ERC-8004](https://img.shields.io/badge/ERC--8004-registered-orange?style=flat-square)](https://asterpay.io) — European x402 facilitator with EUR off-ramp via SEPA Instant. First European-focused x402 infrastructure. ElizaOS plugin available.
- [Primev FastRPC](https://facilitator.primev.xyz) [![ERC-8004](https://img.shields.io/badge/ERC--8004-Agent_%2323175-orange?style=flat-square)](https://facilitator.primev.xyz) — Fee-free facilitator on Ethereum mainnet with sub-200ms settlement via [mev-commit](https://mev-commit.xyz) preconfirmations.
- [Bankr x402 Cloud](https://chainwire.org/2026/04/02/bankr-launches-x402-cloud-on-4-02-day-as-x402-protocol-joins-the-linux-foundation/) — Hosted platform for deploying USDC-monetized pay-per-request APIs. Includes hosting, payment processing, and agent discovery indexing. Freemium (5% revenue cut). Built on Base. Launched April 2, 2026.
- [BNB Chain Pieverse](https://twitter.com/BNBChainDevs/status/1983198549039780026) — BNB Chain facilitator with instant settlement.
- [MERX x402 for TRON](https://x402.merx.exchange) — First TRON facilitator. USDT, USDC, USDD on TRON mainnet. Sub-3-second confirmation. [Express middleware](https://npmjs.com/package/merx-x402).
- [XRPL / 54.ai Facilitator](https://www.bitget.com/news/detail/12560605308861) — x402 facilitator for XRP Ledger by Virtuals Protocol / 54.ai. Autonomous XRPL agent transactions with identity and compliance verification.
- [x402 Sponsor Relay](https://github.com/aibtcdev/x402-sponsor-relay) — x402 sponsor relay for AI on Bitcoin (aibtcdev). Agents access gated endpoints without managing their own wallets — relay sponsors on their behalf. ([aibtc.dev](https://aibtc.dev))
- [Satoshi Facilitator](https://bitcoinsapi.com/docs) — Independent facilitator for Bitcoin-focused pay-per-call services. Base, Base Sepolia, Solana Mainnet, Solana Devnet. [Supported networks](https://facilitator.bitcoinsapi.com/supported)

---

## Self-Hosted Facilitators

- [x402-rs Facilitator](https://github.com/x402-rs/x402-rs#facilitator) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/x402-rs/x402-rs) — Production-grade Rust self-hosted facilitator. Docker deployment, multi-chain config, REST API (`/verify`, `/settle`).
- [@facilitator/eip7702](https://github.com/melonask/facilitator) [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](https://github.com/melonask/facilitator) — Supports all EVM blockchains (BNB, Polygon, etc.), all tokens (USDT, DAI, WBTC, etc.), and native coins (POL, AVAX, etc.).

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
| XRPL         | Production | 54.ai / Virtuals                 | Instant       |
| Base Sepolia | Testnet    | Coinbase CDP                     | 2s instant    |
