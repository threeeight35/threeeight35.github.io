# -*- coding: utf-8 -*-
from components import *

PAGES = []   # dicts: path, html, indexable, id, title, kind, status
# ---- CENTRAL INDEXING GATE -------------------------------------------------------------
# Every page is indexable EXCEPT those whose CMS ID is in this set: they are noindex,follow and excluded from sitemap.xml and llms.txt.
# Owner decision 2026-10-22: index the whole site except the held placeholder pages, which carry no treatment information yet.
# Remove an ID once its specialist content has been written and reviewed.
HELD_FROM_INDEX = {"TRT-EYE-05", "TRT-EYE-06", "TRT-GEN-03", "TRT-GEN-04", "TRT-GEN-05", "TRT-HEA-05", "TRT-IVF-07"}
def gate_reason(p):
    review = outstanding_review(p)
    if p["id"] in HELD_FROM_INDEX: return "HELD placeholder: noindex until specialist content is written; " + review
    return "Indexed (owner decision 2026-10-22)" + ("; still outstanding: " + review if review else "")

def outstanding_review(p):
    i = p["id"]
    if i.startswith("CAT-"): return "Clinical review pending (v11 Clinical status: PENDING)"
    if i.startswith("TRT-"): return "Clinical review pending" + ("; HELD for specialist review" if p["kind"] == "Held clinical record" else "")
    if i == "GEO-AU-01": return "Derived copy/metadata; editorial approval required"
    if i.startswith("GEO-AU-"): return "Derived copy; editorial approval required"
    if i in ("SUP-HOW", "SUP-FAQ"): return "Derived from v11 statements; editorial approval required"
    if i == "SUP-07": return "Derived from v11 publishing rules; editorial approval required"
    if i == "SUP-06": return "Derived copy; legal review recommended; editorial approval required"
    if i == "SUP-09": return "Legal/consumer-law review recommended before publication; derived page metadata"
    if i == "SUP-04": return "Form consent wording awaiting legal approval; send a live test enquiry before clearing"
    if i in ("SUP-05", "SUP-08"): return "Legal review pending"
    return ""

def add(p, main, active="", crumbs=None, hero=False, extra_ld=None):
    cur = p["path"]
    p["indexable"] = p["id"] not in HELD_FROM_INDEX
    p["robots"] = "index,follow,max-image-preview:large" if p["indexable"] else "noindex,follow"
    p["gate"] = gate_reason(p)
    ld = [webpage_ld(p, crumbs or [])]
    if crumbs and len(crumbs) > 1: ld.append(breadcrumb_ld(crumbs))
    ld += (extra_ld or [])
    p["jsonld"] = ld
    p["hero"] = hero
    bc = breadcrumb_html(cur, crumbs) if crumbs and len(crumbs) > 1 else ""
    html_ = head(p) + header(cur, active) + f'\n<main id="main" tabindex="-1" data-cms-id="{p["id"]}">{bc}{main}</main>\n' + footer(cur)
    p["html"] = html_
    PAGES.append(p)

def pagehead(eyebrow, h1, lead="", cls=""):
    e = f'<p class="eyebrow">{esc(eyebrow)}</p>' if eyebrow else ""
    l = f'<p class="lead">{esc(lead)}</p>' if lead else ""
    return f'<section class="page-head {cls}"><div class="container">{e}<h1>{esc(h1)}</h1>{l}</div></section>'

def prose(html_, cls=""):
    return f'<section class="section"><div class="container prose {cls}">{html_}</div></section>'

