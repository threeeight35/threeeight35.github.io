# -*- coding: utf-8 -*-
from pages import *

def pending(msg): return f'<div class="banner banner-hold" role="note"><strong>Status:</strong> {esc(msg)}</div>'

def qa(h, body_html): return f'<section class="qa"><h2>{esc(h)}</h2>{body_html}</section>'

# ---------------- Packages ----------------
def build_packages():
    cur = "patient-packages/"
    p = dict(path=cur, id="SUP-09", kind="Packages & pricing", title="Medical Travel Coordination Packages | threeeight35°",
             desc="Coordination package prices from threeeight35°: Essential Care A$4,950, Executive Wellness & Recovery A$9,900, VIP Bespoke from A$14,900. Treatment and travel costs are separate.",
             indexable=True, status="Business-confirmed package pricing; legal/consumer-law review recommended; payment/cancellation/refund terms withheld pending legal review")
    three = '''<div class="cards3"><article class="card"><span class="card-num" aria-hidden="true">1</span><h3>Your treatment</h3><p>Quoted by and paid directly to the independent clinic or hospital. threeeight35° does not publish, determine or collect medical treatment fees.</p></article>
<article class="card"><span class="card-num" aria-hidden="true">2</span><h3>Your threeeight35° package</h3><p>The medical-travel coordination package fee paid to threeeight35°. The package price covers the defined non-clinical coordination services listed for that package.</p></article>
<article class="card"><span class="card-num" aria-hidden="true">3</span><h3>Your travel</h3><p>Accommodation and private transport are arranged by threeeight35° and itemised separately. They are not represented as included in the coordination package price unless expressly confirmed in writing.</p></article></div>'''
    main = pagehead("TAILORED COORDINATION PACKAGES", "Medical Travel Coordination Packages",
                    "Choose the level of coordination that fits your journey. threeeight35° package prices cover our non-clinical medical-travel coordination services. Your medical treatment and travel costs are separate.")
    main += section("WHO YOU PAY, AND FOR WHAT", "Three separate parts of your journey cost", "", three, tone="tone-cream")
    main += section("PACKAGES", "Choose your coordination package", "All prices are in Australian dollars (AUD).", package_cards(cur) +
        '<div class="prose narrow"><p>Before you proceed you receive a written, itemised proposal showing your selected coordination package, confirmed inclusions and exclusions, separately itemised travel arrangements and the independent provider\'s treatment quotation. A treatment fee is never combined with a threeeight35° package price into a single advertised treatment price.</p></div>')
    main += accommodation_section(cur)
    main += section("", "Questions about packages", "",
        f'<div class="prose"><p>See our <a href="{rel(cur,"faqs/")}">FAQs</a>, read how <a href="{rel(cur,"how-it-works/")}">the journey works</a> or <a href="{rel(cur,"contact/#enquiry")}">make an enquiry</a>. Full payment, cancellation and refund terms are being finalised and will be published in the <a href="{rel(cur,"terms/")}">Terms &amp; Conditions</a>.</p></div>')
    main += enquiry_cta(cur)
    add(p, main, "packages", crumbs=[("Home", ""), ("Patient Packages", cur)])

# ---------------- How it works ----------------
def build_how():
    cur = "how-it-works/"
    p = dict(path=cur, id="SUP-HOW", kind="How it works (derived from v11 statements)", title="How Medical Travel Coordination Works | threeeight35°",
             desc="How threeeight35° coordinates the practical side of medical travel to Türkiye, from first enquiry to follow-up after you return to Australia.",
             indexable=True, status="Derived from Version 11 statements; editorial approval required (v11 has no dedicated How It Works record)")
    main = pagehead("THE PATIENT JOURNEY", "How It Works", "A clear pathway for the practical side of medical travel, with a firm boundary: we coordinate, and independent licensed clinicians make every medical decision.")
    main += section("", "Your coordination journey", "", journey_list(cur))
    main += f'''<section class="section tone-cream"><div class="container"><div class="notice-card"><h2>Important coordination notice</h2><p>{esc(NOTICE.replace("Important Medical Coordination Notice: ",""))}</p>
<p><a href="{rel(cur,"medical-travel-turkiye-from-australia/")}">Read more about medical travel from Australia</a> · <a href="{rel(cur,"privacy-overseas-health-information-disclosure/")}">Privacy and overseas health-information disclosure</a></p></div></div></section>'''
    main += enquiry_cta(cur)
    add(p, main, "how", crumbs=[("Home", ""), ("How It Works", cur)])

