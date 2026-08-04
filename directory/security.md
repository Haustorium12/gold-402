# Security & Audits

Security tools, spending controls, audit resources, and best practices for x402 implementations.

---

> ★ **Featured — August 2026: [Hermes Plant Action Safety](https://hermesplant.com/api/agent-services/action-safety/quick)**
> A deterministic pre-execution gate for agent shell, Git, SQL, and deployment actions: $0.01 for a quick verdict, $0.25 for a signed-receipt workflow. One of the few paid x402 services with repeat buyers visible on-chain.

## Smart Contract Audits

- [Coinbase x402 Security Audit](https://docs.cdp.coinbase.com/x402/security) — Official security audit of x402 protocol smart contracts.
- [EIP-3009 Security Analysis](https://eips.ethereum.org/EIPS/eip-3009#security-considerations) — Security considerations for TransferWithAuthorization.
- [CVE Database](https://github.com/x402-foundation/x402/security/advisories) — Known vulnerabilities and patches for the x402 protocol.

---

## Security Best Practices

- [x402 Security Checklist](https://docs.cdp.coinbase.com/x402/security/checklist) — Production deployment security requirements: signature verification, replay attack prevention, nonce management, rate limiting.
- [Payment Verification Guide](https://github.com/x402-foundation/x402/blob/main/SECURITY.md) — Proper payment verification: facilitator trust models, on-chain verification fallbacks, amount and recipient validation.
- [Key Management](https://docs.cdp.coinbase.com/x402/security/keys) — Secure private key handling for automated payments: hardware wallet integration, key rotation, multi-sig setups.
- [Replay Attack Prevention](https://docs.cdp.coinbase.com/x402/security/replay) — Nonce and deadline handling.

---

## Security Monitoring Tools

- [ShieldAPI](https://shield.vainplex.dev) — x402-native security intelligence API. 9 endpoints: password/email breach check (900M+ HIBP hashes), domain/IP reputation, URL safety scanning, prompt injection detection, skill security analysis. Micropayments on Base. [MCP Server](https://www.npmjs.com/package/shieldapi-mcp)
- [stripe-mcps](https://www.npmjs.com/package/stripe-mcps) — Trust verification + AML sanctions screening before Stripe/x402 payments. Agent identity (ECDSA), 75K+ sanctions entries (UK HMT + OFAC SDN), behavioural spend limits. OWASP MCP Security Cheat Sheet aligned.
- [KaelAi](https://kaelai.io) — Wallet trust scoring API for the agentic economy. Scores wallets 0-100 across 10 chains with behavioural analysis. Built for x402 servers to vet incoming/outgoing payment wallets before serving or initiating requests.
- [PaySentry](https://github.com/mkmkkkkk/paysentry) — Control plane for AI agent payments. Spending limits, circuit breakers, anomaly detection, audit trails. npm: `@paysentry/x402`.
- [x402 Notary](https://github.com/x402notary/notary) — Enterprise-grade audit and compliance platform. Full visibility into agent spending, policy enforcement, cryptographic audit trails.
- [Sentinel/Valeo](https://sentinel.valeocash.com) — Enterprise audit layer. Budget enforcement, structured audit trails, real-time dashboard, public payment explorer. SDK: `@x402sentinel/x402`.
- [Viridis MCP Security Preflight](https://mcp.viridisconservation.com/x402/security-preflight/security_preflight?agent_id=viridis-probe&manifest=%7B%7D) — Deterministic static preflight for caller-supplied MCP manifests that checks endpoint and authentication declarations, closed tool schemas, approval-policy conflicts, and prompt-injection indicators, returning an input-redacted signed receipt after x402 USDC settlement on Base.

---

## Spending Controls

- [Paybound](https://github.com/pando-b/paybound) — Open-source governance proxy for x402 agent payments. Per-agent budgets, time-windowed limits, circuit breakers, full audit trail. MIT licensed.
- [PolicyLayer](https://policylayer.com) — Non-custodial spending controls for AI agents. Daily limits, per-transaction caps, recipient whitelists, rate limiting. No private key custody.
- [ICME Labs](https://docs.icme.io) — Formal verification for AI agent actions. Natural language policies compile to SMT-LIB logic, checked by SMT solver. Wrapped in zero knowledge proofs. $0.10 USDC on Base.
- [Decision Anchor](https://api.decision-anchor.com) — External accountability proof before x402 payment execution. Records what was authorized, when, and at what scope. Non-judgmental.
- [Hermes Plant Action Safety](https://hermesplant.com/api/agent-services/action-safety/quick) — Deterministic pre-execution gate for agent shell, Git, SQL, infrastructure, and deployment actions, with a $0.01 quick check and a $0.25 signed-receipt workflow on Base.

---

## Agent Trust & Reputation

- [Revettr](https://revettr.com) — Counterparty risk scoring for x402 agentic commerce. Scores wallet addresses, domains, IPs, and companies 0-100 for payment safety.
- [MoltGuard](https://api.moltrust.ch/guard/) — Agent trust scoring (0-100), Sybil detection with funding cluster analysis, Polymarket integrity, Ed25519 Verifiable Credentials. 7 MCP tools. $0.005-$0.05 USDC on Base.
- [DJD AgentScore](https://github.com/djd-agent-score/djd-agent-score) — On-chain reputation scoring for AI agent wallets. 0-100 trust score across 5 dimensions (identity, behavior, reliability, viability, capability) from x402 settlement history on Base. Free tier.
- [ScoutScore](https://scoutscore.ai) — Trust scoring for x402 services (not agents). Monitors 1,700+ services with continuous health checks and fidelity probes.

---

## Compliance & Sanctions

- [CYBERA Compliance API](https://compliance-api-ruddy.vercel.app) — VASP address identification (20,468 addresses, 29 chains), risk scoring, sanctions/mixer screening. $0.01 USDC on Base.
- [SENTINEL](https://mru-oracle.com) — AML/CFT compliance intelligence. 77K+ sanctions entities (OFAC, UN, EU, PEP, Interpol, World Bank, crypto watchlists), 159-country jurisdiction risk scoring. MCP server at `/mcp`. $0.001-$0.015 USDC on Base.

---

## Bug Bounty Programs

- [Coinbase Bug Bounty](https://hackerone.com/coinbase) — Report x402 vulnerabilities for rewards up to $50,000.
- [Immunefi x402 Program](https://immunefi.com) — Decentralized bug bounty platform with x402 listings.
