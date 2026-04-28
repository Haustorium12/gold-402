# Contributing to gold-402

gold-402 is curated, not exhaustive. Every entry earns its place.

## What We List

Five categories are in scope:

1. **Facilitators** — hosted or self-hosted x402 payment facilitators processing real USDC (or supported stablecoin) transactions.
2. **SDKs & Frameworks** — code libraries and middleware for implementing x402 as a server or client.
3. **APIs & MCP Servers** — x402-payable endpoints and Model Context Protocol servers that accept payment via the x402 protocol.
4. **Tools & Infrastructure** — monitoring, analytics, spending controls, CLI utilities, and CI/CD integrations for x402 builders.
5. **Learning & Community** — documentation, tutorials, news, events, and channels directly useful to x402 builders.

**Out of scope:** general crypto wallets, general USDC infrastructure, and AI agent platforms that do not have a specific x402 integration.

---

## Entry Format

```
[Name](url) [![badge](badge-url)](link) — One sentence description starting uppercase, ending with period.
```

- Em dash separator (` — `) between name/badges and description.
- Description is factual. No "powerful", "amazing", "best", or "revolutionary".
- URL: direct link to service, GitHub repo, or docs page.
- No trailing whitespace.

---

## Acceptance Criteria

ALL must be true:

- Publicly accessible — live URL or public GitHub repo.
- x402-specific — actually uses the x402 protocol (HTTP 402 + X-Payment header), not just USDC or general crypto payments.
- Active — last commit or service activity within 12 months, OR carries a `24K Verified` tag (see below).
- Not a duplicate of an existing entry without meaningful differentiation.
- Description is one line, factual, no marketing language.
- Link is live and resolves correctly.

---

## Rejection Criteria

ANY fails the submission:

- Not actually x402 — mentions USDC or on-chain payments but does not implement the x402 protocol.
- Dead, private, or "coming soon" with no production deployment.
- Archived, deprecated, or last activity older than 12 months without qualifying for `24K Verified`.
- Duplicates an existing entry with no meaningful difference.
- Description uses marketing language.
- Broken or redirected link.

---

## 24K Verified Tier

[![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](CONTRIBUTING.md#24k-verified-tier)

A `24K Verified · YYYY-MM` tag means: as of the date shown, the maintainers confirmed this entry is **live in production, processing real transactions**. To carry the tag, an entry must satisfy ALL of the following at the time of verification:

1. Has a live production endpoint serving real x402 requests (not just demo or testnet).
2. Has processed real USDC (or supported stablecoin) transactions on at least one mainnet chain.
3. Not deprecated, archived, or in "coming soon" / alpha-only state.
4. Responsive to requests — returns correct 402 headers and accepts valid payment headers.

The tag is re-verified quarterly. If any criterion fails on re-check, the tag is removed or the entry is retired.

Verified entries appear in their natural categories alongside unverified entries — the tag is about transparency, not segregation.

---

## 24K Featured Tier

[![24K Featured](https://img.shields.io/badge/24K_Featured-2026--04-C0C0C0?style=plastic)](FEATURED.md)

A `24K Featured · YYYY-MM` tag means the entry was selected as the monthly editorial pick and spotlighted in the README's Featured This Month section. Featured picks are archived in [FEATURED.md](FEATURED.md).

Selection criteria, in roughly this order:

1. **Quality of execution** — the implementation is clean, the docs are real, and the service does what it claims.
2. **Active deployment** — real traffic, real transactions, evidence of actual use in the ecosystem.
3. **Distinct value** — solves a real problem or fills a gap not well-served before.
4. **Underexposure** — preference for excellent work that has not yet hit mainstream coverage.

When a Featured pick also appears in a curated category table, its row gets a silver `24K Featured · YYYY-MM` badge to mark the editorial history. The badges form a three-metal hierarchy: gold for `24K Verified`, silver for `24K Featured`, bronze for informational tags.

---

## Informational Tags

These tags carry no quality judgment — they communicate protocol or compliance facts that are useful to builders selecting services.

| Tag | Color | Meaning |
|-----|-------|---------|
| [![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)](url) | Green | Source code is publicly available. |
| [![Multi-Chain](https://img.shields.io/badge/Multi--Chain-2+-blue?style=flat-square)](url) | Blue | Supports 2 or more chains. |
| [![ERC-8004](https://img.shields.io/badge/ERC--8004-registered-orange?style=flat-square)](url) | Orange | Registered or integrated with the ERC-8004 on-chain agent registry. |
| [![MiCA](https://img.shields.io/badge/MiCA-aware-blue?style=flat-square)](url) | Blue | EU Markets in Crypto Assets regulation aware or compliant. |
| [![A2A Ready](https://img.shields.io/badge/A2A-ready-purple?style=flat-square)](url) | Purple | Compatible with Google's Agent-to-Agent protocol. |

Informational tags are applied by the maintainers on review. To request a tag for your entry, note it in your pull request with a link to documentation supporting the claim.

---

## How to Submit

1. Open a Pull Request titled `Add [Name]`.
2. Add the entry to the bottom of the correct section in the relevant `directory/` file.
3. Use the format: `[Name](url) — Description starting uppercase, ending with period.`
4. Verify the link is live before submitting.
5. One entry per PR.

To suggest an entry without writing the PR yourself, open an [issue](https://github.com/Haustorium12/gold-402/issues) with the name, URL, and a one-sentence description.

---

## Maintenance Cadence

**Monthly:**
- Rotate the Featured pick in `README.md`, archive the previous pick to `FEATURED.md`.
- Update the What's New section with the month's notable additions and ecosystem events.

**Quarterly:**
- Re-verify all `24K Verified` tagged entries against the four criteria.
- Check all links in `README.md` and `directory/` files — remove or update dead links.
- Scan [x402.org/ecosystem](https://x402.org/ecosystem) and x402 Foundation announcements for new entries worth adding.
- Promote standout entries from `directory/` to the curated README sections if they have matured.

Sources for the quarterly audit: [x402.org/ecosystem](https://x402.org/ecosystem), [agenteconomy.to](https://agenteconomy.to), [Dune Analytics x402](https://dune.com/x402), [x402scan](https://x402scan.com).
