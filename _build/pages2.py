# -*- coding: utf-8 -*-
from pages import *
from legal import *

def pending(msg): return f'<div class="banner banner-hold" role="note"><strong>{L("Status:", "ملاحظة:")}</strong> {esc(msg)}</div>'

def qa(h, body_html): return f'<section class="qa"><h2>{esc(h)}</h2>{body_html}</section>'

# ---------------- Packages ----------------
def build_packages():
    cur = "patient-packages/"
    p = dict(path=cur, id="SUP-09", kind="Packages & pricing", title=L("Medical Travel Coordination Packages | threeeight35°", "باقات تنسيق السفر العلاجي | threeeight35°"),
             desc=L("Essential Care A$4,950, Executive Wellness & Recovery A$9,900, VIP from A$14,900. Includes accommodation and Istanbul transfers; treatment and flights extra.",
                    "الرعاية الأساسية A$4,950، والعافية والتعافي التنفيذية A$9,900، والرحلة المخصصة VIP ابتداءً من A$14,900. تشمل الإقامة والتنقلات؛ العلاج والطيران منفصلان."),
             indexable=True, status="Business-confirmed package pricing; legal/consumer-law review recommended; payment/cancellation/refund terms withheld pending legal review")
    three = L('''<div class="cards3"><article class="card"><span class="card-num" aria-hidden="true">1</span><h3>Your treatment</h3><p>Quoted by and paid directly to the independent clinic or hospital. threeeight35° does not publish, determine or collect medical treatment fees.</p></article>
<article class="card"><span class="card-num" aria-hidden="true">2</span><h3>Your threeeight35° package</h3><p>Paid to threeeight35°. The fixed package price covers coordination, accommodation and private transfers in Istanbul for the nights and guests shown for your package.</p></article>
<article class="card"><span class="card-num" aria-hidden="true">3</span><h3>Your flights and any extras</h3><p>You book and pay for your own flights. Extra nights you choose to add are paid directly to the hotel; a longer stay advised by your treating clinician is quoted separately.</p></article></div>''',
'''<div class="cards3"><article class="card"><span class="card-num" aria-hidden="true">1</span><h3>علاجك</h3><p>يُسعَّر ويُدفع مباشرةً إلى العيادة أو المستشفى المستقل. ولا تنشر threeeight35° أسعار العلاج الطبي ولا تحدّدها ولا تتقاضاها.</p></article>
<article class="card"><span class="card-num" aria-hidden="true">2</span><h3>باقتك من threeeight35°</h3><p>تُدفع إلى threeeight35°. ويغطي السعر الثابت للباقة التنسيق والإقامة والتنقلات الخاصة في إسطنبول لعدد الليالي والضيوف الموضّح لباقتك.</p></article>
<article class="card"><span class="card-num" aria-hidden="true">3</span><h3>رحلات الطيران وأي إضافات</h3><p>تحجز رحلات الطيران وتدفع ثمنها بنفسك. تُدفع الليالي الإضافية التي تختارها مباشرةً إلى الفندق، أما الإقامة الأطول التي ينصح بها طبيبك المعالج فتُسعَّر بشكل منفصل.</p></article></div>''')
    main = pagehead(L("TAILORED COORDINATION PACKAGES", "باقات تنسيق مصمّمة لك"), L("Medical Travel Coordination Packages", "باقات تنسيق السفر العلاجي"),
                    L("Choose the level of coordination that fits your journey. threeeight35° package prices include our non-clinical coordination, your accommodation and private transfers in Istanbul. Medical treatment and flights are paid separately.",
                      "اختر مستوى التنسيق الذي يناسب رحلتك. تشمل أسعار باقات threeeight35° خدمات التنسيق غير السريرية وإقامتك وتنقلاتك الخاصة في إسطنبول. ويُدفع العلاج الطبي وتذاكر الطيران بشكل منفصل."))
    main += section(L("WHO YOU PAY, AND FOR WHAT", "لمن تدفع، ومقابل ماذا"), L("Three separate parts of your journey cost", "ثلاثة أجزاء منفصلة من تكلفة رحلتك"), "", three, tone="tone-cream")
    main += section(L("PACKAGES", "الباقات"), L("Choose your coordination package", "اختر باقة التنسيق"), L("All prices are in Australian dollars (AUD).", "جميع الأسعار بالدولار الأسترالي (AUD)."), package_cards(cur) +
        L('<div class="prose narrow"><p>Before you proceed you receive a written, itemised proposal showing your selected coordination package, confirmed inclusions and exclusions, any extras quoted separately and the independent provider\'s treatment quotation. A treatment fee is never combined with a threeeight35° package price into a single advertised treatment price.</p></div>',
          '<div class="prose narrow"><p>قبل المتابعة، تستلم عرضاً مكتوباً ومفصّلاً يوضّح باقة التنسيق التي اخترتها، وما هو مشمول وغير مشمول، وأي إضافات مسعّرة بشكل منفصل، وعرض سعر العلاج من مقدّم الرعاية المستقل. ولا تُدمج رسوم العلاج أبداً مع سعر باقة threeeight35° في سعر علاج واحد معلَن.</p></div>'))
    main += accommodation_section(cur)
    main += section("", L("Questions about packages", "أسئلة حول الباقات"), "",
        L(f'<div class="prose"><p>See our <a href="{rel(cur,"faqs/")}">FAQs</a>, read how <a href="{rel(cur,"how-it-works/")}">the journey works</a> or <a href="{rel(cur,"contact/#enquiry")}">make an enquiry</a>. Full payment, cancellation and refund terms are being finalised and will be published in the <a href="{rel(cur,"terms/")}">Terms &amp; Conditions</a>.</p></div>',
          f'<div class="prose"><p>اطّلع على <a href="{rel(cur,"faqs/")}">الأسئلة الشائعة</a>، واقرأ <a href="{rel(cur,"how-it-works/")}">كيف تسير الرحلة</a>، أو <a href="{rel(cur,"contact/#enquiry")}">أرسل استفسارك</a>. يجري حالياً إعداد الشروط الكاملة للدفع والإلغاء والاسترداد، وستُنشر في <a href="{rel(cur,"terms/")}">الشروط والأحكام</a>.</p></div>'))
    main += enquiry_cta(cur)
    add(p, main, "packages", crumbs=[(L("Home", "الرئيسية"), ""), (L("Patient Packages", "الباقات"), cur)], extra_ld=[service_ld(cur)])

