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

## What credibility / licensing you actually need — and what it realistically costs

**The blunt headline first: neither idea requires a licence to operate.** Canada does not license software companies. There is no permit for "landlord software" or "trades software," no regulator you apply to, no exam you sit. What you actually need splits into three layers: (1) basic corporate hygiene both ideas share, (2) liability engineering specific to #1, and (3) trust engineering specific to #2. None of it is a wall; all of it is a speed bump with a price tag — itemized below. But note the flip side: no licensing barrier for you means no licensing barrier for competitors either. Permission is not the moat in either business. Correctness and distribution are.

### Layer 1 — The shared foundation (both ideas, do this once)

| Item | Realistic cost | Notes |
|---|---|---|
| Incorporation | ~$200 federal (online) or ~$300 Ontario, one-time | Incorporate from day one — both ideas carry liability you do not want on your personal names. Add ~$300–700/yr for an accountant to file the corporate return. |
| GST/HST registration | Free | Mandatory once you pass $30K revenue in four quarters; register early anyway so invoices look established. |
| Tech E&O + cyber insurance | [$500–2,500/yr in Canada](https://getcertain.ca/business/errors-omissions/) | The single most important credibility purchase either idea makes. Priced by revenue, so it starts cheap and scales with you. |
| Terms of service + privacy policy | $500–2,000 one-time (lawyer-reviewed) | PIPEDA compliance itself costs nothing to "acquire" — it's a set of obligations (consent, safeguards, breach reporting), not a registration. |
| Trademark | ~$480/class via CIPO, deferrable | Skip at launch; file when the name has proven it's worth keeping. |

**Foundation total: roughly $1,500–4,000 in year one.** That's the entire regulatory cost of existing as a credible Canadian software company.

### Layer 2 — Idea #1's real spend: liability engineering, not licensing

- **The legal line you must not cross, precisely stated:** under Ontario's Law Society Act, *providing legal services* — advice or representation — requires a lawyer or [licensed paralegal](https://www.runsensible.com/blog/paralegals-authorized-ontario/) (LTB representation is squarely paralegal scope). *Self-help document assembly* with clear disclaimers is the established carve-out that LawDepot and every will-kit in the country operates in. Your product must live on the document-assembly side of that line in its wording everywhere: "this tool prepares forms based on your inputs; review before serving" — never "you should evict" or "we recommend."
- **One-time template and wording review by a paralegal or landlord-tenant lawyer: ~$1,500–4,000.** This is the closest thing to a "licence" Idea #1 has, and it's the best money in the whole plan. It buys three things at once: correctness of the N4/N5/N12 logic, a professional opinion that your framing stays on the right side of the LSO line, and a name you can put on the website — which is also your single biggest credibility asset with landlords.
- **Ongoing rule-tracking: ~$200–500 per legislative update** if you pay the same professional to re-verify when forms or guidelines change (roughly annually). Cheap insurance for the risk that actually kills you.
- **E&O at the higher end of the band (~$1,500–3,000/yr)** and make sure the policy explicitly covers the document-generation function — say what the product does when applying; a claim denied for misrepresentation is worse than no policy.
- **Two things to explicitly NOT acquire:** do not become a consumer reporting agency (Ontario's Consumer Reporting Act registration plus credit-bureau vetting is heavy, slow, and built for bigger companies — integrate SingleKey/Certn as a partner API instead, $0 licensing, revenue share), and do not touch rent money (holding or transmitting funds walks you toward FINTRAC money-services registration — let payments stay landlord-to-tenant, or use Stripe if you ever add them).

**Idea #1 realistic total: ~$4,000–8,000 in year one** on top of the foundation-level basics it shares. Hard? No — it's two professional engagements and an insurance policy. The difficulty isn't acquiring any of it; it's the *discipline* of keeping every pixel of the product on the self-help side of the line as you grow.

### Layer 3 — Idea #2's real spend: trust engineering, not licensing

- **Genuinely zero licences.** Trades are licensed; software for trades is not. Displaying and calculating GST/HST correctly is arithmetic, not tax advice. There is no regulator between you and launch.
- **Payments: let Stripe carry the regulatory weight.** Stripe Connect makes Stripe the regulated money-transmitter; onboarding is a KYB check measured in days, and costs you nothing but the per-transaction fees. The one rule: never custody funds yourself — money flows homeowner → contractor with you as the platform, or you've walked into FINTRAC territory no two-person team wants.
- **The actual credibility spend is social, not regulatory.** Trades buy from people vouched for by other trades. The budget that matters: local construction/home-builders' association membership ($200–1,000/yr — puts a recognizable logo on your site and you in the room), a table at one regional trade show ($500–2,000), and the unpaid-but-expensive currency of showing up in trade Facebook groups helpfully for months before selling anything. Insurance at the standard band ($500–1,500/yr) since nothing you ship creates legal exposure.

**Idea #2 realistic total: ~$1,500–4,000 in year one, mostly overlapping the shared foundation.** The "licensing" chapter of this idea is one page long; the trust chapter never ends.

### The honest comparison

Idea #1's credibility stack costs roughly twice as much and involves lawyers, but every dollar buys something durable: reviewed templates and a professional's name are assets competitors must also pay for. Idea #2's stack is nearly free, which is exactly the problem — it's nearly free for everyone else too. In both cases the realistic all-in regulatory-and-credibility budget for year one is **under $10,000 combined**, which means this layer should never be the reason to hesitate. The expensive part of both businesses was never the permission. It's the eighteen months of consistency after you have it.

---

## Verdict

Neither risk profile is disqualifying; they're just different bets. **#1 is the better business with the scarier failure mode** — a real gap, proven willingness to pay, and a defensible provincial moat, purchased by accepting legal-correctness liability that must be engineered and insured against from day one, not patched in later. **#2 is the safer product with the harder business** — nothing you ship can void someone's eviction case, but you're grinding out thin-margin subscriptions in a market where the incumbent can nuke your positioning at will. If you run the portfolio sequence from the main document, the honest implication is: start #1 *because* its risks are front-loaded and controllable (lawyer review, insurance, Ontario-only scope), and treat #2 as the follow-on you enter only once free-channel distribution has been proven to work — because #2 without a working zero-cost acquisition machine is just an unfunded price war.
