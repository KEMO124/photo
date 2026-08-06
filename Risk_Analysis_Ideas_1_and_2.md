# Risk Analysis — Ideas #1 and #2
### An honest look at what can go wrong with the Small-Landlord OS and the Solo-Trades App

*Prepared August 2026. Companion to "Opportunities in the Canadian Market." This document deliberately argues against both ideas — if they survive this, they're worth building.*

---

## The one-paragraph honest summary

These two ideas have **opposite risk shapes**. Idea #1's risks are mostly **liability-shaped**: the market gap is real, but you're generating quasi-legal documents where a single wrong date can cost a customer months of rent — and one viral failure story can kill you in the exact communities you market in. Idea #2's risks are mostly **business-model-shaped**: nothing you ship can hurt anyone, but you're entering a crowded market on the weakest moat there is (price), against funded incumbents, with structurally high churn and thin unit economics. #1 has the higher ceiling and the sharper tail risk. #2 has the safer floor and the grindier climb.

---

## Idea #1 — Small-Landlord OS: the risks, ranked by how much they should scare you

**1. The correctness liability is existential, not cosmetic.** An N4 with a miscalculated termination date, a wrong rent figure, or an outdated form version gets dismissed at the LTB — after the landlord has waited through a hearing backlog measured in **months**. Your bug doesn't cost them $20/month; it costs them thousands in unrecovered rent and a restarted process. The original document called this a "reputation event." Be more honest: it's a potential lawsuit, and it will happen eventually at scale no matter how carefully you test, because tenancy edge cases (partial payments, verbal agreements, mid-month tenancies) are endless. **Mitigations that are non-negotiable, not optional:** a lawyer or paralegal reviews every template before launch; errors & omissions insurance from day one (real money — budget $1,500–3,000/yr); aggressive "review before serving / not legal advice" framing; Ontario only until the machine is proven.

**2. You may be closer to "practicing law" than is comfortable.** Static form-filling (LawDepot-style) is established self-help territory. But a workflow engine that says *"you can file the L1 on Thursday"* is edging from document assembly toward legal advice, and Ontario's rules on unauthorized practice are enforced by the Law Society. This probably lands on the right side of the line with careful wording — but "probably" deserves a few hundred dollars of actual legal advice before launch, not after a complaint.

**3. Your paid product is an incumbent's free feature.** SingleKey and FrontLobby make their margin on screening reports and credit tooling. If your workflow tool gets traction, the rational competitive response is for them to give away a version of it as lead generation for the products they actually monetize. You'd be competing against *free*, from brands the audience already trusts. Your only defences are speed, depth of provincial correctness (which is expensive for them to bother with), and locking in the ledger/tax-history data that makes switching annoying.

**4. The revenue is spikier than "recurring" suggests.** Landlord pain is event-driven: they sign up when a tenant stops paying and are tempted to cancel when it's resolved. Rent receipts, the ledger, and the T776 export exist precisely to convert crisis users into year-round users — but assume real-world churn will be worse than the SaaS averages you'd model, and push annual billing hard.

**5. The optics risk is real and personal.** A tool that streamlines eviction paperwork, launched during a housing crisis, with your names on it. Tenant-advocacy backlash, hostile press framing, and Reddit brigading are all plausible, and the same Facebook groups that can make you can amplify any failure story. Position relentlessly as compliance/paperwork software (receipts, guideline calculations, proper notice — things that *protect tenants too*), never as an eviction accelerator. Also note: you'll be holding tenants' personal data, which means PIPEDA obligations and breach liability sitting on a two-person team.

---

## Idea #2 — Solo-Trades App: the risks, ranked the same way

**1. Price is the weakest moat in software, and it's your whole wedge.** Jobber can launch a $19 "Lite" tier or a six-month promo any quarter it wants, and your differentiation evaporates overnight — they have the brand, the content team, and the capital to hold that price longer than you can hold your breath. Competing on price also selects for the most price-sensitive customers in the economy, who are also the quickest to cancel. The honest version of this idea's pitch is not "cheaper Jobber," it's "the only tool with genuinely correct Canadian tax handling and a five-minute learning curve" — price is the hook, not the moat.

**2. The unit economics are unforgiving.** At $19/month, a customer is worth roughly $380 of lifetime revenue if monthly churn runs ~5% — and SMB churn at this end of the market genuinely runs 3–7%/month, because solo trades businesses fail, go seasonal (landscaping and snow are half-year businesses), and downgrade to free tools when cash is tight. That LTV means your customer-acquisition cost must be near zero *forever*. Free-channel distribution isn't a nice-to-have in this plan; it is the plan, and if the SEO doesn't compound, there is no fallback that doesn't lose money.

**3. Support costs don't scale down to $19/month.** Trades customers are excellent bullshit detectors and terrible software users. They expect to call someone, the "my invoice didn't send" message arrives at 6:45am from a job site, and every hour of support is an hour not spent building or marketing — there are only two of you. Ruthless product simplicity is the only real mitigation: every feature you don't build is support you never do.

**4. Taking deposits puts you in the money flow.** The moment payments run through you (Stripe Connect), you inherit chargebacks, fraud flags, contractor account holds, and disputes between homeowners and tradespeople — home-services work is a chargeback-heavy category. This is the hidden operational iceberg of the idea; budget real time for it or launch with invoicing-only and add deposits once you understand the exposure.

**5. The feature treadmill erodes the wedge.** Your first fifty customers will ask for QuickBooks sync, GPS tracking, and a second user seat. Each "yes" makes you a worse, cheaper Jobber instead of a different product, and slowly rebuilds the complexity you were the escape from. Saying no — publicly, as a philosophy — is a survival skill here, not stubbornness.

---

## Risks they share (worth stating once, honestly)

- **Two-person concentration.** One burnout, one illness, one falling-out, and the company stops. Support + development + marketing is three jobs split two ways, indefinitely.
- **Vibe-coding cuts both ways.** AI-accelerated development is the enabler of the whole plan, but AI-generated code with light review is exactly how security holes ship — and both apps hold sensitive data (tenant PII in #1, payment flows in #2). Budget genuine review time for anything touching auth, money, or personal data.
- **The grind is measured in years.** Both are "small dollars from small customers" businesses: ~1,000 paying users before the revenue is meaningful. At realistic conversion rates that's 18–36 months of consistent execution, not a launch spike. The risk isn't that the ideas are wrong — it's that you stop at month seven, which is when most two-person teams quietly do.

---

## Verdict

Neither risk profile is disqualifying; they're just different bets. **#1 is the better business with the scarier failure mode** — a real gap, proven willingness to pay, and a defensible provincial moat, purchased by accepting legal-correctness liability that must be engineered and insured against from day one, not patched in later. **#2 is the safer product with the harder business** — nothing you ship can void someone's eviction case, but you're grinding out thin-margin subscriptions in a market where the incumbent can nuke your positioning at will. If you run the portfolio sequence from the main document, the honest implication is: start #1 *because* its risks are front-loaded and controllable (lawyer review, insurance, Ontario-only scope), and treat #2 as the follow-on you enter only once free-channel distribution has been proven to work — because #2 without a working zero-cost acquisition machine is just an unfunded price war.
