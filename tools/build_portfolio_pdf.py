# -*- coding: utf-8 -*-
import html, os, io

FONTS = open('/tmp/claude-0/-home-user-photo/6fbe66dd-ce10-50e4-8a80-94a54949912d/scratchpad/fonts.css').read()

CSS = r"""
:root{
  --paper:#FFFFFF; --panel:#F2F5F1; --band:#E7EDE7;
  --ink:#111917; --soft:#414E4A; --faint:#77837D;
  --rule:#C9D2CA; --hair:#E0E6DF;
  --verd:#0F5C52; --verd-wash:#E3EDE9; --amber:#8A5A12; --amber-wash:#F1E8D8;
}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;background:#fff;}
body{
  font-family:"Source Serif 4",Georgia,serif; color:var(--ink);
  font-size:13.3px; line-height:1.54;
  -webkit-print-color-adjust:exact; print-color-adjust:exact;
}
h1,h2,h3,h4,.disp{font-family:Archivo,Arial,sans-serif;margin:0;}
.mono,.eyebrow,.chip,.lane-label,.rail dt,.rail dd,.code,.foot,.pg{font-family:"IBM Plex Mono",monospace;}

@page{size:8.5in 11in;margin:0;}
.sheet{
  width:8.5in;height:11in;position:relative;overflow:hidden;
  page-break-after:always;break-after:page;background:var(--paper);
}
.sheet:last-child{page-break-after:auto;break-after:auto;}
.pad{position:absolute;top:.60in;left:.72in;right:.72in;bottom:.62in;}
.foot{
  position:absolute;left:.72in;right:.72in;bottom:.34in;
  border-top:.5px solid var(--rule);padding-top:5px;
  display:flex;justify-content:space-between;align-items:baseline;
  font-size:8.4px;letter-spacing:.11em;color:var(--faint);text-transform:uppercase;
}
.pg{font-variant-numeric:tabular-nums;font-weight:500;color:var(--verd);}

/* ---------- cover ---------- */
.cover .pad{top:.72in;bottom:.72in;display:flex;flex-direction:column;}
.wordmark{display:flex;align-items:center;gap:9px;font-family:Archivo,sans-serif;
  font-weight:800;font-stretch:118%;font-size:14.5px;letter-spacing:.03em;}
.wordmark .glyph{width:11px;height:11px;background:var(--verd);transform:rotate(45deg);flex:none;}
.cover .stamp{font-family:"IBM Plex Mono",monospace;font-size:8px;letter-spacing:.13em;
  color:var(--faint);text-transform:uppercase;margin-top:4px;}
.cover-rule{height:2.5px;background:var(--verd);margin:26px 0 0;}
.cover h1{font-weight:800;font-stretch:110%;font-size:47px;line-height:1.02;
  letter-spacing:-.022em;margin-top:74px;max-width:9.2in;}
.cover h1 em{font-style:normal;color:var(--verd);}
.cover .lede{margin-top:26px;display:grid;grid-template-columns:1fr 1fr;gap:26px;max-width:6.9in;}
.cover .lede p{margin:0;font-size:12.4px;line-height:1.55;color:var(--soft);}
.cover-claim{margin-top:auto;padding-top:16px;border-top:2px solid var(--verd);max-width:6.5in;}
.cover-claim p{margin:0;font-family:Archivo,sans-serif;font-weight:500;font-stretch:104%;
  font-size:16.5px;line-height:1.42;letter-spacing:-.006em;color:var(--ink);}
.cover-claim p b{font-weight:700;color:var(--verd);}
.toc{margin-top:auto;}
.toc .eyebrow{font-size:8px;letter-spacing:.15em;text-transform:uppercase;color:var(--faint);
  display:block;padding-bottom:8px;border-bottom:1px solid var(--rule);}
.toc ol{list-style:none;margin:0;padding:0;}
.toc li{display:flex;align-items:baseline;gap:11px;padding:7.5px 0;border-bottom:.5px solid var(--hair);}
.toc .n{font-family:"IBM Plex Mono",monospace;font-size:9px;color:var(--verd);
  font-variant-numeric:tabular-nums;width:20px;flex:none;font-weight:500;}
.toc .t{font-family:Archivo,sans-serif;font-weight:600;font-size:12.6px;font-stretch:102%;}
.toc .d{flex:1;border-bottom:.5px dotted var(--rule);margin:0 6px 3px;}
.toc .p{font-family:"IBM Plex Mono",monospace;font-size:9.5px;color:var(--faint);
  font-variant-numeric:tabular-nums;}
.cover-foot{margin-top:22px;display:flex;justify-content:space-between;
  font-family:"IBM Plex Mono",monospace;font-size:8.4px;letter-spacing:.09em;
  color:var(--faint);text-transform:uppercase;border-top:1px solid var(--rule);padding-top:9px;}

/* ---------- generic page head ---------- */
.phead{display:flex;justify-content:space-between;align-items:baseline;
  border-bottom:1px solid var(--rule);padding-bottom:6px;margin-bottom:26px;}
.phead .l{font-family:Archivo,sans-serif;font-weight:700;font-size:9.5px;
  letter-spacing:.14em;text-transform:uppercase;}
.phead .r{font-family:"IBM Plex Mono",monospace;font-size:8px;letter-spacing:.12em;
  color:var(--faint);text-transform:uppercase;}

/* ---------- principles / process ---------- */
h2.big{font-weight:800;font-stretch:110%;font-size:29px;line-height:1.06;letter-spacing:-.017em;}
.intro{font-size:13.6px;color:var(--soft);max-width:5.9in;margin-top:12px;}
.prin{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:34px;}
.prin .bar{width:26px;height:2.5px;background:var(--verd);margin-bottom:11px;}
.prin h3{font-size:13.5px;font-weight:700;font-stretch:105%;margin-bottom:5px;}
.prin p{margin:0;font-size:12.2px;color:var(--soft);line-height:1.5;}
.steps{list-style:none;counter-reset:s;margin:26px 0 0;padding:0;
  display:grid;grid-template-columns:repeat(5,1fr);gap:18px;}
.steps li{counter-increment:s;border-top:1px solid var(--rule);padding-top:10px;}
.steps li::before{content:counter(s,decimal-leading-zero);display:block;
  font-family:"IBM Plex Mono",monospace;font-size:9px;color:var(--verd);
  font-weight:600;margin-bottom:7px;font-variant-numeric:tabular-nums;}
.steps h4{font-family:Archivo,sans-serif;font-size:12px;font-weight:700;margin:0 0 4px;font-stretch:104%;}
.steps p{margin:0;font-size:11.2px;color:var(--soft);line-height:1.45;}
.sect-lab{font-family:"IBM Plex Mono",monospace;font-size:8.5px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--faint);display:block;margin-bottom:9px;}
.divider{height:1px;background:var(--rule);margin:48px 0 40px;}

/* ---------- case pages ---------- */
.grid{display:grid;grid-template-columns:1.52in 5.22in;gap:.32in;}
.rail .code{font-family:"IBM Plex Mono",monospace;font-size:9.5px;letter-spacing:.11em;
  color:var(--verd);font-weight:600;display:block;margin-bottom:14px;}
.rail dl{margin:0;border-top:1px solid var(--hair);}
.rail dt{font-size:7.4px;letter-spacing:.13em;text-transform:uppercase;color:var(--faint);margin-top:10px;}
.rail dd{margin:1px 0 9px;font-size:9.4px;line-height:1.45;color:var(--soft);}
.case h2{font-weight:800;font-stretch:110%;font-size:30px;line-height:1.05;
  letter-spacing:-.018em;margin-bottom:7px;}
.case .sub{color:var(--verd);font-family:Archivo,sans-serif;font-weight:600;
  font-size:12.8px;line-height:1.35;margin:0 0 22px;}
h3.lab{font-family:"IBM Plex Mono",monospace;font-size:8.5px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--faint);font-weight:600;margin:0 0 8px;}
.case p{margin:0 0 11px;}
.case p:last-child{margin-bottom:0;}
.gap{margin-top:22px;}
ul.build{list-style:none;margin:0;padding:0;}
ul.build li{padding:8.5px 0 8.5px 19px;border-bottom:.5px solid var(--hair);
  position:relative;font-size:12.3px;line-height:1.47;}
ul.build li:first-child{border-top:.5px solid var(--hair);}
ul.build li::before{content:"";position:absolute;left:1px;top:15px;width:7px;height:1.2px;background:var(--verd);}
ul.build strong{font-family:Archivo,sans-serif;font-weight:700;font-size:11.8px;font-stretch:104%;}

/* flow */
.flow{background:var(--panel);border:.5px solid var(--rule);padding:15px 17px 16px;}
.lane + .lane{margin-top:14px;padding-top:14px;border-top:.5px dashed var(--rule);}
.lane-label{font-size:7.6px;letter-spacing:.15em;text-transform:uppercase;
  font-weight:600;display:block;margin-bottom:8px;}
.lane--before .lane-label{color:var(--amber);}
.lane--after .lane-label{color:var(--verd);}
.chain{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;align-items:center;gap:5px 2px;}
.chain li{display:flex;align-items:center;gap:2px;}
.chip{font-family:"IBM Plex Mono",monospace;font-size:8.6px;line-height:1.3;
  padding:4px 7px;border:.5px solid var(--rule);display:inline-block;background:#fff;}
.lane--before .chip{border-style:dashed;border-color:var(--amber);background:var(--amber-wash);}
.lane--after .chip{border-color:var(--verd);background:var(--verd-wash);}
.chain li:not(:last-child)::after{content:"\2192";font-family:"IBM Plex Mono",monospace;
  font-size:9px;color:var(--faint);padding:0 2px;}
.lane--after .chain li:not(:last-child)::after{color:var(--verd);}
.flow figcaption{font-family:"IBM Plex Mono",monospace;font-size:8.8px;color:var(--faint);
  margin-top:12px;line-height:1.55;}

.outcome{border-left:2.5px solid var(--verd);padding:2px 0 2px 15px;margin-top:6px;}

/* ---------- flagship ---------- */
.fl-banner{display:flex;gap:12px;align-items:center;margin-bottom:14px;}
.tag{font-family:"IBM Plex Mono",monospace;font-size:8px;letter-spacing:.14em;
  text-transform:uppercase;color:#fff;background:var(--verd);padding:3px 8px;font-weight:600;}
.fl h2{font-weight:800;font-stretch:113%;font-size:34px;line-height:1.04;letter-spacing:-.02em;}
.fl .sub{color:var(--verd);font-family:Archivo,sans-serif;font-weight:600;font-size:13.4px;margin:9px 0 0;max-width:6in;}
.fl-body{max-width:6.1in;margin-top:20px;}
.fl-body p{margin:0 0 11px;}
.modules{display:grid;grid-template-columns:1fr 1fr;gap:20px 30px;margin-top:22px;}
.module{border-top:1.8px solid var(--verd);padding-top:10px;}
.module h4{font-family:Archivo,sans-serif;font-size:12.4px;font-weight:700;margin:0 0 4px;font-stretch:104%;}
.module p{margin:0;font-size:11.6px;color:var(--soft);line-height:1.48;}

/* ---------- closing ---------- */
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:14px;}
.chips span{font-family:"IBM Plex Mono",monospace;font-size:9.4px;padding:5px 8px;
  border:.5px solid var(--rule);color:var(--soft);}
.cta{border:1.5px solid var(--verd);background:var(--verd-wash);padding:30px 32px;margin-top:34px;}
.cta h2{font-weight:800;font-stretch:110%;font-size:25px;line-height:1.08;letter-spacing:-.015em;max-width:6in;}
.cta p{margin:11px 0 0;color:var(--soft);font-size:13px;max-width:5.5in;}
.contact{display:flex;gap:34px;margin-top:22px;padding-top:16px;border-top:1px solid rgba(15,92,82,.3);}
.contact div{font-family:"IBM Plex Mono",monospace;font-size:10px;line-height:1.7;color:var(--soft);}
.contact b{display:block;font-size:7.6px;letter-spacing:.13em;text-transform:uppercase;
  color:var(--verd);font-weight:600;margin-bottom:3px;}
.ask{margin-top:34px;}
.ask ol{list-style:none;counter-reset:a;margin:14px 0 0;padding:0;
  display:grid;grid-template-columns:repeat(3,1fr);gap:22px;}
.ask li{counter-increment:a;border-top:1px solid var(--rule);padding-top:10px;}
.ask li::before{content:counter(a,decimal-leading-zero);display:block;
  font-family:"IBM Plex Mono",monospace;font-size:9px;color:var(--verd);font-weight:600;
  margin-bottom:6px;font-variant-numeric:tabular-nums;}
.ask h4{font-family:Archivo,sans-serif;font-size:12px;font-weight:700;margin:0 0 4px;font-stretch:104%;}
.ask p{margin:0;font-size:11.4px;color:var(--soft);line-height:1.47;}
.endmark{margin-top:auto;display:flex;align-items:center;gap:9px;
  font-family:"IBM Plex Mono",monospace;font-size:8.4px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--faint);}
.close .pad{display:flex;flex-direction:column;}
.case-page .pad{display:flex;flex-direction:column;}
.case-page .grid{flex:1;min-height:0;}
.case-page .col{display:flex;flex-direction:column;}
.case p.contd{margin-top:auto;padding-top:9px;border-top:.5px solid var(--hair);
  font-family:"IBM Plex Mono",monospace;font-size:8.2px;letter-spacing:.13em;
  text-transform:uppercase;color:var(--faint);margin-bottom:0;}
.case p.contd b{color:var(--verd);font-weight:500;}
"""

