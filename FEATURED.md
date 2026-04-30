# Past Featured Picks

gold-402 spotlights one service, SDK, or tool each month. The [Featured This Month](README.md#featured-this-month) section in the main README rotates on the 1st of every month. Past picks are archived here with their original write-up.

Selection criteria are documented in [CONTRIBUTING.md](CONTRIBUTING.md#24k-featured-tier).

---

## May 2026 — The x402 Foundation

> [**x402 Foundation**](https://www.x402.org) under the [Linux Foundation](https://www.linuxfoundation.org/x402foundation)

[![24K Featured](https://img.shields.io/badge/24K_Featured-2026--05-C0C0C0?style=plastic)](CONTRIBUTING.md#24k-featured-tier)

On April 2, 2026, Coinbase contributed the x402 protocol to the Linux Foundation and launched the x402 Foundation with 22 founding members: Adyen, AWS, American Express, Circle, Cloudflare, Coinbase, Fiserv, Google, KakaoPay, Mastercard, Microsoft, Polygon Labs, Shopify, Solana Foundation, Stripe, Thirdweb, Visa, and others.

The protocol moved from `coinbase/x402` to `x402-foundation/x402`. A Technical Charter was published. Vendor-neutral governance went live.

This is the governance story April's "What's New" bullet didn't have room for. The x402 Foundation is the moment the protocol stopped being a company's product and became an open standard — the event that, historically, precedes ecosystem-wide adoption by years.

[**→ Read the full write-up**](articles/2026-05-x402-foundation.md)

---

## April 2026 — Stripe x402 Machine Payments

> [**Stripe x402 Machine Payments**](https://docs.stripe.com/payments/machine/x402) by [Stripe](https://stripe.com)

[![24K Featured](https://img.shields.io/badge/24K_Featured-2026--04-C0C0C0?style=plastic)](CONTRIBUTING.md#24k-featured-tier) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier)

The biggest open question about x402 has always been whether payment processors — not just crypto-native companies — would actually show up. Stripe answered it.

Machine Payments launched in March 2026 on Base with USDC. The name signals the intent clearly: this is not a payment flow designed for humans. No checkout pages, no redirect UX, no session tokens. An AI agent hits a 402, pays the EIP-3009 signed transfer, retries — and gets the resource. The whole exchange fits inside HTTP headers.

What makes this genuinely significant is what Stripe brings to the table: dispute resolution, fraud detection, compliance tooling, and dashboard visibility over every agent transaction. The x402 protocol handles the payment primitive; Stripe handles the enterprise layer around it. That combination — crypto-native speed with enterprise-grade infrastructure — is the stack that actually gets deployed in production at scale.

Stripe joining the x402 Foundation as a founding member on April 2, 2026 was the announcement. Machine Payments is the product. It's the clearest signal yet that x402 has cleared the enterprise credibility bar.

For builders: if your customers operate in regulated environments or need chargebacks and dispute workflows alongside autonomous agent payments, this is the path.

**Chains:** Base (USDC) | **Docs:** [docs.stripe.com/payments/machine/x402](https://docs.stripe.com/payments/machine/x402)