def service_ld(cur):
    offers = []
    for pk in PACKAGES:
        amount = "".join(c for c in pk["price"] if c.isdigit())
        ar = PKG_AR[pk["key"]]
        o = {"@type": "Offer", "name": L(pk["name"], ar["name"]), "url": page_url(cur), "priceCurrency": "AUD",
             "description": L(f"Medical travel coordination, accommodation for {pk['nights']} for {pk['guests']}, and private transfers in Istanbul. Medical treatment and flights are not included.",
                              f"تنسيق السفر العلاجي، وإقامة لمدة {ar['nights']} {ar['guests']}، وتنقلات خاصة في إسطنبول. العلاج الطبي وتذاكر الطيران غير مشمولة.")}
        if pk["price"].startswith("From"):
            o["priceSpecification"] = {"@type": "PriceSpecification", "minPrice": amount, "priceCurrency": "AUD"}
        else:
            o["price"] = amount
        offers.append(o)
    return {"@context": "https://schema.org", "@type": "Service", "@id": page_url(cur) + "#service",
            "name": L("Medical travel coordination", "تنسيق السفر العلاجي"), "serviceType": "Medical travel coordination",
            "description": L("Non-clinical coordination of medical travel to Türkiye, including accommodation and private transfers in Istanbul. threeeight35° is not a healthcare provider; treatment is provided and charged by independent clinics and hospitals.",
                             "تنسيق غير سريري للسفر العلاجي إلى تركيا، يشمل الإقامة والتنقلات الخاصة في إسطنبول. threeeight35° ليست مقدّم رعاية صحية، إذ تقدّم العيادات والمستشفيات المستقلة العلاج وتتقاضى رسومه."),
            "provider": {"@id": BASE + "#organization"},
            "areaServed": [{"@type": "Country", "name": "Australia"}, {"@type": "Country", "name": "United Arab Emirates"}],
            "offers": offers}

# ---------------- How it works ----------------
def build_how():
    cur = "how-it-works/"
    p = dict(path=cur, id="SUP-HOW", kind="How it works (derived from v11 statements)", title=L("How Medical Travel Coordination Works | threeeight35°", "كيف يعمل تنسيق السفر العلاجي | threeeight35°"),
             desc=L("How threeeight35° coordinates the practical side of medical travel to Türkiye, from first enquiry to follow-up after you return to Australia.",
                    "كيف تنسّق threeeight35° الجانب العملي من السفر العلاجي إلى تركيا، من الاستفسار الأول حتى المتابعة بعد عودتك."),
             indexable=True, status="Derived from Version 11 statements; editorial approval required (v11 has no dedicated How It Works record)")
    main = pagehead(L("THE PATIENT JOURNEY", "رحلة المريض"), L("How It Works", "كيف نعمل"),
                    L("A clear pathway for the practical side of medical travel, with a firm boundary: we coordinate, and independent licensed clinicians make every medical decision.",
                      "مسار واضح للجانب العملي من السفر العلاجي، مع حدّ فاصل ثابت: نحن ننسّق، والأطباء المستقلون المرخّصون يتخذون كل قرار طبي."))
    main += section("", L("Your coordination journey", "رحلة التنسيق خطوة بخطوة"), "", journey_list(cur))
    links = L(f'<p><a href="{rel(cur,"medical-travel-turkiye-from-australia/")}">Read more about medical travel from Australia</a> · <a href="{rel(cur,"privacy-overseas-health-information-disclosure/")}">Privacy and overseas health-information disclosure</a></p>', "")
    main += f'''<section class="section tone-cream"><div class="container"><div class="notice-card"><h2>{L("Important coordination notice", "تنويه مهم بشأن التنسيق")}</h2><p>{L(esc(NOTICE.replace("Important Medical Coordination Notice: ","")), NOTICE_AR_BODY)}</p>
{links}</div></div></section>'''
    main += enquiry_cta(cur)
    add(p, main, "how", crumbs=[(L("Home", "الرئيسية"), ""), (L("How It Works", "كيف نعمل"), cur)])