MEASURE = r"""
<script>
(function(){
  function run(){
    var out=[];
    document.querySelectorAll('.sheet').forEach(function(s,i){
      var pad=s.querySelector('.pad');
      var pr=pad.getBoundingClientRect(), bot=pr.top;
      pad.querySelectorAll('*').forEach(function(el){
        var r=el.getBoundingClientRect();
        if(r.height>0 && r.bottom>bot && getComputedStyle(el).position!=='absolute') bot=r.bottom;
      });
      out.push((i+1)+':'+Math.round(bot-pr.top)+'/'+Math.round(pr.height));
    });
    var d=document.createElement('div');
    d.id='MEASUREMENTS';
    d.textContent='OVERFLOW '+out.join(' ');
    document.body.appendChild(d);
  }
  if(document.fonts && document.fonts.ready){document.fonts.ready.then(run);}else{run();}
})();
</script>
"""

def e(s):
    return s

# ---------------------------------------------------------------- content
SERVICES = [
 dict(
  n="01", anchor="sales-orders",
  title="Sales Order Automation",
  sub="Orders that arrive as documents, entered as data — without anyone retyping them.",
  rail=[("Discipline","Order-to-cash operations"),
        ("Intake","Email, PDF, WhatsApp, customer portals, spreadsheets"),
        ("Writes to","ERP / accounting system of record"),
        ("Human role","Approves exceptions only")],
  situation=[
   "Orders reached the client in every format a customer felt like using: a PDF purchase order attached to an email, a photo of a signed order form on WhatsApp, a line item scribbled in the body of a message, a spreadsheet export from a larger buyer’s procurement system. Every one of them ended the same way — a person opening the ERP and typing it in by hand.",
   "That created three costs the business felt but could not isolate. Orders sat unentered for hours or overnight, so stock was allocated late and shipments slipped a day. Typos in SKUs and quantities produced wrong shipments, credit notes and returns that cost far more than the original order was worth. And every peak season meant hiring temporary help just to keep up with data entry, because the process scaled with headcount and nothing else."],
  build=[
   ("A single intake layer.","One monitored inbox, plus WhatsApp and portal connections, so every incoming order lands in one queue regardless of how the customer chose to send it."),
   ("Document understanding.","AI extraction reads PDFs, scans, photos and message text into structured line items — customer, product, quantity, requested date, delivery address, reference number."),
   ("Catalogue matching that learns.","Customers describe products in their own words, not the client’s SKUs. The system matches free-text descriptions against the real catalogue and remembers each customer’s aliases, so “12mm ply, 8x4, B grade” resolves to the correct part every time after the first."),
   ("Validation before anything is written.","Price checked against the contracted tier, quantity against minimum order and pack size, availability against live stock, and the account against credit limit and unpaid balance."),
   ("Write-back into the system of record.","Clean orders are created directly in the ERP, with the original document attached to the order so the source is always one click away."),
   ("An exception desk.","Anything ambiguous — a discontinued item, a price mismatch, an unreadable scan, an over-limit account — is routed to a person with the source document and the system’s best interpretation side by side, for a one-click confirm or correct.")],
  before=["PO arrives","Sits in inbox","Staff reads it","Looks up SKUs","Checks price list","Types into ERP","Errors found at picking"],
  after=["PO arrives","Parsed &amp; matched","Priced &amp; credit-checked","Order created in ERP","Exceptions only → human"],
  caption="Seven manual steps become one automated path with a single human checkpoint, reached only when the order is genuinely unclear.",
  changed=[
   "Orders now enter the system in minutes from arrival instead of waiting for someone to get to them, which pulls the entire picking, packing and invoicing chain forward — the business gets paid sooner on the same sales.",
   "Errors that used to surface in the warehouse now surface at intake, where fixing them costs a click instead of a return shipment. And because the workload no longer scales with headcount, the client absorbs seasonal peaks with the same team, while the people who used to key in orders spend that time on customers instead."],
  split=4),

 dict(
  n="02", anchor="quotations",
  title="Quotation Automation",
  sub="Same-day quotes, priced by the rules the business actually agreed to.",
  rail=[("Discipline","Pre-sales &amp; pricing"),
        ("Intake","RFQ emails, web forms, spec sheets"),
        ("Encodes","Cost build-up, margin &amp; discount rules"),
        ("Output","Branded quote, approval trail, follow-up")],
  situation=[
   "Quoting was the client’s slowest and most valuable process at the same time. A request for quote came in, and someone senior had to dig through supplier cost sheets, look up what this customer paid last time, apply a discount from memory, work out freight, build the document, and send it. It took days when they were busy — and buyers who wait days often buy from whoever answered first.",
   "Worse, the margin discipline lived in one or two people’s heads. Different staff quoted the same job at different prices. Discounts got granted that nobody had authorised. Quotes went out and then sat, unfollowed, until they quietly expired, and no one could say what the win rate actually was or which quotes were lost on price."],
  build=[
   ("RFQ parsing.","Incoming requests — email text, attached spec sheets, drawings and bills of materials — are read into a structured list of what is being asked for, with quantities and specifications."),
   ("Automatic cost build-up.","Each line is priced from live supplier and internal cost data, with freight, currency conversion, packaging and any surcharge logic applied rather than estimated."),
   ("The pricing rules, written down.","Volume breaks, customer tiers, contract pricing, minimum margins and approved discount ranges are encoded once, so every quote from every person applies the same policy."),
   ("Guardrail approvals.","A quote inside policy goes out immediately. Anything below the margin floor or outside the discount band routes to a manager with the numbers and the reason it was flagged."),
   ("Generated documents.","A branded, correctly formatted quotation is produced automatically — line items, terms, validity period, reference number — ready to send or e-sign."),
   ("Acceptance and follow-up.","Open quotes get automatic reminders on a schedule, and an accepted quote converts straight into a sales order without re-entry.")],
  before=["RFQ received","Wait for the estimator","Hunt cost sheets","Margin from memory","Build doc by hand","Send &amp; forget"],
  after=["RFQ parsed","Costed from live data","Rules applied","Quote generated","Approval if outside policy","Auto follow-up → order"],
  caption="Pricing policy moves out of individual memory and into the system, where it is applied identically on every quote and logged on every exception.",
  changed=[
   "The client now answers most quote requests the same day they arrive, which in a competitive bid is frequently the whole difference. Margin stopped leaking through informal discounting, because every price below the floor requires a decision by someone entitled to make it — and that decision is recorded.",
   "Nothing expires unnoticed: open quotes chase themselves, and accepted ones become orders without a second round of typing. For the first time the business can see, by customer and by product line, what it quotes, what it wins, and what it loses."],
  split=4),

 dict(
  n="03", anchor="database-ai",
  title="Database AI Integration",
  sub="The business asks a question in plain language. The database answers it, and shows its working.",
  rail=[("Discipline","Data access &amp; reporting"),
        ("Sits over","ERP tables, SQL databases, warehouses, spreadsheets"),
        ("Access model","Read-only, permission-scoped"),
        ("Guarantee","Every answer shows its query")],
  situation=[
   "The client’s operational history — every order, product, customer, movement and invoice — sat in their database, and almost nobody could reach it. Answering “which customers ordered less this quarter than last?” meant asking the one person who could write a query, or exporting to a spreadsheet and pivoting by hand. Requests queued behind that person. Reports that took an hour to build got built once and then went stale.",
   "So decisions got made on instinct and on whatever the standard monthly report happened to show. The data existed, was accurate, and was effectively unavailable to the people whose decisions depended on it."],
  build=[
   ("A semantic layer in the company’s own vocabulary.","We mapped the terms the business actually uses — “active customer”, “net margin”, “overdue”, “slow-moving” — onto the real tables and columns, with the definitions agreed once and applied consistently everywhere."),
   ("Natural-language querying with hard limits.","Questions are translated into SQL against that model, executed read-only, and bounded by row limits and timeouts. The system cannot write, delete or alter anything."),
   ("Permission-aware answers.","Access follows the person asking. A sales rep sees their own accounts; a manager sees the region; payroll and cost data stay behind their existing permissions."),
   ("Answers that show the query.","Every result displays the SQL that produced it and the rows it came from. Numbers are never generated by the model — they are returned by the database, and anyone can verify how."),
   ("Charts and exports on demand.","Results render as tables or charts and drop into a spreadsheet or a slide without a rebuild."),
   ("Scheduled watchlists.","Recurring questions run themselves — Monday’s slow-moving stock, this week’s customers trending down, anything overdue past terms — and arrive by email or chat before someone has to think to ask.")],
  before=["Question arises","Ask the one technical person","Wait in the queue","CSV export","Pivot in Excel","Answer, days later"],
  after=["Question asked in plain English","Query built on the semantic model","Read-only execution","Answer + the SQL behind it"],
  caption="The bottleneck was never the data. It was the single person who could translate a business question into a query.",
  changed=[
   "Questions that used to take days now take a sentence, so people ask far more of them — and follow-up questions, which is where the useful findings usually live. The business stopped depending on one individual for access to its own records.",
   "Because every answer carries its query, the numbers are trusted enough to act on and correctable when a definition turns out to be wrong. And the scheduled watchlists changed the posture from asking after the fact to being told early: slow stock, slipping accounts and overdue balances now surface while there is still time to act on them."],
  split=4),

 dict(
  n="04", anchor="quality-lab",
  title="Quality Lab Automation",
  sub="From sample intake to signed certificate, with the paper trail built in rather than reconstructed.",
  rail=[("Discipline","QA / QC laboratory operations"),
        ("Captures","Instrument output, technician entry, batch records"),
        ("Produces","Certificates of analysis, NCR workflow, trends"),
        ("Built for","Audit &amp; traceability requirements")],
  situation=[
   "The lab ran on printouts and spreadsheets. Samples were logged in a book, instrument results came off the machine on thermal paper and were transcribed into Excel by hand, spec limits were checked by eye against a laminated sheet, and certificates of analysis were typed up individually and emailed out. Batches waited on that paperwork before they could be released.",
   "Two risks sat inside that. Transcription is where quality records fail — a decimal in the wrong place on a hand-typed result is a serious problem on a document a customer relies on. And traceability existed only in the physical files, so preparing for an audit or a customer complaint meant a person spending days pulling folders to reconstruct what happened to one batch six months ago."],
  build=[
   ("Sample intake with identity attached.","Every sample is registered on arrival, given a barcoded label, and linked to its batch, product, supplier and the test plan that applies to it — with custody recorded at each handoff."),
   ("Instrument capture instead of transcription.","Results are read directly from instrument output files and interfaces, so the number on the certificate is the number the instrument produced. Manual entry, where an instrument cannot be connected, is double-checked and attributed."),
   ("Specification checking on every result.","Each measurement is compared automatically against the correct spec for that product and grade, and flagged pass, warning or out-of-specification the moment it lands."),
   ("Certificates generated, not typed.","A complete certificate of analysis is produced from the verified results, formatted to the customer’s requirements, with method references and the analyst on record."),
   ("Non-conformance handled as a workflow.","An out-of-spec result raises a non-conformance, notifies the right people immediately, holds the batch, and tracks investigation, disposition and sign-off to closure."),
   ("Trending and early warning.","Results are charted over time by product, line, shift and supplier, so drift toward a limit is visible while it is still drift — before it becomes a failed batch."),
   ("An audit trail that assembles itself.","Raw results, revisions, approvals and timestamps are retained and immutable. Any batch’s full history is retrievable on demand.")],
  before=["Sample logged in a book","Instrument printout","Typed into Excel","Checked by eye","COA typed by hand","Batch waits for paperwork","Audit = days of folders"],
  after=["Barcoded intake","Instrument result captured","Auto spec check","COA generated","Out-of-spec → NCR + hold","Audit trail on demand"],
  caption="Transcription is removed from the one place it does the most damage: the record a customer, a regulator and a recall investigation all rely on.",
  changed=[
   "Batches are released as soon as the testing is genuinely finished rather than when the paperwork catches up, which frees warehouse space and shortens lead times to customers. The most likely source of an incorrect quality record — a human copying a number — is gone from the routine path.",
   "Out-of-spec results now stop a batch automatically instead of relying on someone noticing, and the escalation is on record from the first minute. And audits changed character entirely: evidence that used to take a week of preparation is produced from the system while the auditor is sitting there."],
  split=4),

 dict(
  n="05", anchor="social",
  title="Social Media Automation",
  sub="A consistent presence, drafted in the business’s own voice and tied to what it is actually selling.",
  rail=[("Discipline","Marketing operations"),
        ("Sources","Product data, promotions, seasonality, past posts"),
        ("Channels","Instagram, Facebook, LinkedIn, TikTok, X"),
        ("Human role","Approves the calendar, not each post")],
  situation=[
   "The client knew social media mattered and treated it as whatever was left at the end of the week. Posting came in bursts — three in a good week, nothing for a month — because it depended on someone with an operational job finding time to think of something to say, write it, find an image and post it across four platforms individually.",
   "The bigger loss was on the way back in. Comments and direct messages included real buying questions — price, availability, delivery — and they went unanswered for days because nobody owned the inbox. Enquiries that arrived warm went cold in a notifications tab."],
  build=[
   ("A voice model built from their own approved posts.","Drafts come out sounding like the business rather than like generic marketing copy, with the vocabulary, claims and tone the owner already signed off on."),
   ("A calendar driven by real events.","The content plan is generated from things that are actually happening — new stock arriving, a promotion, a seasonal peak, a completed project — instead of from a blank page every Monday."),
   ("Assets assembled with the copy.","Product photography, past project images and templated graphics are matched to each draft and sized correctly per platform."),
   ("One approval step.","The week’s queue arrives for review in a single pass. Approve, edit or reject; nothing publishes without that sign-off."),
   ("Publishing across channels.","Approved posts go out automatically at scheduled times to every connected platform, in the right format for each."),
   ("Inbound triage.","Comments and DMs are classified as sales enquiry, support issue, spam or general engagement. Sales enquiries alert the right person immediately with a drafted reply; routine questions get a suggested response; spam is filtered."),
   ("A weekly report that feeds back.","What reached people, what converted to enquiries, and what did not — used to shape the next calendar rather than filed and forgotten.")],
  before=["Someone finds time","Thinks of a post","Writes it","Finds an image","Posts to each platform","DMs go unread"],
  after=["Calendar from real events","Drafts in brand voice","One weekly approval","Auto-published everywhere","Enquiries routed same hour"],
  caption="The owner still decides what the business says. They stop being the bottleneck for producing and distributing it.",
  changed=[
   "Posting became consistent, which is most of what performance on these platforms rewards — and it stopped competing with operational work for the same person’s attention, since a week of content is now reviewed in one sitting.",
   "The content also stopped being generic: because the calendar is driven by stock and promotions, posts point at things customers can actually buy this week. Most valuably, inbound enquiries are answered in the hour rather than the week, so interest that used to evaporate now reaches a salesperson while it is still live."],
  split=4),
]

