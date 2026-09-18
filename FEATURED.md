# Past Featured Picks

gold-402 features one pick per shelf each month (one pick per shelf since August 2026; a single monthly pick before that). The [Featured This Month](README.md#featured-this-month) section in the main README rotates on the 1st of every month. Past picks are archived here with their original write-up.

Selection criteria are documented in [CONTRIBUTING.md](CONTRIBUTING.md#24k-featured-tier).

---

## September 2026 — The Slate

One pick per shelf.

**APIs & Services — [Forge Attestation](https://forgesignals.org/.well-known/forge-attestation)**
Signed third-party evidence for x402 transactions that labels every claim `witnessed` or `asserted` — the same distinction this shelf makes about its own entries, applied as a product. Nothing here claims correctness, only what was actually observed.

**MCP Servers — [Council of AI GSPC MCP](https://councilof.ai/mcp)**
Calls itself a measurement MCP, not a certification — the same line gold-402 drew when it retired its own verified badge. Free board tools, paid evidence tools over x402.

**SDKs & Libraries — [x402-rs](https://github.com/x402-rs/x402-rs)**
The real Rust implementation — Axum middleware, reqwest client wrapper, self-hostable facilitator, 41 published versions. Worth naming directly this month: a thin placeholder crate named `x402` also exists on crates.io and ships no working code.

**Facilitators — [NEAR x402 Facilitator](https://x402.mikedotexe.com/)**
Open source and API-key-gated, and unusual for publishing its own sanitized paid-flow evidence for both NEAR and Base mainnet rather than asking you to take settlement on faith.

**Frameworks — [@moltrust/x402](https://www.npmjs.com/package/@moltrust/x402)**
One line of middleware — `app.use(requireScore({ minScore: 60 }))` — reads a wallet's trust score off the X-Payment header and blocks anything below the bar before your endpoint ever runs. Zero dependencies.

**Tools — [nohumans.directory](https://nohumans.directory)**
Runs the same experiment gold-402 ran in July, at roughly four times the sample size: 550 endpoints actually purchased with real USDC, 332 delivered, full outcome breakdown and the SQL behind it published. This is the kind of check we'd rather see more of, not less.

**Security — [MIDAX402](https://midax402.com/.well-known/x402.json)**
Signed EIP-712 conformance verdicts on a public registry, with a paid board-position ladder kept in a separate column from the verdict itself — no payment changes a rating or its verification-date ordering. The pay-to-rank problem, solved by not letting the two touch.

**Ecosystem — [Skyfire](https://docs.skyfire.xyz)**
Agent identity and payment credentials as ES256 JWTs with a public JWKS endpoint — the rare pattern in this space a stranger can verify without contacting the issuer. Worth studying if you're designing receipts of your own.

**Aggregators & Proxies — [402Signal](https://402signal.com/route)**
A router that fails closed: it authorizes payment only once it has found a live, eligible endpoint, so a typed miss costs nothing. This shelf ran empty in August; this is its first pick.

**The Global Agent Economy — [Alipay Open Platform](https://open.alipay.com)**
Read in full this month after being JavaScript-walled on the first pass in July — including AI收, Ant Group's own HTTP-402-shaped rail for agents, running on a one-time bounded human authorization at what is reportedly national scale.

**Learning — [The Agent Times](https://theagenttimes.com)**
Independent news for the agent economy, published with citations and confidence scores and queryable by agents directly — built for the moment before an agent installs something, not for humans reading after the fact.

**Community — [Human Pages](https://humanpages.ai)**
An open directory that runs the marketplace in the other direction — agents hire humans for real-world tasks, paid per use on Base. Also just a normal job board if you're a person looking for gig work.

**Market Data — [MCP Scores](https://mcpscores.com)**
A money-flow observatory over 36,000+ MCP/x402 listings that publishes its own wash-risk flags and methodology instead of one clean number with no seams. The register itself is free.

---

## August 2026 — The Slate

One pick per shelf. Aggregators & Proxies ran empty.

**APIs & Services — [The Bot Wire](https://thebotwire.com)**
Fifty-seven primary-source data wires — SEC EDGAR, Federal Register, federal courts, Fed and ECB, CISA, arXiv — behind one x402 gate at $0.005–$0.01 a call, with a free three-result preview on every wire. Agents get the source document, not a scrape of someone's summary of it. Manifest, OpenAPI, and a routing table published side by side.

**MCP Servers — [Razorpay MCP Server](https://github.com/razorpay/razorpay-mcp-server)**
One of India's largest payment processors, shipping an official MCP server and doing the unglamorous part right: its AGENTS.md sets explicit conventions for agent-authored tools, including a money-unit safety rule. Worth reading even if you never route a payment through it.

**SDKs & Libraries — [ra2a](https://github.com/qntx/ra2a)**
A Rust SDK for the Agent2Agent protocol with x402 integration built in — the two halves of agent commerce, discovery and payment, in one typed crate.

**Facilitators — [Primev FastRPC](https://facilitator.primev.xyz)**
A fee-free facilitator on Ethereum mainnet with sub-200ms settlement, done with mev-commit preconfirmations rather than a sidechain. Most facilitators route around mainnet latency; this one engineers through it.

**Frameworks — [machi](https://github.com/qntx/machi)**
Agent behavior that compiles — an execution framework with x402 payment primitives baked in rather than bolted on. Payment as a language feature, not an afterthought.

**Tools — [portal-tunnel](https://github.com/gosuda/portal-tunnel)**
Publishes localhost services to the agentic web through self-hostable, trustless tunnels with x402 gating on the way in. The missing on-ramp for anyone whose service runs on a machine at home.

**Security — [Hermes Plant Action Safety](https://hermesplant.com/api/agent-services/action-safety/quick)**
A deterministic pre-execution gate for agent shell, Git, SQL, and deployment actions: $0.01 for a quick verdict, $0.25 for a signed-receipt workflow. One of the few paid x402 services with repeat buyers visible on-chain.

**Ecosystem — [Glama](https://glama.ai/mcp/servers)**
An MCP registry indexing 64,000+ servers — and the only one publishing both its scoring rubric and its health data. In a space full of unexplained ranks, you can see what it checked and how it decided.

**The Global Agent Economy — [ONDC](https://ondc.org)**
India's government-backed open commerce network: an operating, population-scale version of what open agent commerce is trying to become, built on a different foundation. If you study one non-Western rail, study this one.

**Learning — [Tangle Network: x402 Production Runway](https://dev.to/tangle_network/series/37294)**
A multi-part engineering series that takes x402 seriously as production software: the Rust implementation, the facilitator trust problem, what decentralized verification would actually require. Written by people running the code, not summarizing it.

**Community — [WorkProtocol](https://workprotocol.ai)**
An open job marketplace where AI agents take structured work, deliver artifacts, and get paid in USDC on Base — escrow-backed, with portable reputation. The rare community surface where participation is a transaction, not a post.

**Market Data — [Valoria](https://x402.valoria.net)**
Revenue rankings, service analysis, and pricing data across 90,000+ indexed services and $148M+ in tracked on-chain volume — their published figures. Most dashboards count transactions; this one tries to answer what anything earns.

---

## July 2026 — 24K Labs Verification Report

> [**Three-Quarters of the x402 Bazaar Is Dead**](articles/2026-07-verification-findings.md) by [24K Labs](https://24klabs.ai)

[![24K Featured](https://img.shields.io/badge/24K_Featured-2026--07-C0C0C0?style=plastic)](CONTRIBUTING.md#24k-featured-tier)

The first Featured pick that is our own work, chosen because it states the thesis better than anything external could. We probed all 22,545 x402 services listed in the CDP Bazaar. 5,792 returned a valid 402 Payment Required response; the other 16,753 were gone, misconfigured, or unreachable — a 74% dead rate.

Verification is the product; presence is the verdict. A raw listing reflects everything ever submitted and can't tell a live endpoint from a dead one. This report can, with a reproducible method.

[**→ Read the full report**](articles/2026-07-verification-findings.md)

---

## June 2026 — Fireblocks Agentic Payments Suite

> [**Fireblocks Agentic Payments Suite**](https://www.fireblocks.com/products/agentic-payments) by [Fireblocks](https://www.fireblocks.com)

[![24K Featured](https://img.shields.io/badge/24K_Featured-2026--06-C0C0C0?style=plastic)](CONTRIBUTING.md#24k-featured-tier)

Fireblocks launched its Agentic Payments Suite on May 20, 2026 and joined the x402 Foundation. The platform — which has secured $14T+ in digital asset transactions — delivered the enterprise controls layer the protocol had been missing: MPC agentic wallets with delegation rules, a merchant Gateway for stablecoin payment acceptance, and a formal security extension to the x402 spec adding request integrity and spend governance. Built-in KYT, Travel Rule compliance, and structured audit trails make regulated enterprise deployments viable for the first time.

[**→ Read the full write-up**](articles/2026-06-fireblocks-agentic-payments.md)

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
