# ResolveAI Canada — Build & Launch Plan
### Vibe-coding the consumer-complaint engine, with a plan built for its transactional revenue shape

*Prepared August 2026. Companion to the BillShield plan — assumes the same stack, method, and two-founder rhythm; this document covers what's different. Rated 19/25: highest pain evidence of the five, weakest revenue shape. The plan below is designed around that weakness, not in denial of it.*

---

## 0. What we're building, in one paragraph

An AI consumer-dispute engine for Canadians: describe what happened, upload the paper trail, and get an eligibility assessment, an evidence checklist, a properly-structured complaint package, and deadline tracking. Module #1 is air travel (the CTA had 84,000+ backlogged complaints and quotes 24-month waits — people are desperate for anything that makes their file undeniable). Module #2 is telecom (CCTS complaints at record highs). **The core design truth: nobody has a dispute every month.** Revenue is transactional ($19–39 per package), so the business is an SEO-and-conversion machine, not a retention machine — and every decision below follows from that.

**Scope discipline:**

| Build now | Build later (month 4+) | Never |
|---|---|---|
| Airline module (APPR-based): eligibility screen, evidence checklist, complaint package | Telecom module (CCTS process) | Representing users or filing on their behalf |
| Deadline tracker + response analyzer ("upload the airline's reply") | E-commerce non-delivery, warranty modules | Contingency-fee recovery (that's a collections business with trust-account problems) |
| One-off Stripe checkout ($19/$39) | $9.99/mo case-tracking membership | "AI lawyer" positioning, in any wording, anywhere |
| Free eligibility checker (the funnel) | Family protection plan | Guaranteeing outcomes |

---

## 1. The build plan — what's different from BillShield

**Same foundation:** Next.js + Supabase (ca-central) + Stripe + Claude API + PostHog, spec-first vertical slices, human review gates on PII and money. If BillShield is built first, the document-extraction and account layers are reused wholesale — this is the second front-end on the shared engine.

**The idea-specific core asset: a cited rules engine, not a chatbot.** Encode the Air Passenger Protection Regulations as explicit, versioned rules (airline size, disruption category, notice period, delay length → entitlement band), every output carrying a citation to the authoritative source. Build the **scenario eval suite** before the app: 40–60 hand-labelled real disruption scenarios (from friends, Reddit threads, CTA decisions) with the correct eligibility answer. Every prompt or rules change runs against it. Wrong eligibility answers are this product's version of BillShield's misread bill — the failure mode you instrument from day one.

**The UPL guardrail, stated once and enforced everywhere:** this is *consumer information and document preparation*, never advice. "Based on what you've entered, APPR section X may apply — here is a complaint package to send" — never "you will win" or "you should sue." High-complexity inputs (injury, big losses) get routed to "this needs a professional." Same line the landlord OS walks; same discipline.

**Deadline math is tested code, not LLM output.** Response windows and escalation timelines are deterministic functions with unit tests. The LLM writes prose; the calendar is arithmetic.

## 2. Timeline — 12 weeks, with revenue arriving earlier than BillShield's

Transactional pricing means the first dollar can arrive in week 8, not month 4.

| Phase | Weeks | Deliverable | Definition of done |
|---|---|---|---|
| **Validate** | 0–1 | Free eligibility-checker landing page | 200 completions of a 6-question flight-disruption quiz. Disruption anger is searchable and constant; if a free checker can't pull 200 users in 2 weeks, the funnel thesis is wrong — diagnose before building. |
| **Rules core** | 2–4 | APPR rules engine + scenario eval suite | ≥95% correct eligibility banding on the eval suite. This gate is absolute. |
| **Package builder** | 5–7 | Upload evidence → checklist → generated complaint package (PDF) | A real disrupted passenger produces a send-ready package in under 20 minutes. |
| **Monetize** | 8 | Stripe one-off checkout: $19 standard / $39 escalation pack | **First paying customer.** Free checker → paid package conversion instrumented from the first day. |
| **Deepen** | 9–10 | Response analyzer + deadline tracker + email nudges | User uploads the airline's rejection; product compares it against their evidence and drafts the escalation. This is the "wow" feature — prioritize it over breadth. |
| **Launch** | 11–12 | SEO pages live + PFC/travel-community launch | 30 published route/scenario pages; first organic paid conversions. |
| **Module 2** | Months 4–6 | Telecom (CCTS) module | Only after airline module hits 50 paid packages/month — breadth before depth is how this idea dies. |

**Milestone math:** at ~$29 average, $4,000/month ≈ 138 packages ≈ 4–5 per day. That volume comes from search traffic, which compounds slowly: expect month 8–12, with spikes around travel-chaos events (storms, strikes) that you must be pre-positioned to catch.

## 3. Marketing — an SEO machine with a newsjacking reflex

**Positioning:** *"Make your complaint impossible to ignore."* Not "get revenge," not "AI lawyer" — the file-quality angle is both the honest value and the legally safe one.

- **Channel 1 — Long-tail disruption SEO (the business itself).** "WestJet cancelled flight compensation," "Air Canada delayed baggage claim," "flight delayed 4 hours what am I owed Canada" — per-airline, per-scenario pages, each embedding the free eligibility checker. This intent is evergreen, high-emotion, and weakly served. 2–3 pages/week forever; the Dubai founder owns the calendar.
- **Channel 2 — Newsjacking weather and strikes.** Every winter storm, IT outage, and labour dispute creates thousands of simultaneous searchers. Pre-write the templates ("Toronto snowstorm cancellations: your rights") and publish within hours of an event. A single well-timed event page can outperform a quarter of regular content.
- **Channel 3 — Reddit + travel communities.** r/PersonalFinanceCanada, r/travel, r/canada threads after every disruption event are full of "what am I owed?" questions. Same rules as BillShield's PFC play: months of genuinely helpful, cited answers before any product mention.
- **Channel 4 — Short-form "know your rights" video.** The genre already performs enormously on TikTok. "Your flight was cancelled — here's what the airline hopes you don't know" with real APPR numbers. Every video ends at the free checker.
- **Email is the repeat-purchase engine.** One dispute per customer per year means the list is the asset: everyone who uses the free checker gets seasonal "flying this winter? know your rights" emails. The membership upsell ($9.99/mo tracking + family plan) comes later, only if the data says people want it.

## 4. Metrics, targets, and kill criteria

| Metric | Target | Why |
|---|---|---|
| Free checker → paid package conversion | 5–10% | The whole funnel in one number; below 2% the packaging or pricing is wrong. |
| Eligibility accuracy (eval suite) | ≥95%, always | Wrong answers here are existential. |
| Paid packages/month | 50 by month 5, 138+ by month 9–12 | The $4K line. |
| Organic traffic growth | +25%/month through month 6 | The compounding engine; if it stalls, everything stalls. |
| Refund rate | <5% | High refunds mean packages aren't landing — quality signal. |

**Kill / pivot criteria:** fewer than 100 total paid packages by month 6, or conversion stuck under 2% despite pricing tests → the willingness-to-pay thesis failed; keep the SEO asset (it retargets perfectly into BillShield) and stop building. **Secondary trigger:** if the CTA meaningfully automates its own intake and clears the backlog, the airline module's urgency fades — that's the signal to lead with telecom instead.

---

*One-sentence version: encode the APPR as tested, cited rules; charge per package from week 8; treat SEO pages and storm-day newsjacking as the actual product; and judge the business on checker-to-package conversion, not signups.*