# ---------------- About ----------------
def build_about():
    cur = "about/"
    p = dict(path=cur, id="SUP-03", kind="About / Organisation", title=L("About threeeight35° Medical Travel Agency", "عن وكالة threeeight35° للسفر العلاجي"),
             desc=L("Learn about threeeight35° Medical Travel Agency, our coordination role, mission, values and founder, Hommam Azizieh.",
                    "تعرّف على وكالة threeeight35° للسفر العلاجي ودورنا في التنسيق ورسالتنا وقيمنا ومؤسسنا همام عزيزية."),
             indexable=True, status="Editorially ready after factual/business verification and technical QA")
    values = L([("Patient-Centred Coordination", "We listen to each patient's needs, preferences and circumstances and, where the patient wishes, include companions or family members in appropriate parts of the planning process."),
                ("Transparency", "We provide itemised written quotations, confirm inclusions in writing and never promise medical outcomes or risk-free procedures."),
                ("Privacy and Discretion", "We handle personal and health information with care, restrict access to authorised personnel and do not ask patients to submit medical records or clinical photographs through public website forms."),
                ("Clear Boundaries", "We coordinate. Independent, licensed clinicians make every medical decision."),
                ("Precision", "We aim for reliable, detail-oriented coordination at every stage of the journey."),
                ("Care and Dignity", "We treat every patient and companion with attention and respect.")],
               [("تنسيق يتمحور حول المريض", "نستمع إلى احتياجات كل مريض وتفضيلاته وظروفه، ونُشرك مرافقيه أو أفراد عائلته في المراحل المناسبة من التخطيط متى رغب في ذلك."),
                ("الشفافية", "نقدّم عروض أسعار مكتوبة ومفصّلة، ونؤكّد ما تشمله الخدمة كتابياً، ولا نَعِد أبداً بنتائج طبية أو بإجراءات خالية من المخاطر."),
                ("الخصوصية والتكتّم", "نتعامل مع المعلومات الشخصية والصحية بعناية، ونقصر الوصول إليها على الموظفين المخوّلين، ولا نطلب من المرضى إرسال سجلات طبية أو صور سريرية عبر نماذج الموقع العامة."),
                ("حدود واضحة", "نحن ننسّق، والأطباء المستقلون المرخّصون يتخذون كل قرار طبي."),
                ("الدقة", "نسعى إلى تنسيق موثوق يهتم بالتفاصيل في كل مرحلة من مراحل الرحلة."),
                ("الرعاية والكرامة", "نعامل كل مريض ومرافق باهتمام واحترام.")])
    vh = '<div class="cards3 values">' + "".join(f'<article class="card"><h3>{esc(a)}</h3><p>{esc(b)}</p></article>' for a, b in values) + "</div>"
    main = pagehead(L("AGENCY PHILOSOPHY", "فلسفة الوكالة"), L("About threeeight35° Medical Travel Agency", "عن وكالة threeeight35° للسفر العلاجي"))
    main += L(f'''<section class="section"><div class="container prose"><h2>About Us</h2>
<p>threeeight35° Medical Travel Agency is an independent medical travel coordination service for patients from Australia, the UAE and other international markets who are exploring treatment in Türkiye. We manage the practical side of the journey. We connect patients with independent healthcare providers and hospitals in Istanbul, arrange consultations and quotations, and coordinate accommodation, private transfers and support in English, Arabic and Turkish during the stay.</p>
<p>Our name reflects how we work. Like a coordinate, we aim to be precise, dependable and clear about where you stand at every step. From the first enquiry through our Australia &amp; International or UAE &amp; GCC contact line to follow-up coordination after returning home, patients work with a dedicated coordinator and receive written, itemised proposals before committing.</p>
<p><strong>We are not a healthcare provider.</strong> We do not diagnose, prescribe or recommend treatment. Every clinical assessment and all medical care are provided independently by licensed healthcare professionals in Türkiye. Patients are encouraged to discuss overseas treatment with their usual doctor or an appropriate healthcare professional where relevant.</p>
<p class="small">Australian Business Number (ABN): {ABN}</p></div></section>''',
f'''<section class="section"><div class="container prose"><h2>من نحن</h2>
<p>وكالة threeeight35° للسفر العلاجي هي خدمة مستقلة لتنسيق السفر العلاجي للمرضى من أستراليا والإمارات العربية المتحدة والأسواق الدولية الأخرى الذين يستكشفون العلاج في تركيا. نتولى الجانب العملي من الرحلة: نربط المرضى بمقدّمي رعاية صحية ومستشفيات مستقلة في إسطنبول، ونرتّب الاستشارات وعروض الأسعار، وننسّق الإقامة والتنقلات الخاصة والدعم باللغات العربية والإنجليزية والتركية خلال الإقامة.</p>
<p>يعكس اسمنا طريقة عملنا. فكما تحدّد الإحداثيات موقعاً بدقة، نسعى إلى أن نكون دقيقين وموثوقين وواضحين بشأن موقعك في كل خطوة. ومن الاستفسار الأول عبر خط التواصل لأستراليا والدول الأخرى أو خط الإمارات ودول الخليج حتى تنسيق المتابعة بعد العودة، يعمل المرضى مع منسّق مخصّص ويستلمون عروضاً مكتوبة ومفصّلة قبل الالتزام.</p>
<p><strong>لسنا مقدّم رعاية صحية.</strong> نحن لا نشخّص ولا نصف ولا نوصي بأي علاج. ويُقدَّم كل تقييم سريري وكل رعاية طبية بشكل مستقل من قِبل أخصائيي رعاية صحية مرخّصين في تركيا. ونشجّع المرضى على مناقشة العلاج في الخارج مع طبيبهم المعتاد أو مع أخصائي رعاية صحية مناسب عند الاقتضاء.</p>
<p class="small">رقم الأعمال الأسترالي (ABN): {ABN}</p></div></section>''')
    main += section("", L("Our Mission", "رسالتنا"), "", L('<div class="prose"><p>To make international medical travel clearer and better organised for patients and their families through transparent information, personalised coordination and practical support, while respecting privacy and leaving every clinical decision to independent medical professionals.</p></div>',
                                                         '<div class="prose"><p>أن نجعل السفر العلاجي الدولي أوضح وأفضل تنظيماً للمرضى وعائلاتهم، من خلال معلومات شفافة وتنسيق شخصي ودعم عملي، مع احترام الخصوصية وترك كل قرار سريري لأخصائيين طبيين مستقلين.</p></div>'), tone="tone-cream")
    main += section("", L("Our Vision", "رؤيتنا"), "", L('<div class="prose"><p>To be a respected name in international medical travel coordination, known for a standard of transparency and care that lets patients cross borders for treatment with well-informed confidence.</p></div>',
                                                       '<div class="prose"><p>أن نكون اسماً محترماً في تنسيق السفر العلاجي الدولي، معروفاً بمستوى من الشفافية والرعاية يتيح للمرضى عبور الحدود لتلقي العلاج بثقة مبنية على معرفة واضحة.</p></div>'))
    main += section("", L("Our Core Values", "قيمنا الأساسية"), "", vh, tone="tone-cream")
    main += f'<section class="section" id="founder"><div class="container">{founder_block(cur)}</div></section>'
    main += L(f'''<section class="section tone-cream"><div class="container prose"><h2>Where to go next</h2><ul class="linklist"><li><a href="{rel(cur,"contact/#enquiry")}">Contact / Confidential Enquiry</a></li><li><a href="{rel(cur,"treatments/")}">Treatments Catalogue</a></li><li><a href="{rel(cur,"medical-travel-turkiye-from-australia/")}">Medical Travel to Türkiye from Australia</a></li><li><a href="{rel(cur,"privacy/")}">Privacy Policy</a></li><li><a href="{rel(cur,"medical-disclaimer/")}">Medical Information Disclaimer</a></li><li><a href="{rel(cur,"editorial-policy/")}">Editorial Policy</a></li></ul></div></section>''',
              f'''<section class="section tone-cream"><div class="container prose"><h2>إلى أين بعد ذلك؟</h2><ul class="linklist"><li><a href="{rel(cur,"contact/#enquiry")}">التواصل والاستفسار السرّي</a></li><li><a href="{rel(cur,"treatments/")}">دليل العلاجات</a></li><li><a href="{rel(cur,"patient-packages/")}">الباقات</a></li><li><a href="{rel(cur,"privacy/")}">سياسة الخصوصية</a></li><li><a href="{rel(cur,"medical-disclaimer/")}">إخلاء المسؤولية الطبية</a></li><li><a href="{rel(cur,"editorial-policy/")}">السياسة التحريرية</a></li></ul></div></section>''')
    fnd = {"@context": "https://schema.org", "@type": "Person", "@id": BASE + "about/#founder", "name": "Hommam Azizieh", "jobTitle": "Founder",
           "image": abs_url("assets/img/founder-hommam-azizieh-843.jpg"), "knowsLanguage": ["English", "Arabic", "Turkish"], "knowsAbout": ["Marketing", "Production", "Photography", "Medical travel coordination"],
           "worksFor": {"@id": BASE + "#organization"}}
    add(p, main, "about", crumbs=[(L("Home", "الرئيسية"), ""), (L("About Us", "من نحن"), cur)], extra_ld=[dict(ORG_LD), fnd])

