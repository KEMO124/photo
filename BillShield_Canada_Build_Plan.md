# BillShield Canada — Build & Launch Plan
### The proven way to vibe-code it, a realistic timeline, and the marketing engine that makes it work

*Prepared August 2026. Companion to "Opportunities in the Canadian Market" and the Risk Analysis. Assumes two founders (London ON + Dubai), limited capital, AI-first development.*

---

## 0. What we're building, in one paragraph

A Canadian bill-cutting app: users upload bills and statements (never bank logins at launch), AI extracts every recurring charge, the product finds money — expired promos, price creep, cheaper current plans, forgotten subscriptions — and hands the user a script to claw it back. The retention engine is the **savings ledger**: "You've paid us $156 this year. You've saved $843." The wedge is that Rocket Money doesn't serve Canada, and Canadian telecom billing is uniquely painful (record CCTS complaint volumes, ~$212/month per household on cell + internet alone).

**Scope discipline — decide this now and write it on the wall:**

| Build now | Build later (month 4+) | Never (or not until it's a real company) |
|---|---|---|
| Bill/PDF/screenshot upload + extraction | Email-forwarding ingestion (bills@ inbox) | Bank credential login (trust killer at launch) |
| Top-5 telecom carriers + streaming + common subscriptions | Utilities, insurance categories | Doing negotiations *for* users (ops-heavy) |
| Renewal alerts + price-change detection | Family plan / household sharing | Native mobile apps (PWA is enough) |
| Negotiation & cancellation script library | Open banking via Flinks (only after trust + revenue) | US expansion |
| Savings ledger | Chargeback/refund letter generator | Anything requiring a licence |

---

## 1. The build plan — how to vibe-code this properly

### 1.1 Stack: boring, proven, and maximally AI-legible

The single most important vibe-coding decision is choosing the stack the AI knows best. Exotic choices multiply hallucinated APIs and debugging time. This is the boring-and-correct set:

| Layer | Choice | Why |
|---|---|---|
| App | **Next.js + TypeScript + Tailwind + shadcn/ui** | The most heavily represented stack in AI training data; components AI generates correctly on the first pass. |
| DB / Auth / Storage | **Supabase (Postgres), ca-central region** | Auth, file storage, and row-level security out of the box; **Canadian data residency is a marketing feature** for a bills app, not just compliance. |
| Payments | **Stripe Billing** | Subscriptions, free trials, tax handling — solved problems. |
| AI extraction | **Claude API with structured outputs** | The core engine: bill PDF/image in → typed JSON out (provider, plan, price, promo expiry, line items). |
| Email | Resend or Postmark | Renewal alerts are a core feature, not an afterthought — deliverability matters. |
| Analytics | PostHog | Free tier, session replays, funnels — you need to *watch* early users struggle. |
| Hosting | Vercel + Supabase | ~$0–50/month until real traffic. Total infra burn pre-revenue: **under $100/month**. |

### 1.2 The method: spec-first, slice-by-slice, eval-guarded

This is the difference between "vibe coding" that ships and vibe coding that collapses at week 6:

1. **Write specs before prompts.** Keep a `/specs` folder in the repo: one markdown file per feature describing behaviour, edge cases, and what "done" means. Plus a `CLAUDE.md` with stack conventions. AI output quality tracks spec quality almost linearly — this is where the humans earn their keep.
2. **Build in vertical slices, not layers.** Each session ships one complete user-visible behaviour (e.g., "upload a Rogers bill → see extracted line items"), never "the whole backend first." Every slice ends deployed and clicked-through by a human.
3. **The extraction eval suite is your real IP — build it first.** Before writing app code, collect **30–50 real Canadian bills** (your own, family, friends — with consent, personal details redacted): Rogers, Bell, Telus, Fido, Freedom, Virgin, Vidéotron, plus streaming receipts. Hand-label the correct extraction for each. Every change to the extraction prompt runs against this suite and reports accuracy. This turns your scariest failure mode ("the app read my bill wrong") into a number you watch, and it's an asset no competitor gets without doing the same slow work.
4. **Two review gates AI code must pass a human for:** anything touching **auth/security/PII** and anything touching **money math** (the savings ledger must never overstate savings — it's your credibility engine). Everything else, review lightly and move fast.
5. **Tests only where lying hurts.** Skip UI test theatre. Hard tests on: extraction accuracy (the eval suite), savings calculations, renewal-date math, and Stripe webhook handling. That's the full list.
6. **One founder owns the codebase.** The Dubai/Canada split works if roles are clean: one of you is the engineer-of-record (all merges), the other owns marketing + the plan database (below). The 8-hour offset becomes an advantage: content ships in one timezone while code ships in the other — a near-24-hour operating cycle.

### 1.3 The plan database: the unglamorous moat

The savings engine needs to know what Canadians *should* be paying: current public offers from carriers, ISPs, and streaming services. There is no API for this — it's **manual weekly curation** (2–3 hrs/week, marketing founder owns it). This is simultaneously: (a) the data moat — it's why the product beats pasting a bill into ChatGPT, (b) the content engine — every update is a "best internet deals in Ontario this month" post, and (c) the thing incumbents won't bother maintaining for Canada. Structure it as a proper table (provider, plan, price, region, date-observed) from day one; it compounds.

---

## 2. Timeline — 12 weeks to revenue, honestly stated

Assumes both founders working consistently (evenings/weekends at student intensity, AI-accelerated). Pad by 50% if course load spikes.

| Phase | Weeks | Deliverable | Definition of done |
|---|---|---|---|
| **Validate** | 0–1 | Landing page + waitlist + bill collection | 100 waitlist signups; 30+ real bills collected for the eval suite. If you can't get 100 emails with a good landing page in 2 weeks, that is data — stop and diagnose before building. |
| **Core slice** | 2–5 | Auth → upload → extraction → subscription list | A stranger uploads a Rogers/Bell/Telus bill and sees correct line items ≥90% of the time (eval suite score). Manual-entry fallback for everything else. |
| **Money features** | 6–8 | Savings engine v1 + scripts + ledger + alerts | Promo-expiry and price-creep detection against the plan database; negotiation/cancellation script library (top 20 providers); renewal alerts firing reliably; savings ledger live. |
| **Monetize** | 9–10 | Stripe + free-tier limits + polish | Free: 3 bills + alerts. Plus $12.99/mo: unlimited + optimization + scripts. Annual option at ~2 months free (fights churn from day one). |
| **Private beta** | 10–11 | 50 waitlist users in, watched closely | ≥60% of beta users find one savings opportunity ≥$10/month ("aha" metric). Fix what session replays show. |
| **Launch** | 12 | Public launch sequence (Section 3.4) | First paying strangers. Target: 25 paying by end of month 3. |
| **Iterate** | Months 4–6 | Email ingestion, family plan, more categories | Driven by churn interviews, not roadmap fantasies. |
| **Scale bet** | Month 6+ | Open banking (Flinks) evaluation | Only if churn is <6%/month and users are asking for it. |

**Milestone math** (at $12.99/mo, with the free tier converting 3–5%): ~100 paying ≈ month 4–5 ≈ $1,300 MRR → ~308 paying ≈ $4,000 MRR, realistically month 8–12. Anyone promising $4K MRR in 90 days for a consumer app with no ad budget is selling something.

---

## 3. Marketing — the engine, ranked by expected return per dollar (mostly $0)

### 3.1 Positioning: pick the fight on purpose

**"Rocket Money doesn't work in Canada. We do."** — say it exactly that bluntly. "Rocket Money Canada" and "Rocket Money alternative Canada" are high-intent searches with no good answer; own them with a comparison page from week 1. Secondary frame: *"Your bill went up. You didn't agree to that. Get it back."* — anger at telecom price creep is the most universally shared Canadian financial emotion, and it's renewable.

### 3.2 The four channels, in priority order

**Channel 1 — SEO around cancellation and price-creep intent (compounding, free, starts week 1).**
Cancellation guides are the most underrated acquisition asset in this category: "how to cancel Sportsnet+," "how to cancel Goodlife membership," "cancel Bell internet without a fee" — massive monthly search volume, thin competition, perfect intent (a person cancelling subscriptions is your exact customer), and every guide ends with *"or upload your bill and let BillShield watch all of them."* Ship 2 guides/week forever (Dubai founder's daytime = Canada's night; content never blocks code). Add monthly data pages from the plan database: "Best internet deals in Ontario — August 2026."

**Channel 2 — Reddit r/PersonalFinanceCanada, played correctly (highest-trust channel, zero cost, easiest to burn).**
PFC's most beloved recurring genre is literally your product: "call Rogers, threaten to cancel, here's the script that got me $30/month off." The play is *months of genuine helpfulness* — answering telecom-bill threads with real scripts and current retention-offer intel from your plan database — before any launch post. When you do launch ("we built a free Canadian bill analyzer, roast it"), you're a known member, not a spammer. One good PFC reception is worth more than $5K of ads in this niche. Never astroturf; the sub detects it instantly and the damage is permanent.

**Channel 3 — Short-form video: the bill-reaction format (your age advantage).**
TikTok/Reels/Shorts: "POV: your Fido bill after the 12-month promo expires" / redacted-bill teardowns / "$843 saved" receipt screenshots / "3 subscriptions you forgot you're paying for." You're university students — you *are* the demographic and speak it natively; a 40-year-old fintech marketing team can't fake this. One founder posts 3–4/week; expect nothing for 6 weeks, then outlier videos drive signup spikes. Campus angle: students are broke and subscription-heavy — ambassador/referral pilots at Western and one UAE-expat-Canadian angle later.

**Channel 4 — Earned media via a data asset (quarterly, free, compounding credibility).**
Publish a quarterly **"Canadian Subscription & Bill Inflation Index"** from your plan database + anonymized user data: "average Canadian streaming stack now costs $67/month, up 14% YoY." Canadian outlets cover telecom/subscription pricing relentlessly (it's a proven beat — CBC, Global, BetterDwelling). One pickup = domain authority + a wave of signups. Costs nothing but the database you're already maintaining.

**Paid ads: not yet.** Only after 6 months of churn data proves LTV. The gate: predicted LTV ≥ 3× CAC. At $12.99/month and realistic consumer churn, that means CAC must land under ~$25–35 — achievable with retargeting warm traffic from channels 1–3, ruinous as cold-start strategy.

### 3.3 Referral, built in from day one
Give-a-month-get-a-month, and put the share moment where pride peaks: the savings ledger. "I saved $843 with BillShield" is a natural screenshot — make it beautiful, watermarked, one-tap shareable. That screenshot *is* the TikTok content flywheel feeding itself.

### 3.4 Launch sequence (week 12)
Day 1: waitlist email + PFC launch post (free-tool framing, ask for roasting). Day 2–3: TikTok launch video + respond to every PFC comment within the hour. Week 2: Product Hunt (secondary — US-skewed, but backlinks help SEO) + pitch 3 Canadian personal-finance newsletters. Ongoing: every user's first savings find is a prompted share moment.

---

## 4. Metrics, targets, and kill criteria

| Metric | Target | Why it's the one that matters |
|---|---|---|
| **North star: verified $ saved per active user/month** | ≥ 4× subscription price | The entire retention argument in one number. |
| Activation | First bill analyzed within 10 min of signup | Upload friction is the #1 product risk; watch replays weekly. |
| "Aha" rate | ≥60% of users find a ≥$10/mo saving in week 1 | Below this, the savings engine isn't good enough to charge for. |
| Free→paid conversion | 3–5% | Standard freemium band; below 2% means the free tier gives too much or the paid tier proves too little. |
| Monthly churn | <6% by month 6 | The whole business lives or dies here. Interview every single cancellation personally. |
| Extraction accuracy | ≥90% on eval suite, always | Ship nothing that regresses it. |

**Kill / pivot criteria — agree on these now, while you're calm:** if by **month 6** you have fewer than 50 paying customers, or churn holds above 10%/month for three consecutive months despite fixes, the honest conclusion is that Canadian consumers won't sustain this subscription — stop, take the extraction engine and audience, and redeploy them (the same document-intelligence core powers the landlord OS and every other idea on the shortlist). Deciding the exit test in advance is what separates a portfolio from a sunk-cost trap.

---

## 5. Operating rhythm for two founders, 8 time zones apart

- **Roles:** Founder A (Canada) — engineer-of-record, product, beta-user calls (they're in the market and the timezone). Founder B (Dubai) — marketing engine, plan database, content calendar, support inbox first-pass. Both — weekly strategy call, non-negotiable.
- **The relay cadence:** Canada ships code and goes to sleep → Dubai wakes, tests it, ships content, queues feedback → Canada wakes to a tested build and a task list. Run it deliberately and the 8-hour offset is a feature.
- **Weekly, forever:** eval suite run + accuracy number logged · plan database updated · 2 SEO pieces + 3 short videos shipped · every churned user interviewed · metrics reviewed against Section 4 on the strategy call.
- **First 14 days, concretely:** register the corp (~$200 federal, per the Risk Analysis doc) · Stripe + Supabase + domain · landing page live with waitlist · collect the 30 bills · write `CLAUDE.md` + first three specs · founder B starts the PFC helpfulness clock (it needs a 3-month head start on launch) · first two cancellation guides drafted.

---

*The one-sentence version of this whole plan: build the extraction eval suite and the plan database like they're the company (they are), ship a 12-week MVP on the most boring stack available, spend zero dollars on marketing and six months of consistency on SEO + Reddit + short-form instead, and let the savings ledger do the selling.*