# ---------------- About ----------------
def build_about():
    cur = "about/"
    p = dict(path=cur, id="SUP-03", kind="About / Organisation", title="About threeeight35° Medical Travel Agency",
             desc="Learn about threeeight35° Medical Travel Agency, our coordination role, mission, values and founder, Hommam Azizieh.",
             indexable=True, status="Editorially ready after factual/business verification and technical QA")
    values = [("Patient-Centred Coordination", "We listen to each patient's needs, preferences and circumstances and, where the patient wishes, include companions or family members in appropriate parts of the planning process."),
              ("Transparency", "We provide itemised written quotations, confirm inclusions in writing and never promise medical outcomes or risk-free procedures."),
              ("Privacy and Discretion", "We handle personal and health information with care, restrict access to authorised personnel and do not ask patients to submit medical records or clinical photographs through public website forms."),
              ("Clear Boundaries", "We coordinate. Independent, licensed clinicians make every medical decision."),
              ("Precision", "We aim for reliable, detail-oriented coordination at every stage of the journey."),
              ("Care and Dignity", "We treat every patient and companion with attention and respect.")]
    vh = '<div class="cards3 values">' + "".join(f'<article class="card"><h3>{esc(a)}</h3><p>{esc(b)}</p></article>' for a, b in values) + "</div>"
    main = pagehead("AGENCY PHILOSOPHY", "About threeeight35° Medical Travel Agency")
    main += f'''<section class="section"><div class="container prose"><h2>About Us</h2>
<p>threeeight35° Medical Travel Agency is an independent medical travel coordination service for patients from Australia, the UAE and other international markets who are exploring treatment in Türkiye. We manage the practical side of the journey. We connect patients with independent healthcare providers and hospitals in Istanbul, arrange consultations and quotations, and coordinate accommodation, private transfers and English-speaking support during the stay.</p>
<p>Our name reflects how we work. Like a coordinate, we aim to be precise, dependable and clear about where you stand at every step. From the first enquiry with our Australian or UAE desk to follow-up coordination after returning home, patients work with a dedicated coordinator and receive written, itemised proposals before committing.</p>
<p><strong>We are not a healthcare provider.</strong> We do not diagnose, prescribe or recommend treatment. Every clinical assessment and all medical care are provided independently by licensed healthcare professionals in Türkiye. Patients are encouraged to discuss overseas treatment with their usual doctor or an appropriate healthcare professional where relevant.</p>
<p class="small">Australian Business Number (ABN): {ABN}</p></div></section>'''
    main += section("", "Our Mission", "", '<div class="prose"><p>To make international medical travel clearer and better organised for patients and their families through transparent information, personalised coordination and practical support, while respecting privacy and leaving every clinical decision to independent medical professionals.</p></div>', tone="tone-cream")
    main += section("", "Our Vision", "", '<div class="prose"><p>To be a respected name in international medical travel coordination, known for a standard of transparency and care that lets patients cross borders for treatment with well-informed confidence.</p></div>')
    main += section("", "Our Core Values", "", vh, tone="tone-cream")
    main += f'<section class="section" id="founder"><div class="container">{founder_block(cur)}</div></section>'
    main += f'''<section class="section tone-cream"><div class="container prose"><h2>Where to go next</h2><ul class="linklist"><li><a href="{rel(cur,"contact/#enquiry")}">Contact / Confidential Enquiry</a></li><li><a href="{rel(cur,"treatments/")}">Treatments Catalogue</a></li><li><a href="{rel(cur,"medical-travel-turkiye-from-australia/")}">Medical Travel to Türkiye from Australia</a></li><li><a href="{rel(cur,"privacy/")}">Privacy Policy</a></li><li><a href="{rel(cur,"medical-disclaimer/")}">Medical Information Disclaimer</a></li><li><a href="{rel(cur,"editorial-policy/")}">Editorial &amp; Medical Review Policy</a></li></ul></div></section>'''
    fnd = {"@context": "https://schema.org", "@type": "Person", "@id": BASE + "about/#founder", "name": "Hommam Azizieh", "jobTitle": "Founder",
           "image": abs_url("assets/img/founder-hommam-azizieh-843.jpg"), "knowsLanguage": ["English", "Arabic", "Turkish"],
           "worksFor": {"@id": BASE + "#organization"}}
    add(p, main, "about", crumbs=[("Home", ""), ("About Us", cur)], extra_ld=[dict(ORG_LD), fnd])

