# -*- coding: utf-8 -*-
from lib import *

def cta_btn(cls, href, label, extra=""):
    return f'<a class="btn {cls}" href="{href}"{extra}>{label}</a>'

def disclosure(cls=""):
    return f'<p class="disclosure {cls}"><strong>Treatment and travel costs are separate.</strong> {esc(DISCLOSURE.split("separate. ",1)[1])}</p>'

def section(eyebrow, h2, intro="", body="", cls="", hid=None, tone=""):
    i = f'<p class="lead-sm">{esc(intro)}</p>' if intro else ""
    e = f'<p class="eyebrow">{esc(eyebrow)}</p>' if eyebrow else ""
    hid = f' id="{hid}"' if hid else ""
    return f'<section class="section {tone} {cls}"{hid}><div class="container"><div class="section-head">{e}<h2>{esc(h2)}</h2>{i}</div>{body}</div></section>'

def categories_grid(cur):
    cards = []
    for cid, slug, name, stem, alt, intro in CATS:
        n = sum(len(ids) for _, ids in GROUPS[cid])
        cards.append(f'''<article class="cat-card">
<a class="cat-media" href="{rel(cur, cat_dir(cid))}" tabindex="-1" aria-hidden="true">{img(cur, stem, alt, "(min-width: 1100px) 24vw, (min-width: 700px) 45vw, 92vw", cls="cat-img")}</a>
<div class="cat-body"><p class="cat-count">{n} treatment pages</p>
<h3><a href="{rel(cur, cat_dir(cid))}">{esc(name)}</a></h3>
<p>{esc(intro.split(". ")[0] + ".")}</p>
<a class="more" href="{rel(cur, cat_dir(cid))}">Explore category <span aria-hidden="true">→</span><span class="sr-only"> {esc(name)}</span></a></div></article>''')
    return f'<div class="cat-grid">{"".join(cards)}</div>'

def why_cards():
    cards = [("Personalised Coordination", "From your initial enquiry through pre-departure planning, you receive dedicated coordination support for the practical parts of your journey."),
             ("Direct Clinical Assessment", "Where appropriate and with your authorisation, relevant health information may be provided to independent healthcare professionals in Türkiye for preliminary review. Clinical assessment, suitability and treatment decisions remain entirely with the treating healthcare professionals."),
             ("Bilingual Liaison", "English-speaking coordination support can assist with practical communication and attendance arrangements around scheduled consultations and clinical appointments.")]
    return '<div class="cards3">' + "".join(f'<article class="card"><span class="card-num" aria-hidden="true">{i+1:02d}</span><h3>{esc(h)}</h3><p>{esc(b)}</p></article>' for i, (h, b) in enumerate(cards)) + "</div>"

def accommodation_section(cur, h="h2"):
    hotel = img(cur, "18_accommodation", "A hotel suite bedroom with a large window overlooking the Bosphorus and the Istanbul skyline at dusk.", "(min-width: 800px) 46vw, 92vw", cls="logi-img")
    car = img(cur, "19_chauffeur_transportation", "A black luxury minivan parked at a hotel entrance with the Istanbul skyline at sunset behind it.", "(min-width: 800px) 46vw, 92vw", cls="logi-img")
    body = f'''<div class="logi-grid">
<article class="logi-card"><div class="logi-media">{hotel}</div><div class="logi-body"><p class="eyebrow">COMFORT &amp; RELAXATION</p><h3>Luxury 5-Star Hotels</h3>
<p>Experience comfort, quality, relaxation and a premium hospitality experience. We coordinate stays at carefully selected Luxury 5-Star Hotels located conveniently for your treating healthcare facility. Exact arrangements depend on your confirmed medical travel package and individual itinerary.</p>
<p class="check">Dedicated recovery environments with companion accommodation options, where confirmed in your written proposal.</p>
<p class="small">Accommodation is itemised separately and confirmed in writing. It is not medical care.</p></div></article>
<article class="logi-card"><div class="logi-media">{car}</div><div class="logi-body"><p class="eyebrow">CONVENIENCE &amp; PRIVACY</p><h3>Luxury VIP Cars</h3>
<p>Comfort, convenience, privacy and a premium travel experience. Private chauffeur services in Luxury VIP Cars can be coordinated between the airport, your hotel and scheduled clinical visits. Specific arrangements depend on your confirmed journey plan.</p>
<p class="check">Private ground logistics throughout Istanbul, as confirmed in your written proposal.</p>
<p class="small">Private transport is itemised separately and confirmed in writing. It is not a clinical service.</p></div></article>
</div>
<div class="clarity"><h3>Package Inclusions Clarity</h3><p>Exact accommodation and transportation arrangements depend on your confirmed medical travel package and individual itinerary. An accommodation or transportation service forms part of your package only where it is expressly confirmed in your written proposal.</p>
<a class="btn btn-gold" href="{rel(cur, "patient-packages/")}">View Packages</a></div>'''
    return section("COORDINATED LOGISTICS", "Accommodation and Transportation",
                   "Accommodation and transportation are coordinated as integral components of your medical travel journey, tailored to your individual itinerary and relevant recovery planning.", body, cls="logi", hid="logistics", tone="tone-cream")