MODULES = [
 ("Document ingestion &amp; extraction","Receipts, invoices, statements and slips arrive as photographs, scans and PDFs and come out as structured, categorised financial records — including the messy, unstructured expense documents that automated feeds and government pre-fill services cannot supply."),
 ("Deterministic rules engine","Every calculation runs through a versioned, unit-tested rules engine tied to a specific tax year. Rules are readable, testable and independently verifiable — the requirement that any certification or professional review will impose anyway."),
 ("Audit &amp; anomaly checking","The engine reviews a completed position the way a reviewer would: figures inconsistent with each other, claims outside normal ranges for the profile, duplicate entries, categories that invite scrutiny, and documents that should exist but do not."),
 ("Deduction &amp; credit detection","Extracted records are tested against every credit and deduction the profile is eligible for, so items that only surface when someone reviews the whole picture — rather than one form at a time — get caught."),
 ("Explanations with citations","Each figure comes with a plain-language explanation and a reference to the rule behind it. Users are told why, not just how much — which is what converts a calculated number into one a person is willing to sign."),
 ("Full provenance trail","Every number traces back to the source document, the extraction, the rule version and the timestamp. If a figure is ever questioned, the entire chain that produced it can be reconstructed."),
 ("Forward-looking planning","The same engine runs before the year closes, not just after: liability forecasting and scenario modelling, delivered while there is still time to act rather than as a report on decisions already made."),
 ("Compliance-grade platform","Multi-tenant architecture with per-tenant isolation, role-based access, encryption in transit and at rest, regional data residency, and no raw financial documents sent to third-party model providers without zero-retention terms."),
]

