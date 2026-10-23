# -*- coding: utf-8 -*-
from lib import *

def cta_btn(cls, href, label, extra=""):
    return f'<a class="btn {cls}" href="{href}"{extra}>{label}</a>'

def disclosure(cls=""):
    head, rest = L((DISCLOSURE.split(". ",1)[0] + ".", DISCLOSURE.split(". ",1)[1]), DISCLOSURE_AR)
    return f'<p class="disclosure {cls}"><strong>{esc(head)}</strong> {esc(rest)}</p>'

def section(eyebrow, h2, intro="", body="", cls="", hid=None, tone=""):
    i = f'<p class="lead-sm">{esc(intro)}</p>' if intro else ""
    e = f'<p class="eyebrow">{esc(eyebrow)}</p>' if eyebrow else ""
    hid = f' id="{hid}"' if hid else ""
    return f'<section class="section {tone} {cls}"{hid}><div class="container"><div class="section-head">{e}<h2>{esc(h2)}</h2>{i}</div>{body}</div></section>'

def ar_count(n, few, many):
    """Arabic count phrase: 3–10 take the plural (صفحات), 11+ take the singular (صفحة)."""
    return f"{n} {few if 3 <= n <= 10 else many}"

def treatment_pages(n):
    return L(f"{n} treatment pages", ar_count(n, "صفحات علاجية", "صفحة علاجية"))

def categories_grid(cur):
    cards = []
    for cid, slug, name, stem, alt, intro in CATS:
        n = sum(len(ids) for _, ids in GROUPS[cid])
        if is_ar(): name, intro, alt = CAT_AR[cid][0], CAT_AR[cid][1], CAT_AR[cid][2]
        cards.append(f'''<article class="cat-card">
<a class="cat-media" href="{rel(cur, cat_dir(cid))}" tabindex="-1" aria-hidden="true">{img(cur, stem, alt, "(min-width: 1100px) 24vw, (min-width: 700px) 45vw, 92vw", cls="cat-img")}</a>
<div class="cat-body"><p class="cat-count">{treatment_pages(n)}</p>
<h3><a href="{rel(cur, cat_dir(cid))}">{esc(name)}</a></h3>
<p>{esc(intro.split(". ")[0] + ".")}</p>
<a class="more" href="{rel(cur, cat_dir(cid))}">{L("Explore category", "استكشف الفئة")} <span aria-hidden="true">{arrow()}</span><span class="sr-only"> {esc(name)}</span></a></div></article>''')
    return f'<div class="cat-grid">{"".join(cards)}</div>'

def why_cards():
    cards = L([("Personalised Coordination", "From your initial enquiry through pre-departure planning, you receive dedicated coordination support for the practical parts of your journey."),
               ("Preliminary Provider Review", "Where appropriate and with your authorisation, relevant health information may be provided to independent healthcare professionals in Türkiye for preliminary review. Clinical assessment, suitability and treatment decisions remain entirely with the treating healthcare professionals."),
               ("Support in Three Languages", "Coordination support in English, Arabic and Turkish can assist with practical communication and attendance arrangements around scheduled consultations and clinical appointments.")],
              [("تنسيق شخصي", "من استفسارك الأول وحتى التخطيط لما قبل السفر، تحصل على دعم مخصّص لتنسيق الجوانب العملية من رحلتك."),
               ("تقييم أولي من مقدّم الرعاية", "عند الاقتضاء وبموافقتك، قد تُقدَّم المعلومات الصحية ذات الصلة إلى أخصائيي رعاية صحية مستقلين في تركيا لإجراء تقييم أولي. ويبقى التقييم السريري وتحديد ملاءمة العلاج وقرارات العلاج بالكامل من مسؤولية أخصائيي الرعاية الصحية المعالجين."),
               ("دعم بثلاث لغات", "يمكن لدعم التنسيق باللغات العربية والإنجليزية والتركية أن يساعدك في التواصل العملي وترتيبات الحضور حول الاستشارات والمواعيد الطبية المحددة.")])
    return '<div class="cards3">' + "".join(f'<article class="card"><span class="card-num" aria-hidden="true">{i+1:02d}</span><h3>{esc(h)}</h3><p>{esc(b)}</p></article>' for i, (h, b) in enumerate(cards)) + "</div>"