# ======================= HOME =======================
def build_home():
    cur = ""
    p = dict(path="", id="SUP-01", kind="Agency home", title="threeeight35° Medical Travel Agency | Your Health Journey, Beyond Borders.",
             desc="Personalised medical travel coordination connecting patients from Australia, the UAE and other markets with independent healthcare providers in Türkiye.",
             indexable=True, status="Business identity verified; clinical review not applicable to this page; technical QA pending")
    hero_img = img(cur, "16_health_journey_istanbul",
                   "Sunset over the Istanbul skyline and waterway, with domed mosques and a ferry below an aeroplane in the sky.",
                   "(min-width: 960px) 52vw, 100vw", cls="hero-img", eager=True, fetch=True, pick=1440)
    vid = f'<a class="btn btn-outline-light" href="{VIDEO_CONSULT_URL}">Schedule Video Consultation</a>' if VIDEO_CONSULT_URL else ""
    main = f'''<section class="hero"><div class="hero-copy"><div class="hero-copy-in">
<p class="eyebrow eyebrow-on-dark">AUSTRALIA · UAE · TÜRKİYE</p>
<h1>Your Health Journey, <span>Beyond Borders.</span></h1>
<p class="hero-sub">Personalised medical travel coordination connecting patients from Australia, the UAE and other international markets with independent healthcare providers in Türkiye.</p>
<p class="hero-line">Precisely coordinated. Transparently guided.</p>
<div class="btn-row"><a class="btn btn-gold" href="{rel(cur,"contact/#enquiry")}">Make an Enquiry</a><a class="btn btn-outline-light" href="{rel(cur,"treatments/")}">Explore Treatments</a>{vid}</div>
<dl class="hero-stats"><div><dt>Medical categories</dt><dd>8</dd></div><div><dt>Languages</dt><dd>3</dd></div><div><dt>Coordination</dt><dd>1:1</dd></div></dl>
</div></div><div class="hero-media">{hero_img}</div></section>
<section class="boundary"><div class="container"><p><strong>threeeight35° is a coordination service, not a healthcare provider.</strong> We do not diagnose, prescribe or recommend treatment. All clinical assessment and medical care are provided independently by licensed healthcare professionals in Türkiye.</p></div></section>'''
    main += section("MEDICAL CATEGORIES", "Explore Medical Categories", "Eight medical categories, each with its own treatment pages. Treatment pages explain how to plan and what to confirm; clinical decisions stay with your treating provider.", categories_grid(cur) + f'<p class="center" style="margin-top:2rem"><a class="btn btn-navy" href="{rel(cur,"treatments/")}">View the full treatments catalogue</a></p>', hid="categories")
    main += section("PATIENT-CENTRED COORDINATION", "Why Coordinated Medical Travel?", "Medical travel requires thoughtful planning, direct communication with treating healthcare professionals, and transparent arrangements.", why_cards(), tone="tone-cream")
    main += accommodation_section(cur)
    main += section("PACKAGES", "Medical Travel Coordination Packages",
                    "threeeight35° package prices include our non-clinical coordination, your accommodation and private transfers in Istanbul. Medical treatment and flights are paid separately.", package_cards(cur) + f'<p class="center"><a class="more" href="{rel(cur,"patient-packages/")}">How package, treatment and flight costs fit together <span aria-hidden="true">→</span></a></p>', hid="packages")
    main += section("THE PATIENT JOURNEY", "How It Works", "From first enquiry to follow-up coordination after you return home.", journey_list(cur) + f'<p class="center"><a class="more" href="{rel(cur,"how-it-works/")}">Read the full journey <span aria-hidden="true">→</span></a></p>', tone="tone-cream")
    main += section("ABOUT", "About threeeight35°", "", f'<p class="prose-lead">{esc("threeeight35° Medical Travel Agency is an independent medical travel coordination service for patients from Australia, the UAE and other international markets who are exploring treatment in Türkiye. We manage the practical side of the journey and leave every clinical decision to independent, licensed clinicians.")}</p>' + founder_block(cur, full=False))
    main += contact_cards(cur)
    main += enquiry_cta(cur)
    org = dict(ORG_LD)
    site = {"@context": "https://schema.org", "@type": "WebSite", "@id": BASE + "#website", "name": SITE, "url": BASE, "inLanguage": "en-AU", "publisher": {"@id": BASE + "#organization"}}
    add(p, main, "home", crumbs=[("Home", "")], hero=True, extra_ld=[org, site])

# ======================= TREATMENT DIRECTORY =======================
def tag(t):
    if t["hub"]: return '<span class="tag">Guide</span>'
    return ""