# ---------------- FAQs ----------------
FAQS = [
 ("Is threeeight35° a healthcare provider?", "No. threeeight35° Medical Travel Agency is a medical travel and journey coordination service. Clinical assessment, diagnosis, treatment recommendations, informed consent and medical care are provided independently by licensed healthcare professionals in Türkiye."),
 ("Does threeeight35° recommend a treatment or tell me whether I am suitable?", "No. We do not diagnose, prescribe or recommend treatment. Suitability is decided by the treating healthcare professional after individual assessment."),
 ("How much do your packages cost?", "Essential Care is a fixed A$4,950 Medical Travel Coordination Package. Executive Wellness & Recovery is a fixed A$9,900 Medical Travel Coordination Package. VIP Bespoke Health Journey is from A$14,900, with the final coordination package price confirmed in writing after the scope of the journey is established."),
 ("Do the package prices include my medical treatment?", "No. Treatment and travel costs are separate. Medical treatment is quoted by and paid directly to the independent clinic or hospital. threeeight35° does not publish, determine or collect medical treatment fees."),
 ("Are accommodation and private transport included?", "Accommodation and private transport are arranged and itemised separately. A service forms part of your package only where it is expressly confirmed in your written proposal."),
 ("Do you publish treatment prices?", "No. Treatment prices are quoted by the independent provider after assessment. Your written proposal shows your coordination package, separately itemised travel arrangements and the provider's treatment quotation before you proceed."),
 ("Should I send medical records through the enquiry form?", "No. Please do not include medical records, test results, passport or payment details in the website form. After your initial enquiry, any health information needed for preliminary provider review follows a private health-information and overseas-disclosure workflow."),
 ("How soon can I fly home after treatment?", "There is no universal safe timeframe. The treating clinician determines travel timing from the procedure, your individual recovery and required post-treatment reviews."),
 ("What happens after I return to Australia?", "Follow-up coordination continues after you return home. Before you travel, confirm which records you will bring home and the plan for any concerns after returning to Australia. Where ongoing care may be needed, discussing your plans with an Australian healthcare professional can help."),
 ("Which markets do you serve?", "We coordinate medical travel for patients from Australia, the UAE and other international markets. Our Australia desk covers Sydney and Melbourne, our UAE desk covers Dubai and the GCC, and our Istanbul hub provides in-country coordination during your stay."),
 ("Is “Türkiye” the same as “Turkey”?", "Yes. Türkiye is the country's name in its own language and is the form we use editorially. Many people still search for Turkey, so you may see both."),
]
def build_faqs():
    cur = "faqs/"
    p = dict(path=cur, id="SUP-FAQ", kind="FAQs (derived from v11 statements)", title="Frequently Asked Questions | threeeight35° Medical Travel Agency",
             desc="Answers about threeeight35°'s coordination role, package prices, treatment costs, travel from Australia and privacy when planning treatment in Türkiye.",
             indexable=True, status="Derived from Version 11 statements; editorial approval required (v11 has no dedicated FAQ record)")
    body = "".join(f'<details class="faq"><summary>{esc(q)}</summary><div class="faq-a"><p>{esc(a)}</p></div></details>' for q, a in FAQS)
    main = pagehead("PATIENT GUIDANCE", "Frequently Asked Questions", "Answers about our coordination role, package prices, costs and travel from Australia.")
    main += f'<section class="section"><div class="container prose">{body}<p class="small">Still have a question? <a href="{rel(cur,"contact/#enquiry")}">Make an enquiry</a>.</p></div></section>'
    main += enquiry_cta(cur)
    add(p, main, "faqs", crumbs=[("Home", ""), ("FAQs", cur)])