def accommodation_section(cur, h="h2"):
    hotel = img(cur, "18_accommodation", L("A hotel suite bedroom with a large window overlooking the Bosphorus and the Istanbul skyline at dusk.", "غرفة نوم في جناح فندقي بنافذة كبيرة تطل على مضيق البوسفور وأفق إسطنبول عند الغسق."), "(min-width: 800px) 46vw, 92vw", cls="logi-img")
    car = img(cur, "19_chauffeur_transportation", L("A black minivan parked at a hotel entrance with the Istanbul skyline at sunset behind it.", "سيارة فان سوداء متوقفة عند مدخل فندق وخلفها أفق إسطنبول وقت الغروب."), "(min-width: 800px) 46vw, 92vw", cls="logi-img")
    if not is_ar():
        body = f'''<div class="logi-grid">
<article class="logi-card"><div class="logi-media">{hotel}</div><div class="logi-body"><p class="eyebrow">COMFORT &amp; RELAXATION</p><h3>5-star hotels</h3>
<p>We arrange your stay at a selected 5-star hotel within easy reach of your treating healthcare facility, so you have a comfortable, quiet place to rest between appointments and during recovery. Exact arrangements are confirmed in your written proposal.</p>
<p class="check">Accommodation for you and your guests is included in your package price, for the nights and number of guests shown for your package.</p>
<p class="small">Confirmed in your written proposal. Accommodation is not medical care.</p></div></article>
<article class="logi-card"><div class="logi-media">{car}</div><div class="logi-body"><p class="eyebrow">CONVENIENCE &amp; PRIVACY</p><h3>Private chauffeured cars</h3>
<p>A private driver takes you between the airport, your hotel and your clinic appointments, so you do not need to arrange taxis or find your way around an unfamiliar city. Exact arrangements are confirmed in your written proposal.</p>
<p class="check">Private transfers in Istanbul between the airport, your hotel and clinic appointments are included in your package price.</p>
<p class="small">Confirmed in your written proposal. Transport is not a clinical service.</p></div></article>
</div>
<div class="clarity"><h3>Package Inclusions Clarity</h3><p>Every package includes accommodation and private transfers in Istanbul for the nights and guests shown for that package. If you prefer to arrange your own, we will discuss it with you and quote a final package fee. Extra nights you choose to add are paid directly to the hotel; a longer stay advised by your treating clinician is quoted separately.</p>
<a class="btn btn-gold" href="{rel(cur, "patient-packages/")}">View Packages</a></div>'''
    else:
        body = f'''<div class="logi-grid">
<article class="logi-card"><div class="logi-media">{hotel}</div><div class="logi-body"><p class="eyebrow">الراحة والاسترخاء</p><h3>فنادق 5 نجوم</h3>
<p>نرتّب إقامتك في فندق مختار من فئة 5 نجوم على مقربة من المنشأة الصحية التي تتلقى فيها العلاج، لتحظى بمكان مريح وهادئ للراحة بين المواعيد وخلال فترة التعافي. وتُؤكَّد تفاصيل الترتيبات في عرضك المكتوب.</p>
<p class="check">الإقامة لك ولضيوفك مشمولة في سعر باقتك، لعدد الليالي والضيوف الموضّح لباقتك.</p>
<p class="small">تُؤكَّد في عرضك المكتوب. الإقامة ليست رعاية طبية.</p></div></article>
<article class="logi-card"><div class="logi-media">{car}</div><div class="logi-body"><p class="eyebrow">السهولة والخصوصية</p><h3>سيارات خاصة بسائق</h3>
<p>يتولى سائق خاص نقلك بين المطار وفندقك ومواعيدك في العيادة، فلا تحتاج إلى ترتيب سيارات الأجرة أو البحث عن طريقك في مدينة غير مألوفة. وتُؤكَّد تفاصيل الترتيبات في عرضك المكتوب.</p>
<p class="check">التنقلات الخاصة في إسطنبول بين المطار وفندقك ومواعيدك في العيادة مشمولة في سعر باقتك.</p>
<p class="small">تُؤكَّد في عرضك المكتوب. النقل ليس خدمة سريرية.</p></div></article>
</div>
<div class="clarity"><h3>وضوح ما تشمله الباقة</h3><p>تشمل كل باقة الإقامة والتنقلات الخاصة في إسطنبول لعدد الليالي والضيوف الموضّح لتلك الباقة. إذا كنت تفضّل ترتيب ذلك بنفسك، فسنناقش الأمر معك ونقدّم لك سعراً نهائياً للباقة. تُدفع الليالي الإضافية التي تختارها مباشرةً إلى الفندق، أما الإقامة الأطول التي ينصح بها طبيبك المعالج فتُسعَّر بشكل منفصل.</p>
<a class="btn btn-gold" href="{rel(cur, "patient-packages/")}">عرض الباقات</a></div>'''
    return section(L("COORDINATED LOGISTICS", "ترتيبات منسّقة"), L("Accommodation and Transportation", "الإقامة والتنقلات"),
                   L("Accommodation and transportation are coordinated as integral components of your medical travel journey, tailored to your individual itinerary and relevant recovery planning.",
                     "يُنسَّق كلٌّ من الإقامة والتنقلات كجزء أساسي من رحلتك العلاجية، بما يتناسب مع برنامجك الشخصي وخطة تعافيك."), body, cls="logi", hid="logistics", tone="tone-cream")