# ---------------- FAQs ----------------
FAQS = [
 ("Is threeeight35° a healthcare provider?", "No. threeeight35° Medical Travel Agency is a medical travel and journey coordination service. Clinical assessment, diagnosis, treatment recommendations, informed consent and medical care are provided independently by licensed healthcare professionals in Türkiye."),
 ("Does threeeight35° recommend a treatment or tell me whether I am suitable?", "No. We do not diagnose, prescribe or recommend treatment. Suitability is decided by the treating healthcare professional after individual assessment."),
 ("How much do your packages cost?", "Essential Care is a fixed A$4,950 Medical Travel Coordination Package. Executive Wellness & Recovery is a fixed A$9,900 Medical Travel Coordination Package. VIP Bespoke Health Journey is from A$14,900, with the final coordination package price confirmed in writing after the scope of the journey is established. Every package includes accommodation and private transfers in Istanbul."),
 ("Do the package prices include my medical treatment?", "No. Medical treatment is quoted by and paid directly to the independent clinic or hospital. threeeight35° does not publish, determine or collect medical treatment fees."),
 ("Are accommodation and private transport included?", "Yes. Every package includes accommodation and private transfers in Istanbul between the airport, your hotel and clinic appointments. Essential Care covers 4–7 nights for you and 1 guest (2 people in total), Executive Wellness & Recovery covers 8–10 nights for you and up to 2 guests (3 people in total), and VIP Bespoke Health Journey covers 14 nights for you and up to 5 guests (6 people in total). International flights are not included. Extra nights you choose to add are paid directly to the hotel; a longer stay advised by your treating clinician is quoted separately. For additional guests, please contact us."),
 ("Can I arrange my own accommodation or transport?", "Yes. Tell us what you would prefer to arrange yourself and we will discuss it with you and quote a final package fee."),
 ("Do you publish treatment prices?", "No. Treatment prices are quoted by the independent provider after assessment. Your written proposal shows your coordination package, any extras quoted separately and the provider's treatment quotation before you proceed."),
 ("Should I send medical records through the enquiry form?", "No. Please do not include medical records, test results, passport or payment details in the website form. After your initial enquiry, any health information needed for preliminary provider review follows a private health-information and overseas-disclosure workflow."),
 ("How soon can I fly home after treatment?", "There is no universal safe timeframe. The treating clinician determines travel timing from the procedure, your individual recovery and required post-treatment reviews."),
 ("What happens after I return to Australia?", "Follow-up coordination continues after you return home. Before you travel, confirm which records you will bring home and the plan for any concerns after returning to Australia. Where ongoing care may be needed, discussing your plans with an Australian healthcare professional can help."),
 ("Which markets do you serve?", "We coordinate medical travel for patients from Australia, the UAE and other international markets. Our Australia & International line serves patients in Australia and other countries, our UAE & GCC line serves patients in the UAE and the Gulf, and a coordinator supports you during your stay in Istanbul."),
 ("Is “Türkiye” the same as “Turkey”?", "Yes. Türkiye is the country's name in its own language and is the form we use editorially. Many people still search for Turkey, so you may see both."),
]
def build_faqs():
    cur = "faqs/"
    p = dict(path=cur, id="SUP-FAQ", kind="FAQs (derived from v11 statements)", title=L("Frequently Asked Questions | threeeight35° Medical Travel Agency", "الأسئلة الشائعة | وكالة threeeight35° للسفر العلاجي"),
             desc=L("Answers about threeeight35°'s coordination role, package prices, treatment costs, travel from Australia and privacy when planning treatment in Türkiye.",
                    "إجابات عن دور threeeight35° في التنسيق وأسعار الباقات وتكاليف العلاج والسفر والخصوصية عند التخطيط للعلاج في تركيا."),
             indexable=True, status="Derived from Version 11 statements; editorial approval required (v11 has no dedicated FAQ record)")
    body = "".join(f'<details class="faq"><summary>{esc(q)}</summary><div class="faq-a"><p>{esc(a)}</p></div></details>' for q, a in L(FAQS, FAQS_AR))
    main = pagehead(L("PATIENT GUIDANCE", "إرشادات للمرضى"), L("Frequently Asked Questions", "الأسئلة الشائعة"),
                    L("Answers about our coordination role, package prices, costs and travel from Australia.", "إجابات عن دورنا في التنسيق وأسعار الباقات والتكاليف والسفر."))
    main += f'<section class="section"><div class="container prose">{body}<p class="small">{L("Still have a question?", "هل لديك سؤال آخر؟")} <a href="{rel(cur,"contact/#enquiry")}">{L("Make an enquiry", "أرسل استفسارك")}</a>.</p></div></section>'
    main += enquiry_cta(cur)
    add(p, main, "faqs", crumbs=[(L("Home", "الرئيسية"), ""), (L("FAQs", "الأسئلة الشائعة"), cur)])

