﻿# Security & Audits

Security tools, spending controls, audit resources, and best practices for x402 implementations.

---

> ★ **Featured — August 2026: [Hermes Plant Action Safety](https://hermesplant.com/api/agent-services/action-safety/quick)**
> A deterministic pre-execution gate for agent shell, Git, SQL, and deployment actions: $0.01 for a quick verdict, $0.25 for a signed-receipt workflow. One of the few paid x402 services with repeat buyers visible on-chain.

## Smart Contract Audits

- [EIP-3009 Security Analysis](https://eips.ethereum.org/EIPS/eip-3009#security-considerations) — Security considerations for TransferWithAuthorization.
- [CVE Database](https://github.com/x402-foundation/x402/security/advisories) — Known vulnerabilities and patches for the x402 protocol.

---

## Security Best Practices

- [Payment Verification Guide](https://github.com/x402-foundation/x402/blob/main/SECURITY.md) — Proper payment verification: facilitator trust models, on-chain verification fallbacks, amount and recipient validation.

---

## Security Monitoring Tools

- [DopamineDesk Transaction Preflight](https://ai-data-marketplace-1042299154756.us-central1.run.app/api/v1/transaction_preflight) — Checks an unsigned EVM transaction for simulation errors, gas, proxy evidence, and optional token-security or allowance issues before an agent signs it. `POST` only, $0.005 USDC on Base. ([OpenAPI](https://ai-data-marketplace-1042299154756.us-central1.run.app/openapi.json))
- [ShieldAPI](https://shield.vainplex.dev) — x402-native security intelligence API. 9 endpoints: password/email breach check (900M+ HIBP hashes), domain/IP reputation, URL safety scanning, prompt injection detection, skill security analysis. Micropayments on Base. [MCP Server](https://www.npmjs.com/package/shieldapi-mcp)
- [stripe-mcps](https://www.npmjs.com/package/stripe-mcps) — Trust verification + AML sanctions screening before Stripe/x402 payments. Agent identity (ECDSA), 75K+ sanctions entries (UK HMT + OFAC SDN), behavioural spend limits. OWASP MCP Security Cheat Sheet aligned.
- [KaelAi](https://kaelai.io) — Wallet trust scoring API for the agentic economy. Scores wallets 0-100 across 10 chains with behavioural analysis. Built for x402 servers to vet incoming/outgoing payment wallets before serving or initiating requests.
- [PaySentry](https://github.com/mkmkkkkk/paysentry) — Control plane for AI agent payments. Spending limits, circuit breakers, anomaly detection, audit trails. npm: `@paysentry/x402`.
- [Sentinel/Valeo](https://sentinel.valeocash.com) — Enterprise audit layer. Budget enforcement, structured audit trails, real-time dashboard, public payment explorer. SDK: `@x402sentinel/x402`.
- [Viridis MCP Security Preflight](https://mcp.viridisconservation.com/x402/security-preflight/security_preflight?agent_id=viridis-probe&manifest=%7B%7D) — Deterministic static preflight for caller-supplied MCP manifests that checks endpoint and authentication declarations, closed tool schemas, approval-policy conflicts, and prompt-injection indicators, returning an input-redacted signed receipt after x402 USDC settlement on Base.
- [x402 Manifest Check](https://github.com/ruizmr/x402-api-readiness-review) — Zero-dependency Python CLI and live x402-paid API for static manifest checks covering network, recipient, asset, and amount bindings; neither validates runtime enforcement or settlement.
- [TaskMarket Trust Score](https://95-217-164-43.sslip.io) — Requester reputation scoring for TaskMarket (taskmarket.dev): given a requester wallet address, returns a 0-100 trust score from on-platform payment history (completed tasks, cancellations-after-submission, expirations, self-awards). $0.001 USDC per call on Base, self-facilitated EIP-3009 exact scheme. Example: `GET /trust/0xADDRESS`. Discovery: `GET /.well-known/x402`.
- [x402 Preflight](https://x402-wallet-readiness-service.vercel.app/api/x402/preflight/audit?resource_url=https%3A%2F%2Fx402-wallet-readiness-service.vercel.app%2Fapi%2Fx402%2Fdev%2Frepo-snapshot%3Frepo%3Dchico10117%2Fbasepay-readiness-service&method=GET&expected_network=eip155%3A8453&max_price_usd=1) — Audits a public x402 endpoint before payment via required `resource_url` and optional `method=GET|HEAD`, `expected_network`, and `max_price_usd` query parameters; the audit costs $0.05 USDC on Base.

---

## Spending Controls

- [Paybound](https://github.com/pando-b/paybound) — Open-source governance proxy for x402 agent payments. Per-agent budgets, time-windowed limits, circuit breakers, full audit trail. MIT licensed.
- [PolicyLayer](https://policylayer.com) — Non-custodial spending controls for AI agents. Daily limits, per-transaction caps, recipient whitelists, rate limiting. No private key custody.
- [ICME Labs](https://docs.icme.io) — Formal verification for AI agent actions. Natural language policies compile to SMT-LIB logic, checked by SMT solver. Wrapped in zero knowledge proofs. $0.10 USDC on Base.
- [Decision Anchor](https://api.decision-anchor.com) — External anchoring layer for accountability before x402 payment execution. Records what was authorized, when, and at what scope. Content-blind. Non-judgmental.
- [Hermes Plant Action Safety](https://hermesplant.com/api/agent-services/action-safety/quick) — Deterministic pre-execution gate for agent shell, Git, SQL, infrastructure, and deployment actions, with a $0.01 quick check and a $0.25 signed-receipt workflow on Base.

---

## Agent Trust & Reputation

- [Revettr](https://revettr.com) — Counterparty risk scoring for x402 agentic commerce. Scores wallet addresses, domains, IPs, and companies 0-100 for payment safety.
- [MoltGuard](https://api.moltrust.ch/guard/) — Agent trust scoring (0-100), Sybil detection with funding cluster analysis, Polymarket integrity, Ed25519 Verifiable Credentials. 7 MCP tools. $0.005-$0.05 USDC on Base.

---

## Endpoint Trust & Reputation

- [ScoutScore](https://scoutscore.ai) — Trust scoring for x402 services. Monitors 1,700+ services with continuous health checks and fidelity probes.
- [x402 Trust](https://x402.fuchss.app) — Autonomous trust and reliability scoring for every publicly listed x402 endpoint, derived from continuous live probing and on-chain USDC settlement. Live report via POST /v1/x402-trust, free preview via GET /v1/x402-trust-preview.
- [Cleared Index](https://clearedindex.com) — Trust provider and verification index with a conformant trust-evaluation endpoint: `POST /api/cleared/trust/evaluate` (`x402-trust-evaluation-v0.1`), Ed25519 signed attestations, and public JWKS at `GET /api/cleared/jwks`. Discovery manifest: `/.well-known/x402.json`.
- [x402 Checker (Nock)](https://x402-checker.nock-for-mak.workers.dev/report) — Free `GET /check?url=` honesty probe of a live x402 URL plus free `GET /board` (pay-to-rank, 24h) and `GET /name`; paid `GET /report?url=` is $0.05 USDC on Base via PayAI, and `POST /bid` and `POST /name` are $0.05. Example: `GET /check?url=https://example.com`. ([Manifest](https://x402-checker.nock-for-mak.workers.dev/.well-known/x402)) ([OpenAPI](https://x402-checker.nock-for-mak.workers.dev/openapi.json)) ([GitHub](https://github.com/nock-for-mak/skills))
- [MIDAX402](https://midax402.com) — Signed conformance verdicts for x402 services, published to a public registry anyone can audit. Verdicts cannot be bought.

---

## Compliance & Sanctions

- [CYBERA Compliance API](https://compliance-api-ruddy.vercel.app) — VASP address identification (20,468 addresses, 29 chains), risk scoring, sanctions/mixer screening. $0.01 USDC on Base.
- [SENTINEL](https://mru-oracle.com) — AML/CFT compliance intelligence. 77K+ sanctions entities (OFAC, UN, EU, PEP, Interpol, World Bank, crypto watchlists), 159-country jurisdiction risk scoring. MCP server at `/mcp`. $0.001-$0.015 USDC on Base.

---

## Bug Bounty Programs

- [Coinbase Bug Bounty](https://hackerone.com/coinbase) — Report x402 vulnerabilities for rewards up to $50,000.
- [Immunefi x402 Program](https://immunefi.com) — Decentralized bug bounty platform with x402 listings.