def package_cards(cur, link=True):
    out = []
    for p in PACKAGES:
        if is_ar(): p = {**p, **PKG_AR[p["key"]]}
        note = f'<p class="pkg-note">{esc(p["note"])}</p>' if p.get("note") else ""
        incl = L(f'<li>Medical travel coordination</li><li>Accommodation for {esc(p["nights"])} for {esc(p["guests"])}</li><li>Private transfers in Istanbul between the airport, your hotel and clinic appointments</li>',
                 f'<li>تنسيق السفر العلاجي</li><li>إقامة لمدة {esc(p["nights"])} {esc(p["guests"])}</li><li>تنقلات خاصة في إسطنبول بين المطار وفندقك ومواعيدك في العيادة</li>')
        out.append(f'''<article class="pkg{" pkg-feature" if p["key"]=="executive" else ""}">
<p class="eyebrow">{esc(p["kind"])}</p><h3>{esc(p["name"])}</h3>
<p class="price">{L(esc(p["price"]), "<bdi>" + esc(p["price"]) + "</bdi>")}</p>{note}
<p class="pkg-incl-h">{L("Included in the package price", "يشمل سعر الباقة")}</p>
<ul class="pkg-incl">{incl}</ul>
<ul class="pkg-meta"><li>{esc(p["audience"])}</li><li>{L("If your treating clinician advises a longer stay, extra nights are quoted separately.", "إذا نصح طبيبك المعالج بإقامة أطول، تُسعَّر الليالي الإضافية بشكل منفصل.")}</li></ul>
<p class="small">{L("Your written proposal lists the confirmed coordination inclusions and exclusions for your package.", "يوضّح عرضك المكتوب ما تشمله باقتك وما لا تشمله من خدمات التنسيق المؤكَّدة.")}</p>
{('<a class="btn btn-navy btn-block" href="'+rel(cur,"contact/#enquiry")+'">'+L('Enquire about ', 'استفسر عن باقة ')+esc(p["name"])+'</a>') if link else ""}</article>''')
    return disclosure("disclosure-pkgs") + '<div class="pkg-grid">' + "".join(out) + "</div>"

def enquiry_cta(cur, tone="tone-navy"):
    vid = f'<a class="btn btn-outline-light" href="{VIDEO_CONSULT_URL}">{L("Schedule Video Consultation", "احجز استشارة عبر الفيديو")}</a>' if VIDEO_CONSULT_URL else ""
    return f'''<section class="section cta-band {tone}"><div class="container cta-inner"><p class="eyebrow eyebrow-on-dark">{L("TAKE THE FIRST STEP", "ابدأ الخطوة الأولى")}</p>
<h2>{L("Start Your Medical Travel Enquiry", "ابدأ استفسارك عن السفر العلاجي")}</h2><p class="lead-sm">{L("Tell us what you would like to explore, and our team can help you understand the coordination process and practical next steps.", "أخبرنا بما ترغب في استكشافه، وسيساعدك فريقنا على فهم آلية التنسيق والخطوات العملية التالية.")}</p>
<div class="btn-row"><a class="btn btn-gold" href="{rel(cur, "contact/#enquiry")}">{L("Make an Enquiry", "أرسل استفسارك")}</a>{vid}</div></div></section>'''

