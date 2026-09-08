# The Global Agent Economy

Agent infrastructure and machine-payment rails by continent. Platforms, protocols, and payment networks — including the ones most English-language directories have never indexed.

**Continents with nothing under them are left standing on purpose.** An empty heading is a measurement: it says we have not reached that part of the map, rather than letting the gap go invisible. If you know a rail we are missing, open a PR.

---

> ★ **Featured — August 2026: [ONDC](https://ondc.org)**
> India's government-backed open commerce network: an operating, population-scale version of what open agent commerce is trying to become, built on a different foundation. If you study one non-Western rail, study this one.

> **gold-402 note:** This shelf exists because we checked and found our own map was drawn in one language.
>
> x402 is a US-governed rail: USDC, Base, dollar-denominated, crypto-native. It is not the only answer to machine-to-machine payment, and outside the West it is not the answer being used. China solved delegated agent authorization on existing rails. India solved it with regulated, human-signed mandates that agents execute inside a cap. Neither needed a blockchain, and both were running at scale while the x402 Foundation was weeks old.
>
> The entries below are the parts of that world we could actually reach and read. Several major surfaces we could not — Zhihu and NPCI disallow crawlers, and CSDN and DeepSeek's platform returned blocks. Alipay's agent-payment documentation, JavaScript-walled on the first pass, has since been read in full — including "AI收", its own HTTP-402 payment rail for agents. Where we haven't looked, we say so rather than leaving the gap invisible.
>
> One thing worth stating plainly: **x402 is also the only genuinely open rail we found anywhere.** China's ACT protocol claims openness and publishes no specification. India's rail is human-anchored by regulation, by design. That makes x402 regional — and uniquely permissionless. Both things are true.

---

## Asia

### China — Agent Platforms

- [Coze](https://www.coze.com) — ByteDance's agent-building platform ([coze.cn](https://www.coze.cn) for the domestic market). The one significant proprietary holdout on tooling standards — and it monetizes paid plugins *through* MCP rather than around it. Currently the only place we found anyone selling agent capabilities as a product.
- [Dify](https://dify.ai) — Open-source platform for production agentic workflows, Chinese-origin with broad international adoption. Self-hostable or cloud. [Docs](https://docs.dify.ai).
- [AgentScope](https://github.com/modelscope/agentscope) — Agent framework from the ModelScope team. Built around making agent runs observable and traceable rather than opaque.

### China — Model & Tool Hubs

- [ModelScope MCP Plaza](https://www.modelscope.cn/mcp) — Alibaba's MCP hub (魔搭社区), hosting free Streamable-HTTP servers for tools unreachable from Western registries: Amap, 12306 rail booking, DingTalk, Alipay subscription. Likely the largest MCP surface no English-language directory indexes.
- [Gitee AI](https://ai.gitee.com/docs/integrations/mcp) — MCP integration on China's dominant code-hosting platform. The Gitee ecosystem is substantially invisible from GitHub-centred tooling.
- [Zhipu Open Platform](https://open.bigmodel.cn) — GLM model API platform with an agent and tool layer.
- [Aliyun Bailian](https://www.aliyun.com/product/bailian) — Alibaba's model platform. MCP-compatible, with a free evaluation tier.
- [Baidu AI Cloud](https://ai.baidu.com) — Baidu's model and agent platform. Publishes official MCP servers, including Baidu Maps.

### China — Payment Rails

- [Alipay Open Platform](https://open.alipay.com) — Ant Group's developer platform, and the home of its agent-payment suite (AI订阅 / AI按量付费 / Agent支付). The mechanism is a one-time bounded authorization — the human approves scenario, amount, merchant, task and validity once, and re-enters only on a risk trigger. Structurally the same shape as AP2's mandate model, on a proprietary rail, and reportedly already at national scale. [Developer docs](https://opendocs.alipay.com).
- [WeChat Pay Open Platform](https://pay.weixin.qq.com) — Tencent's payment rail and merchant platform. Programmatic payment at a scale no crypto rail has approached.

### China — Developer Communities

- [Juejin /ai](https://juejin.cn/ai) — Active Chinese developer community channel for AI tooling. A working listening post for which harnesses and skills Chinese developers actually run day to day — including a solo-operator economics thread culture that will look familiar to anyone building alone.

### India — Open Commerce

- [ONDC](https://ondc.org) — Open Network for Digital Commerce, India's government-backed open commerce network. The closest thing anywhere to what x402 wants to become, built on a different foundation. [144 repositories on GitHub](https://github.com/ONDC-Official).
- [Beckn Protocol](https://github.com/ONDC-Official) — The open protocol underneath ONDC. Notable finding: its signing specification carries **no human-verification requirement**, which makes an agent buyer-app protocol-legal today — gated by network-registry onboarding rather than by the spec.

### India — Payment & Mandate Rails

- [NPCI / UPI](https://www.npci.org.in) — The National Payments Corporation of India operates UPI, the highest-volume real-time payment rail in the world. UPI AutoPay is the mechanism that matters for agents: a human signs a mandate once, and execution runs PIN-less inside regulated caps. *(NPCI disallows crawlers; listed from public regulatory sources rather than a site fetch.)*
- [Setu](https://setu.co) — Fintech APIs for UPI, Bharat Bill Pay, Account Aggregator and KYC. Documents auto-notify and auto-execute mandate loops in production — the practical form of programmatic Indian payment. [Docs](https://docs.setu.co).
- [Razorpay](https://razorpay.com) — One of India's largest payment processors, and among the first anywhere to ship an official MCP server. See [mcp-servers.md](mcp-servers.md) for the server itself.
- [Cashfree](https://www.cashfree.com) — Indian payments and payouts platform with a broad API surface.

### Korea

- [Kakao Developers](https://developers.kakao.com) — Developer platform for Korea's dominant messaging and payments ecosystem. Kakao Pay is a founding member of the x402 Foundation with, as of this writing, no shipped x402 surface — worth watching precisely because the commitment exists and the implementation doesn't yet.

## Europe

_Nothing listed yet._ SEPA instant payments, PSD2/PSD3 open banking and the digital euro pilots
are all rails an agent could ride; none is on this shelf because we have not read them properly.

## North America

_Nothing listed yet on this shelf._ x402 itself is a North American rail — USDC, Base,
dollar-denominated — and it is indexed across the other twelve shelves rather than here. What is
missing is everything *else* on this continent: Interac, ACH and RTP mandate rails, Mexico's SPEI.

## South America

_Nothing listed yet._ Brazil's Pix is the highest-volume instant rail in the hemisphere and has a
programmatic surface. It belongs here and we have not indexed it.

## Africa

_Nothing listed yet._ M-Pesa and the mobile-money rails across East and West Africa move machine
payments at scale on infrastructure that predates every protocol on this site.

## Oceania

_Nothing listed yet._ Australia's NPP and PayTo mandate rail is the obvious first entry.

---

_Compiled from a structured expedition run 2026-07-29 across ~450 surfaces in five regions, with blocked and unreachable sources recorded rather than omitted. Corrections and additions welcome — open a PR._