# ---------------- Contact ----------------
FORM_CONSENT = "I understand that threeeight35° is a medical travel coordination service and not a healthcare provider, and I have read the Privacy Policy. I have not included medical records, test results, passport or payment details in this form."
def build_contact():
    cur = "contact/"
    p = dict(path=cur, id="SUP-04", kind="Contact / Enquiry", title="Contact & Confidential Enquiry | threeeight35° Medical Travel Agency",
             desc="Contact the threeeight35° Australia desk, UAE desk or Istanbul hub, or send a confidential medical travel enquiry. No medical records through the form.",
             indexable=True, status="Form delivery: TECHNICAL CONFIGURATION REQUIRED; consent wording: LEGAL INPUT REQUIRED")
    cats = "".join(f'<option value="{att(c[2])}">{esc(c[2])}</option>' for c in CATS)
    procs = "".join(f'<optgroup label="{att(CATMAP[cid][2])}">' + "".join(f'<option value="{att(TREAT[s]["label"])}" data-cat="{att(CATMAP[cid][2])}">{esc(TREAT[s]["label"])}</option>' for _, ids in GROUPS[cid] for s in ids) + "</optgroup>" for cid in [c[0] for c in CATS])
    form = f'''<section class="section" id="enquiry"><div class="container form-wrap"><div class="form-intro"><p class="eyebrow">MEDICAL TRAVEL ENQUIRY</p><h2>Send a confidential enquiry</h2>
<p>Please provide your details below. We practise data minimisation — no diagnostic records, passport or payment details are requested here.</p>
<p>After the initial enquiry, any health information required for preliminary provider review must follow the approved private health-information and overseas-disclosure workflow, not the public web form.</p>
<p class="small">Fields marked * are required.</p></div>
<form class="form" id="enquiry-form" method="post" novalidate data-endpoint-config="T35_FORM">
<div id="form-status" class="form-status" role="status" aria-live="polite" tabindex="-1" hidden></div>
<div class="field"><label for="f-name">Full name *</label><input id="f-name" name="full_name" type="text" autocomplete="name" required maxlength="120"><p class="err" id="e-f-name" hidden></p></div>
<div class="field"><label for="f-email">Email address *</label><input id="f-email" name="email" type="email" autocomplete="email" required maxlength="160"><p class="err" id="e-f-email" hidden></p></div>
<div class="field"><label for="f-country">Country of residence *</label><input id="f-country" name="country" type="text" autocomplete="country-name" required maxlength="80"><p class="err" id="e-f-country" hidden></p></div>
<div class="field"><label for="f-contact">Preferred contact method *</label><select id="f-contact" name="preferred_contact" required><option value="">Select…</option><option>Email</option><option>WhatsApp</option><option>Phone</option></select><p class="err" id="e-f-contact" hidden></p></div>
<div class="field"><label for="f-cat">Treatment category *</label><select id="f-cat" name="treatment_category" required><option value="">Select…</option>{cats}<option>Not sure yet</option></select><p class="err" id="e-f-cat" hidden></p></div>
<div class="field"><label for="f-proc">Specific procedure <span class="opt">(optional)</span></label><select id="f-proc" name="specific_procedure"><option value="">Not sure yet / not listed</option>{procs}</select></div>
<div class="field field-wide"><label for="f-msg">Message <span class="opt">(optional)</span></label><textarea id="f-msg" name="message" rows="5" maxlength="1500" aria-describedby="msg-help"></textarea>
<p id="msg-help" class="help">Please share only your general goals or ideal travel timing. Please don't include medical records, test results or payment details here.</p></div>
<div class="hp" aria-hidden="true"><label for="f-hp">Leave this field empty</label><input id="f-hp" name="_gotcha" type="text" tabindex="-1" autocomplete="off"></div>
<div class="field field-wide consent"><input id="f-consent" name="privacy_consent" type="checkbox" value="yes" required><label for="f-consent">{esc(FORM_CONSENT).replace("Privacy Policy", f'<a href="{rel(cur,"privacy/")}">Privacy Policy</a>')}</label><p class="err" id="e-f-consent" hidden></p></div>
<div id="captcha-slot" class="field-wide"></div>
<input type="hidden" name="_subject" value="New medical travel enquiry — threeeight35° website"><input type="hidden" name="_page" value="{BASE}contact/">
<div class="field-wide"><button class="btn btn-navy btn-lg" type="submit" id="f-submit">Send enquiry</button></div>
</form></div></section>'''
    main = pagehead("PATIENT CONCIERGE", "Contact & Confidential Enquiry", "Reach our Australian, UAE or Türkiye coordination contacts directly or submit an enquiry below.")
    main += contact_cards(cur, with_h=False).join(['<section class="section tone-cream"><div class="container">', '</div></section>'])
    main += form
    add(p, main, "contact", crumbs=[("Home", ""), ("Contact & Enquiries", cur)])