def contact_cards(cur, with_h=True):
    wa_au = "https://wa.me/" + PHONE_AU.replace("+", "").replace(" ", "")
    wa_ae = "https://wa.me/" + PHONE_UAE.replace("+", "").replace(" ", "")
    vid = f'<a class="btn btn-outline-navy" href="{VIDEO_CONSULT_URL}">{L("Schedule Video Call", "احجز مكالمة فيديو")}</a>' if VIDEO_CONSULT_URL else ""
    new_tab = L(" (opens in a new tab)", " (يفتح في علامة تبويب جديدة)")
    cards = f'''<div class="cards3 contact-cards">
<article class="card"><p class="eyebrow">{L("CONTACT LINE", "خط التواصل")}</p><h3>{L("Australia &amp; International", "أستراليا والدول الأخرى")}</h3>
<p><a class="big-link" href="tel:{PHONE_AU.replace(" ","")}">{ltr(PHONE_AU)}</a></p>
<a class="btn btn-navy" href="{wa_au}" rel="noopener noreferrer" target="_blank">{L("WhatsApp", "واتساب")}<span class="sr-only">{L(" Australia &amp; International", " أستراليا والدول الأخرى")}{new_tab}</span></a></article>
<article class="card"><p class="eyebrow">{L("CONTACT LINE", "خط التواصل")}</p><h3>{L("UAE &amp; GCC", "الإمارات ودول الخليج")}</h3>
<p><a class="big-link" href="tel:{PHONE_UAE.replace(" ","")}">{ltr(PHONE_UAE)}</a></p>
<a class="btn btn-navy" href="{wa_ae}" rel="noopener noreferrer" target="_blank">{L("WhatsApp", "واتساب")}<span class="sr-only">{L(" UAE &amp; GCC", " الإمارات ودول الخليج")}{new_tab}</span></a></article>
<article class="card"><p class="eyebrow">{L("DURING YOUR STAY", "خلال إقامتك")}</p><h3>{L("Istanbul", "إسطنبول")}</h3>
<p>{L("A coordinator supports you during your stay in Istanbul. Reach them by email or on WhatsApp through the UAE &amp; GCC line.", "يدعمك منسّق خلال إقامتك في إسطنبول. تواصل معه عبر البريد الإلكتروني أو عبر واتساب على خط الإمارات ودول الخليج.")}</p>
<p><a class="big-link" href="mailto:{EMAIL}">{EMAIL}</a></p>{vid}</article></div>
<p class="emergency" role="note">{L("<strong>Emergency notice:</strong> in a medical emergency in Türkiye, call <strong>112</strong>. This is the emergency service and is separate from threeeight35° contact details.", "<strong>تنبيه للطوارئ:</strong> في حالة الطوارئ الطبية في تركيا، اتصل على الرقم <strong>112</strong>. هذا رقم خدمة الطوارئ، وهو منفصل عن أرقام التواصل مع threeeight35°.")}</p>'''
    if not with_h: return cards
    return section(L("PATIENT CONCIERGE", "خدمة المرضى"), L("Contact Our Care Team", "تواصل مع فريقنا"),
                   L("Reach our Australian, UAE or Türkiye coordination contacts directly or submit an enquiry below.", "تواصل مباشرةً مع مكاتب التنسيق في أستراليا أو الإمارات أو تركيا، أو أرسل استفسارك أدناه."), cards, tone="tone-cream", hid="contact-team")

JOURNEY = [
 ("Make an enquiry", "Tell us which treatment category you would like to explore and your preferred travel timing. Please do not send medical records, test results, passport or payment details through the website form."),
 ("Provider introductions and quotations", "We connect you with independent healthcare providers and hospitals in Istanbul and arrange consultations and quotations."),
 ("Preliminary provider review, with your authorisation", "Where appropriate, relevant health information may be provided to independent healthcare professionals in Türkiye for preliminary review. This follows a private health-information and overseas-disclosure workflow, not the public web form."),
 ("Receive your written proposal", "Before you proceed you receive your selected coordination package, confirmed inclusions and exclusions, any extras quoted separately and the provider's treatment quotation."),
 ("Travel and stay coordination", "Your accommodation and private transfers in Istanbul are included in your package, and we coordinate support in English, Arabic and Turkish during your stay."),
 ("Treatment by your independent provider", "Clinical assessment, suitability, informed consent and all treatment decisions, including when you are fit to fly home, remain with the treating healthcare professionals."),
 ("Returning home", "Follow-up coordination continues after you return home. Confirm in advance which records you will bring home and the plan for any concerns once you're back."),
]
def journey_list(cur):
    return '<ol class="steps">' + "".join(f'<li><span class="step-n" aria-hidden="true">{i+1}</span><div><h3>{esc(h)}</h3><p>{esc(b)}</p></div></li>' for i, (h, b) in enumerate(L(JOURNEY, JOURNEY_AR))) + "</ol>"

