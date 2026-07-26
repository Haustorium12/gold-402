# Contributing to gold-402

**Built something on x402? Submit it.** gold-402 is a curated directory of x402 resources — facilitators, SDKs, frameworks, APIs, MCP servers, tools, and the services agents actually pay to use. Getting listed means builders and AI agents can find you.

- **New entry?** Open a PR titled `Add [Name]` — takes five minutes, format below.
- **Question or discussion?** Open a [GitHub Discussion](https://github.com/Haustorium12/gold-402/discussions).
- **Dead link or stale entry?** Open an [issue](https://github.com/Haustorium12/gold-402/issues) — we fix them fast.

The directory is updated continuously. Each week the newest additions are collected in the README's **New This Week** section, and the week's ecosystem developments in **This Week in x402**.

---

gold-402 is curated, not exhaustive. Every entry earns its place.

## What Gets Listed

In scope — anything that genuinely uses the x402 protocol:

- **Facilitators** — hosted or self-hosted x402 payment facilitators settling real USDC (or a supported stablecoin). → `directory/facilitators.md`
- **SDKs & Libraries** — client and server libraries for implementing x402, in any language. → `directory/sdks.md`
- **Frameworks & Middleware** — server middleware and framework integrations (Express, Hono, Next.js, FastAPI, Axum, Cloudflare Workers, and more). → `directory/frameworks.md`
- **APIs & Services** — x402-payable API endpoints agents call and pay for per request. → `directory/apis.md`
- **MCP Servers** — Model Context Protocol servers that gate access behind x402. → `directory/mcp-servers.md`
- **Tools & Utilities** — proxies, monitoring, analytics, spending controls, CLIs, and CI/CD integrations. → `directory/tools.md`
- **Security & Compliance** — audits, trust scoring, sanctions/AML screening, and spend controls. → `directory/security.md`
- **Ecosystem & Wallets** — agent wallets, marketplaces, and x402-integrated infrastructure. → `directory/ecosystem.md`
- **Learning** — quickstarts, tutorials, and reference material directly useful to x402 builders. → `directory/learning.md`
- **Community** — channels, newsletters, jobs, and events for x402 builders. → `directory/community.md`
- **Market Data** — on-chain analytics and dashboards for the x402 economy. → `directory/market-data.md`

Out of scope: general crypto wallets, general USDC infrastructure, and AI-agent platforms with no specific x402 integration.

## Acceptance

For a **service** — an API, MCP server, facilitator, or anything with a live endpoint — all of the following:

- **It's live.** The URL resolves and the endpoint returns a valid HTTP 402 challenge with correct payment headers, or serves a valid x402 manifest.
- **It's actually x402.** It implements the protocol (HTTP 402 + `X-Payment`), not just "we accept USDC" or general crypto payments.
- **It settles on a supported chain.** Base is the norm; other chains are fine as long as the x402 flow is real.
- **It's not a duplicate service** (see the one-entry-per-service rule below).
- **The description is one factual line.** No marketing language.

For a **library, framework, or learning/community resource** with no payable endpoint of its own: it must be publicly accessible (live URL or public repo), demonstrably x402-specific, active within roughly the last twelve months, and described in one factual line.

We probe every submitted endpoint before merging. Anything that fails gets a friendly note explaining what to fix — never a silent rejection. Fix it and resubmit.

## What "verified" means

gold-402 is one tier: **listed = verified.** There are no bronze/silver/gold levels. If an entry is on the list, the maintainers confirmed its endpoint was live and answered an x402 request correctly at the time of review, and re-check it periodically. That is the whole claim — a liveness-and-protocol check. It is **not** an audit of the provider, a guarantee of uptime, or a confirmation of any particular on-chain settlement. Curation is the bar; the list is the certificate.

## One entry per service (multiple services welcome)

The unit of a listing is the **service**, not the provider.

- **Different services from the same provider are each welcome** — one entry each, in the section each belongs to. A provider running, say, a code-review API and an image-generation API gets two entries, because a builder searching for one won't find it buried inside the other.
- **The same service listed twice is a duplicate** — that's the thing we don't take. One endpoint cross-posted into several categories to look bigger is what to avoid; each service has one home, its primary category.
- **Prefer one entry per pull request.** It keeps diffs clean and lets us verify and merge each independently. But a PR with several genuinely distinct, valid entries is fine — we may split it across commits on merge.

## Entry Format

```
[Name](url) — One factual sentence, starting uppercase, ending with a period.
```

- Em-dash separator (` — `) between the name and the description.
- Description is factual. No "powerful", "amazing", "best", or "revolutionary".
- URL links directly to the service, its repository, or its docs.
- **No badges.** Submissions carry no badges; the one editorial mark gold-402 uses (Featured, below) is applied by the maintainers, never attached by a submitter.
- No trailing whitespace.

**Facilitators exception:** entries in `directory/facilitators.md` may run up to three factual sentences — facilitators have multiple meaningful dimensions (chains, settlement mechanism, production status) that a single line can't carry. Adjectives without data and claims without a source are still out of scope.

## How to Submit

1. Open a Pull Request titled `Add [Name]`.
2. Add the entry to the bottom of the correct section in the relevant `directory/` file.
3. Use the format above, and verify the link is live before submitting.
4. One entry per PR where practical.

To suggest an entry without writing the PR yourself, open an [issue](https://github.com/Haustorium12/gold-402/issues) with the name, URL, and a one-sentence description — we'll take it from there.

## Featured

Now and then the maintainers spotlight one entry as **Featured** in the README, archived in [FEATURED.md](FEATURED.md). Featured is an editorial pick — a judgment that something is well-built, actively used, and worth a second look, with a preference for excellent work that hasn't already had wide coverage. It is the one editorial mark gold-402 carries, and it is always awarded by the maintainers, never requested onto your own entry.

## Maintenance

- **Weekly** — refresh **This Week in x402** (ecosystem developments) and **New This Week** (the week's additions).
- **Monthly** — rotate the Featured pick and archive the previous one to `FEATURED.md`.
- **Ongoing** — probe listed endpoints for liveness, remove or fix dead links, and scan the ecosystem for new entries worth adding.

---

<p align="center">
  <b>Curated by <a href="https://24klabs.ai">24K Labs</a></b><br>
  <sub>If this saved you time, star the repo.</sub>
</p>