# ---------------- Legal & trust ----------------
def build_privacy():
    cur = "privacy/"
    p = dict(path=cur, id="SUP-05", kind="Privacy", title="Privacy Information | threeeight35° Medical Travel Agency",
             desc="How threeeight35° approaches privacy: data minimisation, no medical records through the public form, and a separate private workflow for health information.",
             indexable=False, robots="noindex,follow", status="CONDITIONAL — final Australian privacy/legal review pending (APP 8, retention, consistency)")
    body = f'''{pending("This is a summary of our privacy approach. The full Privacy Policy is being finalised following Australian privacy and legal review and will replace this page.")}
{qa("What do we collect through the website enquiry form?", "<p>Only what is necessary for an initial enquiry: your name, email address, country of residence, preferred contact method, the treatment category (and optionally procedure) you are exploring, and an optional general message. We practise data minimisation.</p>")}
{qa("Should I send medical records through the website?", "<p>No. We do not ask patients to submit medical records or clinical photographs through public website forms, and the form asks you not to include medical records, test results, passport or payment details.</p>")}
{qa("How is health information handled after my enquiry?", f"<p>After the initial enquiry, any health information needed for preliminary provider review follows an approved private health-information and overseas-disclosure workflow, with your authorisation. Where appropriate, relevant health information may then be provided to independent healthcare professionals in Türkiye. See <a href=\"{rel(cur,'privacy-overseas-health-information-disclosure/')}\">Privacy &amp; Overseas Health-Information Disclosure</a>.</p>")}
{qa("Who can access personal and health information?", "<p>We handle personal and health information with care and restrict access to authorised personnel.</p>")}
{qa("Who do I contact about privacy?", f'<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a>. threeeight35° Medical Travel Agency, ABN {ABN}.</p>')}'''
    main = pagehead("", "Privacy Information") + f'<section class="section"><div class="container prose">{body}</div></section>'
    add(p, main, "", crumbs=[("Home", ""), ("Privacy", cur)])

def build_terms():
    cur = "terms/"
    p = dict(path=cur, id="SUP-08", kind="Terms", title="Terms & Conditions | threeeight35° Medical Travel Agency",
             desc="Terms for threeeight35° medical travel coordination services. Treatment, coordination package fees and travel costs are separate.",
             indexable=False, robots="noindex,follow", status="LEGAL INPUT REQUIRED — payment, cancellation and refund terms withheld")
    body = f'''{pending("Full Terms & Conditions, including payment, cancellation and refund terms, are being finalised following legal review. Only the following confirmed points are published now.")}
{qa("Who provides medical treatment?", "<p>Independent clinics, hospitals and licensed healthcare professionals provide all medical assessment and treatment. threeeight35° is a coordination service and not a healthcare provider.</p>")}
{qa("Who do I pay for what?", "<p>Medical treatment is quoted by and paid directly to the independent clinic or hospital. The threeeight35° coordination package fee is paid to threeeight35° for the defined non-clinical coordination services in your package. Accommodation and private transport are arranged and itemised separately, and are not included in the coordination package price unless expressly confirmed in writing.</p>")}
{qa("What do I receive before I proceed?", "<p>A written, itemised proposal showing your selected coordination package, confirmed inclusions and exclusions, separately itemised travel arrangements and the provider's treatment quotation.</p>")}
{qa("Business details", f'<p>threeeight35° Medical Travel Agency · ABN {ABN} · <a href="mailto:{EMAIL}">{EMAIL}</a></p>')}'''
    main = pagehead("", "Terms & Conditions") + f'<section class="section"><div class="container prose">{body}</div></section>'
    add(p, main, "", crumbs=[("Home", ""), ("Terms & Conditions", cur)])