def package_cards(cur, link=True):
    out = []
    for p in PACKAGES:
        note = f'<p class="pkg-note">{esc(p["note"])}</p>' if p.get("note") else ""
        out.append(f'''<article class="pkg{" pkg-feature" if p["key"]=="executive" else ""}">
<p class="eyebrow">{esc(p["kind"])}</p><h3>{esc(p["name"])}</h3>
<p class="price">{esc(p["price"])}</p>{note}
{disclosure("disclosure-in-card")}
<ul class="pkg-meta"><li>{esc(p["audience"])}</li><li>{esc(p["stay"])}. Length of stay is confirmed in your written proposal and follows your treating clinician's advice.</li></ul>
<p class="small">Your written proposal lists the confirmed coordination inclusions and exclusions for your package.</p>
{('<a class="btn btn-navy btn-block" href="'+rel(cur,"contact/#enquiry")+'">Enquire about '+esc(p["name"])+'</a>') if link else ""}</article>''')
    return '<div class="pkg-grid">' + "".join(out) + "</div>"

def enquiry_cta(cur, tone="tone-navy"):
    vid = f'<a class="btn btn-outline-light" href="{VIDEO_CONSULT_URL}">Schedule Video Consultation</a>' if VIDEO_CONSULT_URL else ""
    return f'''<section class="section cta-band {tone}"><div class="container cta-inner"><p class="eyebrow eyebrow-on-dark">TAKE THE FIRST STEP</p>
<h2>Start Your Medical Travel Enquiry</h2><p class="lead-sm">Tell us what you would like to explore, and our team can help you understand the coordination process and practical next steps.</p>
<div class="btn-row"><a class="btn btn-gold" href="{rel(cur, "contact/#enquiry")}">Make an Enquiry</a>{vid}</div></div></section>'''

def contact_cards(cur, with_h=True):
    wa_au = "https://wa.me/" + PHONE_AU.replace("+", "").replace(" ", "")
    wa_ae = "https://wa.me/" + PHONE_UAE.replace("+", "").replace(" ", "")
    vid = f'<a class="btn btn-outline-navy" href="{VIDEO_CONSULT_URL}">Schedule Video Call</a>' if VIDEO_CONSULT_URL else ""
    cards = f'''<div class="cards3 contact-cards">
<article class="card"><p class="eyebrow">AUSTRALIA DESK</p><h3>Sydney &amp; Melbourne</h3>
<p><a class="big-link" href="tel:{PHONE_AU.replace(" ","")}">{PHONE_AU}</a></p>
<a class="btn btn-navy" href="{wa_au}" rel="noopener noreferrer" target="_blank">WhatsApp Australia<span class="sr-only"> (opens in a new tab)</span></a></article>
<article class="card"><p class="eyebrow">UAE DESK</p><h3>Dubai &amp; GCC</h3>
<p><a class="big-link" href="tel:{PHONE_UAE.replace(" ","")}">{PHONE_UAE}</a></p>
<a class="btn btn-navy" href="{wa_ae}" rel="noopener noreferrer" target="_blank">WhatsApp UAE<span class="sr-only"> (opens in a new tab)</span></a></article>
<article class="card"><p class="eyebrow">TÜRKIYE OPERATIONS</p><h3>Istanbul Hub</h3>
<p><a class="big-link" href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>In-country coordination and liaison during your stay.</p>{vid}</article></div>
<p class="emergency" role="note"><strong>Emergency notice:</strong> in a medical emergency in Türkiye, call <strong>112</strong>. This is the emergency service and is separate from threeeight35° contact details.</p>'''
    if not with_h: return cards
    return section("PATIENT CONCIERGE", "Contact Our Care Team", "Reach our Australian, UAE or Türkiye coordination contacts directly or submit an enquiry below.", cards, tone="tone-cream", hid="contact-team")