# ---------------- Contact ----------------
FORM_CONSENT = "I understand that threeeight35° is a medical travel coordination service and not a healthcare provider, and I have read the Privacy Policy. I have not included medical records, test results, passport or payment details in this form."
def build_contact():
    cur = "contact/"
    p = dict(path=cur, id="SUP-04", kind="Contact / Enquiry", title=L("Contact & Confidential Enquiry | threeeight35°", "التواصل والاستفسار السرّي | وكالة threeeight35° للسفر العلاجي"),
             desc=L("Call or WhatsApp threeeight35° on our Australia & International or UAE & GCC line, or send a confidential medical travel enquiry. No medical records, please.",
                    "اتصل بـ threeeight35° أو راسلها عبر واتساب على خط الإمارات ودول الخليج أو خط أستراليا والدول الأخرى، أو أرسل استفساراً سرّياً. دون إرسال سجلات طبية."),
             indexable=True, status="Form delivery: endpoint configured, live test pending; consent wording: LEGAL INPUT REQUIRED")
    # Option values stay in English on both versions: the form back-end checks them and the enquiry email is read in English.
    cats = "".join(f'<option value="{att(c[2])}">{esc(cat_name(c[0]))}</option>' for c in CATS)
    procs = "".join(f'<optgroup label="{att(cat_name(cid))}">' + "".join(f'<option value="{att(TREAT[s]["label"])}" data-cat="{att(CATMAP[cid][2])}">{esc(treat_label(s))}</option>' for _, ids in GROUPS[cid] for s in ids) + "</optgroup>" for cid in [c[0] for c in CATS])
    contacts = L('<option>Email</option><option>WhatsApp</option><option>SMS</option><option>Phone call</option>',
                 '<option value="Email">البريد الإلكتروني</option><option value="WhatsApp">واتساب</option><option value="SMS">رسالة نصية (SMS)</option><option value="Phone call">مكالمة هاتفية</option>')
    not_sure = L('<option>Not sure yet</option>', '<option value="Not sure yet">لم أحدّد بعد</option>')
    req = L(" *", " *")
    consent = L(esc(FORM_CONSENT).replace("Privacy Policy", f'<a href="{rel(cur,"privacy/")}">Privacy Policy</a>'),
                FORM_CONSENT_AR.replace("سياسة الخصوصية", f'<a href="{rel(cur,"privacy/")}">سياسة الخصوصية</a>'))
    opt = L('<span class="opt">(optional)</span>', '<span class="opt">(اختياري)</span>')
    form = f'''<section class="section" id="enquiry"><div class="container form-wrap"><div class="form-intro"><p class="eyebrow">{L("MEDICAL TRAVEL ENQUIRY", "استفسار عن السفر العلاجي")}</p><h2>{L("Send a confidential enquiry", "أرسل استفساراً سرّياً")}</h2>
<p>{L("Please provide your details below. We practise data minimisation — no diagnostic records, passport or payment details are requested here.", "يُرجى تقديم بياناتك أدناه. نلتزم بتقليل البيانات إلى الحد الأدنى، فلا نطلب هنا أي سجلات تشخيصية أو بيانات جواز سفر أو دفع.")}</p>
<p>{L("After the initial enquiry, any health information required for preliminary provider review must follow the approved private health-information and overseas-disclosure workflow, not the public web form.", "بعد الاستفسار الأولي، يجب أن تمرّ أي معلومات صحية مطلوبة للتقييم الأولي من مقدّم الرعاية عبر الإجراءات الخاصة المعتمدة لحماية المعلومات الصحية والإفصاح عنها خارج البلاد، وليس عبر نموذج الموقع العام.")}</p>
<p class="small">{L("Fields marked * are required.", "الحقول المميّزة بعلامة * مطلوبة.")}</p></div>
<form class="form" id="enquiry-form" method="post" novalidate data-endpoint-config="T35_FORM">
<div id="form-status" class="form-status" role="status" aria-live="polite" tabindex="-1" hidden></div>
<div class="field"><label for="f-name">{L("Full name", "الاسم الكامل")}{req}</label><input id="f-name" name="full_name" type="text" autocomplete="name" required maxlength="120"><p class="err" id="e-f-name" hidden></p></div>
<div class="field"><label for="f-email">{L("Email address", "البريد الإلكتروني")}{req}</label><input id="f-email" name="email" type="email" autocomplete="email" required maxlength="160"{L("", ' dir="ltr"')}><p class="err" id="e-f-email" hidden></p></div>
<div class="field"><label for="f-country">{L("Country of residence", "بلد الإقامة")}{req}</label><input id="f-country" name="country" type="text" autocomplete="country-name" required maxlength="80"><p class="err" id="e-f-country" hidden></p></div>
<div class="field"><label for="f-contact">{L("Preferred contact method", "وسيلة التواصل المفضّلة")}{req}</label><select id="f-contact" name="preferred_contact" required><option value="">{L("Select…", "اختر…")}</option>{contacts}</select><p class="err" id="e-f-contact" hidden></p></div>
<div class="field" id="phone-field" hidden><label for="f-phone">{L("Phone number", "رقم الهاتف")}{req}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" maxlength="30" disabled data-describedby="phone-help" aria-describedby="phone-help"{L("", ' dir="ltr"')}><p id="phone-help" class="help">{L("Include your country code, for example +61 4XX XXX XXX or +971 5X XXX XXXX.", 'أدرج رمز الدولة، مثل <span dir="ltr">+971 5X XXX XXXX</span> أو <span dir="ltr">+61 4XX XXX XXX</span>.')}</p><p class="err" id="e-f-phone" hidden></p></div>
<div class="field"><label for="f-cat">{L("Treatment category", "فئة العلاج")}{req}</label><select id="f-cat" name="treatment_category" required><option value="">{L("Select…", "اختر…")}</option>{cats}{not_sure}</select><p class="err" id="e-f-cat" hidden></p></div>
<div class="field"><label for="f-proc">{L("Specific procedure", "الإجراء المحدد")} {opt}</label><select id="f-proc" name="specific_procedure"><option value="">{L("Not sure yet / not listed", "لم أحدّد بعد / غير مدرج")}</option>{procs}</select></div>
<div class="field field-wide"><label for="f-msg">{L("Message", "الرسالة")} {opt}</label><textarea id="f-msg" name="message" rows="5" maxlength="1500" aria-describedby="msg-help"></textarea>
<p id="msg-help" class="help">{L("Please share only your general goals or ideal travel timing. Please don't include medical records, test results or payment details here.", "يُرجى مشاركة أهدافك العامة أو التوقيت المفضّل لسفرك فقط، ودون إدراج سجلات طبية أو نتائج فحوصات أو بيانات دفع هنا.")}</p></div>
<div class="hp" aria-hidden="true"><label for="f-hp">{L("Leave this field empty", "اترك هذا الحقل فارغاً")}</label><input id="f-hp" name="_gotcha" type="text" tabindex="-1" autocomplete="off"></div>
<div class="field field-wide consent"><input id="f-consent" name="privacy_consent" type="checkbox" value="yes" required><label for="f-consent">{consent}</label><p class="err" id="e-f-consent" hidden></p></div>
<div id="captcha-slot" class="field-wide"></div>
<input type="hidden" name="_subject" value="New medical travel enquiry — threeeight35° website"><input type="hidden" name="_page" value="{page_url(cur)}">
<div class="field-wide"><button class="btn btn-navy btn-lg" type="submit" id="f-submit">{L("Send enquiry", "إرسال الاستفسار")}</button></div>
</form></div></section>'''
    main = pagehead(L("PATIENT CONCIERGE", "خدمة المرضى"), L("Contact & Confidential Enquiry", "التواصل والاستفسار السرّي"),
                    L("Reach our Australian, UAE or Türkiye coordination contacts directly or submit an enquiry below.", "تواصل مباشرةً مع مكاتب التنسيق في أستراليا أو الإمارات أو تركيا، أو أرسل استفسارك أدناه."))
    main += contact_cards(cur, with_h=False).join(['<section class="section tone-cream"><div class="container">', '</div></section>'])
    main += form
    add(p, main, "contact", crumbs=[(L("Home", "الرئيسية"), ""), (L("Contact & Enquiries", "التواصل والاستفسارات"), cur)])