def build_directory():
    cur = "treatments/"
    p = dict(path=cur, id="SUP-02", kind="Treatments directory", title="Treatments Catalogue | threeeight35° Medical Travel Agency",
             desc="Browse 8 medical categories and 70 treatment pages for people planning treatment in Türkiye from Australia. Coordination by threeeight35°; care by independent providers.",
             indexable=True, status="Technical QA pending")
    blocks = []
    for cid, slug, name, stem, alt, intro in CATS:
        n = sum(len(i) for _, i in GROUPS[cid])
        gh = []
        for g, ids in GROUPS[cid]:
            lis = "".join(f'<li data-search="{att((TREAT[s]["label"]+" "+name+" "+(g or "")).lower())}"><a href="{rel(cur, TREAT[s]["dir"])}">{esc(TREAT[s]["label"])}</a>{tag(TREAT[s])}</li>' for s in ids)
            gh.append((f'<h4 class="grp">{esc(g)}</h4>' if g else "") + f'<ul class="tlist">{lis}</ul>')
        blocks.append(f'''<section class="dir-cat" id="{slug}" aria-labelledby="h-{slug}"><div class="dir-media">{img(cur, stem, alt, "(min-width: 900px) 28vw, 92vw", cls="dir-img")}</div>
<div class="dir-body"><p class="cat-count">{n} treatment pages</p><h3 id="h-{slug}"><a href="{rel(cur, cat_dir(cid))}">{esc(name)}</a></h3><p>{esc(intro)}</p>{"".join(gh)}</div></section>''')
    search = '''<div class="search"><label for="tsearch">Search treatments</label><input id="tsearch" type="search" placeholder="For example: dental implants, IVF, hernia" autocomplete="off" data-dir-search>
<p id="tsearch-status" class="small" role="status" aria-live="polite">Showing all treatments</p><button type="button" class="btn btn-outline-navy" data-dir-reset hidden>Reset search</button></div>'''
    main = pagehead("AUTHORITATIVE DIRECTORY", "Treatments Catalogue", "8 medical categories and 70 treatment pages. Group headings are for navigation only. Treatment prices are not published by threeeight35°: treatment is quoted by and paid directly to the independent clinic or hospital.")
    main += f'<section class="section"><div class="container">{search}<div class="dir-list">{"".join(blocks)}</div></div></section>'
    main += enquiry_cta(cur)
    add(p, main, "treatments", crumbs=[("Home", ""), ("Treatments", "treatments/")])

