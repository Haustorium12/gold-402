<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
    <img src="assets/hero-light.svg" alt="gold-402 — a hand-checked directory of x402 services. Most of the x402 catalogue no longer answers; these are the ones that did. We check it, we date it, and we tell you what we found. By 24K Labs." width="680">
  </picture>
</p>

# gold-402

> The gold standard for x402 resources. **<!--COUNT:START-->564<!--COUNT:END--> curated entries** — paid endpoints probed for a live 402 before listing, libraries and repos checked for real activity, and the whole shelf re-knocked every night with the result dated. No filler.

[![GitHub stars](https://img.shields.io/github/stars/Haustorium12/gold-402?style=social)](https://github.com/Haustorium12/gold-402)
[![Last Commit](https://img.shields.io/github/last-commit/Haustorium12/gold-402)](https://github.com/Haustorium12/gold-402/commits/main)
[![Curated by 24K Labs](https://img.shields.io/badge/Curated_by-24K_Labs-gold)](https://24klabs.ai)

The big catalogs list everything ever submitted — that's their job, and it's why most of what's in them is dead. We measured it: **67–79% of the free-listing catalogs no longer answer.**

gold-402 is the other thing. Smaller on purpose. A person checked every entry, we publish what we checked and what we didn't, and in July 2026 we started **buying services and reporting what came back**. Automated monitors now do the machine half of that continuously and do it well; what they do not do — by their own published scope — is judge whether the thing that came back was any good. That judgement is what this list is.

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/directory-dark.svg">
  <img src="assets/sections/directory-light.svg" alt="Section: The Directory" width="680">
</picture>

## The Directory

The product. <!--COUNT:START-->564<!--COUNT:END--> entries across <!--SHELVES:START-->13<!--SHELVES:END--> shelves, in [`directory/`](directory/).

| Shelf | What's on it |
|---|---|
| [APIs & Services](directory/apis.md) | Paid endpoints an agent can call. Every one probed for a live 402 before listing. |
| [MCP Servers](directory/mcp-servers.md) | Model Context Protocol servers — utility, crypto, security, identity, escrow, discovery. |
| [SDKs & Libraries](directory/sdks.md) | Client and server libraries across languages. |
| [Facilitators](directory/facilitators.md) | Payment verification and settlement services. |
| [Frameworks](directory/frameworks.md) | Agent frameworks with x402 support. |
| [Tools](directory/tools.md) | CLIs, CI, monitoring, spend controls, testing, discovery. |
| [Security](directory/security.md) | Audit, risk scoring, pre-execution gates, compliance. |
| [Ecosystem](directory/ecosystem.md) | Protocol, infrastructure, wallets, orchestration, marketplaces. |
| [Aggregators & Proxies](directory/aggregators.md) | One integration, many upstreams — services that unify or resell access to other providers' APIs and data. |
| [**The Global Agent Economy**](directory/global.md) | **China, India, Korea — infrastructure no English-language directory indexes.** |
| [Learning](directory/learning.md) | Quickstarts, tutorials, reference docs, news. |
| [Community](directory/community.md) | Channels, newsletters, jobs, events. |
| [Market Data](directory/market-data.md) | On-chain analytics, dashboards, adoption. |

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/verified-dark.svg">
  <img src="assets/sections/verified-light.svg" alt="Section: What being on this list means" width="680">
</picture>

## What being on this list means

There is no stamp. There was one — "Gold402 Verified," one tier, a gold tick — and it was
retired on 2026-09-06 because it said the identical thing about a paid API we knocked last
Tuesday, a community wiki with no endpoint to knock at all, and an entry we hold no dated
receipt for. A mark that everything wears certifies nothing. We have made that criticism of
other people's badges and it was true of ours.

What every entry now carries instead is the finding, per entry:

- **A date** — *this endpoint answered an HTTP 402 when we knocked it, on this day.* An
  automated gate checks the submission, a maintainer confirms it before merge, and a sweep
  re-knocks and writes a dated result. A date is checkable. A tick is not.
- **Or "listed — no knock receipt"** — a human read it and it is on the list. We hold no
  dated knock, and we will not backfill a date we cannot show.
- **Or "listed — no endpoint to knock"** — libraries, guides, wallets, clients and
  community resources. Nothing here answers a 402 because that is not what these things
  do. We read them, and we checked they were publicly reachable.

**None of it is a delivery test.** We have not paid these services and graded what came
back. Read any of it as "we checked what is stated above," never as "this is worth the
money."

**Some entries carry more.** Where we have paid for a service and confirmed what came back,
we say so and keep the receipt — what we sent, what it cost, the transaction hash, what
arrived. That is a stronger claim and we only make it about services we actually bought.
Most of the list has not been through that, and we would rather say so than imply otherwise.

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/ecosystem-dark.svg">
  <img src="assets/sections/ecosystem-light.svg" alt="Section: Ecosystem Data" width="680">
</picture>

## Ecosystem Data

Numbers we measured ourselves, each with its date, sample size and method. Where measurements disagree, both are shown — they were taken on different days by different methods, and blending them into one tidy figure would be the kind of thing this directory exists to argue against.

### How much of the ecosystem is alive

| Measured | Population | Live | Dead | Method |
|---|---|---|---|---|
| 2026-07 | 22,545 CDP Bazaar services | 5,792 | **74%** | full probe crawl, valid 402 required |
| 2026-07-10 | 25,614 catalog services | 5,344 | **79%** | catalog snapshot, verify-state carried forward |
| 2026-07-29 | 24,583 catalog services | — | **~67%** | earlier full crawl, cited in the liveness study |

Three runs, three numbers, one direction: **the large free-listing catalogs are majority dead, and have been all month.** Anyone quoting a single decimal-point figure for this is quoting a moment, not a fact.

### Liveness is predicted by listing friction

Across four independent registries — 204,500 registered agents and services — the dead share tracks one variable: what it costs to get listed.

| Registry | Entry cost | Dead |
|---|---|---|
| CDP Bazaar | free | ~67–79% |
| ERC-8004 on-chain identity | gas only | 85–97% |
| Glama MCP registry | curation + scoring | 47% unhealthy _(their own published figure)_ |

**Free entry selects for abandonment.** Full method, limits, and an open invitation to refute it: [The Liveness Law →](articles/2026-07-the-liveness-law.md)

### Buying is harder than finding

In July 2026 we ran a paid delivery check across our own shelf — actually buying services and recording what came back.

- **16** of 126 listed services were purchasable by a machine at a discoverable address
- **8** delivered exactly what they advertised
- **0** took payment and returned nothing
- **$0.054** spent, every transaction reconciled on-chain

The friction in this economy sits **before** the payment, not after it. Most services are fine; most front doors are not. **We are not claiming that as a finding yet — the sample is 16 services and one day, 2026-07-30.** A wider census was designed the same week and has not run; the blocker is ours, not the ecosystem's. We would rather say that than let the sentence stand.

### Coverage beyond the West

x402 is a US-governed rail. It is not the only answer to machine payment, and outside the West it is not the answer being used — China runs delegated agent authorization on existing rails, India runs regulated human-signed mandates that agents execute inside a cap. Both were operating at scale before the x402 Foundation was a month old.

We index that world too, including surfaces no English-language directory carries: [The Global Agent Economy →](directory/global.md)

_All figures above are ours and reproducible. Where we could not reach something, we say so rather than leaving the gap invisible._

---

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/featured-dark.svg">
  <img src="assets/sections/featured-light.svg" alt="Section: Featured This Month" width="680">
</picture>

## Featured This Month

[![24K Featured](https://img.shields.io/badge/24K_Featured-2026--09-C0C0C0?style=plastic)](FEATURED.md)

**September 2026 — one pick per shelf.** Each shelf opens with its pick and the write-up. Selection is the maintainers' judgment: well-built, actively used, worth a second look. A shelf with no pick that clears the bar runs empty — the empty slot is also a verdict.

| Shelf | September pick |
|---|---|
| APIs & Services | [Forge Attestation](https://forgesignals.org/.well-known/forge-attestation) |
| MCP Servers | [Council of AI GSPC MCP](https://councilof.ai/mcp) |
| SDKs & Libraries | [x402-rs](https://github.com/x402-rs/x402-rs) |
| Facilitators | [NEAR x402 Facilitator](https://x402.mikedotexe.com/) |
| Frameworks | [@moltrust/x402](https://www.npmjs.com/package/@moltrust/x402) |
| Tools | [nohumans.directory](https://nohumans.directory) |
| Security | [MIDAX402](https://midax402.com/.well-known/x402.json) |
| Ecosystem | [Skyfire](https://docs.skyfire.xyz) |
| The Global Agent Economy | [Alipay Open Platform](https://open.alipay.com) |
| Learning | [The Agent Times](https://theagenttimes.com) |
| Community | [Human Pages](https://humanpages.ai) |
| Market Data | [MCP Scores](https://mcpscores.com) |
| Aggregators & Proxies | [402Signal](https://402signal.com/route) |

[Past features →](FEATURED.md)

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/wire-dark.svg">
  <img src="assets/sections/wire-light.svg" alt="Section: This Week in x402" width="680">
</picture>

## This Week in x402

The wire lives at **[24klabs.ai/news](https://24klabs.ai/news)** — dated editions with permanent links, every claim cited. Four editions so far; the most recent is [2026-08-10](https://24klabs.ai/news/2026-08-10/). It is not on a schedule.

---

<!-- NEW-THIS-WEEK:START -->
## New This Week

**This week** (Sep 21—27)

- **[eu-validate](https://88-198-100-115.sslip.io/v1/validate)** — Validates IBAN (mod-97 offline), EU VAT number (VIES), and company domain (DNS/MX) in one x402 call. $0.01 USDC on Base mainnet. Built by Forge, an AI-owned company. Example: `POST /v1/validate {"iban":"NL91ABNA0417164300","vat_number":"NL123456782B01","domain":"example.com"}`. ([GitHub](https://github.com/forgeaicompany/eu-validate-examples))
- **[Solana Wallet Research](https://solana-wallet-research.empty-thistle.workers.dev/.well-known/x402)** — Returns bounded finalized public-data reports for Solana wallet addresses for $0.01 USDC per call on Solana mainnet via x402.
- **[HydraTrader x402 Catalog](https://x402.hydratrader.ai/.well-known/x402)** — Three pay-per-call Base USDC helpers via x402 (no API key): `POST /v1/cheap-errand` ($0.01) summarize/rewrite/classify/keywords/sentiment/translate; `POST /v1/structured-extract` ($0.03) schema-bound extract from pasted text or public URLs; `POST /v1/research-brief` ($0.08) short public-web briefs with citations (fair-use snippets only). ([SKILL](https://x402.hydratrader.ai/SKILL.md) | [OpenAPI](https://x402.hydratrader.ai/openapi.json) | [llms.txt](https://x402.hydratrader.ai/llms.txt))
- **[Agent Bazaar](https://bazaar.saylorinnovations.com)** — Open, permissionless x402 discovery marketplace mirroring Coinbase's CDP Bazaar catalog (15,000+ resources) plus independently-submitted listings, with an MCP server and A2A agent registry, no account required to list or read.
- **[openai-agents-nano](https://github.com/PANDeveloper001/openai-agents-nano-x402)** — Nano (XNO) x402 client for the OpenAI Agents SDK. Free, feeless pay-per-call for agent frameworks.
- **[SignalHarness.ai](https://signalharness.ai/.well-known/x402)** — Publishes 330 production x402 API services for AI agents covering web and data processing, validation, AI utilities, and blockchain and crypto utilities.
- **[100pro Token Contract Risk Screen](https://x402.rendraputra.dev/.well-known/x402)** — Pre-trade risk screen for EVM (Base) and Solana token contracts: honeypot, clone/mimic and owner-privilege signals returned with the evidence behind each flag, $0.05 USDC per call on Base. The report is served only after the USDC settlement is verified on Base, so a caller is never charged for a screening that did not settle. Example: `GET /screen?token=0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913&chain=base`. ([OpenAPI](https://x402.rendraputra.dev/openapi.json), [llms.txt](https://x402.rendraputra.dev/llms.txt))
- **[Agent Embassy](https://agent-embassy.fly.dev/v1/check/verify)** — Agents pay per call in USDC via x402 for verified web checks with signed Outcome Receipts, encrypted recovery registration, and GPU market data.
- **[Brian Booms x402 Store](https://pay.brianbooms.com/api/v1/buy/wallpaper-pack-vol1)** — 33 digital products (music licenses, podcast packs, sample packs, custom commissions, wallpapers) sold via x402 micropayments in USDC on Base, Polygon, Arbitrum, Avalanche, and Solana, priced $0.05–$999 with instant download delivery. ([Catalog](https://brianbooms.com/.well-known/purchase-catalog.json))

**Last week** (Sep 14—20)

- **[url2md](https://url2md.io/v1/md?url=https%3A%2F%2Fexample.com)** — PDFs and x402-tolled pages, returned as clean Markdown. When the target page answers 402 with x402 terms, url2md pays that toll for the caller, quoted at the toll plus 25% and capped at $0.05. JavaScript-rendered pages and ordinary HTML go through the same conversion engine. Follows robots.txt per RFC 9309. $0.005 USDC on Base via the Coinbase CDP facilitator. Example: `GET /v1/md?url=https://example.com` or `POST /v1/md {"url":"https://example.com"}`. The origin is paid only after the caller's own payment has settled. ([OpenAPI](https://url2md.io/openapi.json)) ([MCP server](https://www.npmjs.com/package/@url2md-io/mcp)) ([llms.txt](https://url2md.io/llms.txt))
- **[x402 Crypto Research API](https://x402-crypto-research-api-production.up.railway.app/research)** — Generates current, source-linked cryptocurrency ecosystem research reports for 0.01 USDC per POST request on Base mainnet. Example: `{"topic":"Give a concise current status update on the Base ecosystem."}`. ([GitHub](https://github.com/stgzwpzy8w-eng/x402-crypto-research-api))
- **[402cron](https://402cron.com/buy/trial)** — Schedules signed HTTP deliveries to a registered endpoint on a cron schedule, paid per delivery in USDC on Base via x402, no account or card required.
- **[gravee](https://x402.getgravee.com)** — 23 pay-per-call business lead generation and market intelligence endpoints: scored leads by vertical and location, business scoring, contact extraction, competitor analysis, multi-source verification, digital health audits, WHOIS, social presence, tech stack detection, formation data, hiring signals, review aggregation, market saturation, gap analysis, growth trajectory, website status, email and phone verification, competitive pricing. $0.005–$0.75 USDC per call on Base and Solana. No API keys — wallet is auth. ([Manifest](https://x402.getgravee.com/.well-known/x402.json)) ([llms.txt](https://x402.getgravee.com/llms.txt))
- **[AgentPay Summarize](https://agentpay.help/v1/summarize)** — Summarizes up to 20,000 characters of text into a 250-word summary returned as JSON. `POST` only, $0.01 USDC on Base mainnet. Example: `POST /v1/summarize {"text":"..."}`. ([Manifest](https://agentpay.help/.well-known/x402)) ([MCP](https://agentpay.help/mcp)) ([OpenAPI](https://agentpay.help/openapi.json))
- **[AgentPay Token Safety](https://agentpay.help/v1/token-safety)** — Reports rug-pull and honeypot risk signals and liquidity for a token contract address. `POST` only, $0.02 USDC on Base mainnet. Example: `POST /v1/token-safety {"address":"0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"}`. ([Manifest](https://agentpay.help/.well-known/x402)) ([MCP](https://agentpay.help/mcp)) ([OpenAPI](https://agentpay.help/openapi.json))
- **[AgentPay Insurance Lead Analysis](https://agentpay.help/v1/insurance-analysis)** — Classifies an inbound insurance lead, extracts structured fields from it, and returns a lead summary in one call. `POST` only, $0.10 USDC on Base mainnet. Example: `POST /v1/insurance-analysis {"text":"..."}`. ([Manifest](https://agentpay.help/.well-known/x402)) ([MCP](https://agentpay.help/mcp)) ([OpenAPI](https://agentpay.help/openapi.json))
- **[Basalt](https://basalt-n6lt.onrender.com/.well-known/x402.json)** — 20 pay-per-call utility tools for AI agents: URL metadata extraction, domain availability via RDAP, email/MX validation, HTML-to-Markdown and Markdown-to-HTML, QR code generation, PDF text extraction, TLS certificate checks, language detection (186 languages), JSON Schema validation, EIP-191/EIP-712 signature recovery, IBAN/BIC/card-number checksums, geo distance, time-zone conversion, LLM token counting, hashing and HMAC, JWT decoding, URL parsing and canonicalization, EVM address checksum, and IP classification with CIDR checks. $0.002-$0.01 USDC on Base. Example: `POST /domain-check {"domain":"example.com"}`. ([OpenAPI](https://basalt-n6lt.onrender.com/openapi.json))
- **[D-007 Document Classify and Rename Plan](https://friction-product-commerce-production.id4-score.workers.dev/v1/x402/document-classify-rename-plan)** — Generates a dry-run classification, traversal-safe filename, folder proposal, and duplicate signals for one supplied document record. $0.01 USDC on Base mainnet via x402. Example: POST /v1/x402/document-classify-rename-plan {"originalFilename":"invoice-2026-09.txt","extension":".txt","size":1024,"textExcerpt":"Invoice for order","metadata":{}}.
- **[DreamWidget](https://dreamwidget.com/.well-known/x402)** — Website widgets (logo showcases, a YouTube/Vimeo/Twitch/TikTok video wall) for an agent's client: POST /api/v1/plan answers 402 for a plan term in USDC on Base, USDC on Solana, XRP, or HBAR and USDC on Hedera; the paid retry grants the plan and returns the account and API key. OpenAPI at /openapi.json.
- **[4yearcycle data catalog](https://4yearcycle.com/.well-known/x402)** — Twelve pay-per-call data endpoints for agents covering EU tenders (TED) and grants (CORDIS), crypto derivatives, DeFi yields, ERC-20 token safety, gas, ECB FX rates, German weather (DWD), live flights, news headlines, Bitcoin on-chain state and web search, $0.005–$0.02 USDC on Base mainnet via the Coinbase CDP facilitator with no API key or account. Example: `GET https://4yearcycle.com/x402/fx-rates?base=USD&symbols=EUR,GBP,JPY`. ([OpenAPI](https://4yearcycle.com/openapi.json)) ([Manifest](https://4yearcycle.com/.well-known/x402)) ([Site](https://4yearcycle.com/x402/))
- **[X402 Git](https://x402git.com)** — Sells paid access to private git repositories (agent skills, harnesses, libraries) over x402 v2, USDC on Base, settled through the CDP facilitator; the manifest (file tree, languages, licence, security scan, release log) is public before payment and the code is private until settlement, every listing is its own 402 endpoint declaring the `bazaar` extension, and creators publish headlessly through an API with a buy-side MCP server for agents. ([Discovery](https://x402git.com/.well-known/x402), [OpenAPI](https://x402git.com/openapi.json))
- **[MadeOnSol](https://madeonsol.com/.well-known/x402)** — Solana KOL trade feeds, deployer reputation, token risk/buyer-quality scoring, and wallet PnL for AI agents, $0.005-$0.02 USDC on Solana with self-verified settlement (no facilitator); manifest lists all 25 endpoints. Example: `GET /api/x402/token/{mint}`.
<!-- NEW-THIS-WEEK:END -->

---

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/quickstart-dark.svg">
  <img src="assets/sections/quickstart-light.svg" alt="Section: Quick Start" width="680">
</picture>

## Quick Start

> **New to x402?** Three steps to your first payment.

**1. Pick a facilitator**

| Use case | Facilitator |
|----------|-------------|
| Most chains, full SDK support | [Coinbase CDP](https://docs.cdp.coinbase.com/x402) |
| Edge deployment, global latency | [Cloudflare x402](https://developers.cloudflare.com/agents/tools/payments/x402/) |
| Enterprise billing + disputes | [Stripe Machine Payments](https://docs.stripe.com/payments/machine/x402) |

**2. Install the SDK**

```bash
# TypeScript
npm install x402-express        # or the core package: @coinbase/x402

# Python
pip install x402
```

```bash
# Rust
cargo add x402-axum x402-reqwest   # x402-rs — see SDKs & Libraries shelf
```

_Checked 2026-09-20. A crate literally named `x402` exists on crates.io but is a placeholder
with no working code — use `x402-rs`'s crates (`x402-axum` for servers, `x402-reqwest` for
clients) instead._

**3. Add payment middleware**

```typescript
import { paymentMiddleware } from '@coinbase/x402-express';

app.use(paymentMiddleware(wallet, {
  '/api/data': { price: '$0.01', network: 'base-mainnet' }
}));
```

That's it. The middleware returns 402 with payment details, verifies the client's payment header, and lets the request through.

[Full quickstart →](https://docs.cdp.coinbase.com/x402/quickstart-for-sellers) · [Testnet setup →](https://docs.cdp.coinbase.com/x402/network-support)

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/howitworks-dark.svg">
  <img src="assets/sections/howitworks-light.svg" alt="Section: How x402 Works" width="680">
</picture>

## How x402 Works

```
1. Client  →  GET /api/data                              (initial request)
2. Server  ←  402 Payment Required                       (payment details in header)
               payment-required: <base64 challenge>       (v2; v1 used X-Payment-Required
                                                           and put the detail in the body)
3. Client  →  EIP-3009 gasless USDC transfer             (client signs + submits)
4. Client  →  GET /api/data  +  X-Payment: {signed tx}  (retry with payment)
5. Facilitator  →  verify + settle on-chain              (~2 seconds)
6. Server  ←  200 OK  +  X-Payment-Response              (resource returned)
```

No gas for the sender. No subscription. No API key. Payment IS authentication.

[Protocol spec →](https://github.com/coinbase/x402) · [EIP-3009 →](https://eips.ethereum.org/EIPS/eip-3009)

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/needmore-dark.svg">
  <img src="assets/sections/needmore-light.svg" alt="Section: Need More?" width="680">
</picture>

## Need More?

This README is the front door. The full curated directory — every shelf, every entry — is in [`directory/`](directory/).

**Other lists worth knowing:** the community [awesome-x402](https://github.com/xpaysh/awesome-x402) accepts everything and is the right place for exhaustive coverage. [Glama](https://glama.ai/mcp/servers) indexes MCP servers at enormous scale and publishes its own health data, which is rarer than it should be. Different jobs. Use all three.

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sections/contributing-dark.svg">
  <img src="assets/sections/contributing-light.svg" alt="Section: Contributing" width="680">
</picture>

## Contributing

gold-402 is curated, not exhaustive. Every entry earns its place.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the curation standard, badge system, acceptance criteria, and submission process.

**Quick rules:**
- Entry must use the x402 protocol (HTTP 402 + X-Payment), not just USDC or general crypto payments.
- Live URL or public GitHub repo. Link must work.
- Last activity within 12 months (for libraries and resources without a live endpoint).
- One entry per pull request. Format: `[Name](url) — Description starting uppercase, ending with period.`
- Descriptions are factual. No marketing language.

---

<p align="center">
  <b>Curated by <a href="https://24klabs.ai">24K Labs</a></b><br>
  <sub>If this saved you time, star the repo.</sub><br><br>
  <a href="https://24klabs.ai">24klabs.ai</a> •
  <a href="https://x402.org">x402.org</a> •
  <a href="https://github.com/coinbase/x402">Protocol Spec</a> •
  <a href="https://docs.cdp.coinbase.com/x402">Coinbase Docs</a> •
  <a href="https://discord.gg/x402">Discord</a> •
  <a href="https://agenteconomy.to">Live Dashboard</a>
</p>