# ---------------- Legal & trust ----------------
def legal_page(cur, doc_en, doc_ar):
    """Render a legal document (list of (heading, html)) with its last-updated date and links resolved for this page."""
    links = dict(EMAIL=EMAIL, ABN=ABN, OVERSEAS=rel(cur, "privacy-overseas-health-information-disclosure/"),
                 PACKAGES=rel(cur, "patient-packages/"), CONTACT=rel(cur, "contact/"), PRIVACY=rel(cur, "privacy/"))
    body = "".join(qa(h, html_.format(**links)) for h, html_ in L(doc_en, doc_ar))
    return f'<p class="small">{L("Last updated", "آخر تحديث")}: {L(*LEGAL_UPDATED)}</p>' + body

def build_privacy():
    cur = "privacy/"
    p = dict(path=cur, id="SUP-05", kind="Privacy", title=L("Privacy Policy | threeeight35° Medical Travel Agency", "سياسة الخصوصية | وكالة threeeight35° للسفر العلاجي"),
             desc=L("How threeeight35° collects, uses, discloses and protects personal and health information, including overseas disclosure, retention and your rights.",
                    "كيف تجمع threeeight35° المعلومات الشخصية والصحية وتستخدمها وتفصح عنها وتحميها، بما في ذلك الإفصاح خارج البلاد ومدة الاحتفاظ وحقوقك."),
             indexable=True, status="Full policy drafted 22 Oct 2026 (Australian Privacy Principles); lawyer check recommended")
    main = pagehead("", L("Privacy Policy", "سياسة الخصوصية")) + f'<section class="section"><div class="container prose">{legal_page(cur, PRIVACY_EN, PRIVACY_AR)}</div></section>'
    add(p, main, "", crumbs=[(L("Home", "الرئيسية"), ""), (L("Privacy Policy", "سياسة الخصوصية"), cur)])

def build_terms():
    cur = "terms/"
    p = dict(path=cur, id="SUP-08", kind="Terms", title=L("Terms & Conditions | threeeight35° Medical Travel Agency", "الشروط والأحكام | وكالة threeeight35° للسفر العلاجي"),
             desc=L("Terms for threeeight35° medical travel coordination: our role, package inclusions, 50% deposit and payment timing, your responsibilities and consumer rights.",
                    "شروط خدمات تنسيق السفر العلاجي من threeeight35°: دورنا وما تشمله الباقات والعربون ومواعيد الدفع ومسؤولياتك وحقوقك كمستهلك."),
             indexable=True, status="Full terms drafted 22 Oct 2026; refund policy provided with each written proposal; lawyer check recommended")
    main = pagehead("", L("Terms & Conditions", "الشروط والأحكام")) + f'<section class="section"><div class="container prose">{legal_page(cur, TERMS_EN, TERMS_AR)}</div></section>'
    add(p, main, "", crumbs=[(L("Home", "الرئيسية"), ""), (L("Terms & Conditions", "الشروط والأحكام"), cur)])