JOURNEY = [
 ("Make an enquiry", "Tell us which treatment category you would like to explore and your preferred travel timing. Please do not send medical records, test results, passport or payment details through the website form."),
 ("Provider introductions and quotations", "We connect you with independent healthcare providers and hospitals in Istanbul and arrange consultations and quotations."),
 ("Preliminary provider review, with your authorisation", "Where appropriate, relevant health information may be provided to independent healthcare professionals in Türkiye for preliminary review. This follows a private health-information and overseas-disclosure workflow, not the public web form."),
 ("Receive your written proposal", "Before you proceed you receive your selected coordination package, confirmed inclusions and exclusions, separately itemised travel arrangements and the provider's treatment quotation."),
 ("Travel and stay coordination", "Accommodation, private transfers and English-speaking support during your stay are coordinated where they are confirmed in your written proposal."),
 ("Treatment by your independent provider", "Clinical assessment, suitability, informed consent and all treatment decisions, including when you are fit to fly home, remain with the treating healthcare professionals."),
 ("Returning home", "Follow-up coordination continues after you return home. Confirm in advance which records you will bring home and the plan for any concerns after returning to Australia."),
]
def journey_list(cur):
    return '<ol class="steps">' + "".join(f'<li><span class="step-n" aria-hidden="true">{i+1}</span><div><h3>{esc(h)}</h3><p>{esc(b)}</p></div></li>' for i, (h, b) in enumerate(JOURNEY)) + "</ol>"

def founder_block(cur, full=True):
    pic = (f'<picture><source type="image/webp" srcset="{rel(cur,"assets/img/founder-hommam-azizieh-360.webp")} 360w, {rel(cur,"assets/img/founder-hommam-azizieh-600.webp")} 600w, {rel(cur,"assets/img/founder-hommam-azizieh-843.webp")} 843w" sizes="(min-width: 800px) 36vw, 80vw">'
           f'<img src="{rel(cur,"assets/img/founder-hommam-azizieh-843.jpg")}" width="843" height="1197" alt="Hommam Azizieh, Founder of threeeight35° Medical Travel Agency" class="founder-img" loading="lazy" decoding="async"></picture>')
    bio = ('<p>Based in Abu Dhabi for more than 15 years, Hommam speaks English, Arabic and Turkish and has two years of experience working in medical tourism in Istanbul across patient relations and business development.</p>'
           '<p>That experience highlighted how difficult it can be for international patients to navigate treatment information, quotations, travel arrangements and communication across borders. threeeight35° was created to provide a clearer and better-coordinated experience.</p>'
           '<p>Hommam is not a clinician and does not provide medical advice or recommend treatment. His role is to help ensure each patient\'s medical travel journey is clearly explained, carefully organised and practically coordinated, while all clinical decisions remain with the treating healthcare professionals.</p>')
    more = "" if full else f'<a class="more" href="{rel(cur, "about/")}">About threeeight35° <span aria-hidden="true">→</span></a>'
    if not full: bio = bio.split("</p>")[0] + "</p>" + bio.split("</p>")[2] + "</p>"
    return f'''<div class="founder"><figure class="founder-fig">{pic}<figcaption>Hommam Azizieh — Founder, threeeight35° Medical Travel Agency</figcaption></figure>
<div class="founder-text"><p class="eyebrow">MEET THE FOUNDER</p><h3>Hommam Azizieh</h3><p class="role">Founder, threeeight35° Medical Travel Agency · Based in Abu Dhabi</p>{esc_html_p(bio)}{more}</div></div>'''

def esc_html_p(s): return typo(s)

def status_banner(kind):
    if kind == "held":
        return ('<div class="banner banner-hold" role="note"><strong>Under specialist review.</strong> This topic is retained in our catalogue, but we are not publishing patient guidance on it until specialist clinical review is complete. '
                'You can still ask us how medical travel coordination works.</div>')
    return ('<div class="banner" role="note"><strong>Clinical information is under review.</strong> Treatment-specific clinical content for this page (such as definitions, suitability, risks and recovery) is not published here yet. '
            'It will be added only after review by qualified clinicians.</div>')
