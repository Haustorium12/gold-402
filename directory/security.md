# Security & Audits

Security tools, spending controls, audit resources, and best practices for x402 implementations.

---

## Smart Contract Audits

- [Coinbase x402 Security Audit](https://docs.cdp.coinbase.com/x402/security) — Official security audit of x402 protocol smart contracts.
- [EIP-3009 Security Analysis](https://eips.ethereum.org/EIPS/eip-3009#security-considerations) — Security considerations for TransferWithAuthorization.
- [CVE Database](https://github.com/coinbase/x402/security/advisories) — Known vulnerabilities and patches for the x402 protocol.

---

## Security Best Practices

- [x402 Security Checklist](https://docs.cdp.coinbase.com/x402/security/checklist) — Production deployment security requirements: signature verification, replay attack prevention, nonce management, rate limiting.
- [Payment Verification Guide](https://github.com/coinbase/x402/blob/main/SECURITY.md) — Proper payment verification: facilitator trust models, on-chain verification fallbacks, amount and recipient validation.
- [Key Management](https://docs.cdp.coinbase.com/x402/security/keys) — Secure private key handling for automated payments: hardware wallet integration, key rotation, multi-sig setups.
- [Replay Attack Prevention](https://docs.cdp.coinbase.com/x402/security/replay) — Nonce and deadline handling.

---

## Security Monitoring Tools

- [ShieldAPI](https://shield.vainplex.dev) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/alberthild/shieldapi-mcp) — x402-native security intelligence API. 9 endpoints: password/email breach check (900M+ HIBP hashes), domain/IP reputation, URL safety scanning, prompt injection detection, skill security analysis. Micropayments on Base. [MCP Server](https://www.npmjs.com/package/shieldapi-mcp)
- [stripe-mcps](https://www.npmjs.com/package/stripe-mcps) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/razashariff/stripe-mcps) — Trust verification + AML sanctions screening before Stripe/x402 payments. Agent identity (ECDSA), 75K+ sanctions entries (UK HMT + OFAC SDN), behavioural spend limits. OWASP MCP Security Cheat Sheet aligned.
- [KaelAi](https://kaelai.io) — Wallet trust scoring API for the agentic economy. Scores wallets 0-100 across 10 chains with behavioural analysis. Built for x402 servers to vet incoming/outgoing payment wallets before serving or initiating requests.
- [PaySentry](https://github.com/mkmkkkkk/paysentry) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/mkmkkkkk/paysentry) — Control plane for AI agent payments. Spending limits, circuit breakers, anomaly detection, audit trails. npm: `@paysentry/x402`.
- [x402 Notary](https://github.com/x402notary/notary) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/x402notary/notary) — Enterprise-grade audit and compliance platform. Full visibility into agent spending, policy enforcement, cryptographic audit trails.
- [Sentinel/Valeo](https://sentinel.valeocash.com) — Enterprise audit layer. Budget enforcement, structured audit trails, real-time dashboard, public payment explorer. SDK: `@x402sentinel/x402`.

---

## Spending Controls

- [Paybound](https://github.com/pando-b/paybound) [![24K Verified](https://img.shields.io/badge/24K_Verified-2026--04-D4AF37?style=plastic)](../CONTRIBUTING.md) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/pando-b/paybound) — Open-source governance proxy for x402 agent payments. Per-agent budgets, time-windowed limits, circuit breakers, full audit trail. MIT licensed.
- [PolicyLayer](https://policylayer.com) — Non-custodial spending controls for AI agents. Daily limits, per-transaction caps, recipient whitelists, rate limiting. No private key custody.
- [ICME Labs](https://docs.icme.io) — Formal verification for AI agent actions. Natural language policies compile to SMT-LIB logic, checked by SMT solver. Wrapped in zero knowledge proofs. $0.10 USDC on Base.
- [Decision Anchor](https://api.decision-anchor.com) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/zse4321/decision-anchor-sdk) — External accountability proof before x402 payment execution. Records what was authorized, when, and at what scope. Non-judgmental.

---

## Agent Trust & Reputation

- [Revettr](https://revettr.com) [![A2A Ready](https://img.shields.io/badge/A2A-ready-8250DF?style=plastic)](https://revettr.com) — Counterparty risk scoring for x402 agentic commerce. Scores wallet addresses, domains, IPs, and companies 0-100 for payment safety.
- [MoltGuard](https://api.moltrust.ch/guard/) [![ERC-8004](https://img.shields.io/badge/ERC--8004-registered-E36209?style=plastic)](https://api.moltrust.ch) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/moltrust/moltguard) — Agent trust scoring (0-100), Sybil detection with funding cluster analysis, Polymarket integrity, Ed25519 Verifiable Credentials. 7 MCP tools. $0.005-$0.05 USDC on Base.
- [DJD AgentScore](https://github.com/djd-agent-score/djd-agent-score) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/djd-agent-score/djd-agent-score) — On-chain reputation scoring for AI agent wallets. 0-100 trust score across 5 dimensions (identity, behavior, reliability, viability, capability) from x402 settlement history on Base. Free tier.
- [ScoutScore](https://scoutscore.ai) — Trust scoring for x402 services (not agents). Monitors 1,700+ services with continuous health checks and fidelity probes.

---

## Compliance & Sanctions

- [CYBERA Compliance API](https://compliance-api-ruddy.vercel.app) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/tedddb-ai/compliance-api) [![MiCA](https://img.shields.io/badge/MiCA-aware-0550AE?style=plastic)](https://compliance-api-ruddy.vercel.app) — VASP address identification (20,468 addresses, 29 chains), risk scoring, sanctions/mixer screening. $0.01 USDC on Base.
- [SENTINEL](https://mru-oracle.com) [![Open Source](https://img.shields.io/badge/Open_Source-2EA44F?style=plastic)](https://github.com/INJprotocol/mauritius-oracle-) — AML/CFT compliance intelligence. 77K+ sanctions entities (OFAC, UN, EU, PEP, Interpol, World Bank, crypto watchlists), 159-country jurisdiction risk scoring. MCP server at `/mcp`. $0.001-$0.015 USDC on Base.

---

## Bug Bounty Programs

- [Coinbase Bug Bounty](https://hackerone.com/coinbase) — Report x402 vulnerabilities for rewards up to $50,000.
- [Immunefi x402 Program](https://immunefi.com) — Decentralized bug bounty platform with x402 listings.
