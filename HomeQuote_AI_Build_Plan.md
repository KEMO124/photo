# HomeQuote AI Canada — Build & Launch Plan
### Vibe-coding the contractor-quote decision room, built for a once-a-decade customer

*Prepared August 2026. Companion to the BillShield plan — same stack, method, and founder rhythm; this covers what's different. Rated 16/25 (lowest of the five): the easiest sale on the list — $49 against a $40,000 decision — attached to the worst usage frequency (people renovate every 5–10 years) in a category crowding fast. The plan accepts the frequency problem and designs the whole business around surviving it.*

---

## 0. What we're building, in one paragraph

A homeowner uploads two or three contractor quotes for the same renovation. The product normalizes them into one honest comparison table — what each quote actually *includes* — then flags the risk patterns: vague allowances, missing scope (who pays for disposal? permits?), oversized deposits, absent warranty language, change-order traps, and payment schedules that front-load risk onto the homeowner. It ends with the exact questions to ask each contractor. The customer is about to sign the biggest cheque of their year; $49 for clarity is the easiest yes across all five ideas. The hard part is that they won't need you again for years — so the model is transactional revenue plus a **Renovation Decision Room** that keeps them for the 3–12 month project, and an acquisition engine built on referral partners who face this question weekly even though each homeowner faces it rarely.

**Scope discipline:**