TOC = [("01","Sales Order Automation",3),("02","Quotation Automation",5),
       ("03","Database AI Integration",7),("04","Quality Lab Automation",9),
       ("05","Social Media Automation",11),("06","AI Tax Auditing Engine — our own SaaS",13)]

# ---------------------------------------------------------------- builders
sheets = []

def foot(label):
    return ('<div class="foot"><span>Onyx Automate &middot; Selected Work</span>'
            '<span>%s</span><span class="pg">%%PG%%</span></div>') % label

def sheet(cls, inner, label):
    sheets.append('<section class="sheet %s"><div class="pad">%s</div>%s</section>'
                  % (cls, inner, foot(label)))

def rail(n, pairs, cont=False):
    code = "SVC / %s%s" % (n, "" if not cont else "  ·  CONT.")
    dl = "".join("<dt>%s</dt><dd>%s</dd>" % (k, v) for k, v in pairs)
    return '<aside class="rail"><span class="code">%s</span><dl>%s</dl></aside>' % (code, dl)

def chain(items):
    return "".join("<li><span class=\"chip\">%s</span></li>" % i for i in items)

def flow(s):
    return ('<figure class="flow">'
            '<div class="lane lane--before"><span class="lane-label">Before</span>'
            '<ol class="chain">%s</ol></div>'
            '<div class="lane lane--after"><span class="lane-label">After</span>'
            '<ol class="chain">%s</ol></div>'
            '<figcaption>%s</figcaption></figure>'
            % (chain(s["before"]), chain(s["after"]), s["caption"]))