def founder_block(cur, full=True):
    alt = L("Hommam Azizieh, Founder of threeeight35° Medical Travel Agency", "همام عزيزية، مؤسس وكالة threeeight35° للسفر العلاجي")
    pic = (f'<picture><source type="image/webp" srcset="{rel(cur,"assets/img/founder-hommam-azizieh-360.webp")} 360w, {rel(cur,"assets/img/founder-hommam-azizieh-600.webp")} 600w, {rel(cur,"assets/img/founder-hommam-azizieh-843.webp")} 843w" sizes="(min-width: 800px) 36vw, 80vw">'
           f'<img src="{rel(cur,"assets/img/founder-hommam-azizieh-843.jpg")}" width="843" height="1197" alt="{alt}" class="founder-img" loading="lazy" decoding="async"></picture>')
    # Founder bio in Hommam's own voice on every page (owner decision 2026-10-23). The home page shows the first and last
    # paragraphs; the About page (full=True) also shows why he started threeeight35°.
    intro = L("<p>I've been based in Abu Dhabi for more than 15 years and speak English, Arabic and Turkish. I specialise in Marketing &amp; Production, with expertise in Photography. "
              "Before founding threeeight35° Medical Travel Agency, I spent two years working in medical tourism in Istanbul, where I gained experience in patient relations and business development.</p>",
              "<p>أقيم في أبوظبي منذ أكثر من 15 عاماً، وأتحدث الإنجليزية والعربية والتركية. أتخصص في التسويق والإنتاج، ولديّ خبرة في التصوير الفوتوغرافي. "
              "وقبل تأسيس وكالة threeeight35° للسفر العلاجي، عملت لمدة عامين في مجال السياحة العلاجية في إسطنبول، حيث اكتسبت خبرة في علاقات المرضى وتطوير الأعمال.</p>")
    why = L("<p>That experience showed me how difficult it can be for international patients to navigate treatment information, quotations, travel arrangements and communication across borders. "
            "I created threeeight35° to provide a clearer and better-coordinated experience.</p>",
            "<p>كشفت لي تلك التجربة مدى صعوبة تعامل المرضى الدوليين مع معلومات العلاج وعروض الأسعار وترتيبات السفر والتواصل عبر الحدود. ولهذا أسست threeeight35° لتقديم تجربة أوضح وأفضل تنسيقاً.</p>")
    role_p = L("<p>I'm not a clinician, and I don't provide medical advice or recommend treatments. My role is to make your medical travel journey clear, organised and carefully coordinated from beginning to end. "
               "I take care of the practical details around your journey, while all clinical decisions remain with your treating healthcare professionals.</p>",
               "<p>لست طبيباً، ولا أقدّم استشارات طبية ولا أوصي بأي علاج. يتمثل دوري في جعل رحلتك العلاجية واضحة ومنظّمة ومنسّقة بعناية من البداية إلى النهاية. "
               "أتولى التفاصيل العملية لرحلتك، بينما تبقى جميع القرارات السريرية من مسؤولية أخصائيي الرعاية الصحية المعالجين.</p>")
    bio = intro + (why if full else "") + role_p
    role = L("Founder, threeeight35° Medical Travel Agency | Abu Dhabi", "مؤسس وكالة threeeight35° للسفر العلاجي | أبوظبي")
    more = "" if full else f'<a class="more" href="{rel(cur, "about/")}">{L("About threeeight35°", "عن threeeight35°")} <span aria-hidden="true">{arrow()}</span></a>'
    return f'''<div class="founder"><figure class="founder-fig">{pic}<figcaption>{L("Hommam Azizieh — Founder, threeeight35° Medical Travel Agency", "همام عزيزية — مؤسس وكالة threeeight35° للسفر العلاجي")}</figcaption></figure>
<div class="founder-text"><p class="eyebrow">{L("MEET THE FOUNDER", "تعرّف على المؤسس")}</p><h3>{L("Hommam Azizieh", "همام عزيزية")}</h3><p class="role">{role}</p>{esc_html_p(bio)}{more}</div></div>'''

def esc_html_p(s): return typo(s)