def build_disclaimer():
    cur = "medical-disclaimer/"
    p = dict(path=cur, id="SUP-06", kind="Medical disclaimer", title="Medical Information Disclaimer | threeeight35°",
             desc="threeeight35° is a medical travel coordination service, not a healthcare provider. Read how our information differs from medical advice.",
             indexable=True, status="Uses Version 11 approved coordination notice; legal review recommended")
    body = f'''{qa("What threeeight35° is and is not", f"<p>{esc(NOTICE.replace('Important Medical Coordination Notice: ',''))}</p>")}
{qa("What this website provides", "<p>General information about planning medical travel and coordination. It does not diagnose a condition, recommend a treatment for an individual or replace advice from a suitably qualified healthcare professional. Suitability, risks, alternatives, recovery and fitness to travel must be determined by the treating clinician.</p>")}
{qa("Results and costs", "<p>No treatment result, recovery time or travel timeframe is guaranteed. Treatment prices are quoted by and paid directly to the independent clinic or hospital.</p>")}
{qa("In an emergency", "<p>In a medical emergency in Türkiye, call 112. This is separate from threeeight35° contact details.</p>")}
{qa("Discuss your plans", "<p>Patients are encouraged to discuss overseas treatment with their usual doctor or an appropriate healthcare professional where relevant.</p>")}'''
    main = pagehead("", "Medical Information Disclaimer") + f'<section class="section"><div class="container prose">{body}</div></section>'
    add(p, main, "", crumbs=[("Home", ""), ("Medical Information Disclaimer", cur)])

def build_editorial():
    cur = "editorial-policy/"
    p = dict(path=cur, id="SUP-07", kind="Editorial & medical review policy", title="Editorial & Medical Review Policy | threeeight35°",
             desc="How threeeight35° plans, reviews and gates its medical-travel content: clinician review, sources, business confirmation and legal review.",
             indexable=True, status="Derived from Version 11 publishing rules; editorial approval required")
    body = f'''{qa("Our publishing rules", "<ul><li>threeeight35° is a medical-travel coordination agency, not the treating healthcare provider.</li><li>We do not invent prices, provider credentials, accreditation, recovery promises, minimum stays, medication, tests, hotel inclusions, transfers or outcomes.</li><li>Pages use answer-first questions, descriptive internal links and a clear path to the category, the Australia guide and contact.</li><li>Public copy uses Australian English. We use Türkiye editorially; Turkey may appear naturally as a search-language variant.</li></ul>")}
{qa("Review gates", "<p>Each page moves through: Draft, Editorial Approved, Clinical Review Passed, Business Confirmed, Legal Cleared where applicable, Technical QA Passed, then Published. Clinical statements are published only after review by a qualified clinician, and the reviewer's name, credentials, jurisdiction, date and content version are recorded.</p>")}
{qa("Sources", "<p>Authoritative sources are mapped to substantive medical claims at claim level. A category bibliography is not treated as a substitute for claim-level support.</p>")}
{qa("Current status", "<p>Clinical review of treatment-specific content is pending. Until a qualified clinician has signed off a page, treatment pages carry only coordination information and say so. Pages on topics that need specialist scope are marked under review.</p>")}
{qa("Provider and package facts", "<p>Provider-specific facts, prices, inclusions, accommodation, transfers, tests, medicines, stay durations and follow-up promises are verified in writing before publication.</p>")}'''
    main = pagehead("", "Editorial & Medical Review Policy") + f'<section class="section"><div class="container prose">{body}</div></section>'
    add(p, main, "", crumbs=[("Home", ""), ("Editorial & Medical Review Policy", cur)])

