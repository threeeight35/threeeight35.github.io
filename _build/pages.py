# -*- coding: utf-8 -*-
from components import *
from treatment_guides import GUIDES, GUIDE_META
from treatments_ar import FOCUS_AR, UND_END_AR, CONFIRM_AR, GUIDES_AR, GUIDE_META_AR
from treatments_tr import FOCUS_TR, UND_END_TR, CONFIRM_TR, GUIDES_TR, GUIDE_META_TR

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
    return ""

def add(p, main, active="", crumbs=None, hero=False, extra_ld=None):
    cur = p["path"]
    p["en_path"] = cur
    if lang() != "en": p["canon"] = prefix() + cur
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
    if lang() != "en": p["path"] = prefix() + cur; p["id"] += "-" + lang().upper(); p["kind"] += f" ({LANG_INFO[lang()]['name']})"
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
    p = dict(path="", id="SUP-01", kind="Agency home", title=L("threeeight35° | Medical Travel Coordination for Türkiye", "وكالة threeeight35° للسفر العلاجي | رحلتك الصحية، بلا حدود.", "threeeight35° | Türkiye'de Tıbbi Seyahat Koordinasyonu"),
             desc=L("Personalised medical travel coordination connecting patients from Australia, the UAE and other markets with independent healthcare providers in Türkiye.",
                    "تنسيق شخصي للسفر العلاجي يربط المرضى من الإمارات وأستراليا والأسواق الأخرى بمقدّمي رعاية صحية مستقلين في تركيا.", "Avustralya, BAE ve diğer pazarlardaki hastaları Türkiye'deki bağımsız sağlık kuruluşlarıyla buluşturan kişiye özel tıbbi seyahat koordinasyonu."),
             indexable=True, status="Business identity verified; clinical review not applicable to this page; technical QA pending")
    hero_img = img(cur, "16_health_journey_istanbul",
                   L("Sunset over the Istanbul skyline and waterway, with domed mosques and a ferry below an aeroplane in the sky.", "غروب الشمس فوق أفق إسطنبول ومضيق البوسفور، مع مساجد بقباب وعبّارة وطائرة في السماء.", "İstanbul silueti ve Boğaz üzerinde gün batımı; kubbeli camiler, bir vapur ve gökyüzünde bir uçak."),
                   "(min-width: 960px) 52vw, 100vw", cls="hero-img", eager=True, fetch=True, pick=1440)
    vid = f'<a class="btn btn-outline-light" href="{VIDEO_CONSULT_URL}">{L("Schedule Video Consultation", "احجز استشارة عبر الفيديو", "Görüntülü Görüşme Planlayın")}</a>' if VIDEO_CONSULT_URL else ""
    main = f'''<section class="hero"><div class="hero-copy"><div class="hero-copy-in">
<p class="eyebrow eyebrow-on-dark">{L("AUSTRALIA · UAE · TÜRKİYE", "أستراليا · الإمارات · تركيا", "AVUSTRALYA · BAE · TÜRKİYE")}</p>
<h1>{L("Your Health Journey, <span>Beyond Borders.</span>", "رحلتك الصحية، <span>بلا حدود.</span>", "Sağlık Yolculuğunuz, <span>Sınırların Ötesinde.</span>")}</h1>
<p class="hero-sub">{L("Personalised medical travel coordination connecting patients from Australia, the UAE and other international markets with independent healthcare providers in Türkiye.", "تنسيق شخصي للسفر العلاجي يربط المرضى من أستراليا والإمارات العربية المتحدة والأسواق الدولية الأخرى بمقدّمي رعاية صحية مستقلين في تركيا.", "Avustralya, BAE ve diğer uluslararası pazarlardaki hastaları Türkiye'deki bağımsız sağlık kuruluşlarıyla buluşturan kişiye özel tıbbi seyahat koordinasyonu.")}</p>
<p class="hero-line">{L("Precisely coordinated. Transparently guided.", "تنسيق دقيق. وإرشاد بشفافية.", "Titizlikle koordine edilir. Şeffaflıkla yönlendirilir.")}</p>
<div class="btn-row"><a class="btn btn-gold" href="{rel(cur,"contact/#enquiry")}">{L("Make an Enquiry", "أرسل استفسارك", "Talep Gönderin")}</a><a class="btn btn-outline-light" href="{rel(cur,"treatments/")}">{L("Explore Treatments", "استكشف العلاجات", "Tedavileri Keşfedin")}</a>{vid}</div>
<dl class="hero-stats"><div><dt>{L("Medical categories", "فئات طبية", "Tıbbi kategoriler")}</dt><dd>8</dd></div><div><dt>{L("Languages", "اللغات", "Diller")}</dt><dd class="dd-langs">{L('<span aria-hidden="true">EN · AR · TR</span><span class="sr-only">English, Arabic, Turkish</span>', '<span class="nw">عربي ·</span> <span class="nw">إنجليزي ·</span> <span class="nw">تركي</span>', '<span aria-hidden="true">EN · AR · TR</span><span class="sr-only">İngilizce, Arapça, Türkçe</span>')}</dd></div><div><dt>{L("Coordination", "تنسيق شخصي", "Koordinasyon")}</dt><dd>1:1</dd></div></dl>
</div></div><div class="hero-media">{hero_img}</div></section>
<section class="boundary"><div class="container"><p>{L("<strong>threeeight35° is a coordination service, not a healthcare provider.</strong> We do not diagnose, prescribe or recommend treatment. All clinical assessment and medical care are provided independently by licensed healthcare professionals in Türkiye.",
                                                        "<strong>threeeight35° خدمة تنسيق، وليست مقدّم رعاية صحية.</strong> نحن لا نشخّص ولا نصف ولا نوصي بأي علاج. ويُقدَّم كل تقييم سريري وكل رعاية طبية بشكل مستقل من قِبل أخصائيي رعاية صحية مرخّصين في تركيا.", "<strong>threeeight35° bir koordinasyon hizmetidir, sağlık hizmeti sağlayıcısı değildir.</strong> Teşhis koymaz, reçete yazmaz ve tedavi önermeyiz. Tüm klinik değerlendirme ve tıbbi bakım, Türkiye'deki lisanslı sağlık profesyonelleri tarafından bağımsız olarak sağlanır.")}</p></div></section>'''
    main += section(L("MEDICAL CATEGORIES", "الفئات الطبية", "TIBBİ KATEGORİLER"), L("Explore Medical Categories", "استكشف الفئات الطبية", "Tıbbi Kategorileri Keşfedin"),
                    L("Eight medical categories, each with its own treatment pages. Treatment pages explain how to plan and what to confirm; clinical decisions stay with your treating provider.",
                      "ثماني فئات طبية، لكل منها صفحاتها العلاجية. تشرح صفحات العلاج كيفية التخطيط وما يجب التأكد منه، بينما تبقى القرارات السريرية لمقدّم الرعاية المعالج.", "Her birinin kendi tedavi sayfaları olan sekiz tıbbi kategori. Tedavi sayfaları nasıl planlama yapacağınızı ve neyi teyit etmeniz gerektiğini açıklar; klinik kararlar tedaviyi yürüten sağlık kuruluşunuza aittir."),
                    categories_grid(cur) + f'<p class="center" style="margin-top:2rem"><a class="btn btn-navy" href="{rel(cur,"treatments/")}">{L("View the full treatments catalogue", "عرض دليل العلاجات الكامل", "Tüm tedavi kataloğunu görüntüleyin")}</a></p>', hid="categories")
    main += section(L("PATIENT-CENTRED COORDINATION", "تنسيق يتمحور حول المريض", "HASTA ODAKLI KOORDİNASYON"), L("Why Coordinated Medical Travel?", "لماذا السفر العلاجي المنسَّق؟", "Neden Koordineli Tıbbi Seyahat?"),
                    L("Medical travel requires thoughtful planning, direct communication with treating healthcare professionals, and transparent arrangements.",
                      "يتطلب السفر العلاجي تخطيطاً مدروساً، وتواصلاً مباشراً مع أخصائيي الرعاية الصحية المعالجين، وترتيبات تتسم بالشفافية.", "Tıbbi seyahat; özenli planlama, tedaviyi yürüten sağlık profesyonelleriyle doğrudan iletişim ve şeffaf düzenlemeler gerektirir."), why_cards(), tone="tone-cream")
    main += accommodation_section(cur)
    main += section(L("PACKAGES", "الباقات", "PAKETLER"), L("Medical Travel Coordination Packages", "باقات تنسيق السفر العلاجي", "Tıbbi Seyahat Koordinasyon Paketleri"),
                    L("threeeight35° package prices include our non-clinical coordination, your accommodation and private transfers in Istanbul. Medical treatment and flights are paid separately.",
                      "تشمل أسعار باقات threeeight35° خدمات التنسيق غير السريرية وإقامتك وتنقلاتك الخاصة في إسطنبول. ويُدفع العلاج الطبي وتذاكر الطيران بشكل منفصل.", "threeeight35° paket fiyatları, klinik dışı koordinasyonumuzu, konaklamanızı ve İstanbul'daki özel transferlerinizi kapsar. Tıbbi tedavi ve uçuşlar ayrıca ödenir."),
                    package_cards(cur) + f'<p class="center"><a class="more" href="{rel(cur,"patient-packages/")}">{L("How package, treatment and flight costs fit together", "كيف تتوزع تكاليف الباقة والعلاج والطيران", "Paket, tedavi ve uçuş maliyetlerinin nasıl ayrıldığı")} <span aria-hidden="true">{arrow()}</span></a></p>', hid="packages")
    main += section(L("THE PATIENT JOURNEY", "رحلة المريض", "HASTA YOLCULUĞU"), L("How It Works", "كيف نعمل", "Nasıl Çalışır"), L("From first enquiry to follow-up coordination after you return home.", "من الاستفسار الأول حتى تنسيق المتابعة بعد عودتك.", "İlk talepten eve dönüşünüzden sonraki takip koordinasyonuna kadar."),
                    journey_list(cur) + f'<p class="center"><a class="more" href="{rel(cur,"how-it-works/")}">{L("Read the full journey", "اقرأ تفاصيل الرحلة كاملة", "Yolculuğun tamamını okuyun")} <span aria-hidden="true">{arrow()}</span></a></p>', tone="tone-cream")
    main += section(L("ABOUT", "من نحن", "HAKKIMIZDA"), L("About threeeight35°", "عن threeeight35°", "threeeight35° Hakkında"), "", f'<p class="prose-lead">{esc(L("threeeight35° Medical Travel Agency is an independent medical travel coordination service for patients from Australia, the UAE and other international markets who are exploring treatment in Türkiye. We manage the practical side of the journey and leave every clinical decision to independent, licensed clinicians.", "وكالة threeeight35° للسفر العلاجي هي خدمة مستقلة لتنسيق السفر العلاجي للمرضى من أستراليا والإمارات العربية المتحدة والأسواق الدولية الأخرى الذين يستكشفون العلاج في تركيا. نتولى الجانب العملي من الرحلة، ونترك كل قرار سريري لأطباء مستقلين ومرخّصين.", "threeeight35° Tıbbi Seyahat Acentesi, Türkiye'de tedavi seçeneklerini araştıran Avustralya, BAE ve diğer uluslararası pazarlardaki hastalar için bağımsız bir tıbbi seyahat koordinasyon hizmetidir. Yolculuğun pratik tarafını üstlenir, her klinik kararı bağımsız ve lisanslı hekimlere bırakırız."))}</p>' + founder_block(cur, full=False))
    main += contact_cards(cur)
    main += enquiry_cta(cur)
    org = dict(ORG_LD)
    site = {"@context": "https://schema.org", "@type": "WebSite", "@id": BASE + "#website", "name": SITE, "url": BASE, "inLanguage": "en-AU", "publisher": {"@id": BASE + "#organization"}}
    add(p, main, "home", crumbs=[(L("Home", "الرئيسية", "Ana Sayfa"), "")], hero=True, extra_ld=[org, site])

# ======================= TREATMENT DIRECTORY =======================
def tag(t):
    if t["hub"]: return f'<span class="tag">{L("Guide", "دليل", "Rehber")}</span>'
    return ""

def treat_label(sid): return L(TREAT[sid]["label"], TREAT_AR[sid], TREAT_TR[sid])
def treat_link_attrs(): return ""
EN_ONLY_NOTE_AR = ""

def build_directory():
    cur = "treatments/"
    p = dict(path=cur, id="SUP-02", kind="Treatments directory", title=L("Treatments Catalogue | threeeight35° Medical Travel Agency", "دليل العلاجات | وكالة threeeight35° للسفر العلاجي", "Tedavi Kataloğu | threeeight35° Tıbbi Seyahat Acentesi"),
             desc=L("Browse 8 medical categories and 70 treatment pages for planning treatment in Türkiye. Coordination by threeeight35°; care by independent providers.",
                    "تصفّح 8 فئات طبية و70 صفحة علاجية للتخطيط للعلاج في تركيا. التنسيق من threeeight35°، والرعاية من مقدّمي رعاية صحية مستقلين.", "Türkiye'de tedavi planlamak için 8 tıbbi kategori ve 70 tedavi sayfasına göz atın. Koordinasyon threeeight35°'ten, bakım bağımsız sağlık kuruluşlarından."),
             indexable=True, status="Technical QA pending")
    blocks = []
    for cid, slug, name, stem, alt, intro in CATS:
        n = sum(len(i) for _, i in GROUPS[cid])
        en_name = name
        if lang() != "en": name, intro, alt = cat_tx(cid)[:3]
        gh = []
        for g, ids in GROUPS[cid]:
            gname = L(g, GROUP_AR.get(g), GROUP_TR.get(g)) if g else None
            lis = "".join(f'<li data-search="{att((TREAT[s]["label"]+" "+en_name+" "+(g or "")+L("", " "+TREAT_AR[s]+" "+name+" "+(gname or ""), " "+TREAT_TR[s]+" "+name+" "+(gname or ""))).lower())}"><a href="{rel(cur, TREAT[s]["dir"])}"{treat_link_attrs()}>{esc(treat_label(s))}</a>{tag(TREAT[s])}</li>' for s in ids)
            gh.append((f'<h4 class="grp">{esc(gname)}</h4>' if gname else "") + f'<ul class="tlist">{lis}</ul>')
        blocks.append(f'''<section class="dir-cat" id="{slug}" aria-labelledby="h-{slug}"><div class="dir-media">{img(cur, stem, alt, "(min-width: 900px) 28vw, 92vw", cls="dir-img")}</div>
<div class="dir-body"><p class="cat-count">{treatment_pages(n)}</p><h3 id="h-{slug}"><a href="{rel(cur, cat_dir(cid))}">{esc(name)}</a></h3><p>{esc(intro)}</p>{"".join(gh)}</div></section>''')
    search = f'''<div class="search"><label for="tsearch">{L("Search treatments", "ابحث عن علاج", "Tedavi arayın")}</label><input id="tsearch" type="search" placeholder="{L("For example: dental implants, IVF, hernia", "مثال: زراعة الأسنان، أطفال الأنابيب، الفتق", "Örneğin: diş implantı, tüp bebek, fıtık")}" autocomplete="off" data-dir-search>
<p id="tsearch-status" class="small" role="status" aria-live="polite">{L("Showing all treatments", "عرض جميع العلاجات", "Tüm tedaviler gösteriliyor")}</p><button type="button" class="btn btn-outline-navy" data-dir-reset hidden>{L("Reset search", "إعادة ضبط البحث", "Aramayı sıfırla")}</button></div>'''
    main = pagehead(L("AUTHORITATIVE DIRECTORY", "الدليل الشامل", "KAPSAMLI REHBER"), L("Treatments Catalogue", "دليل العلاجات", "Tedavi Kataloğu"),
                    L("8 medical categories and 70 treatment pages. Group headings are for navigation only. Treatment prices are not published by threeeight35°: treatment is quoted by and paid directly to the independent clinic or hospital.",
                      "8 فئات طبية و70 صفحة علاجية. العناوين الفرعية للتصفّح فقط. لا تنشر threeeight35° أسعار العلاج، إذ يُسعَّر العلاج ويُدفع مباشرةً إلى العيادة أو المستشفى المستقل.", "8 tıbbi kategori ve 70 tedavi sayfası. Grup başlıkları yalnızca gezinme içindir. threeeight35° tedavi fiyatlarını yayınlamaz: tedavi, bağımsız klinik veya hastane tarafından fiyatlandırılır ve doğrudan onlara ödenir."))
    main += f'<section class="section"><div class="container">{search}{L("", EN_ONLY_NOTE_AR, "")}<div class="dir-list">{"".join(blocks)}</div></div></section>'
    main += enquiry_cta(cur)
    add(p, main, "treatments", crumbs=[(L("Home", "الرئيسية", "Ana Sayfa"), ""), (L("Treatments", "العلاجات", "Tedaviler"), "treatments/")])

# ======================= CATEGORY PAGES =======================
def build_category(c):
    cid, slug, name, stem, alt, intro = c
    cur = cat_dir(cid)
    r = BYID[cid]; f = r["fields"]
    # Owner decision 2026-10-23: use the site's fuller category names everywhere (v11's short names, e.g. "Dental in Türkiye", read awkwardly).
    title = f"{name} in Türkiye | threeeight35°"
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
    h1 = f"{name} in Türkiye"
    if lang() != "en": name, intro, alt, h1, title, desc = cat_tx(cid)
    p = dict(path=cur, id=cid, kind="Category landing page", title=title, desc=desc, indexable=True,
             status="Editorial remediation complete; clinical review pending; technical QA pending")
    groups_html = []
    for g, ids in GROUPS[cid]:
        cards = []
        for s in ids:
            t = TREAT[s]
            focus = ""
            m = re.search(r"should be researched in the context of (.*?)\. The final clinical plan", t["rec"]["pre"])
            if m and not t["held"]: focus = L(m.group(1), FOCUS_AR.get(s, ""), FOCUS_TR.get(s, ""))
            if t["held"]: focus = L("Coordination enquiries only", "استفسارات التنسيق فقط", "Yalnızca koordinasyon talepleri")
            elif t["hub"]: focus = L("Guide to the specific options under this broader term", "دليل للخيارات المحددة ضمن هذا المصطلح العام", "Bu genel terim altındaki belirli seçeneklere yönelik rehber")
            elif focus: focus = upper(focus[0]) + focus[1:]
            cards.append(f'<li class="tcard"><a href="{rel(cur, t["dir"])}"{treat_link_attrs()}><span class="tcard-t">{esc(treat_label(s))}</span><span class="tcard-d">{esc(focus)}</span></a>{tag(t)}</li>')
        gname = L(g, GROUP_AR.get(g), GROUP_TR.get(g)) if g else None
        groups_html.append((f'<h3 class="grp">{esc(gname)}</h3>' if gname else "") + f'<ul class="tgrid">{"".join(cards)}</ul>')
    media = img(cur, stem, alt, "(min-width: 900px) 40vw, 92vw", cls="cat-hero-img", eager=True, fetch=True)
    au_btn = L(f'<a class="btn btn-outline-navy" href="{rel(cur,"medical-travel-turkiye-from-australia/")}">Medical travel from Australia</a>', "", "")
    meta = L(f"{n} treatment pages in this category", ar_count(n, "صفحات علاجية", "صفحة علاجية") + " في هذه الفئة", f"Bu kategoride {n} tedavi sayfası")
    main = f'''<section class="page-head cat-head"><div class="container cat-head-grid"><div><p class="eyebrow">{esc(upper(name))}</p><h1>{esc(h1)}</h1>
<p class="lead">{esc(intro)}</p><p class="cat-meta">{meta}</p>
<div class="btn-row"><a class="btn btn-navy" href="{rel(cur,"contact/#enquiry")}">{L("Make an Enquiry", "أرسل استفسارك", "Talep Gönderin")}</a>{au_btn}</div></div>
<div class="cat-head-media">{media}</div></div></section>'''
    main += f'<section class="section"><div class="container"><h2 class="sec-h">{L("Treatments in this category", "العلاجات في هذه الفئة", "Bu kategorideki tedaviler")}</h2>{L("", EN_ONLY_NOTE_AR, "")}{"".join(groups_html)}</div></section>'
    if lang() == "en":
        main += section("COSTS", f"How is {name.split(' &')[0].lower() if cid!='CAT-06' else 'health check-up'} cost handled?", "",
            f'<div class="prose"><p>There is no category-wide price. Treatment prices are not published by threeeight35°: medical treatment and clinical fees are quoted by and paid directly to the independent clinic or hospital, in writing, after assessment. threeeight35° coordination package fees are separate — see <a href="{rel(cur,"patient-packages/")}">Patient Packages</a>.</p></div>', tone="tone-cream")
        main += section("TRAVEL FROM AUSTRALIA", "Planning travel, insurance and follow-up", "",
            f'<div class="prose"><p>Questions about travelling from Australia, insurance, flying home, records and privacy are answered in our guide <a href="{rel(cur,"medical-travel-turkiye-from-australia/")}">Medical Travel to Türkiye from Australia</a>. Travel timing is always set by your treating clinician, not by a generic website timeframe.</p></div>')
    elif lang() == "tr":
        main += section("MALİYETLER", "Bu kategoride tedavi maliyetleri nasıl belirlenir?", "",
            f'<div class="prose"><p>Kategori genelinde tek bir fiyat yoktur. threeeight35° tedavi fiyatlarını yayınlamaz: tıbbi tedavi ve klinik ücretleri, değerlendirmeden sonra bağımsız klinik veya hastane tarafından yazılı olarak fiyatlandırılır ve doğrudan onlara ödenir. threeeight35° koordinasyon paketi ücretleri ayrıdır; bkz. <a href="{rel(cur,"patient-packages/")}">Paketler</a>.</p></div>', tone="tone-cream")
        main += section("SEYAHAT PLANLAMASI", "Seyahat, sigorta ve takip planlaması", "",
            f'<div class="prose"><p>Seyahat zamanınızı her zaman tedaviyi yürüten hekiminiz belirler; bir web sitesindeki genel bir süre değil. Seyahat sigortanızın komplikasyonları ve tıbbi tahliyeyi kapsadığını kontrol edin; seyahatten önce yanınızda götüreceğiniz kayıtları ve takip planını teyit edin. Pratik sorularınız için <a href="{rel(cur,"contact/#enquiry")}">bizimle iletişime geçin</a>.</p></div>')
    else:
        main += section("التكاليف", "كيف تُحدَّد تكاليف العلاج في هذه الفئة؟", "",
            f'<div class="prose"><p>لا يوجد سعر موحّد للفئة. لا تنشر threeeight35° أسعار العلاج، إذ تُسعِّر العيادة أو المستشفى المستقل العلاج الطبي والرسوم السريرية كتابياً بعد التقييم، وتُدفع مباشرةً إلى الجهة نفسها. أما رسوم باقات التنسيق من threeeight35° فهي منفصلة، اطّلع على <a href="{rel(cur,"patient-packages/")}">الباقات</a>.</p></div>', tone="tone-cream")
        main += section("التخطيط للسفر", "التخطيط للسفر والتأمين والمتابعة", "",
            f'<div class="prose"><p>يحدّد طبيبك المعالج توقيت سفرك دائماً، وليس إطاراً زمنياً عاماً منشوراً على موقع إلكتروني. تحقّق من أن تأمين سفرك يغطي المضاعفات والإخلاء الطبي، وتأكّد قبل السفر من السجلات التي ستعود بها ومن خطة المتابعة. لأي أسئلة عملية، <a href="{rel(cur,"contact/#enquiry")}">تواصل معنا</a>.</p></div>')
    main += enquiry_cta(cur)
    add(p, main, "treatments", crumbs=[(L("Home", "الرئيسية", "Ana Sayfa"), ""), (L("Treatments", "العلاجات", "Tedaviler"), "treatments/"), (name, cur)])

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

def treatment_meta(t, v11):
    """The v11 meta descriptions all end ", costs and planning from Australia." although no costs are published and the site also serves
    the UAE. Keep each page's topic summary and replace that ending with what the page actually offers."""
    focus = re.sub(r",\s*costs and planning from Aus\w*\.?$", "", v11.split(":", 1)[1].strip())
    focus = re.sub(r"^guide to |business-defined ", "", focus).rstrip(". ")
    focus = re.sub(r"^.* (planning, alternatives and travel considerations)$", r"\1", focus)   # "facelift planning, …" repeated the name
    focus = focus.replace("Australian follow-up", "follow-up at home").replace(
        "premium coordination/check-up package, not clinical superiority", "premium coordination around a health check-up")
    for tail in (" What to confirm before you travel and how threeeight35° coordinates your trip.", " What to confirm before you travel."):
        d = f"{t['label']} in Türkiye: {focus}.{tail}"
        if len(d) <= 160: return d
    return f"{t['label']} in Türkiye: what to confirm before you travel and how threeeight35° coordinates your trip."

def build_treatment(sid):
    if is_ar(): return build_treatment_ar(sid)
    if is_tr(): return build_treatment_tr(sid)
    t = TREAT[sid]; r = t["rec"]; f = r["fields"]; secs = dict(r["secs"]); cid = t["cid"]; cat = CATMAP[cid]
    cur = t["dir"]
    title = f["SEO title"].replace("│", "|")
    notes = []
    if sid == "AES-14":
        title = "Body Contouring Surgery in Türkiye | threeeight35°"
        notes.append("V11 SEO title truncated (…'in'); corrected to standard pattern")
    if t["held"]:
        desc = f"{t['label']} in Türkiye: ask threeeight35° about medical travel coordination. threeeight35° coordinates medical travel and does not provide clinical care."
        notes.append("V11 meta description contains internal review wording; neutral meta used for held page")
    else:
        desc = GUIDE_META.get(sid) or treatment_meta(t, f["Meta description"])
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
        for h, body in GUIDES.get(sid, []):   # treatment-specific planning content (treatment_guides.py)
            inner = f"<p>{esc(body)}</p>" if isinstance(body, str) else '<ul class="plain-list">' + "".join(f"<li>{esc(b)}</li>" for b in body) + "</ul>"
            blocks.append(f'<section class="tsec"><h2>{esc(h)}</h2>{inner}</section>')
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

def build_treatment_ar(sid):
    """Arabic treatment page: same structure as build_treatment, with text from treatments_ar.py."""
    t = TREAT[sid]; r = t["rec"]; f = r["fields"]; secs = dict(r["secs"]); cid = t["cid"]
    cur = t["dir"]; name = TREAT_AR[sid]; cat_ar = cat_name(cid); focus = FOCUS_AR.get(sid, "")
    if t["held"]:
        desc = f"{name} في تركيا: استفسر من threeeight35° عن تنسيق السفر العلاجي. threeeight35° تنسّق السفر العلاجي ولا تقدّم رعاية سريرية."
        lead = f"لا ننشر معلومات علاجية عن {name} على موقعنا. ولا يزال بإمكانك الاستفسار عن تنسيق السفر العلاجي لهذا العلاج."
    else:
        desc = GUIDE_META_AR.get(sid) or next(d for d in (f"{name} في تركيا: {focus}. ما يجب تأكيده قبل السفر وكيف تنسّق threeeight35° رحلتك.",
                                                         f"{name} في تركيا: {focus}. ما يجب تأكيده قبل السفر.", f"{name} في تركيا: ما يجب تأكيده قبل السفر.") if len(d) <= 160)
        lead = (f"{name} موضوع عام وليس إجراءً واحداً موحّداً. تساعدك هذه الصفحة على التمييز بين الخيارات المحددة التي تندرج تحته." if t["hub"] else
                f"عند البحث في {name} في تركيا، من المهم فهم {focus}. ويجب أن تستند الخطة السريرية النهائية إلى تقييم فردي من أخصائي الرعاية الصحية المعالج.")
    p = dict(path=cur, id=r["id"], kind=f["Page type"], title=f"{name} في تركيا | threeeight35°", desc=desc, indexable=True,
             status=f["Publication status"], notes="Arabic version")
    rows = [("الفئة", f'<a href="{rel(cur, cat_dir(cid))}">{esc(cat_ar)}</a>'),
            ("دور الصفحة", "دليل لموضوع أشمل" if t["hub"] else ("استفسارات التنسيق فقط" if t["held"] else "نظرة عامة على التخطيط والتنسيق")),
            ("رسوم العلاج", "لا تنشرها threeeight35°. تُسعَّر وتُدفع مباشرةً إلى العيادة أو المستشفى المستقل."),
            ("القرارات السريرية", "يتخذها أخصائي الرعاية الصحية المعالج بعد تقييم فردي."),
            ("دور threeeight35°", "تنسيق غير سريري للسفر والتواصل.")]
    sec = lambda h, body: f'<section class="tsec"><h2>{h}</h2>{body}</section>'
    blocks = [sec("نظرة سريعة", '<dl class="glance">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in rows) + "</dl>")]
    if not t["held"]:
        u = secs.get("What should this page help a patient understand?", "")
        kind = ("dental" if "staged care" in u else "eye" if "ophthalmic" in u or "eye procedure" in u else "fertility" if "fertility pathway" in u
                else "checkup" if "abnormal findings" in u else "surgical")
        blocks.append(sec("ما يجب فهمه قبل أن تقرّر", f"<p>قبل أن تقرّر، من المفيد أن تفهم: {focus}{UND_END_AR[kind]}</p>"))
        if "What legal or regulatory issues need review?" in secs:
            blocks.append(sec("الاعتبارات القانونية والأخلاقية", "<p>قد تنطوي موضوعات الخصوبة والأجنة والأمشاج والفحص الجيني على متطلبات قانونية وأخلاقية ومتطلبات موافقة تختلف من بلد إلى آخر. تأكّد من هذه المتطلبات مع مقدّم الرعاية المعالج قبل السفر.</p>"))
        c = secs.get("What should be confirmed before travelling?", "")
        ck = ("dental" if c.startswith("Confirm the diagnosis") else "eye" if c.startswith("Confirm what examinations") else
              "fertility" if c.startswith("Confirm required records") else "surgical" if c else None)
        if ck: blocks.append(sec("ما يجب تأكيده قبل السفر", f"<p>{CONFIRM_AR[ck]}</p>"))
        if "When can a patient fly home?" in secs:
            blocks.append(sec("متى يمكنني السفر عائداً إلى بلدي؟", "<p>لا توجد مدة زمنية آمنة تنطبق على الجميع. يجب أن يحدّد الطبيب المعالج توقيت السفر بناءً على الإجراء وتعافيك الشخصي ومواعيد المتابعة اللازمة بعد العلاج.</p>"))
        if "When can a patient travel home?" in secs:
            blocks.append(sec("متى يمكنني السفر عائداً؟", "<p>يجب أن يتبع توقيت السفر نصيحة طبيب العيون المعالج ونتائج الفحص الفردية. ولا يمكن تحديد مدة عامة للقدرة على السفر دون دعم سريري خاص بالعلاج.</p>"))
        if "What happens after the results?" in secs:
            blocks.append(sec("ماذا يحدث بعد ظهور النتائج؟", "<p>ينبغي أن يوضّح مقدّم الرعاية كيف تُسلَّم النتائج، وأي النتائج تتطلب تقييماً إضافياً، وما السجلات التي يجب أخذها إلى طبيبك أو الأخصائي المناسب في بلدك. ولا يمكن لأي فحص أن يعد بتشخيص أو باستبعاد شامل للأمراض.</p>"))
        if "Does this page need recovery or fitness-to-fly advice?" in secs:
            blocks.append(sec("هل أحتاج إلى التخطيط وفق قيود على السفر؟", "<p>لا تُناقَش قيود السفر إلا عندما يفرضها فحص أو إجراء معيّن. ويقدّم لك مقدّم الرعاية المعالج النصيحة بشأن أي قيود تنطبق عليك.</p>"))
        for h, body in GUIDES_AR.get(sid, []):
            blocks.append(sec(esc(h), f"<p>{esc(body)}</p>" if isinstance(body, str) else '<ul class="plain-list">' + "".join(f"<li>{esc(b)}</li>" for b in body) + "</ul>"))
        if "What affects the cost?" in secs:
            cost_h, cost_p = "ما الذي يؤثر على التكلفة؟", ("قد تختلف التكلفة بحسب نطاق العلاج والفحوصات التشخيصية والمواد والعمل المخبري وعدد الأسنان أو مواضع العلاج وعدد المراحل. "
                              "ويقدّم مقدّم الرعاية عرض سعر العلاج الطبي مباشرةً، ولا تنشر threeeight35° رسوم العلاج ولا تتقاضاها. ويقدّم مقدّم الرعاية عرض السعر كتابياً بعد التقييم.")
        else:
            cost_h, cost_p = "كيف يُسعَّر العلاج؟", ("لا تنشر threeeight35° أسعار العلاج. ويُسعَّر العلاج الطبي والرسوم السريرية ويُدفعان مباشرةً إلى العيادة أو المستشفى المستقل، "
                              "وينبغي أن تحصل على عرض سعر مكتوب من مقدّم الرعاية بعد التقييم. وتُؤكَّد العوامل التي تؤثر على عرض السعر مع مقدّم الرعاية وفق خطتك الفردية.")
        blocks.append(sec(cost_h, f'<p>{cost_p}</p><p>تُسعَّر باقات التنسيق من threeeight35° بشكل منفصل، اطّلع على <a href="{rel(cur,"patient-packages/")}">الباقات</a>.</p>'))
    else:
        blocks.append(sec("ما يمكنك فعله الآن", f'<p>يمكنك قراءة <a href="{rel(cur,"how-it-works/")}">كيف يعمل تنسيق السفر العلاجي</a>، أو طرح سؤال عام عن التنسيق. لن نقدّم أي استشارة سريرية، وأي سؤال سريري يُوجَّه إلى أخصائي معالج مستقل.</p>'))
    blocks.append(sec("كيف تندرج threeeight35° في رحلتك؟", f'<p>تنسّق threeeight35° التواصل وتخطيط السفر ومكوّنات الرحلة المؤكَّدة حول الرعاية التي يقدّمها مقدّمو رعاية صحية مستقلون. أما التشخيص وتحديد الملاءمة والموافقة المستنيرة والعلاج وقرارات المتابعة السريرية فهي من مسؤولية أخصائيي الرعاية الصحية المعالجين. اقرأ المزيد <a href="{rel(cur,"about/")}">عن threeeight35°</a> وعن <a href="{rel(cur,"how-it-works/")}">كيف تسير الرحلة</a>.</p>'))
    rel_ids, _ = related_ids(sid)
    rl = "".join(f'<li><a href="{rel(cur, TREAT[s]["dir"])}">{esc(TREAT_AR[s])}</a></li>' for s in rel_ids)
    blocks.append(sec("صفحات ذات صلة", f'<ul class="linklist">{rl}<li><a href="{rel(cur, cat_dir(cid))}">جميع صفحات {esc(cat_ar)}</a></li></ul>'))
    blocks.append(f'<p class="disclaimer-small">تقدّم هذه الصفحة معلومات عامة عن تنسيق السفر العلاجي فقط. ولا تشخّص أي حالة، ولا توصي بعلاج لشخص بعينه، ولا تغني عن استشارة أخصائي رعاية صحية مؤهّل. <a href="{rel(cur,"medical-disclaimer/")}">إخلاء المسؤولية الطبية</a></p>')
    aside = f'''<aside class="tside" aria-label="الخطوات التالية"><div class="side-card"><h2>استفسر عن التنسيق</h2><p>أخبرنا بما تبحث عنه، ونحن نساعدك في الجانب العملي من الرحلة.</p>
<a class="btn btn-navy btn-block" href="{rel(cur,"contact/#enquiry")}">أرسل استفسارك</a>
<p class="small">يُرجى عدم إرسال سجلات طبية عبر نموذج الاستفسار.</p>
<ul class="linklist"><li><a href="{rel(cur, cat_dir(cid))}">{esc(cat_ar)}</a></li><li><a href="{rel(cur,"patient-packages/")}">الباقات</a></li></ul></div></aside>'''
    main = f'''<section class="page-head tpage-head"><div class="container"><p class="eyebrow">{esc(cat_ar)}</p><h1>{esc(name)} في تركيا</h1><p class="lead">{esc(lead)}</p></div></section>
<div class="container tlayout"><article class="tmain">{"".join(blocks)}</article>{aside}</div>'''
    main += enquiry_cta(cur)
    add(p, main, "treatments", crumbs=[("الرئيسية", ""), ("العلاجات", "treatments/"), (cat_ar, cat_dir(cid)), (name, cur)])

def build_treatment_tr(sid):
    """Turkish treatment page: same structure as build_treatment, with text from treatments_tr.py."""
    t = TREAT[sid]; r = t["rec"]; f = r["fields"]; secs = dict(r["secs"]); cid = t["cid"]
    cur = t["dir"]; name = TREAT_TR[sid]; cat_tr = cat_name(cid); focus = FOCUS_TR.get(sid, "")
    if t["held"]:
        desc = f"Türkiye'de {name}: tıbbi seyahat koordinasyonu için threeeight35°'e danışın. threeeight35° tıbbi seyahati koordine eder, klinik bakım sağlamaz."
        lead = f"Web sitemizde {name} hakkında tedavi bilgisi yayınlamıyoruz. Yine de bu tedavi için tıbbi seyahat koordinasyonu hakkında bilgi alabilirsiniz."
    else:
        desc = GUIDE_META_TR.get(sid) or next(d for d in (f"Türkiye'de {name}: {focus}. Seyahatten önce teyit edilmesi gerekenler ve threeeight35°'in yolculuğunuzu nasıl koordine ettiği.",
                                                         f"Türkiye'de {name}: {focus}. Seyahatten önce teyit edilmesi gerekenler.", f"Türkiye'de {name}: seyahatten önce teyit edilmesi gerekenler.") if len(d) <= 160)
        lead = (f"{name} tek ve standart bir işlem değil, genel bir başlıktır. Bu sayfa, bu başlık altındaki belirli seçenekleri ayırt etmenize yardımcı olur." if t["hub"] else
                f"Türkiye'de {name} seçeneklerini araştırırken şu konuyu anlamak önemlidir: {focus}. Nihai klinik plan, tedaviyi yürüten sağlık profesyonelinin bireysel değerlendirmesine dayanmalıdır.")
    p = dict(path=cur, id=r["id"], kind=f["Page type"], title=f"Türkiye'de {name} | threeeight35°", desc=desc, indexable=True,
             status=f["Publication status"], notes="Turkish version")
    rows = [("Kategori", f'<a href="{rel(cur, cat_dir(cid))}">{esc(cat_tr)}</a>'),
            ("Sayfanın rolü", "Daha geniş bir konu için rehber" if t["hub"] else ("Yalnızca koordinasyon talepleri" if t["held"] else "Planlama ve koordinasyona genel bakış")),
            ("Tedavi ücretleri", "threeeight35° tarafından yayınlanmaz. Bağımsız klinik veya hastane tarafından fiyatlandırılır ve doğrudan onlara ödenir."),
            ("Klinik kararlar", "Bireysel değerlendirmeden sonra tedaviyi yürüten sağlık profesyoneli tarafından verilir."),
            ("threeeight35°'in rolü", "Seyahat ve iletişimin klinik dışı koordinasyonu.")]
    sec = lambda h, body: f'<section class="tsec"><h2>{h}</h2>{body}</section>'
    blocks = [sec("Kısa bakış", '<dl class="glance">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in rows) + "</dl>")]
    if not t["held"]:
        u = secs.get("What should this page help a patient understand?", "")
        kind = ("dental" if "staged care" in u else "eye" if "ophthalmic" in u or "eye procedure" in u else "fertility" if "fertility pathway" in u
                else "checkup" if "abnormal findings" in u else "surgical")
        blocks.append(sec("Karar vermeden önce anlamanız gerekenler", f"<p>Karar vermeden önce şunları anlamak faydalıdır: {focus}{UND_END_TR[kind]}</p>"))
        if "What legal or regulatory issues need review?" in secs:
            blocks.append(sec("Yasal ve etik konular", "<p>Doğurganlık, embriyolar, gametler ve genetik testlerle ilgili konular ülkeden ülkeye değişen yasal, etik ve onam gerekliliklerini içerebilir. Seyahatten önce bu gereklilikleri tedaviyi yürüten sağlık kuruluşuyla teyit edin.</p>"))
        c = secs.get("What should be confirmed before travelling?", "")
        ck = ("dental" if c.startswith("Confirm the diagnosis") else "eye" if c.startswith("Confirm what examinations") else
              "fertility" if c.startswith("Confirm required records") else "surgical" if c else None)
        if ck: blocks.append(sec("Seyahatten önce teyit edilmesi gerekenler", f"<p>{CONFIRM_TR[ck]}</p>"))
        if "When can a patient fly home?" in secs:
            blocks.append(sec("Ülkeme ne zaman uçabilirim?", "<p>Herkes için geçerli güvenli bir süre yoktur. Seyahat zamanını; işleme, kişisel iyileşmenize ve tedavi sonrası gereken kontrollere göre tedaviyi yürüten hekim belirlemelidir.</p>"))
        if "When can a patient travel home?" in secs:
            blocks.append(sec("Ne zaman dönebilirim?", "<p>Seyahat zamanı, tedaviyi yürüten göz hekiminin önerisine ve bireysel muayene sonuçlarına göre belirlenmelidir. Tedaviye özgü klinik destek olmadan seyahat edebilirlik için genel bir süre belirlenemez.</p>"))
        if "What happens after the results?" in secs:
            blocks.append(sec("Sonuçlardan sonra ne olur?", "<p>Sağlık kuruluşu, sonuçların nasıl teslim edileceğini, hangi bulguların ek değerlendirme gerektirdiğini ve ülkenizdeki doktorunuza veya ilgili uzmana hangi kayıtları götürmeniz gerektiğini açıklamalıdır. Hiçbir tarama bir teşhis veya hastalıkların kapsamlı biçimde dışlanmasını vaat edemez.</p>"))
        if "Does this page need recovery or fitness-to-fly advice?" in secs:
            blocks.append(sec("Seyahat kısıtlamalarına göre plan yapmam gerekir mi?", "<p>Seyahat kısıtlamaları yalnızca belirli bir tetkik veya işlem bunu gerektirdiğinde ele alınır. Sizin için geçerli kısıtlamalar konusunda tedaviyi yürüten sağlık kuruluşu sizi bilgilendirir.</p>"))
        for h, body in GUIDES_TR.get(sid, []):
            blocks.append(sec(esc(h), f"<p>{esc(body)}</p>" if isinstance(body, str) else '<ul class="plain-list">' + "".join(f"<li>{esc(b)}</li>" for b in body) + "</ul>"))
        if "What affects the cost?" in secs:
            cost_h, cost_p = "Maliyeti neler etkiler?", ("Maliyet; tedavinin kapsamına, teşhis amaçlı tetkiklere, malzemelere, laboratuvar çalışmasına, diş veya tedavi bölgesi sayısına ve aşama sayısına göre değişebilir. "
                              "Tıbbi tedavinin fiyat teklifini doğrudan sağlık kuruluşu verir; threeeight35° tedavi ücretlerini yayınlamaz ve tahsil etmez. Sağlık kuruluşu fiyat teklifini değerlendirmeden sonra yazılı olarak sunar.")
        else:
            cost_h, cost_p = "Tedavi nasıl fiyatlandırılır?", ("threeeight35° tedavi fiyatlarını yayınlamaz. Tıbbi tedavi ve klinik ücretleri bağımsız klinik veya hastane tarafından fiyatlandırılır ve doğrudan onlara ödenir; "
                              "değerlendirmeden sonra sağlık kuruluşundan yazılı bir fiyat teklifi almalısınız. Teklifi etkileyen etkenler, bireysel planınıza göre sağlık kuruluşuyla teyit edilir.")
        blocks.append(sec(cost_h, f'<p>{cost_p}</p><p>threeeight35° koordinasyon paketleri ayrıca fiyatlandırılır; bkz. <a href="{rel(cur,"patient-packages/")}">Paketler</a>.</p>'))
    else:
        blocks.append(sec("Şimdi neler yapabilirsiniz", f'<p><a href="{rel(cur,"how-it-works/")}">Tıbbi seyahat koordinasyonunun nasıl işlediğini</a> okuyabilir veya koordinasyonla ilgili genel bir soru sorabilirsiniz. Klinik tavsiye vermeyiz; klinik sorular bağımsız ve tedaviyi yürüten bir uzmana yönlendirilir.</p>'))
    blocks.append(sec("threeeight35° yolculuğunuzda nerede yer alır?", f'<p>threeeight35°, bağımsız sağlık kuruluşlarının sunduğu bakım etrafında iletişimi, seyahat planlamasını ve yolculuğun teyit edilmiş bölümlerini koordine eder. Teşhis, uygunluk, aydınlatılmış onam, tedavi ve klinik takip kararları tedaviyi yürüten sağlık profesyonellerinin sorumluluğundadır. <a href="{rel(cur,"about/")}">threeeight35° hakkında</a> ve <a href="{rel(cur,"how-it-works/")}">yolculuğun nasıl işlediği</a> hakkında daha fazlasını okuyun.</p>'))
    rel_ids, _ = related_ids(sid)
    rl = "".join(f'<li><a href="{rel(cur, TREAT[s]["dir"])}">{esc(TREAT_TR[s])}</a></li>' for s in rel_ids)
    blocks.append(sec("İlgili sayfalar", f'<ul class="linklist">{rl}<li><a href="{rel(cur, cat_dir(cid))}">Tüm {esc(cat_tr)} sayfaları</a></li></ul>'))
    blocks.append(f'<p class="disclaimer-small">Bu sayfa yalnızca tıbbi seyahat koordinasyonu hakkında genel bilgi sunar. Herhangi bir rahatsızlığa teşhis koymaz, bir kişiye tedavi önermez ve uygun nitelikli bir sağlık profesyonelinin tavsiyesinin yerini tutmaz. <a href="{rel(cur,"medical-disclaimer/")}">Tıbbi Bilgilendirme ve Sorumluluk Reddi</a></p>')
    aside = f'''<aside class="tside" aria-label="Sonraki adımlar"><div class="side-card"><h2>Koordinasyon hakkında bilgi alın</h2><p>Ne araştırdığınızı bize anlatın; yolculuğun pratik tarafında size yardımcı olalım.</p>
<a class="btn btn-navy btn-block" href="{rel(cur,"contact/#enquiry")}">Talep Gönderin</a>
<p class="small">Lütfen talep formu üzerinden tıbbi kayıt göndermeyin.</p>
<ul class="linklist"><li><a href="{rel(cur, cat_dir(cid))}">{esc(cat_tr)}</a></li><li><a href="{rel(cur,"patient-packages/")}">Paketler</a></li></ul></div></aside>'''
    main = f'''<section class="page-head tpage-head"><div class="container"><p class="eyebrow">{esc(cat_tr)}</p><h1>Türkiye'de {esc(name)}</h1><p class="lead">{esc(lead)}</p></div></section>
<div class="container tlayout"><article class="tmain">{"".join(blocks)}</article>{aside}</div>'''
    main += enquiry_cta(cur)
    add(p, main, "treatments", crumbs=[("Ana Sayfa", ""), ("Tedaviler", "treatments/"), (cat_tr, cat_dir(cid)), (name, cur)])

INDEX_TREATMENTS = False   # clinical gate: flip to True only when Clinical Review Passed (see README)