def builditems(items):
    return "".join("<li><strong>%s</strong> %s</li>" % (a, b) for a, b in items)

# --- 1. cover
toc_html = "".join(
    '<li><span class="n">%s</span><span class="t">%s</span>'
    '<span class="d"></span><span class="p">%02d</span></li>' % (n, t, p)
    for n, t, p in TOC)
cover = """
<div class="wordmark"><span class="glyph"></span>ONYX AUTOMATE</div>
<div class="stamp">Operations &amp; AI systems</div>
<div class="cover-rule"></div>
<h1>We take the work that eats your week and hand it back <em>done.</em></h1>
<div class="lede">
  <p>Most small businesses do not lose time to hard problems. They lose it to the same twenty minutes repeated forty times a day — retyping an order that arrived as a PDF, rebuilding a quote from a price list, copying a lab result into a certificate, chasing a number that lives in a database nobody can query.</p>
  <p>We build the systems that absorb that work: intake, decision rules, the write-back into whatever software you already run, and a clean exception path for the cases a person genuinely needs to see. Inside is what we have built, and what changed for the people who run it.</p>
</div>
<div class="cover-claim">
  <p><b>Five automation systems running in client operations. One AI SaaS platform of our own.</b> Every one of them built on the same principle: the machine does the repetition, a person keeps the judgment.</p>
</div>
<div class="toc">
  <span class="eyebrow">Selected work</span>
  <ol>%s</ol>
  <div class="cover-foot"><span>How we build &middot; page 02</span><span>Working with us &middot; page 15</span></div>
</div>
""" % toc_html
sheets.append('<section class="sheet cover"><div class="pad">%s</div></section>' % cover)