def build_disclaimer():
    cur = "medical-disclaimer/"
    p = dict(path=cur, id="SUP-06", kind="Medical disclaimer", title=L("Medical Information Disclaimer | threeeight35°", "إخلاء المسؤولية الطبية | threeeight35°"),
             desc=L("threeeight35° is a medical travel coordination service, not a healthcare provider. Read how our information differs from medical advice.",
                    "threeeight35° خدمة لتنسيق السفر العلاجي وليست مقدّم رعاية صحية. تعرّف على الفرق بين معلوماتنا والاستشارة الطبية."),
             indexable=True, status="Uses Version 11 approved coordination notice; legal review recommended")
    if not is_ar():
        body = f'''{qa("What threeeight35° is and is not", f"<p>{esc(NOTICE.replace('Important Medical Coordination Notice: ',''))}</p>")}
{qa("What this website provides", "<p>General information about planning medical travel and coordination. It does not diagnose a condition, recommend a treatment for an individual or replace advice from a suitably qualified healthcare professional. Suitability, risks, alternatives, recovery and fitness to travel must be determined by the treating clinician.</p>")}
{qa("Results and costs", "<p>No treatment result, recovery time or travel timeframe is guaranteed. Treatment prices are quoted by and paid directly to the independent clinic or hospital.</p>")}
{qa("In an emergency", "<p>In a medical emergency in Türkiye, call 112. This is separate from threeeight35° contact details.</p>")}
{qa("Discuss your plans", "<p>Patients are encouraged to discuss overseas treatment with their usual doctor or an appropriate healthcare professional where relevant.</p>")}'''
    else:
        body = f'''{qa("ما هي threeeight35° وما ليست هي", f"<p>{NOTICE_AR_BODY}</p>")}
{qa("ما يقدّمه هذا الموقع", "<p>معلومات عامة عن التخطيط للسفر العلاجي وتنسيقه. ولا يشخّص الموقع أي حالة، ولا يوصي بعلاج لشخص بعينه، ولا يغني عن استشارة أخصائي رعاية صحية مؤهّل. ويجب أن يحدّد الطبيب المعالج مدى ملاءمة العلاج ومخاطره وبدائله ومدة التعافي والقدرة على السفر.</p>")}
{qa("النتائج والتكاليف", "<p>لا نضمن أي نتيجة علاجية أو مدة تعافٍ أو إطار زمني للسفر. ويُسعَّر العلاج ويُدفع مباشرةً إلى العيادة أو المستشفى المستقل.</p>")}
{qa("في حالات الطوارئ", "<p>في حالة الطوارئ الطبية في تركيا، اتصل على الرقم 112. وهذا الرقم منفصل عن أرقام التواصل مع threeeight35°.</p>")}
{qa("ناقش خططك", "<p>نشجّع المرضى على مناقشة العلاج في الخارج مع طبيبهم المعتاد أو مع أخصائي رعاية صحية مناسب عند الاقتضاء.</p>")}'''
    main = pagehead("", L("Medical Information Disclaimer", "إخلاء المسؤولية الطبية")) + f'<section class="section"><div class="container prose">{body}</div></section>'
    add(p, main, "", crumbs=[(L("Home", "الرئيسية"), ""), (L("Medical Information Disclaimer", "إخلاء المسؤولية الطبية"), cur)])