# ---------------- GEO hub + spokes ----------------
SMART = "https://www.smartraveller.gov.au/travel-essentials/travel-health/medical-tourism"
SPOKES = [
 ("GEO-AU-02", "checking-an-overseas-healthcare-provider/", "Checking an Overseas Healthcare Provider", "Questions to ask about who will treat you, where, and what is confirmed in writing before you travel for treatment in Türkiye.",
  [("What should I check about my treating provider?", "<p>Confirm who will be your treating clinician, the proposed procedure, the anaesthesia and facility arrangements where relevant, and the expected reviews in Türkiye. Provider qualifications and facility details should be supplied and verified before you commit; threeeight35° does not claim blanket accreditation or credentials for every provider.</p>"),
   ("What does the Australian Government advise?", f'<p>Smartraveller, the Australian Government travel advisory service, advises researching the health system of your destination, reading the destination travel advisory and not going to an unofficial medical facility. Read it at <a href="{SMART}" rel="noopener noreferrer" target="_blank">smartraveller.gov.au</a>.</p>')]),
 ("GEO-AU-03", "medical-travel-insurance/", "Medical Travel Insurance", "What to check about insurance when planning medical treatment overseas from Australia.",
  [("Does basic travel insurance cover medical travel?", f'<p>Smartraveller notes that basic travel insurance policies rarely cover medical tourism, and advises making sure your insurance covers complications and medical evacuation. Policy wording and exclusions matter. Source: <a href="{SMART}" rel="noopener noreferrer" target="_blank">Smartraveller – Medical tourism</a>.</p>'),
   ("Can threeeight35° advise on my policy?", "<p>No. We do not provide insurance or legal advice. Check your policy with your insurer before you travel.</p>")]),
 ("GEO-AU-04", "flying-home-after-medical-treatment/", "Flying Home After Medical Treatment", "Why there is no universal safe timeframe for flying home after treatment, and who decides.",
  [("When can I fly home to Australia after treatment?", "<p>There is no universal safe timeframe. The treating clinician must determine travel timing from the procedure, individual recovery and required post-treatment reviews.</p>"),
   ("Does a package duration set my return date?", "<p>No. Your return date follows your treating clinician's advice and the reviews they require. It is not set by a generic package duration.</p>")]),
 ("GEO-AU-05", "medical-records-follow-up/", "Medical Records & Follow-Up", "What to confirm about records and follow-up before you leave, and who to contact after you return to Australia.",
  [("What records should I confirm before travelling?", "<p>Confirm which records you will bring home and the plan for concerns after returning to Australia. Ask your provider how results and follow-up findings will be shared with an Australian GP or relevant specialist.</p>"),
   ("Who follows up after I return?", "<p>Follow-up coordination continues after you return home. Where ongoing care may be needed, discussing your plans with an Australian healthcare professional can help, and some concerns may need assessment by a local service.</p>")]),
 ("GEO-AU-06", "complication-planning/", "Complication Planning", "Planning before you travel for what happens if you have a concern during your stay or after you return.",
  [("What should I plan for before I travel?", "<p>Confirm the plan for concerns after returning to Australia, and check that your insurance covers complications and medical evacuation.</p>"),
   ("What if I need urgent help in Türkiye?", "<p>In a medical emergency in Türkiye, call 112. This emergency service is separate from threeeight35° contact details.</p>")]),
 ("GEO-AU-07", "comparing-medical-treatment-quotations/", "Comparing Medical Treatment Quotations", "How to compare written treatment quotations and what threeeight35° does and does not price.",
  [("What should a written quotation show?", "<p>Your complete proposal, including confirmed inclusions and exclusions, is provided in writing before you proceed. It shows your coordination package, separately itemised travel arrangements and the independent provider's treatment quotation.</p>"),
   ("Why can't I compare a package price with a treatment price?", "<p>They are different things. Treatment is quoted by and paid directly to the independent clinic or hospital; the threeeight35° package fee covers non-clinical coordination; travel is itemised separately. A treatment fee is not combined with a package price into one advertised price.</p>")]),
 ("GEO-AU-08", "privacy-overseas-health-information-disclosure/", "Privacy & Overseas Health-Information Disclosure", "How health information is handled after your initial enquiry, and why it is kept out of the public web form.",
  [("Why is health information kept out of the website form?", "<p>The public form is for initial enquiries only and is designed for data minimisation. After your enquiry, any health information needed for preliminary provider review follows an approved private health-information and overseas-disclosure workflow, with your authorisation.</p>"),
   ("Is this process legally certified?", "<p>Not yet. The workflow is documented, but final Australian privacy and legal review is still pending. This page will be updated when it is complete.</p>")]),
]
def build_geo():
    cur = "medical-travel-turkiye-from-australia/"
    p = dict(path=cur, id="GEO-AU-01", kind="Supporting GEO / patient-journey hub", title="Medical Travel to Türkiye from Australia | threeeight35°",
             desc="How medical travel from Australia to Türkiye works: coordination, quotations, travel, flying home and follow-up. threeeight35° coordinates; providers treat.",
             indexable=True, status="Hub: title/meta/copy drafted from Version 11 statements (v11 supplies name and URL only); editorial approval required")
    cats = "".join(f'<li><a href="{rel(cur, cat_dir(c[0]))}">{esc(c[2])}</a></li>' for c in CATS)
    spokes = "".join(f'<li><a href="{rel(cur, s[1])}">{esc(s[2])}</a></li>' for s in SPOKES)
    body = f'''{qa("How does medical travel from Australia to Türkiye work?", f'<p>Medical travel from Australia to Türkiye generally involves exploring a treatment and independent provider, receiving a written proposal and quotation, arranging travel, attending the provider\'s assessment, receiving treatment only where the treating clinician considers it suitable, and arranging follow-up after returning to Australia. threeeight35° coordinates the non-clinical journey. See <a href="{rel(cur,"how-it-works/")}">How It Works</a>.</p>')}
{qa("What does threeeight35° coordinate?", "<p>We connect patients with independent healthcare providers and hospitals in Istanbul, arrange consultations and quotations, and coordinate accommodation, private transfers and English-speaking support during the stay. Clinical assessment, diagnosis, treatment recommendations, informed consent and medical care are the responsibility of the treating provider.</p>")}
{qa("What should I confirm before travelling?", "<p>Confirm the treating clinician, the proposed procedure, anaesthesia and facility arrangements where relevant, expected reviews in Türkiye, records to bring home, and the plan for concerns after returning to Australia.</p>")}
{qa("When can I fly home?", f'<p>There is no universal safe timeframe. The treating clinician must determine travel timing from the procedure, individual recovery and required post-treatment reviews. See <a href="{rel(cur,"flying-home-after-medical-treatment/")}">Flying Home After Medical Treatment</a>.</p>')}
{qa("What does it cost, and who do I pay?", f'<p>{esc(DISCLOSURE)} See <a href="{rel(cur,"patient-packages/")}">Patient Packages</a>.</p>')}
{qa("What does the Australian Government say?", f'<p>Smartraveller advises researching the destination health system, making sure travel insurance covers complications and medical evacuation, and notes that basic travel insurance policies rarely cover medical tourism. <a href="{SMART}" rel="noopener noreferrer" target="_blank">Read the Smartraveller guidance</a>.</p>')}'''
    main = pagehead("AUSTRALIA TO TÜRKIYE", "Medical Travel to Türkiye from Australia", "A practical guide for Australians researching treatment in Türkiye (often searched as Turkey). We coordinate the journey; independent providers deliver all clinical care.")
    main += f'<section class="section"><div class="container prose">{body}</div></section>'
    main += f'<section class="section tone-cream"><div class="container two-col"><div><h2>Guides in this series</h2><ul class="linklist">{spokes}</ul></div><div><h2>Treatment categories</h2><ul class="linklist">{cats}</ul></div></div></section>'
    main += enquiry_cta(cur)
    add(p, main, "", crumbs=[("Home", ""), ("Medical Travel to Türkiye from Australia", cur)])
    for sid, slug, name, intro, qas in SPOKES:
        c2 = slug
        pp = dict(path=c2, id=sid, kind="GEO support guide", title=f"{name} | threeeight35°", desc=intro, indexable=False, robots="noindex,follow",
                  status="Spoke drafted from Version 11 statements (v11 lists the name only); editorial approval required; noindex until approved")
        b = "".join(qa(h, x) for h, x in qas)
        m = pagehead("AUSTRALIA TO TÜRKIYE GUIDE", name, intro)
        m += f'<section class="section"><div class="container prose">{pending("This guide is in editorial review. It contains only confirmed coordination information.")}{b}<p><a href="{rel(c2,"medical-travel-turkiye-from-australia/")}">← Medical Travel to Türkiye from Australia</a></p></div></section>'
        m += enquiry_cta(c2)
        add(pp, m, "", crumbs=[("Home", ""), ("Medical Travel to Türkiye from Australia", "medical-travel-turkiye-from-australia/"), (name, slug)])