| Build now | Build later (month 4+) | Never |
|---|---|---|
| Multi-quote upload → normalized comparison table | Renovation Decision Room: change-order log, payment tracker, receipt vault, progress photos | Recommending specific contractors (destroys neutrality — neutrality *is* the product) |
| Red-flag engine (allowances, deposits, scope gaps, warranty, payment terms) | Milestone payment-schedule generator | Contractor marketplace / lead-gen (two-sided trap, and a conflict of interest) |
| Question-arsenal per contractor | Ontario consumer-protection info layer (cooling-off, deposit norms — cited, not advised) | Estimating what a renovation *should* cost from scratch (you're auditing quotes, not replacing quantity surveyors) |
| One-off Stripe checkout: $49/project (covers up to 3 quotes) | Second project type packs (roofing, windows, bathroom, kitchen) | Legal or engineering advice of any kind |

---

## 1. The build plan — what's different from BillShield

**Same foundation, same reused extraction engine** — contractor quotes are the messiest documents in the whole portfolio (Word docs, photographed napkin math, 14-page PDFs), which is exactly why normalizing them is worth $49.

**1. The scope taxonomy is the product.** Build a canonical checklist per project type — demolition, structural, electrical, plumbing, fixtures, finishes, disposal, permits, cleanup, warranty, payment terms — starting with the two highest-volume types only (kitchens and bathrooms). Every quote gets mapped against the taxonomy: *included / excluded / allowance / unclear*. "Unclear" is the money finding — it's the word that starts the right conversation with the contractor. Resist project-type breadth until the engine is excellent on two.

**2. The red-flag library is curated judgment, encoded.** Deposit size vs. Ontario norms, allowance vagueness ("$4,000 fixtures allowance" with no spec), missing change-order process, no lien-holdback awareness, payment schedules ahead of work completed. Each flag carries plain-language "why this matters" text reviewed once by a construction-savvy advisor (find one — a retired PM or estimator will review your library for a few hundred dollars and their name adds instant credibility).

**3. Eval suite: 25 real quote sets.** Harder to collect than bills — source from renovation Facebook groups, family, and by *offering free audits during validation* (every free audit is both training data and a testimonial). Gate releases on extraction + taxonomy-mapping accuracy, same discipline as every other product in the portfolio.

## 2. Timeline — 12 weeks, revenue by week 8, spring surge as the real launch

Renovation demand peaks March–June. A fall/winter build hits the market exactly when planning season starts (people plan in February, sign in April).

| Phase | Weeks | Deliverable | Definition of done |
|---|---|---|---|
| **Validate** | 0–1 | "Send us your renovation quotes, get a free comparison" concierge offer | 15 real quote sets audited *manually* (founders do it by hand, AI-assisted). This validates willingness-to-pay AND builds the eval suite simultaneously — the manual audits are the spec. |
| **Extraction + taxonomy** | 2–5 | Upload → normalized comparison table (kitchens + bathrooms) | ≥85% correct inclusion/exclusion mapping on the eval suite (quotes are messier than bills; 85% + human-review flag beats fake 95%). |
| **Red-flag engine** | 6–7 | Flags + question arsenal + advisor-reviewed language | A homeowner reads the report and books follow-up conversations with contractors — measured in beta. |
| **Monetize** | 8 | Stripe one-off: $49/project; free tier = 1 quote, basic table | **First paying customer.** Free-to-paid instrumented from day one. |
| **Polish + PDF** | 9–10 | Beautiful, shareable report (spouses and co-signers are the second reader) | ≥8/10 "would recommend to a friend renovating." |
| **Launch** | 11–12 | SEO base + partner outreach begins | 25 cost/red-flag pages live; 3 referral partners sending traffic. |
| **Decision Room** | Months 4–6 | Change-order log, payment tracker, vault ($9.99/mo during active project) | Build only if ≥30% of report buyers say they want ongoing tracking — otherwise stay transactional and cheap to run. |

**Milestone math:** $4,000/month ≈ 82 reports ≈ ~3/day — the *lowest* volume requirement of the five ideas, which partially offsets the frequency problem. Realistic: 20/month by month 5 through partners + early SEO, the $4K line by month 9–12 riding the spring surge.

## 3. Marketing — partners who face the question weekly, plus renovation-cost SEO

**Positioning:** *"Before you sign for $40,000, know what's actually in the quote."* Neutral auditor, contractor-friendly in tone — good contractors *benefit* when vague competitors get exposed, and some will voluntarily send clients ("get it audited, mine will hold up").

- **Channel 1 — Referral partners (the frequency fix).** The homeowner renovates once a decade, but realtors, home inspectors, mortgage brokers, and interior designers get asked "is this quote reasonable?" *every week*. A neutral $49 tool is an easy hand-off that makes them look good, with no conflict. Ten warm partners producing 2 referrals/week ≈ the entire month-5 target. This is founder-B's primary outbound motion from week 10.
- **Channel 2 — Renovation-cost SEO.** "Kitchen renovation cost Ontario 2027," "contractor deposit rules Ontario," "renovation quote red flags," "what should a bathroom reno include" — high-intent, Canada-specific, weakly served. 2 pages/week; every page embeds a "paste one quote, see the analysis" free taste.
- **Channel 3 — Facebook renovation and homeowner groups.** This demographic lives in local Facebook groups, not TikTok. Months of genuinely useful presence ("here's what an 'allowance' means and why it bites people"), then the free single-quote tool. Same never-astroturf rule as every other channel.
- **Channel 4 — Red-flag content as short-form/press.** Anonymized real-quote teardowns ("this $46K quote has no demolition line — someone's paying for that later") work as Reels and as pitchable consumer-protection stories; renovation-nightmare coverage is a perennial Canadian media beat.

## 4. Metrics, targets, and kill criteria

| Metric | Target | Why |
|---|---|---|
| Concierge validation conversions (weeks 0–1) | ≥5 of 15 free-audit users say they'd have paid $49 | Cheapest possible test of the entire thesis, before real code. |
| Free single-quote → paid full-report conversion | ≥10% | Intent is white-hot; below this the report isn't proving its value. |
| Paid reports/month | 20 by month 5; 82 (the $4K line) by month 9–12 | The honest volume path. |
| Active referral partners | 10 by month 6 | The channel that defeats the frequency problem. |
| "Would recommend" score | ≥8/10 | Each customer disappears for years — their referral is their LTV. |

**Kill / pivot criteria:** if the week-0 concierge test can't find 5 willing payers among 15 free audits, stop before building — that's the whole point of testing it manually first. Post-launch: under 60 total paid reports by month 6, or partners refusing to refer (the tell that neutrality/quality isn't landing) → fold the taxonomy and red-flag library into content, keep the SEO asset, and redeploy. **Standing competitive check:** this category is crowding (QuoteGuard et al.); if a funded player owns "renovation quote audit" search intent before you do, partners become the only channel — reassess honestly at that point.

---

*One-sentence version: validate with 15 hand-done audits before writing real code, charge $49 from week 8, solve the once-a-decade customer problem with partners who face the question weekly, and let the pre-agreed concierge test — not sunk cost — decide if this one gets built at all.*
