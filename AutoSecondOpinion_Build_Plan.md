# AutoSecondOpinion Canada — Build & Launch Plan
### Vibe-coding the repair-quote second opinion, with the liability rails welded on first

*Prepared August 2026. Companion to the BillShield plan — same stack, method, and founder rhythm; this covers what's different. Rated 17/25: excellent willingness to pay at the decision moment, but low usage frequency, emerging competition (Fixxr et al.), the sharpest "why not just ChatGPT?" exposure of the five, and real safety-liability stakes. The plan is built to defuse those four things specifically.*

---

## 0. What we're building, in one paragraph

Upload a mechanic's quote before you say yes to it. The product extracts every line item, explains each repair in plain language, flags vagueness and duplication, benchmarks labour hours and parts where reliable references exist, arms the customer with the exact questions to ask, and — the killer feature — runs a **repair-vs-replace decision model**: given this vehicle, this odometer, this quote, and Canadian market values, is fixing it still rational? Users are deciding on $800–$5,000 in the next 48 hours; $9.99–$19.99 against that decision is trivially easy to justify. What's hard is everything after the first purchase — so the plan optimizes for evergreen search acquisition and near-zero CAC, not retention fantasy.

**Scope discipline:**

| Build now | Build later (month 4+) | Never |
|---|---|---|
| Quote upload → line-item extraction + plain-language explanation | Vehicle Plan membership ($9.99/mo: records, maintenance schedule, recall alerts) | Definitive "you don't need this repair" statements — especially brakes, steering, structural |
| Question-arsenal generator ("ask why the labour is 4.5 hours") | Multi-quote comparison (two shops) | Diagnosing from sounds/symptoms (that's a mechanic's job) |
| Repair-vs-replace report ($19.99) | Regional labour-rate refinement | OBD hardware, marketplace, booking — scope traps all |
| Urgency *framing* with mandatory safety language | Winter-prep seasonal reports | Guaranteeing any price is "fair" |

---

## 1. The build plan — what's different from BillShield

**Same foundation, same reused extraction engine** — a repair quote is just another messy Canadian document. The new engineering is three things:

**1. The liability rails come first, as code — not as a disclaimer page.** A hard-coded category system: safety-critical systems (brakes, steering, suspension structure, airbags, tires) can never receive a "defer this" framing from any prompt path — outputs for those categories are template-constrained to "safety-related: confirm urgency with a licensed mechanic." Red-team this in the eval suite with adversarial cases. This single design decision is what makes the product insurable (tech E&O, disclosed accurately) and sleep-at-night shippable.

**2. The benchmark database is the anti-ChatGPT moat.** ChatGPT can explain what a control arm is; it does not know current shop labour rates in Ontario vs Alberta, Canadian parts pricing, or book hours for common jobs. Curate exactly that (published shop rates, parts retailer prices, book-hour references) — the same weekly-curation muscle as BillShield's plan database, owned by the marketing founder. Every report cites its benchmarks; being *visibly sourced* is the product's credibility and its differentiation in one move.

**3. The repair-vs-replace model is deterministic and shows its work.** Inputs: vehicle value band (Canadian Black Book-style references), quote total, loan balance, expected ownership horizon, forward maintenance expectation for that platform. Output: a transparent side-by-side with every assumption editable by the user. Tested arithmetic, not LLM vibes — this is the report people screenshot and share.

**Eval suite:** 40 real quotes (dealers, chains, independents — collect via friends/family and local Facebook groups) hand-labelled for extraction accuracy *and* correct safety-category routing. Both numbers gate every release.

## 2. Timeline — 12 weeks, transactional revenue by week 8