# ======================= CATEGORY PAGES =======================
def build_category(c):
    cid, slug, name, stem, alt, intro = c
    cur = cat_dir(cid)
    r = BYID[cid]; f = r["fields"]
    title = f["SEO title"].replace("│", "|")
    n = sum(len(i) for _, i in GROUPS[cid])
    desc = {  # v11 gives no category meta description; drafted from v11 category scope (flagged DERIVED in report)
     "CAT-01": f"Compare aesthetic and plastic surgery options in Türkiye — facial, breast and body procedures — and plan travel from Australia with threeeight35° coordination.",
     "CAT-02": "Research hair transplantation in Türkiye — FUE, DHI, Sapphire FUE, beard, eyebrow and hairline planning — with Australia-to-Türkiye coordination from threeeight35°.",
     "CAT-03": "Research dental treatment in Türkiye — implants, full-mouth restoration, veneers, crowns and general dentistry — and plan visits from Australia with threeeight35°.",
     "CAT-04": "Research eye care and vision correction in Türkiye — LASIK, refractive and lens-based surgery, cataract surgery — with coordination from threeeight35°.",
     "CAT-05": "Research bariatric and weight-loss surgery in Türkiye — sleeve gastrectomy, gastric bypass and revision surgery — with follow-up planning from Australia.",
     "CAT-06": "Research health check-ups and preventive screening in Türkiye, and how results and follow-up work for Australians, with coordination by threeeight35°.",
     "CAT-07": "Research IVF and fertility treatment pathways in Türkiye — assessment, IVF, ICSI, embryo transfer and preservation — with coordination by threeeight35°.",
     "CAT-08": "Research general surgery in Türkiye — hernia, gallbladder and other procedures — and plan travel and follow-up from Australia with threeeight35°.",
    }[cid]
    p = dict(path=cur, id=cid, kind="Category landing page", title=title, desc=desc, indexable=True,
             status="Editorial remediation complete; clinical review pending; technical QA pending")
    groups_html = []
    for g, ids in GROUPS[cid]:
        cards = []
        for s in ids:
            t = TREAT[s]
            focus = ""
            m = re.search(r"should be researched in the context of (.*?)\. The final clinical plan", t["rec"]["pre"])
            if m and not t["held"]: focus = m.group(1)
            if t["held"]: focus = "Coordination enquiries only"
            elif t["hub"]: focus = "Guide to the specific options under this broader term"
            elif focus: focus = focus[0].upper() + focus[1:]
            cards.append(f'<li class="tcard"><a href="{rel(cur, t["dir"])}"><span class="tcard-t">{esc(t["label"])}</span><span class="tcard-d">{esc(focus)}</span></a>{tag(t)}</li>')
        groups_html.append((f'<h3 class="grp">{esc(g)}</h3>' if g else "") + f'<ul class="tgrid">{"".join(cards)}</ul>')
    media = img(cur, stem, alt, "(min-width: 900px) 40vw, 92vw", cls="cat-hero-img", eager=True, fetch=True)
    main = f'''<section class="page-head cat-head"><div class="container cat-head-grid"><div><p class="eyebrow">{esc(name.upper())}</p><h1>{esc(f["H1"])}</h1>
<p class="lead">{esc(intro)}</p><p class="cat-meta">{n} treatment pages in this category</p>
<div class="btn-row"><a class="btn btn-navy" href="{rel(cur,"contact/#enquiry")}">Make an Enquiry</a><a class="btn btn-outline-navy" href="{rel(cur,"medical-travel-turkiye-from-australia/")}">Medical travel from Australia</a></div></div>
<div class="cat-head-media">{media}</div></div></section>'''
    main += f'<section class="section"><div class="container"><h2 class="sec-h">Treatments in this category</h2>{"".join(groups_html)}</div></section>'
    main += section("COSTS", f"How is {name.split(' &')[0].lower() if cid!='CAT-06' else 'health check-up'} cost handled?", "",
        f'<div class="prose"><p>There is no category-wide price. Treatment prices are not published by threeeight35°: medical treatment and clinical fees are quoted by and paid directly to the independent clinic or hospital, in writing, after assessment. threeeight35° coordination package fees are separate — see <a href="{rel(cur,"patient-packages/")}">Patient Packages</a>.</p></div>', tone="tone-cream")
    main += section("TRAVEL FROM AUSTRALIA", "Planning travel, insurance and follow-up", "",
        f'<div class="prose"><p>Questions about travelling from Australia, insurance, flying home, records and privacy are answered in our guide <a href="{rel(cur,"medical-travel-turkiye-from-australia/")}">Medical Travel to Türkiye from Australia</a>. Travel timing is always set by your treating clinician, not by a generic website timeframe.</p></div>')
    main += enquiry_cta(cur)
    add(p, main, "treatments", crumbs=[("Home", ""), ("Treatments", "treatments/"), (name, cur)])

# ======================= TREATMENT PAGES =======================
def fix_understand(sid, body):
    t = TREAT[sid]
    b = body.replace("It should explain ", "", 1)
    ov = {"DEN-10": "combined cosmetic dental planning", "EYE-04": "refractive surgery options",
          "GEN-06": "digestive-system surgical services", "GEN-07": "abdominal surgery and how it differs from abdominoplasty",
          "GEN-08": "laparoscopy as a surgical approach rather than a single operation",
          "HEA-02": "the scope of a comprehensive check-up", "HEA-03": "the scope of an executive check-up",
          "HEA-08": "the premium coordination arrangements around a check-up, which are not a measure of clinical superiority"}
    if sid in ov:
        b = re.sub(r"^.*?(?=, what the service actually includes|, including whether| without implying|\.$|, the purpose)", ov[sid], b, count=1)
    b = re.sub(r"guide to ", "", b)
    b = b.replace(" without implying that one eye procedure is suitable for everyone. Ophthalmic assessment determines the relevant options.",
                  ". No single eye procedure is suitable for everyone; ophthalmic assessment determines the relevant options.")
    b = b.replace(" and where the step sits", ", and where the step sits")
    b = b.replace("what the service actually includes", "what the service includes")
    b = b.replace("Australia–Türkiye coordination, and", "Australia–Türkiye coordination, and")
    first = b[0].lower() + b[1:] if not re.match(r"^[A-Z]{2,}|^LASIK|^FUE|^DHI|^ICSI|^IVF|^E-Max|^All-on|^Sapphire", b) else b
    return "Before you decide, it helps to understand: " + first

