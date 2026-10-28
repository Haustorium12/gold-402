# Security & Audits

Security tools, spending controls, audit resources, and best practices for x402 implementations.

---

> ★ **Featured — October 2026: [ICME Labs](https://docs.icme.io)**
> Turns a plain-language spending policy into SMT-LIB logic and has a solver check an agent's action against it — a proof the rule held, not a score that says it probably did. $0.10 USDC on Base.

## Smart Contract Audits

- [EIP-3009 Security Analysis](https://eips.ethereum.org/EIPS/eip-3009#security-considerations) — Security considerations for TransferWithAuthorization.
- [CVE Database](https://github.com/x402-foundation/x402/security/advisories) — Known vulnerabilities and patches for the x402 protocol.

---

## Security Best Practices

- [Payment Verification Guide](https://github.com/x402-foundation/x402/blob/main/SECURITY.md) — Proper payment verification: facilitator trust models, on-chain verification fallbacks, amount and recipient validation.

---

## Security Monitoring Tools

- [DopamineDesk Transaction Preflight](https://ai-data-marketplace-1042299154756.us-central1.run.app/api/v1/transaction_preflight) — Checks an unsigned EVM transaction for simulation errors, gas, proxy evidence, and optional token-security or allowance issues before an agent signs it. `POST` only, $0.005 USDC on Base. ([OpenAPI](https://ai-data-marketplace-1042299154756.us-central1.run.app/openapi.json))
- [ShieldAPI](https://shield.vainplex.dev/.well-known/x402.json) — x402-native security intelligence API. 9 endpoints: password/email breach check (900M+ HIBP hashes), domain/IP reputation, URL safety scanning, prompt injection detection, skill security analysis. Micropayments on Base. [MCP Server](https://www.npmjs.com/package/shieldapi-mcp)
- [stripe-mcps](https://www.npmjs.com/package/stripe-mcps) — Trust verification + AML sanctions screening before Stripe/x402 payments. Agent identity (ECDSA), 75K+ sanctions entries (UK HMT + OFAC SDN), behavioural spend limits. OWASP MCP Security Cheat Sheet aligned.
- [PaySentry](https://github.com/mkmkkkkk/paysentry) — Control plane for AI agent payments. Spending limits, circuit breakers, anomaly detection, audit trails. npm: `@paysentry/x402`.
- [Sentinel/Valeo](https://sentinel.valeocash.com) — Enterprise audit layer. Budget enforcement, structured audit trails, real-time dashboard, public payment explorer. SDK: `@x402sentinel/x402`.
- [Viridis MCP Security Preflight](https://mcp.viridisconservation.com/x402/security-preflight/security_preflight?agent_id=viridis-probe&manifest=%7B%7D) — Deterministic static preflight for caller-supplied MCP manifests that checks endpoint and authentication declarations, closed tool schemas, approval-policy conflicts, and prompt-injection indicators, returning an input-redacted signed receipt after x402 USDC settlement on Base.
- [x402 Manifest Check](https://github.com/ruizmr/x402-api-readiness-review) — Zero-dependency Python CLI and live x402-paid API for static manifest checks covering network, recipient, asset, and amount bindings; neither validates runtime enforcement or settlement.
- [x402 Preflight](https://x402.chikocorp.com/api/x402/preflight/audit?resource_url=https%3A%2F%2Fx402.chikocorp.com%2Fapi%2Fx402%2Fdev%2Frepo-snapshot%3Frepo%3Dchico10117%2Fbasepay-readiness-service&method=GET&expected_network=eip155%3A8453&max_price_usd=1) — Audits a public x402 endpoint before payment via required `resource_url` and optional `method=GET|HEAD`, `expected_network`, and `max_price_usd` query parameters; the audit costs $0.05 USDC on Base.
- [GPT-6 Agent Guard & Calldata Decoder](https://gpt.558686.xyz/v1/guard/tx) — Pre-transaction safety analyzer and calldata decoder for autonomous agents to vet contracts and prevent wallet draining, $0.15 USDC on Base. ([OpenAPI](https://gpt.558686.xyz/openapi.json))
- [HostDeFi Token Risk](https://hostdefi.com/api/v1/x402/token-risk/solana/So11111111111111111111111111111111111111112) — x402 machine-payable multi-chain token risk scanner: instant on-chain safety grades for Solana and EVM tokens (authorities, liquidity, holder concentration, honeypot checks) plus JSON-RPC on 82 chains. Free web scanner at [hostdefi.com/scan](https://hostdefi.com/scan). ([Docs](https://hostdefi.com/features/x402-rpc/)) ([MCP](https://hostdefi.com/api/v1/mcp))
- [Automaton-Sovereign](https://api.automatonsvrn.xyz/.well-known/x402) — Pre-flight safety checks for Base before an agent signs: EVM bytecode analysis with honeypot and mint-backdoor detection (`GET /v2/security/scan?address=0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`, $0.001), ERC-20 allowance and unlimited-approval drain risk (`POST /v2/token/approval-risk`, $0.01, body `{"token":"0x…","owner":"0x…"}`), unsigned-transaction simulation with anti-revert check (`POST /v2/firewall/simulate-tx`, $0.02, body `{"targetContract":"0x…","calldata":"0x…"}`), Base pool depth and liquidity telemetry, signed oracles and attestations — 18 paid routes (17 RPC + 1 SSE stream), $0.001–$0.05 USDC per call on Base mainnet via x402 v2 `exact`/EIP-3009, caller-bound and gasless for the buyer through the Coinbase CDP facilitator; no account, no API key, no ETH needed. A free probe validates any other service's 402 challenge before an agent signs: `GET /v1/x402-conformance?url=` (9 named checks, no payment). MCP server with 20 tools at `/mcp` and official Agent Kit SDK. ([Manifest](https://api.automatonsvrn.xyz/.well-known/x402)) ([OpenAPI](https://api.automatonsvrn.xyz/openapi.json)) ([llms.txt](https://api.automatonsvrn.xyz/llms.txt)) ([Agent Kit](https://github.com/baianomarceloeduardo-jpg/automaton-agent-kit))
- [x402 Agent Safety Store](https://x402.dailyelo.com/.well-known/x402) — Pre-transaction safety checks for agents on Base: decode what a signature or transaction does before signing, catch address-poisoning look-alikes, audit token approvals, and read a feed of recently flagged addresses. Its manifest lists 20 routes, from $0.005 USDC per call on Base. Example: `POST /v1/sign-decode`.
- [VM3 x402 Public Quote Preflight](https://vm5-openapi-x402.onrender.com/v1/x402-preflight) — Performs offline structural checks of caller-supplied unsigned x402 v2 payment quotes for $0.01 Circle USDC per GET on Base, with a [free synthetic sample](https://vm5-openapi-x402.onrender.com/v1/x402-sample) and [public source](https://github.com/livastic-vm3-primary-tmp-260920/vm3-x402-quote-preflight).

---
- [KaelAi](https://kaelai.io) — Wallet trust scoring API for the agentic economy. Scores wallets 0-100 across 10 chains with behavioural analysis. Built for x402 servers to vet incoming/outgoing payment wallets before serving or initiating requests.

## Spending Controls

- [Paybound](https://github.com/pando-b/paybound) — Open-source governance proxy for x402 agent payments. Per-agent budgets, time-windowed limits, circuit breakers, full audit trail. MIT licensed.
- [PolicyLayer](https://policylayer.com) — Non-custodial spending controls for AI agents. Daily limits, per-transaction caps, recipient whitelists, rate limiting. No private key custody.
- [ICME Labs](https://docs.icme.io) — Formal verification for AI agent actions. Natural language policies compile to SMT-LIB logic, checked by SMT solver. Wrapped in zero knowledge proofs. $0.10 USDC on Base.
- [Decision Anchor](https://api.decision-anchor.com) — External anchoring layer for accountability before x402 payment execution. Records what was authorized, when, and at what scope. Content-blind. Non-judgmental.
- [Hermes Plant Action Safety](https://hermesplant.com/api/agent-services/action-safety/quick) — Deterministic pre-execution gate for agent shell, Git, SQL, infrastructure, and deployment actions, with a $0.01 quick check and a $0.25 signed-receipt workflow on Base.
- [agent.pw](https://github.com/smithery-ai/agent.pw) — Self-hostable MIT credential vault for agent API keys and OAuth tokens. Addresses the gap nobody in the pay-per-call world talks about: agents still need somewhere safe to keep the keys x402 didn't replace.

- [SpendPreflight](https://api.spendpreflight.com/.well-known/x402) — Operated by SpendPreflight, an x402 service providing OFAC/domain screening and allow/hold/block payment preflight with signed receipts for $0.01/$0.02 USDC on Base.
- [Burnbound](https://www.npmjs.com/package/@burnbound/mcp) — Buyer-side spending controls for x402: per-agent daily caps, per-payment limits, allowed hosts and human approval are checked before the customer's own wallet signs, through the MCP server `@burnbound/mcp`.
- [MoneySwitch](https://github.com/dongsheng123132/moneyswitch) — Self-hosted x402 payer with per-agent spending keys, budget and host limits, revocation, and human approval for payments above a configured threshold.

---
- [wren-guard Pro](https://wren-guard-pro.wrenonbase.workers.dev/sample) — TypeScript/viem guard for agent wallets (capped, simulated sends; approval, permit and EIP-7702 decoding; injection screen) with an 89-scenario drain corpus and a GitHub Action. `GET /sample` returns 5 scenarios for 0.01 USDC on Base; `GET /buy/19` (or 49, 99) returns a 7-day download link to the kit. MIT core: [wren-guard](https://github.com/claudeisgod/wren-guard).

## Trust & Reputation

- [agent-exec](https://agent-exec.448c.org/check/address?via=223) — Address and URL risk checks from public risk feeds: verdict, score and reasons, $0.02 USDC flat on Base or Solana, charged only on success. `POST /check/address` and `POST /check/url`. ([OpenAPI](https://agent-exec.448c.org/openapi.json?via=223))
- [Revettr](https://revettr.com/.well-known/x402.json) — Counterparty risk scoring for x402 agentic commerce. Scores wallet addresses, domains, IPs, and companies 0-100 for payment safety.
- [MoltGuard](https://api.moltrust.ch/.well-known/x402.json) — Agent trust scoring (0-100), Sybil detection with funding cluster analysis, Polymarket integrity, Ed25519 Verifiable Credentials. 7 MCP tools. $0.005-$0.05 USDC on Base.
- [ChainWard](https://api.chainward.ai/.well-known/x402) — Evidence-linked on-chain risk report for a Base or BNB Chain address before an agent pays it, $0.05 USDC on Base per call (`GET /api/risk/x402?address=0xADDRESS`, add `&chain=bsc` for BNB Chain), never charged when the check fails.
- [ScoutScore](https://scoutscore.ai) — Trust scoring for x402 services. Monitors 1,700+ services with continuous health checks and fidelity probes.
- [x402 Trust](https://x402.fuchss.app/.well-known/x402) — Autonomous trust and reliability scoring for every publicly listed x402 endpoint, derived from continuous live probing and on-chain USDC settlement. Live report via POST /v1/x402-trust, free preview via GET /v1/x402-trust-preview.
- [Cleared Index](https://clearedindex.com/.well-known/x402.json) — Trust provider and verification index with a conformant trust-evaluation endpoint: `POST /api/cleared/trust/evaluate` (`x402-trust-evaluation-v0.1`), Ed25519 signed attestations, and public JWKS at `GET /api/cleared/jwks`. Discovery manifest: `/.well-known/x402.json`.
- [x402 Checker (Nock)](https://x402-checker.nock-for-mak.workers.dev/report) — Free `GET /check?url=` honesty probe of a live x402 URL plus free `GET /board` (pay-to-rank, 24h) and `GET /name`; paid `GET /report?url=` is $0.05 USDC on Base via PayAI, and `POST /bid` and `POST /name` are $0.05. Example: `GET /check?url=https://example.com`. ([Manifest](https://x402-checker.nock-for-mak.workers.dev/.well-known/x402)) ([OpenAPI](https://x402-checker.nock-for-mak.workers.dev/openapi.json)) ([GitHub](https://github.com/nock-for-mak/skills))
- [MIDAX402](https://midax402.com/.well-known/x402.json) — Signed EIP-712 conformance verdicts for x402 services, appended to a public registry. Paid board position available ($1–$100 ladder) as a separate column; no payment changes a verdict or the verification-date ordering.
- [Verdix](https://api.verdixapi.com/.well-known/x402.json) — Checks an EVM address on Base before an agent sends funds to it: OFAC sanctions, scam/phishing lists, live address-poisoning detection, and flagged deployers, answering safe, caution, or danger, $0.01-$0.50 USDC per call, never charged if the check can't complete.
- [SkyeSkiff](https://skyeskiff.skyemeta.com/.well-known/x402) — Condition-gated rooms for AI agents: each agent signs a wallet challenge and is checked against the room's on-chain conditions and, if the room asks, who it acts for (an ERC-7710 delegation from an accepted principal or an ERC-8004 agent ID) before it joins, gets a signed result, and is removed at a later re-check if it no longer qualifies; $0.50 to open a room, $0.15 per join or re-check, USDC on Base, Polygon, Arbitrum or Solana.
- [Lumi Trades Vendor Trust](https://lumitrades.io) — Free 0-100 trust scores for XRPL-payable x402 sellers, built from unpaid 402-quote probes every 30 minutes and daily paid test-buys verified on the XRP Ledger, plus a per-vendor observation report for $0.02 USDC on Base, $0.02 RLUSD/USDC or 0.015 XRP on the XRP Ledger. Free list: `GET /v1/trust/vendors`; paid report: `GET /v1/trust/vendors/{id}/report`. ([API](https://api.lumitrades.io)) ([Manifest](https://api.lumitrades.io/.well-known/x402)) ([OpenAPI](https://api.lumitrades.io/openapi.json))

---

## Compliance & Sanctions

- [CYBERA Compliance API](https://compliance-api-ruddy.vercel.app) — VASP address identification (20,468 addresses, 29 chains), risk scoring, sanctions/mixer screening. $0.01 USDC on Base.
- [SENTINEL](https://mru-oracle.com) — AML/CFT compliance intelligence. 77K+ sanctions entities (OFAC, UN, EU, PEP, Interpol, World Bank, crypto watchlists), 159-country jurisdiction risk scoring. MCP server at `/mcp`. $0.001-$0.015 USDC on Base.
- [ScreenSeal](https://api-1-screening.agent-tollbooth.workers.dev/screen) — Sanctions screening for AI agents against OFAC SDN, OFAC Consolidated Non-SDN, and EU FSF lists, returning match confidence scores with an EIP-712 attestation seal at $0.02 USDC per call on Base mainnet via x402.
- [LION](https://lionx402.com/.well-known/x402.json) — Compliance and company lookups for agents: OFAC SDN wallet screening that answers pass, warn or block, a multi-list sanctions bundle, and company research and enrichment. Its manifest lists 21 routes, from $0.001 USDC per call on Base. Example: `GET /api/x402/wallet-screen-json`.

---
- [Checkpoint402 Sanctions Screening](https://api.checkpoint402.com/v1/sanctions-screen) — Screens a person or company name (fuzzy, alias-aware) and/or a crypto wallet address against the US Treasury OFAC SDN list including its extended remarks, for $0.05 USDC per call on Base; informational, not a compliance determination. Example: `GET /v1/sanctions-screen?address=0x098B716B8Aaf21512996dC57EB0615e2383E2f96`. ([OpenAPI](https://api.checkpoint402.com/openapi.json))

## Bug Bounty Programs

- [Coinbase Bug Bounty](https://hackerone.com/coinbase) — Report x402 vulnerabilities for rewards up to $50,000.
- [Immunefi x402 Program](https://immunefi.com) — Decentralized bug bounty platform with x402 listings.
