# Contributing to gold-402

**Built something on x402? Submit it.** gold-402 is a curated directory of x402 resources — facilitators, SDKs, frameworks, APIs, MCP servers, tools, and the services agents actually pay to use. Getting listed means builders and AI agents can find you.

- **New entry?** Open a PR titled `Add [Name]` — takes five minutes, format below. **This is the only way in.** An issue asking to be listed isn't a submission — see below.
- **Question or discussion?** Open a [GitHub Discussion](https://github.com/Haustorium12/gold-402/discussions).
- **Dead link, stale entry, or something wrong with the repo?** Open an [issue](https://github.com/Haustorium12/gold-402/issues) — we fix them fast. **An issue titled "Add X" gets pointed back here, not landed by hand** — one intake lane, so every entry gets the same PR-gate check before a human reads it.

The directory is updated continuously. Each week the newest additions are collected in the README's **New This Week** section.

---

## What Gets Listed

In scope — anything that genuinely uses the x402 protocol:

- **Facilitators** — hosted or self-hosted x402 payment facilitators settling real USDC (or a supported stablecoin). → `directory/facilitators.md`
- **SDKs & Libraries** — client and server libraries for implementing x402, in any language. → `directory/sdks.md`
- **Frameworks & Middleware** — server middleware and framework integrations (Express, Hono, Next.js, FastAPI, Axum, Cloudflare Workers, and more), and agent frameworks with x402 support. → `directory/frameworks.md`
- **APIs & Services** — x402-payable API endpoints agents call and pay for per request. → `directory/apis.md`
- **MCP Servers** — Model Context Protocol servers that gate access behind x402. → `directory/mcp-servers.md`
- **Tools & Utilities** — proxies, monitoring, analytics, CLIs, and CI/CD integrations. → `directory/tools.md`
- **Security & Compliance** — audits, trust scoring, sanctions/AML screening, and spend controls. → `directory/security.md`
- **Ecosystem & Wallets** — agent wallets, marketplaces, and x402-integrated infrastructure. → `directory/ecosystem.md`
- **Learning** — quickstarts, tutorials, videos and talks, and reference material directly useful to x402 builders. → `directory/learning.md`
- **Community** — channels, newsletters, jobs, and events for x402 builders. → `directory/community.md`
- **Aggregators & Proxies** — one integration, many upstreams: services that unify or resell access to other providers' APIs and data. → `directory/aggregators.md`
- **The Global Agent Economy** — agent payment infrastructure outside the West. → `directory/global.md`
- **Market Data** — on-chain analytics and dashboards for the x402 economy. → `directory/market-data.md`
- **Examples** — working x402 example projects: full-stack apps, API examples, and client examples. → `directory/examples.md`
- **Use Cases & Patterns** — documented x402 deployments and payment patterns, by industry. → `directory/use-cases.md`
- **Research & Audits** — published studies, security audits, and papers about x402, with the method disclosed. → `directory/research.md`
- **Publisher & Crawler Monetization** — x402 pay-per-crawl and publisher paywall tooling and services. → `directory/publishers.md`

Out of scope: general crypto wallets, general USDC infrastructure, and AI-agent platforms with no specific x402 integration.

## Acceptance

For a **service** — an API, MCP server, facilitator, or anything with a live endpoint — all of the following:

- **It's live.** The URL resolves and the endpoint returns a valid HTTP 402 challenge with correct payment headers, or serves a valid x402 manifest.
- **It's actually x402.** It implements the protocol (HTTP 402 + `PAYMENT-SIGNATURE`), not just "we accept USDC" or general crypto payments.
- **It settles on a supported chain.** Base is the norm; other chains are fine as long as the x402 flow is real.
- **It's not a duplicate service** (see the one-entry-per-service rule below).
- **The description is one factual line.** No marketing language.
- **An agent can actually reach it.** Give us the URL where the 402 lives — the endpoint itself, or a `/.well-known/x402` manifest that points at it. Not a homepage that a person has to read their way out of.
- **A working example request**, if your endpoint needs parameters. A method and a minimal body is plenty: `POST /v1/quote  {"symbol":"BTC"}`. If a caller has to guess the shape, they can't buy from you.

For a **library, framework, or learning/community resource** with no payable endpoint of its own: it must be publicly accessible (live URL or public repo), demonstrably x402-specific, with a commit or release in the last 12 months (an older resource that still matters, such as a finished spec, needs a maintainer's exception written on its PR), and described in one factual line.

**The door you name stays on file.** The `URL:` line and any `Example:` in your PR aren't only for the check before merge — we keep them and use them in the nightly knock, so a listing link that a bot can't read isn't mistaken for a dead service. If your endpoint moves, open a PR with the new one.

**Optional, for people:** your website, and one line on who you are. Like contact, it's never required and no entry is rejected without it — and like everything in a PR description, it's public.

We probe every submitted endpoint before merging. Every submission that fails gets a comment saying what failed and how to fix it — never a silent rejection. Fix it and resubmit.

**Why we ask for the last two.** An agent can only pay for what it can find and call. A homepage isn't a door, and an undocumented request shape is a locked one. So we ask for the door, and the shape of the knock.

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

**Where it lives.** In the pull request description, not in your directory entry. **This repository is public, so anyone can read a pull request description, and GitHub keeps its edit history.** Only put a contact there that you're comfortable having public: a project address, a handle, or a contact form, not a personal inbox. If you'd rather not share one at all, leave it out and we'll open an issue on your repo instead.

**Where this breaks, honestly.** A lot of entries are a bare endpoint with no repo. For those we have no way to reach anyone, and a dead endpoint just moves to departures. That's the gap this line exists to close, one entry at a time.

## What "verified" means

gold-402 has **no stamp and no tiers.** There was a single-tier mark — "listed = verified" — and it was retired on 2026-09-06 because it said the same thing about a paid API we had knocked and about a wallet or a wiki with no endpoint to knock at all.

Every entry now carries the finding rather than a mark:

- **A date** — the endpoint answered an HTTP 402 when we knocked it, on that day. The submission gate checks it, a maintainer confirms before merge, and a sweep re-knocks every listed endpoint every night and writes a dated result.
- **"listed — no knock receipt"** — a human read it; we hold no dated knock and will not backfill one.
- **"listed — no endpoint to knock"** — libraries, guides, wallets, clients, community resources. Nothing here answers a 402 because that is not what these things do.

That is the whole claim. It is **not** an audit of the provider, a guarantee of uptime, a promise that any given call will succeed, or a delivery test — we have not paid these services and graded what came back.

**When a claim doesn't reproduce.** If your description says something our knock can't confirm — a price, a chain, a feature — we don't quietly rewrite it. We send it back to you once to fix, or it ships exactly as you wrote it with what we saw noted on the pull request. Changing your words is never something we do on our own.

## When a service stops answering

A listing that fails our knock on two different days isn't deleted. It moves to departures with the date it first failed, and the site shows a running count — "no answer for N days" — from that date. If it comes back, it's restored and the record shows it returned. The dates are the point: they're how a reader can tell a service that's been solid for months from one that came back yesterday.

## One entry per service (multiple services welcome)

The unit of a listing is the **service**, not the provider.

- **Different services from the same provider are each welcome**: one entry each, in the section each belongs to.
- **A separate service is one a builder would search for on its own.** Routes of one API share one line: `/audit`, `/links` and `/quote` on the same host are one service, with their prices in that line.
- **A wrapper is its own entry when it speaks a different protocol**, such as an MCP server over a provider's HTTP APIs. Its line says what it wraps and links the wrapper's own address, not the upstream one.
- **The same service listed twice is a duplicate.** That's the thing we don't take.
- **Listings paid to the same wallet are shown together.** When two or more listings name the same payTo address in their 402 answers, each listing's page on 24klabs.ai says so and links the others. It covers listings that answer 402 to a plain request, and the page shows the date it was read.
- **Prefer one entry per pull request.** A PR with several genuinely distinct, valid entries is fine.

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
2. Add the entry to the bottom of the correct section in the relevant `directory/` file. We may move it to a different shelf if we think it fits better there.
3. Use the format above, and verify the link is live before submitting.
4. One entry per PR where practical.
5. **If your endpoint requires request parameters** before it can answer with 402 (e.g. an OpenAI-compatible API that validates the body first), add an `Example:` line with a single-line JSON request body to the PR description — the submission gate will probe your endpoint with that body instead of an empty `{}`:

   ```
   Example: {"model":"gpt-4o","messages":[{"role":"user","content":"hi"}]}
   ```

   Endpoints without an `Example:` line are probed with `{}` (existing behavior).

6. **Optionally, tell us how to reach you** — add a `Contact:` line to the PR description. It's public, so use an address you don't mind being seen:

   ```
   Contact: you@example.com
   ```

   Email, X, Telegram, a Discord, a contact form, anything. Entirely optional; leave it out and we'll open an issue on your repo instead. [What we'd use it for](#how-we-reach-you).

## Featured

On the 1st of each month the maintainers select one **Featured** pick per shelf, shown at the top of each shelf and indexed in the README, with past slates archived in [FEATURED.md](FEATURED.md). Featured is an editorial pick — a judgment that something is well-built, actively used, and worth a second look, with a preference for excellent work that hasn't already had wide coverage. A shelf with no entry that clears the bar runs empty that month; the empty slot is also a verdict. Featured is the one editorial mark gold-402 carries, and it is always awarded by the maintainers, never requested onto your own entry, and never sold.

## Maintenance

- **Weekly** — refresh **New This Week** (the week's additions).
- **Monthly** — rotate the Featured slate (one pick per shelf) and archive the previous month to `FEATURED.md`.
- **Nightly** — knock every listed endpoint and move dead entries to departures.
- **Ongoing** — scan the ecosystem for new entries worth adding.

---

<p align="center">
  <b>Curated by <a href="https://24klabs.ai">24K Labs</a></b><br>
  <sub>If this saved you time, star the repo.</sub>
</p>
