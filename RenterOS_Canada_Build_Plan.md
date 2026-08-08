# RenterOS Canada — Build & Launch Plan
### Vibe-coding the renter's operating system, designed around its one real weakness: renters don't pay

*Prepared August 2026. Companion to the BillShield plan — same stack, method, and founder rhythm; this covers what's different. Rated 17/25: huge market (≈5M renter households), real pain, weak willingness to pay. This plan treats RenterOS as a freemium audience machine monetized at high-stakes moments — and is honest that it may end up as the marketing front door for other products rather than a standalone business.*

---

## 0. What we're building, in one paragraph

A free-first toolkit for Canadian renters: scan your lease and understand it, build a timestamped move-in evidence vault, keep a maintenance paper trail, check a rent-increase notice against provincial rules, and generate a moving-out package. The free core must be genuinely excellent — the monetization happens at the three moments a renter's money is actually at stake: signing, a rent increase, and moving out (deposit/dispute time). Ontario first; the LTB's 88,000 applications a year is the proof of how much friction exists in these relationships.

**Scope discipline:**

| Build now | Build later (month 4+) | Never |
|---|---|---|
| Lease scanner (upload → plain-language breakdown, free, 1 lease) | Household sharing (roommates) | Landlord-side features (that's the other product) |
| Move-in evidence vault (photos, timestamps, auto-generated condition report) | Maintenance-dispute letter pack | Encouraging LTB filings — the tone is protection, not war |
| Rent-increase checker (Ontario guideline math + notice-period check) | BC/Alberta rule packs | Legal advice in any form; same document-assembly line as everything else |
| Moving-out package ($ one-off) + Renter+ $9.99/mo | Renewal negotiation scripts | Payment processing / rent collection |

---

## 1. The build plan — what's different from BillShield

**Same foundation and heavy reuse:** the lease scanner *is* the BillShield extraction engine pointed at a different document type. Supabase storage does the evidence vault. The genuinely new engineering is small: the condition-report generator (photos + labels → clean PDF), Ontario rule math, and mobile-first camera flows.

**The idea-specific core asset: the evidence vault UX.** Everything else can be adequate; the vault must be effortless — guided room-by-room photo capture on a phone, automatic timestamps and categorization, and a professional-looking move-in report PDF at the end. That PDF is also the growth mechanic: it's designed to be shown to landlords and roommates, with the product's name on the footer of every page.

**Eval suite:** 30 real leases (student housing, condo, purpose-built, basement apartment — the messy variety matters) hand-labelled for the scanner, plus a unit-tested rules module for Ontario guideline increases, notice periods, and deposit rules. The rent-increase checker's math must be flawless — it's the feature people screenshot.

**The wording guardrail:** outputs describe what rules *say*, with citations, and generate documents — they never advise ("your landlord is breaking the law") — identical discipline to the landlord OS and ResolveAI.

## 2. Timeline — 12 weeks, aimed at a hard seasonal deadline

**The calendar is the strategy here.** Student-rental signing runs roughly January–April; the mass move-in wave is September 1. Miss the wave and acquisition costs 5× more for eight months. Working backwards: **the product must be live and polished by early August.** If starting later, target the winter signing season instead and use the fall to build the content base.

| Phase | Weeks | Deliverable | Definition of done |
|---|---|---|---|
| **Validate** | 0–1 | "Upload your lease, get a plain-English breakdown" free tool + waitlist | 150 lease uploads. Western/Fanshawe housing groups make this cheap to test — the London founder is literally on-site in Canada's best beachhead campus market. |
| **Lease scanner** | 2–4 | Upload → extraction → readable breakdown | ≥90% field accuracy on the 30-lease eval suite. |
| **Evidence vault** | 5–7 | Guided move-in capture + condition report PDF | A first-time renter completes a full move-in capture in under 15 minutes on a phone. |
| **Money moments** | 8–9 | Rent-increase checker + moving-out package + Stripe | Free: scanner + basic vault. One-offs: moving-out package $14.99. Renter+ $9.99/mo: unlimited docs, full vault, letters. |
| **Beta** | 10 | 50 student renters through the full flow | ≥50% complete a vault; qualitative "would you tell your roommate" ≥8/10. |
| **Launch** | 11–12 | Campus + TikTok + SEO launch, timed to the season | 1,000 free users in the first month of the wave. |
| **Deepen** | Months 4–6 | Roommate sharing, dispute letter pack, BC rules | Only what churn/usage data demands. |

**Milestone math, stated honestly:** at $9.99 with a realistic **1–3%** free-to-paid conversion (renters convert worse than homeowners), $4,000 MRR needs ~400 paying from a free base of **15,000–40,000 users**. That's a year-plus of seasonal compounding, not a quarter. The one-off moving-out package will likely outearn the subscription early — watch the data and follow it.

## 3. Marketing — campus-out, season-timed

**Positioning:** *"Never lose money to a landlord again."* Protection and receipts, not conflict.

- **Channel 1 — The campus beachhead (the unfair advantage).** Western + Fanshawe: housing Facebook groups, res-life instagram, student unions, off-campus housing offices (they *want* move-in documentation tools to recommend — a genuinely free, good tool gets institutional distribution for nothing). Posters in student-housing neighbourhoods in August with a QR code. Win London completely before spending a dollar anywhere else; then the playbook replicates campus by campus.
- **Channel 2 — TikTok/Reels move-in content.** "5 things to photograph before you move in," "what this lease clause actually means," "my landlord kept my deposit — here's what beat him: timestamps." September move-in content is a guaranteed annual demand spike; build the library in July–August.
- **Channel 3 — SEO on renter-rights intent.** "Ontario rent increase 2027 maximum," "landlord entry rules Ontario," "N4 received what do I do" (renter side), "moving out checklist Ontario." Steady 2/week; compounds into the product's long-term moat as campus growth saturates.
- **Channel 4 — The condition-report PDF as viral object.** Every generated report is seen by a landlord and usually roommates. Make it beautiful; that's 2–4 impressions per user in exactly the right audience, free.

## 4. Metrics, targets, and kill criteria

| Metric | Target | Why |
|---|---|---|
| Free users (season 1) | 1,000 in first month, 5,000 by month 6 | The audience *is* the asset in a low-WTP market. |
| Vault completion rate | ≥50% of signups | The product's core habit; below this the UX isn't effortless enough. |
| Free → any-payment conversion | ≥2% within 6 months | The honesty gate on the whole thesis. |
| Moving-out package attach rate | ≥10% of users who move | The likeliest real revenue line. |
| Campus penetration (London) | Recognizable in Western housing groups by October | Beachhead proof before replication. |

**Kill / pivot criteria — decided now:** if by month 8 free adoption is strong but payment conversion sits under 1.5% despite pricing experiments, accept what the data says: **renters won't fund a standalone subscription.** Do not grind against it — RenterOS then becomes a deliberate audience asset (tens of thousands of young Canadians who trust you with financial documents feed BillShield directly, and the rules engine feeds the landlord OS). If *both* adoption and conversion are weak by month 6, sunset it cleanly. Either outcome recycles ~80% of the code.

---

*One-sentence version: win one campus completely with a genuinely free, genuinely excellent evidence vault timed to September 1, monetize only the three moments money is at stake, and let a 2% conversion threshold — not hope — decide whether this is a business or a brilliant funnel.*