| Phase | Weeks | Deliverable | Definition of done |
|---|---|---|---|
| **Validate** | 0–1 | "Upload your repair quote, get a free plain-English breakdown" landing page | 100 quote uploads. Post in London/Ontario car and student groups; a free teardown of a scary quote is an easy ask. |
| **Extraction + explain** | 2–4 | Upload → line items → explanations + question arsenal | ≥90% extraction accuracy; 100% correct safety-category routing on the eval suite (this gate is absolute). |
| **Benchmarks** | 5–6 | Labour/parts reference layer, cited in reports | Every flagged line shows *why* ("book time for this job is typically 2.5–3.0h; this quote says 4.5h"). |
| **Monetize** | 7–8 | Stripe one-offs: $9.99 audit / $19.99 repair-vs-replace | **First paying customer.** Free tier keeps the basic breakdown; paid unlocks benchmarks + the decision report. |
| **The killer report** | 9–10 | Repair-vs-replace model, shareable PDF | A real user facing a $3K quote gets a decision they act on; ≥8/10 "would recommend." |
| **Launch** | 11–12 | SEO base + community launch | 30 model/repair-specific pages live; first organic paid reports. |
| **Deepen** | Months 4–6 | Vehicle Plan membership, second-quote comparison | Membership only if repeat-usage data supports it — don't force a subscription onto a transactional product. |

**Milestone math:** at ~$15 average, $4,000/month ≈ 267 reports ≈ 9/day — the highest volume requirement of the five ideas, which is why the SEO engine below is the actual business. Realistic path: 50 reports/month by month 5, the $4K line closer to month 10–14. Winter is the demand amplifier (battery, brakes, rust, tires) — be positioned before November.

## 3. Marketing — evergreen repair-intent SEO, plus the most meme-able content format of the five

**Positioning:** *"A second opinion before you spend $3,000."* Allied with good mechanics, adversarial to vague quotes — never "mechanics are scamming you" (it's false, it kills shop partnerships later, and the internet will punish it).

- **Channel 1 — Repair-cost SEO (the business).** "Wheel bearing replacement cost Canada," "is it worth fixing a 2015 Civic transmission," "[model] common problems and repair costs" — enormous, evergreen, transaction-adjacent intent that generic US content serves badly for Canadian prices. Every page embeds the free quote analyzer. 2–3 pages/week forever.
- **Channel 2 — Quote-teardown short-form video.** Redacted real quotes, reacted to line by line: "$4,800 at a dealership — let's see what's actually on here." It's the bill-reaction format with higher stakes and better drama. User-submitted quotes become an endless content pipeline (with consent), and every teardown recruits the next submissions.
- **Channel 3 — Reddit, carefully.** r/MechanicAdvice and r/Justrolledintotheshop are mechanic-run — be an honest, humble presence or stay out. r/PersonalFinanceCanada car-decision threads ("fix or replace?") are the better home: the repair-vs-replace framing is native there.
- **Channel 4 — Referral partners who get asked anyway.** Driving instructors, used-car inspectors, CAA-adjacent content creators, campus car clubs — people constantly asked "should I fix it?" who'd happily hand off a $9.99 tool.

## 4. Metrics, targets, and kill criteria

| Metric | Target | Why |
|---|---|---|
| Safety-routing accuracy (eval suite) | 100%, always | Non-negotiable; a single miss is the nightmare scenario. |
| Free analysis → paid report conversion | 8–12% | Higher than typical freemium because intent is white-hot at upload time. |
| Paid reports/month | 50 by month 5; 267 (the $4K line) by month 10–14 | Honest volume math. |
| Organic traffic growth | +25%/month through month 6 | The compounding engine. |
| Refund/complaint rate | <5% | Report quality signal. |

**Kill / pivot criteria:** under 150 total paid reports by month 6, or conversion stuck below 4% despite pricing tests → the ChatGPT-substitution thesis won the argument; keep the SEO asset and benchmark database (both retarget into BillShield's audience) and stop. **Standing competitive check:** if Fixxr or a funded player ships Canadian benchmarks properly, differentiation collapses to the repair-vs-replace report — reassess at that moment, not after six more months of denial.

---

*One-sentence version: weld the safety rails into the code before anything else, make the benchmark database the visible reason you beat a chatbot, charge per report from week 8, and let repair-cost SEO — not retention — carry a business whose customers only need you once a year.*