def build_editorial():
    cur = "editorial-policy/"
    p = dict(path=cur, id="SUP-07", kind="Editorial policy", title=L("Editorial Policy | threeeight35°", "السياسة التحريرية | threeeight35°"),
             desc=L("How threeeight35° prepares its medical-travel content: publishing rules, sources, and how provider and package facts are confirmed.",
                    "كيف تُعدّ threeeight35° محتوى السفر العلاجي: قواعد النشر والمصادر وكيفية التحقق من معلومات مقدّمي الرعاية والباقات."),
             indexable=True, status="Derived from Version 11 publishing rules; editorial approval required")
    body = f'''{qa("Our publishing rules", "<ul><li>threeeight35° is a medical-travel coordination agency, not the treating healthcare provider.</li><li>We do not invent prices, provider credentials, accreditation, recovery promises, minimum stays, medication, tests, hotel inclusions, transfers or outcomes.</li><li>Pages use answer-first questions, descriptive internal links and a clear path to the category, the Australia guide and contact.</li><li>Public copy uses Australian English. We use Türkiye editorially; Turkey may appear naturally as a search-language variant.</li></ul>")}
{qa("Clinical content", "<p>threeeight35° does not publish clinical advice. Our treatment pages cover planning and coordination only. Diagnosis, suitability, risks, recovery and treatment decisions come from your treating healthcare professional after an individual assessment.</p>")}
{qa("Sources", "<p>Authoritative sources are mapped to substantive medical claims at claim level. A category bibliography is not treated as a substitute for claim-level support.</p>")}
{qa("Provider and package facts", "<p>Provider-specific facts, prices, inclusions, accommodation, transfers, tests, medicines, stay durations and follow-up promises are verified in writing before publication.</p>")}'''
    if is_ar():
        body = f'''{qa("قواعد النشر لدينا", "<ul><li>threeeight35° وكالة لتنسيق السفر العلاجي، وليست مقدّم الرعاية الصحية المعالج.</li><li>لا نختلق الأسعار أو مؤهلات مقدّمي الرعاية أو الاعتمادات أو وعود التعافي أو الحد الأدنى لمدة الإقامة أو الأدوية أو الفحوصات أو ما تشمله الإقامة الفندقية أو التنقلات أو النتائج.</li><li>تبدأ الصفحات بالإجابة عن السؤال مباشرةً، وتستخدم روابط داخلية واضحة، وتوفّر مساراً واضحاً إلى الفئة المعنية وصفحة التواصل.</li><li>يستخدم المحتوى الإنجليزي الإنجليزية الأسترالية، ويستخدم المحتوى العربي اللغة العربية الفصحى المعاصرة واسم «تركيا».</li></ul>")}
{qa("المحتوى السريري", "<p>لا تنشر threeeight35° أي استشارات سريرية. وتقتصر صفحات العلاج لدينا على التخطيط والتنسيق. أما التشخيص وتحديد الملاءمة والمخاطر والتعافي وقرارات العلاج فتأتي من أخصائي الرعاية الصحية المعالج بعد تقييم فردي.</p>")}
{qa("المصادر", "<p>تُربط المصادر الموثوقة بكل معلومة طبية جوهرية على حدة. ولا تُعدّ قائمة المراجع العامة للفئة بديلاً عن توثيق كل معلومة.</p>")}
{qa("معلومات مقدّمي الرعاية والباقات", "<p>نتحقق كتابياً قبل النشر من المعلومات الخاصة بمقدّمي الرعاية، والأسعار، وما تشمله الخدمات، والإقامة، والتنقلات، والفحوصات، والأدوية، ومدد الإقامة، ووعود المتابعة.</p>")}'''
    main = pagehead("", L("Editorial Policy", "السياسة التحريرية")) + f'<section class="section"><div class="container prose">{body}</div></section>'
    add(p, main, "", crumbs=[(L("Home", "الرئيسية"), ""), (L("Editorial Policy", "السياسة التحريرية"), cur)])

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
  [("What should a written quotation show?", "<p>Your complete proposal, including confirmed inclusions and exclusions, is provided in writing before you proceed. It shows your coordination package, any extras quoted separately and the independent provider's treatment quotation.</p>"),
   ("Why can't I compare a package price with a treatment price?", "<p>They are different things. Treatment is quoted by and paid directly to the independent clinic or hospital; the threeeight35° package fee covers coordination, accommodation and Istanbul transfers; flights are booked separately. A treatment fee is not combined with a package price into one advertised price.</p>")]),
 ("GEO-AU-08", "privacy-overseas-health-information-disclosure/", "Privacy & Overseas Health-Information Disclosure", "How health information is handled after your initial enquiry, and why it is kept out of the public web form.",
  [("Why is health information kept out of the website form?", "<p>The public form is for initial enquiries only and is designed for data minimisation. After your enquiry, any health information needed for preliminary provider review follows an approved private health-information and overseas-disclosure workflow, with your authorisation.</p>")]),
]
def build_geo():
    cur = "medical-travel-turkiye-from-australia/"
    p = dict(path=cur, id="GEO-AU-01", kind="Supporting GEO / patient-journey hub", title="Medical Travel to Türkiye from Australia | threeeight35°",
             desc="How medical travel from Australia to Türkiye works: coordination, quotations, travel, flying home and follow-up. threeeight35° coordinates; providers treat.",
             indexable=True, status="Hub: title/meta/copy drafted from Version 11 statements (v11 supplies name and URL only); editorial approval required")
    cats = "".join(f'<li><a href="{rel(cur, cat_dir(c[0]))}">{esc(c[2])}</a></li>' for c in CATS)
    spokes = "".join(f'<li><a href="{rel(cur, s[1])}">{esc(s[2])}</a></li>' for s in SPOKES)
    body = f'''{qa("How does medical travel from Australia to Türkiye work?", f'<p>Medical travel from Australia to Türkiye generally involves exploring a treatment and independent provider, receiving a written proposal and quotation, arranging travel, attending the provider\'s assessment, receiving treatment only where the treating clinician considers it suitable, and arranging follow-up after returning to Australia. threeeight35° coordinates the non-clinical journey. See <a href="{rel(cur,"how-it-works/")}">How It Works</a>.</p>')}
{qa("What does threeeight35° coordinate?", "<p>We connect patients with independent healthcare providers and hospitals in Istanbul, arrange consultations and quotations, and coordinate accommodation, private transfers and support in English, Arabic and Turkish during the stay. Clinical assessment, diagnosis, treatment recommendations, informed consent and medical care are the responsibility of the treating provider.</p>")}
{qa("What should I confirm before travelling?", "<p>Confirm the treating clinician, the proposed procedure, anaesthesia and facility arrangements where relevant, expected reviews in Türkiye, records to bring home, and the plan for concerns after returning to Australia.</p>")}
{qa("When can I fly home?", f'<p>There is no universal safe timeframe. The treating clinician must determine travel timing from the procedure, individual recovery and required post-treatment reviews. See <a href="{rel(cur,"flying-home-after-medical-treatment/")}">Flying Home After Medical Treatment</a>.</p>')}
{qa("What does it cost, and who do I pay?", f'<p>{esc(DISCLOSURE)} See <a href="{rel(cur,"patient-packages/")}">Patient Packages</a>.</p>')}
{qa("What does the Australian Government say?", f'<p>Smartraveller advises researching the destination health system, making sure travel insurance covers complications and medical evacuation, and notes that basic travel insurance policies rarely cover medical tourism. <a href="{SMART}" rel="noopener noreferrer" target="_blank">Read the Smartraveller guidance</a>.</p>')}'''
    main = pagehead("AUSTRALIA TO TÜRKİYE", "Medical Travel to Türkiye from Australia", "A practical guide for Australians researching treatment in Türkiye. We coordinate the journey; independent providers deliver all clinical care.")
    main += f'<section class="section"><div class="container prose">{body}</div></section>'
    main += f'<section class="section tone-cream"><div class="container two-col"><div><h2>Guides in this series</h2><ul class="linklist">{spokes}</ul></div><div><h2>Treatment categories</h2><ul class="linklist">{cats}</ul></div></div></section>'
    main += enquiry_cta(cur)
    add(p, main, "", crumbs=[("Home", ""), ("Medical Travel to Türkiye from Australia", cur)])
    for sid, slug, name, intro, qas in SPOKES:
        c2 = slug
        pp = dict(path=c2, id=sid, kind="GEO support guide", title=f"{name} | threeeight35°", desc=intro, indexable=False, robots="noindex,follow",
                  status="Spoke drafted from Version 11 statements (v11 lists the name only); editorial approval required; noindex until approved")
        b = "".join(qa(h, x) for h, x in qas)
        m = pagehead("AUSTRALIA TO TÜRKİYE GUIDE", name, intro)
        m += f'<section class="section"><div class="container prose">{b}<p><a href="{rel(c2,"medical-travel-turkiye-from-australia/")}">← Medical Travel to Türkiye from Australia</a></p></div></section>'
        m += enquiry_cta(c2)
        add(pp, m, "", crumbs=[("Home", ""), ("Medical Travel to Türkiye from Australia", "medical-travel-turkiye-from-australia/"), (name, slug)])