# --- 2. principles + process
p2 = """
<div class="phead"><span class="l">How we build</span><span class="r">Onyx Automate</span></div>
<span class="sect-lab">Operating principles</span>
<h2 class="big">Three rules we do not break, because they are what make automation safe to trust.</h2>
<div class="prin">
  <div><div class="bar"></div><h3>Rules decide. AI reads.</h3>
  <p>The AI extracts, matches and explains. Prices, tax, spec limits and eligibility are computed by deterministic rules you can read and test. Nothing critical is left to a model’s guess.</p></div>
  <div><div class="bar"></div><h3>Exceptions go to humans.</h3>
  <p>Automation handles the ninety percent that is routine and routes the rest to a person with the source document beside it. Your team stops doing data entry and starts doing judgment.</p></div>
  <div><div class="bar"></div><h3>Everything leaves a trace.</h3>
  <p>Every automated action records what it saw, what rule it applied and what it wrote. When an auditor, a customer or your accountant asks why, the answer is one click away.</p></div>
</div>
<div class="divider"></div>
<span class="sect-lab">How an engagement runs</span>
<h2 class="big">We start with one workflow, not a transformation programme.</h2>
<ol class="steps">
  <li><h4>Walk the process</h4><p>We sit with the people doing the work and map what actually happens, including the workarounds nobody documented.</p></li>
  <li><h4>Pick the one that pays</h4><p>We rank candidates by hours consumed, error cost and how contained the change is, then start with a single workflow.</p></li>
  <li><h4>Build against reality</h4><p>We build on your real documents and your real edge cases, integrating with the software you already run rather than replacing it.</p></li>
  <li><h4>Run in parallel</h4><p>The automation runs beside the manual process until its output matches, so nothing is trusted before it has earned it.</p></li>
  <li><h4>Hand over</h4><p>Your team gets documentation, the exception desk and control of the rules — plus monitoring and support from us as volumes grow.</p></li>
</ol>
"""
sheet("", p2, "How we build")