def cost_text(sid, secs):
    t = TREAT[sid]
    if "What affects the cost?" in secs:
        c = secs["What affects the cost?"].replace("number of teeth or treatment sites, number of stages.", "number of teeth or treatment sites and number of stages.")
        c = c.replace("; threeeight35° does not publish or collect the treatment fee.", ". threeeight35° does not publish or collect the treatment fee.")
        return c + " The provider quotes in writing after assessment."
    return ("threeeight35° does not publish treatment prices. Medical treatment and clinical fees are quoted by and paid directly to the independent clinic or hospital, "
            "and you should obtain a written provider quotation after assessment. The factors that affect a provider's quotation are confirmed with the provider for your individual plan.")

def build_treatment(sid):
    t = TREAT[sid]; r = t["rec"]; f = r["fields"]; secs = dict(r["secs"]); cid = t["cid"]; cat = CATMAP[cid]
    cur = t["dir"]
    title = f["SEO title"].replace("│", "|")
    notes = []
    if sid == "AES-14":
        title = "Body Contouring Surgery: Which Procedures Are Different? | threeeight35°"
        notes.append("V11 SEO title truncated (…'in'); corrected to standard pattern")
    if t["held"]:
        desc = f"{t['label']} in Türkiye: ask threeeight35° about medical travel coordination. threeeight35° coordinates medical travel and does not provide clinical care."
        notes.append("V11 meta description contains internal review wording; neutral meta used for held page")
    else:
        desc = f["Meta description"]
    if len(desc) > 160: notes.append(f"meta {len(desc)} chars (v11)")
    indexable = INDEX_TREATMENTS and not t["held"]
    p = dict(path=cur, id=r["id"], kind=f["Page type"], title=title, desc=desc, indexable=indexable,
             robots="index,follow,max-image-preview:large" if indexable else "noindex,follow",
             status=f["Publication status"], notes="; ".join(notes))
    # lead (answer-first)
    pre = r["pre"].split("## ")[0].strip()
    if t["held"]:
        lead = f"We don't publish treatment information on {t['label']} on our website. You can still ask us about coordinating medical travel for it."
    elif t["hub"]:
        lead = pre.replace("The page should help patients distinguish the specific options that sit underneath the broader term.", "This page helps you distinguish the specific options that sit underneath the broader term.").replace("is treated here as a guide or umbrella topic rather than as one standard procedure", "is an umbrella topic rather than one standard procedure")
    else: lead = pre
    rows = [("Category", f'<a href="{rel(cur, cat_dir(cid))}">{esc(cat[2])}</a>'),
            ("Page role", "Guide to a broader topic" if t["hub"] else ("Coordination enquiries only" if t["held"] else "Planning and coordination overview")),
            ("Treatment fees", "Not published by threeeight35°. Quoted by and paid directly to the independent clinic or hospital."),
            ("Clinical decisions", "Made by your treating healthcare professional after individual assessment."),
            ("threeeight35° role", "Non-clinical travel and communication coordination.")]
    glance = '<dl class="glance">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in rows) + "</dl>"
    blocks = [f'<section class="tsec"><h2>At a glance</h2>{glance}</section>']
    if not t["held"]:
        u = secs.get("What should this page help a patient understand?")
        if u: blocks.append(f'<section class="tsec"><h2>What to understand before you decide</h2><p>{esc(fix_understand(sid, u))}</p></section>')
        if "What legal or regulatory issues need review?" in secs:
            blocks.append(f'<section class="tsec"><h2>Legal and ethical considerations</h2><p>{esc("Fertility, embryo, gamete and genetic-testing topics can involve jurisdiction-specific legal, ethical and consent requirements. Confirm these requirements with your treating provider before you travel.")}</p></section>')
        c = secs.get("What should be confirmed before travelling?")
        if c: blocks.append(f'<section class="tsec"><h2>What to confirm before you travel</h2><p>{esc(c)}</p></section>')
        if "When can a patient fly home?" in secs:
            blocks.append(f'<section class="tsec"><h2>When can I fly home to Australia?</h2><p>{esc(secs["When can a patient fly home?"])}</p></section>')
        if "When can a patient travel home?" in secs:
            blocks.append(f'<section class="tsec"><h2>When can I travel home?</h2><p>{esc("Travel timing must follow the treating ophthalmologist’s advice and the individual review findings. A universal fitness-to-fly timeframe cannot be given without treatment-specific clinical support.")}</p></section>')
        if "What happens after the results?" in secs:
            blocks.append(f'<section class="tsec"><h2>What happens after the results?</h2><p>{esc("The provider should explain how results are delivered, which findings require further assessment and what records should be taken to an Australian GP or relevant specialist. A check-up cannot promise a diagnosis or the comprehensive exclusion of disease.")}</p></section>')
        if "Does this page need recovery or fitness-to-fly advice?" in secs:
            blocks.append(f'<section class="tsec"><h2>Do I need to plan around travel restrictions?</h2><p>{esc("Travel restrictions are only discussed where a specific test or procedure creates one. Your treating provider advises on any that apply to you.")}</p></section>')
        blocks.append(f'<section class="tsec"><h2>{"What affects the cost?" if "What affects the cost?" in secs else "How is the cost of treatment quoted?"}</h2><p>{esc(cost_text(sid, secs))}</p><p>threeeight35° coordination packages are priced separately — see <a href="{rel(cur,"patient-packages/")}">Patient Packages</a>.</p></section>')
    else:
        blocks.append(f'<section class="tsec"><h2>What you can do now</h2><p>You can read how medical travel coordination works from Australia, or ask us a general coordination question. We will not provide clinical advice, and any clinical question is for an independent treating specialist.</p></section>')
    blocks.append(f'<section class="tsec"><h2>How does threeeight35° fit in?</h2><p>threeeight35° coordinates communication, travel planning and confirmed journey components around care by independent healthcare providers. Diagnosis, suitability, informed consent, treatment and clinical follow-up decisions belong to the treating healthcare professionals. Read more <a href="{rel(cur,"about/")}">about threeeight35°</a> and how <a href="{rel(cur,"how-it-works/")}">the journey works</a>.</p></section>')
    # related
    rel_ids, miss = related_ids(sid)
    if miss: p["notes"] += "; unmatched related: " + ", ".join(miss)
    rl = "".join(f'<li><a href="{rel(cur, TREAT[s]["dir"])}">{esc(TREAT[s]["label"])}</a></li>' for s in rel_ids)
    related = f'<section class="tsec"><h2>Related pages</h2><ul class="linklist">{rl}<li><a href="{rel(cur, cat_dir(cid))}">All {esc(cat[2])} pages</a></li><li><a href="{rel(cur,"medical-travel-turkiye-from-australia/")}">Medical Travel to Türkiye from Australia</a></li></ul></section>' if True else ""
    blocks.append(related)
    blocks.append(f'<p class="disclaimer-small">{esc("This page provides general information about medical travel coordination only. It does not diagnose a condition, recommend a treatment for an individual or replace advice from a suitably qualified healthcare professional.")} <a href="{rel(cur,"medical-disclaimer/")}">Medical Information Disclaimer</a></p>')
    aside = f'''<aside class="tside" aria-label="Next steps"><div class="side-card"><h2>Ask about coordination</h2><p>Tell us what you are researching. We help with the practical side of the journey.</p>
<a class="btn btn-navy btn-block" href="{rel(cur,"contact/#enquiry")}">Make an Enquiry</a>
<p class="small">Please do not send medical records through the enquiry form.</p>
<ul class="linklist"><li><a href="{rel(cur, cat_dir(cid))}">{esc(cat[2])}</a></li><li><a href="{rel(cur,"medical-travel-turkiye-from-australia/")}">Travel from Australia</a></li><li><a href="{rel(cur,"patient-packages/")}">Patient Packages</a></li></ul></div></aside>'''
    main = f'''<section class="page-head tpage-head"><div class="container"><p class="eyebrow">{esc(cat[2].upper())}</p><h1>{esc(t["h1"])}</h1><p class="lead">{esc(lead)}</p></div></section>
<div class="container tlayout"><article class="tmain">{"".join(blocks)}</article>{aside}</div>'''
    main += enquiry_cta(cur)
    crumbs = [("Home", ""), ("Treatments", "treatments/"), (cat[2], cat_dir(cid)), (t["label"], cur)]
    add(p, main, "treatments", crumbs=crumbs)

INDEX_TREATMENTS = False   # clinical gate: flip to True only when Clinical Review Passed (see README)
