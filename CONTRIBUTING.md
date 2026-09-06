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
- **An agent can actually reach it.** Give us the URL where the 402 lives — the endpoint itself, or a `/.well-known/x402` manifest that points at it. Not a homepage that a person has to read their way out of.
- **A working example request**, if your endpoint needs parameters. A method and a minimal body is plenty: `POST /v1/quote  {"symbol":"BTC"}`. If a caller has to guess the shape, they can't buy from you.

For a **library, framework, or learning/community resource** with no payable endpoint of its own: it must be publicly accessible (live URL or public repo), demonstrably x402-specific, active within roughly the last twelve months, and described in one factual line.

We probe every submitted endpoint before merging. Anything that fails gets a friendly note explaining what to fix — never a silent rejection. Fix it and resubmit.

**Why we ask for the last two.** We buy things now. In July 2026 we ran the first paid delivery check across our own shelf and found that of 126 listed services, only 16 could be purchased by a machine at a findable address — and four of those still failed because the request shape wasn't documented anywhere a caller could find it. The services were fine. The front doors weren't.

That's not a complaint about anyone's product. It's the single biggest thing standing between a working service and an agent that would have paid for it. So we ask for the door, and the shape of the knock.

## How we reach you

**Our default is your repo.** If something goes wrong with your listing, we open an issue on the repository your entry links to. No signup, no address to hand over, and the message lands somewhere you already look. That's the standard and it needs nothing from you.

**If you'd rather be reached somewhere else, tell us.** Add a line to the pull request description:

```
Contact: you@example.com
```

Anything you like goes there — an email, an X or Telegram handle, a Discord, a link to a different repo's issues, a contact form. Whatever actually reaches you. It's an ask, not a requirement: **no entry is ever rejected for leaving it out**, and we'll fall back to your repo.

**What we'd use it for. This is the whole list:**

- Your endpoint stopped answering our liveness knock, and you're about to be delisted.
- Something in your entry is wrong and we want to fix it correctly rather than guess.
- You're a Featured pick and we're about to say so publicly.

**What we never do with it:** no newsletter, no announcements, no marketing, no "we thought you'd be interested in", no selling it, no sharing it, no passing it to anyone else for any reason. It is not a mailing list and it will never become one.

**Where it lives.** In the pull request description — **not in your directory entry.** Public markdown gets scraped by address harvesters within days, and we're not going to be the reason your inbox fills up. We keep it privately and only while your entry is listed. Ask us to delete it and we will, and your listing is unaffected.

**Where this breaks, honestly.** Two thirds of the current directory doesn't link a repo at all — a lot of entries are a bare endpoint and nothing else. For those we have no way to reach anyone, and a dead endpoint just gets delisted. That's the gap this line exists to close, one entry at a time.

## What "verified" means

gold-402 has **no stamp and no tiers.** There was a single-tier mark — "listed = verified" — and it was retired on 2026-09-06 because it said the same thing about a paid API we had knocked and about a wallet or a wiki with no endpoint to knock at all.

Every entry now carries the finding rather than a mark:

- **A date** — the endpoint answered an HTTP 402 when we knocked it, on that day. The submission gate checks it, a maintainer confirms before merge, and a sweep re-knocks and writes a dated result.
- **"listed — no knock receipt"** — a human read it; we hold no dated knock and will not backfill one.
- **"listed — no endpoint to knock"** — libraries, guides, wallets, clients, community resources. Nothing here answers a 402 because that is not what these things do.

That is the whole claim. It is **not** an audit of the provider, a guarantee of uptime, a promise that any given call will succeed, or a delivery test — we have not paid these services and graded what came back.

**Some entries carry more than that.** Where we have paid for a service and confirmed what came back, we say so and we keep the receipt — what we sent, what it cost, the transaction, and what arrived. That's a stronger claim than liveness and we only make it about services we actually bought. Most of the list hasn't been through that yet.

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
5. **If your endpoint requires request parameters** before it can answer with 402 (e.g. an OpenAI-compatible API that validates the body first), add an `Example:` line with a single-line JSON request body to the PR description — the submission gate will probe your endpoint with that body instead of an empty `{}`:

   ```
   Example: {"model":"gpt-4o","messages":[{"role":"user","content":"hi"}]}
   ```

   Endpoints without an `Example:` line are probed with `{}` (existing behavior).

6. **Optionally, tell us how to reach you** — add a `Contact:` line to the PR description:

   ```
   Contact: you@example.com
   ```

   Email, X, Telegram, a Discord, a contact form, anything. Entirely optional; leave it out and we'll open an issue on your repo instead. [What we'd use it for](#how-we-reach-you).

To suggest an entry without writing the PR yourself, open an [issue](https://github.com/Haustorium12/gold-402/issues) with the name, URL, and a one-sentence description — we'll take it from there.

## Featured

On the 1st of each month the maintainers select one **Featured** pick per shelf, shown at the top of each shelf and indexed in the README, with past slates archived in [FEATURED.md](FEATURED.md). Featured is an editorial pick — a judgment that something is well-built, actively used, and worth a second look, with a preference for excellent work that hasn't already had wide coverage. A shelf with no entry that clears the bar runs empty that month; the empty slot is also a verdict. Featured is the one editorial mark gold-402 carries, and it is always awarded by the maintainers, never requested onto your own entry.

## Maintenance

- **Weekly** — refresh **This Week in x402** (ecosystem developments) and **New This Week** (the week's additions).
- **Monthly** — rotate the Featured slate (one pick per shelf) and archive the previous month to `FEATURED.md`.
- **Ongoing** — probe listed endpoints for liveness, remove or fix dead links, and scan the ecosystem for new entries worth adding.

---

<p align="center">
  <b>Curated by <a href="https://24klabs.ai">24K Labs</a></b><br>
  <sub>If this saved you time, star the repo.</sub>
</p>