# --- services
for s in SERVICES:
    sp = s["split"]
    a = """
<div class="phead"><span class="l">%s &nbsp;/&nbsp; %s</span><span class="r">Selected work</span></div>
<div class="grid case">
  %s
  <div class="col">
    <h2>%s</h2>
    <p class="sub">%s</p>
    <h3 class="lab">The situation</h3>
    %s
    <h3 class="lab gap">What we built</h3>
    <ul class="build">%s</ul>
    <p class="contd">Continued overleaf <b>&rarr;</b></p>
  </div>
</div>""" % (s["n"], s["title"], rail(s["n"], s["rail"]), s["title"], s["sub"],
             "".join("<p>%s</p>" % p for p in s["situation"]),
             builditems(s["build"][:sp]))
    sheet("case-page", a, s["title"])

    b = """
<div class="phead"><span class="l">%s &nbsp;/&nbsp; %s</span><span class="r">Continued</span></div>
<div class="grid case">
  %s
  <div>
    <h3 class="lab">What we built <span style="color:var(--rule)">/</span> continued</h3>
    <ul class="build">%s</ul>
    <h3 class="lab gap">The workflow, before and after</h3>
    %s
    <h3 class="lab gap">What it changed</h3>
    <div class="outcome">%s</div>
  </div>
</div>""" % (s["n"], s["title"], rail(s["n"], s["rail"], cont=True),
             builditems(s["build"][sp:]), flow(s),
             "".join("<p>%s</p>" % p for p in s["changed"]))
    sheet("case-page", b, s["title"])

# --- taxos A
mods = ['<div class="module"><h4>%s</h4><p>%s</p></div>' % m for m in MODULES]
t1 = """
<div class="phead"><span class="l">06 &nbsp;/&nbsp; AI Tax Auditing Engine</span><span class="r">Our own product</span></div>
<div class="fl">
  <div class="fl-banner"><span class="tag">Our own product</span>
    <span class="r" style="font-family:'IBM Plex Mono',monospace;font-size:8px;letter-spacing:.13em;text-transform:uppercase;color:var(--faint)">SVC / 06 &middot; AI SaaS engineering</span></div>
  <h2>AI Tax Auditing &amp;<br>Optimisation Engine</h2>
  <p class="sub">A multi-tenant SaaS platform that reads financial documents, audits a return against the rules, and explains every number it produces.</p>
  <div class="fl-body">
    <p>Client automation shows we can make an existing operation faster. This shows we can build and run a regulated software product end to end — because we built one for ourselves, in the least forgiving domain we could have chosen.</p>
    <p>Tax is unforgiving for a specific reason: a confident wrong answer is worse than no answer. That constraint shaped the architecture, and the architecture is the part worth showing a prospective client. <strong>The AI never does the arithmetic.</strong> A deterministic, testable rules engine computes every figure — eligibility, thresholds, limits, liability. The AI does what it is genuinely reliable at: reading messy documents, matching them to the right treatment, spotting what is missing or inconsistent, and explaining the result in plain language with a citation to the provision it relied on.</p>
    <p>That same split — deterministic where it must be right, AI where it must be flexible — is exactly how we build automation for operating businesses. Tax is simply the version where the consequences of getting it wrong are written into law.</p>
  </div>
  <h3 class="lab gap">What the engine does</h3>
  <div class="modules" style="margin-top:10px">%s</div>
</div>""" % ("".join(mods[:4]))
sheet("", t1, "AI Tax Auditing Engine")

t2 = """
<div class="phead"><span class="l">06 &nbsp;/&nbsp; AI Tax Auditing Engine</span><span class="r">Continued</span></div>
<div class="fl">
  <h3 class="lab">What the engine does <span style="color:var(--rule)">/</span> continued</h3>
  <div class="modules" style="margin-top:10px">%s</div>
  <div class="divider"></div>
  <span class="sect-lab">Why this matters to your business</span>
  <h2 class="big" style="max-width:6.2in">If we hold that standard where an error is a legal liability, the same engineering goes into your order intake.</h2>
  <div class="fl-body" style="margin-top:16px">
    <p>The techniques are identical across everything in this document: read the document, apply the rule, write the result, explain it, keep the trace. What changes between a tax engine and a sales-order pipeline is the rulebook, not the discipline.</p>
    <p>It is also why we will tell you when a workflow is not worth automating. A process that runs twice a month, or one where every case genuinely is an exception, will cost more to automate than it returns — and we would rather say so in the first conversation than discover it in month three.</p>
  </div>
</div>""" % ("".join(mods[4:]))
sheet("", t2, "AI Tax Auditing Engine")

# --- closing
CHIPS = ["ERP systems","QuickBooks","Xero","Sage","SQL &amp; Postgres","Google Workspace",
         "Microsoft 365","Shared inboxes","WhatsApp Business","Shopify","Customer portals &amp; EDI",
         "CRM platforms","Lab instruments","E-signature","Meta &amp; LinkedIn APIs","Spreadsheets"]
close = """
<div class="phead"><span class="l">Working with us</span><span class="r">Onyx Automate</span></div>
<span class="sect-lab">We integrate with what you already run</span>
<h2 class="big" style="max-width:6.2in">Automation should slot into the tools your business is already built on — not replace them.</h2>
<p class="intro">Replacing working software is expensive, disruptive and usually unnecessary. Every system in this document was built around what the client already used. In practice that has meant:</p>
<div class="chips">%s</div>
<div class="cta">
  <h2>Tell us the task your team dreads on Monday morning.</h2>
  <p>We will map it, tell you honestly whether it is worth automating, and scope what it would take. That first conversation costs nothing and takes about thirty minutes.</p>
  <div class="contact">
    <div><b>Email</b>sales@onyx-automate.com</div>
    <div><b>Web</b>onyx-automate.com</div>
  </div>
</div>
<div class="ask">
  <span class="sect-lab">What that conversation needs from you</span>
  <ol>
    <li><h4>The workflow, described plainly</h4><p>Who touches it, how often it runs, and where it currently goes wrong. No process documentation required — a conversation is enough.</p></li>
    <li><h4>A handful of real examples</h4><p>Five actual orders, quotes, lab results or enquiries, messy ones included. Real inputs tell us in an afternoon what a specification cannot.</p></li>
    <li><h4>The systems it touches</h4><p>Whatever the work passes through today — the accounting package, the spreadsheet, the inbox, the database. We build around them.</p></li>
  </ol>
</div>
<div class="endmark"><span class="glyph" style="width:9px;height:9px;background:var(--verd);transform:rotate(45deg);display:inline-block"></span>
Onyx Automate &middot; Operations automation, AI systems, SaaS engineering</div>
""" % ("".join("<span>%s</span>" % c for c in CHIPS))
sheet("close", close, "Working with us")

# ---------------------------------------------------------------- assemble
sel = os.environ.get("SHEETS","")
keep = [int(x) for x in sel.split(",")] if sel else None
body = []
for i, s in enumerate(sheets):
    if keep and (i+1) not in keep: continue
    body.append(s.replace("%PG%", "%02d" % (i + 1)))

import sys
MEAS = MEASURE if os.environ.get("MEASURE","1")=="1" else ""
doc = ("<title>Onyx Automate — Selected Work</title>\n<style>\n%s\n%s\n</style>\n%s\n%s"
       % (FONTS, CSS, "\n".join(body), MEAS))

out = os.environ.get('OUT','/tmp/claude-0/-home-user-photo/6fbe66dd-ce10-50e4-8a80-94a54949912d/scratchpad/print.html')
open(out, 'w').write(doc)
print("sheets:", len(sheets), "bytes:", os.path.getsize(out))
