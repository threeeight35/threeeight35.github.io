# -*- coding: utf-8 -*-
import hashlib, html, json, os, re, glob
from urllib.parse import quote
from PIL import Image
from content import *
from content_ar import *
from content_tr import *

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMGDIR = os.path.join(ROOT, "assets", "img")

def typo(s): return s.replace("'", "’")
def esc(s): return typo(html.escape(s, quote=False))
def att(s): return html.escape(s, quote=True)

# ---------- language ----------
# The site is built in English at its usual paths, then again in each translation under its language code (ar/, tr/).
# Builders keep using English logical paths; L(english, arabic, turkish) picks the text for the language being built,
# and rel() points links at the translated version of a page whenever one exists.
LANGS = ("en", "ar", "tr")
LANG_INFO = {"en": dict(name="English", html='lang="en-AU"', hreflang="en-AU", og="en_AU"),
             "ar": dict(name="العربية", html='lang="ar" dir="rtl"', hreflang="ar", og="ar_AE"),
             "tr": dict(name="Türkçe", html='lang="tr"', hreflang="tr", og="tr_TR")}
_LANG = {"code": "en"}
MISSING_TR = []   # English texts that reached a Turkish page without a translation (build.py fails if any)
def set_lang(code): _LANG["code"] = code
def lang(): return _LANG["code"]
def is_ar(): return _LANG["code"] == "ar"
def is_tr(): return _LANG["code"] == "tr"
def L(en, ar, tr=None):
    c = _LANG["code"]
    if c == "ar": return ar
    if c == "tr":
        if tr is None: MISSING_TR.append(en if isinstance(en, str) else repr(en)[:120]); return en
        return tr
    return en
def prefix(): return "" if _LANG["code"] == "en" else _LANG["code"] + "/"
TRANSLATED_PAGES = {"", "treatments/", "patient-packages/", "how-it-works/", "about/", "faqs/", "contact/",
                    "privacy/", "terms/", "medical-disclaimer/", "editorial-policy/"} | {f"treatments/{c[1]}/" for c in CATS}

def upper(s): return s.replace("i", "İ").upper() if is_tr() else s.upper()   # Turkish dotted capital İ
def arrow(): return L("→", "←", "→")
def ltr(s): return f'<span dir="ltr">{s}</span>' if is_ar() else s   # keeps phone numbers in left-to-right order on Arabic pages
def cat_tx(cid): return CAT_AR[cid] if is_ar() else CAT_TR[cid]
def pkg_tx(key): return PKG_AR[key] if is_ar() else PKG_TR[key]
def cat_name(cid): return L(next(c[2] for c in CATS if c[0] == cid), CAT_AR[cid][0], CAT_TR[cid][0])

def rel(cur, target, lang_map=True):
    """relative URL from page dir `cur` ('' or 'a/b/') to site-relative `target` ('' , 'x/', 'x/#id', 'assets/..').
    `cur` is always the English logical path; on translated pages the real directory is one level deeper (ar/, tr/)."""
    depth = len([p for p in cur.strip("/").split("/") if p]) + (0 if lang() == "en" else 1)
    if lang_map and lang() != "en" and target.split("#")[0] in TRANSLATED_PAGES:
        target = prefix() + target
    pre = "../" * depth
    out = pre + target
    return out if out else "./"

def abs_url(path): return BASE + path
def page_url(path):   # absolute URL of a page in the language being built
    return abs_url((prefix() if path.split("#")[0] in TRANSLATED_PAGES else "") + path)

def asset(cur, target):
    """rel() plus a content-hash query string, so browsers fetch CSS/JS again whenever the file changes"""
    with open(os.path.join(ROOT, target), "rb") as fh:
        return rel(cur, target) + "?v=" + hashlib.md5(fh.read()).hexdigest()[:8]

# ---------- images ----------
_dim = {}
def widths(stem):
    ws = []
    for f in glob.glob(os.path.join(IMGDIR, stem + "-*.webp")):
        m = re.search(r"-(\d+)\.webp$", f)
        if m and "-og-" not in f: ws.append(int(m.group(1)))
    return sorted(ws)
def dims(stem, w):
    k = (stem, w)
    if k not in _dim:
        with Image.open(os.path.join(IMGDIR, f"{stem}-{w}.webp")) as im: _dim[k] = im.size
    return _dim[k]

def img(cur, stem, alt, sizes, cls="", eager=False, fetch=False, pick=None, style=""):
    ws = widths(stem)
    srcset = ", ".join(f"{rel(cur, f'assets/img/{stem}-{w}.webp')} {w}w" for w in ws)
    w = pick or ws[len(ws)//2]
    W, H = dims(stem, w)
    loading = 'loading="eager" decoding="async"' + (' fetchpriority="high"' if fetch else "") if eager else 'loading="lazy" decoding="async"'
    st = f' style="{style}"' if style else ""
    return (f'<img src="{rel(cur, f"assets/img/{stem}-{w}.webp")}" srcset="{srcset}" sizes="{sizes}" width="{W}" height="{H}" '
            f'alt="{att(alt)}" class="{cls}" {loading}{st}>')

# ---------- data model ----------
RECS = json.load(open(os.path.join(os.path.dirname(__file__), "v11_records.json"), encoding="utf-8"))
BYID = {}
for r in RECS:
    short = r["id"] if r["id"].startswith("CAT") else r["id"][4:]
    BYID[short] = r
    BYID[r["id"]] = r

def rec_name(r):
    return re.split(r" in Türkiye|:", r["title"])[0].strip()

CATMAP = {c[0]: c for c in CATS}
def cat_dir(cid): return f"treatments/{CATMAP[cid][1]}/"

TREAT = {}  # short id -> dict
NAME2ID = {}
for cid, groups in GROUPS.items():
    for gname, ids in groups:
        for sid in ids:
            r = BYID[sid]
            slug = r["fields"]["Slug"]
            held = r["fields"]["Page type"] == "Held clinical record"
            hub = r["fields"]["Page type"] == "Guide / hub"
            TREAT[sid] = dict(sid=sid, rec=r, cid=cid, group=gname, slug=slug, dir=f"{cat_dir(cid)}{slug}/",
                              label=LABELS.get(sid, rec_name(r)), name=rec_name(r), held=held, hub=hub,
                              h1=r["title"], url=r["fields"]["URL / Canonical"])
            NAME2ID[rec_name(r).lower()] = sid
            NAME2ID[LABELS.get(sid, rec_name(r)).lower()] = sid
NAME2ID['body contouring']='AES-14'; NAME2ID['gynecomastia surgery']='AES-17'
assert len(TREAT) == 70
TRANSLATED_PAGES |= {t["dir"] for t in TREAT.values()}   # treatment pages (pages.build_treatment_ar / build_treatment_tr)
V11_BASE = "https://threeeight35.com/medical-travel-agency/"   # site address in the v11 spec; the site now lives at BASE
for sid, t in TREAT.items():  # URL path integrity vs v11
    assert t["url"] == V11_BASE + t["dir"], (sid, t["url"], V11_BASE + t["dir"])

def related_ids(sid):
    names = [n.strip() for n in TREAT[sid]["rec"]["fields"].get("Related pages", "").split(",") if n.strip()]
    # names with parentheses may contain no commas; rejoin safety
    out, miss = [], []
    for n in names:
        k = n.lower()
        if k in NAME2ID: out.append(NAME2ID[k])
        else: miss.append(n)
    return out, miss

# ---------- layout ----------
NAV = [("Home", "", "home"), ("Treatments", "treatments/", "treatments"), ("Packages", "patient-packages/", "packages"),
       ("How It Works", "how-it-works/", "how"), ("About Us", "about/", "about"), ("FAQs", "faqs/", "faqs"),
       ("Contact", "contact/", "contact")]

VIDEO_CONSULT_URL = ""   # TECHNICAL/BUSINESS INPUT: verified video-consultation booking URL (SUP-13). Empty = CTA hidden.

def head(p):
    cur = p["path"]
    can = abs_url(p.get("canon", cur))
    robots = p.get("robots", "index,follow,max-image-preview:large")
    og_img = abs_url("assets/img/16_health_journey_istanbul-og-1200x630.jpg")
    og_alt = L("Sunset over the Istanbul skyline and waterway, with domed mosques and a ferry below an aeroplane in the sky.",
               "غروب الشمس فوق أفق إسطنبول ومضيق البوسفور، مع مساجد بقباب وعبّارة وطائرة في السماء.", "İstanbul silueti ve Boğaz üzerinde gün batımı; kubbeli camiler, bir vapur ve gökyüzünde bir uçak.")
    en_path = p.get("en_path")
    alts = ""
    if en_path is not None and en_path in TRANSLATED_PAGES:   # page exists in every language: tell search engines about each version
        alts = "".join(f'<link rel="alternate" hreflang="{LANG_INFO[c]["hreflang"]}" href="{abs_url(("" if c == "en" else c + "/") + en_path)}">\n' for c in LANGS)
        alts += f'<link rel="alternate" hreflang="x-default" href="{abs_url(en_path)}">\n'
    pre = ""
    if p.get("hero"):
        ws = widths("16_health_journey_istanbul")
        srcset = ", ".join(f"{rel(cur, f'assets/img/16_health_journey_istanbul-{w}.webp')} {w}w" for w in ws)
        pre = f'<link rel="preload" as="image" imagesrcset="{srcset}" imagesizes="(min-width: 960px) 52vw, 100vw" fetchpriority="high">\n'
    fonts = "".join(f'<link rel="preload" as="font" type="font/woff2" href="{rel(cur, "assets/fonts/"+f)}" crossorigin>\n'
                    for f in ("plus-jakarta-sans-latin-400-normal.woff2", "playfair-display-latin-600-normal.woff2"))
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False, separators=(",", ":"))}</script>' for j in p.get("jsonld", []))
    return f'''<!DOCTYPE html>
<html {LANG_INFO[lang()]["html"]}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{att(p["title"])}</title>
<meta name="description" content="{att(p["desc"])}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{can}">
{alts}<meta name="theme-color" content="#0b1f3b">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{att(SITE)}">
<meta property="og:locale" content="{LANG_INFO[lang()]["og"]}">
<meta property="og:title" content="{att(p.get("og_title", p["title"]))}">
<meta property="og:description" content="{att(p["desc"])}">
<meta property="og:url" content="{can}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{att(og_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{att(p.get("og_title", p["title"]))}">
<meta name="twitter:description" content="{att(p["desc"])}">
<meta name="twitter:image" content="{og_img}">
<meta name="twitter:image:alt" content="{att(og_alt)}">
{fonts}{pre}<link rel="stylesheet" href="{asset(cur, "assets/css/styles.css")}">
{ld}
</head>'''

def lang_target(cur, code):
    """Site path of this page in language `code`. Pages without a translation use the closest translated page above them."""
    if code == "en": return cur
    near = cur
    while near not in TRANSLATED_PAGES:
        near = near.rstrip("/").rpartition("/")[0] + "/" if "/" in near.rstrip("/") else ""
    return code + "/" + near

GLOBE = ('<svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/>'
         '<path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/></svg>')
SHORT = {"en": "EN", "ar": "عربي", "tr": "TR"}

def lang_switch(cur, cls):
    """Language menu: the current language, opening a list of all three, each linking to this page in that language.
    Built on <details>, so it works without JavaScript; main.js adds close-on-outside-tap. In the mobile menu it is a plain list."""
    links = [(c, rel(cur, lang_target(cur, c), lang_map=False)) for c in LANGS]
    if "mnav" in cls:
        return "".join(f'<a class="{cls}" href="{h}" lang="{LANG_INFO[c]["hreflang"]}" hreflang="{LANG_INFO[c]["hreflang"]}">{LANG_INFO[c]["name"]}</a>' for c, h in links if c != lang())
    items = "".join(f'<a href="{h}" lang="{LANG_INFO[c]["hreflang"]}" hreflang="{LANG_INFO[c]["hreflang"]}"{' aria-current="true"' if c == lang() else ""}>{LANG_INFO[c]["name"]}</a>' for c, h in links)
    return (f'<details class="lang-menu {cls}"><summary class="lang-btn" aria-label="{L("Language", "اللغة", "Dil")}: {LANG_INFO[lang()]["name"]}">{GLOBE}<span>{SHORT[lang()]}</span></summary>'
            f'<div class="lang-list">{items}</div></details>')

def header(cur, active):
    links = []
    for label, tgt, key in NAV:
        label = L(label, NAV_AR[key], NAV_TR[key])
        if key == "treatments":
            items = "".join(f'<li><a href="{rel(cur, cat_dir(c[0]))}">{esc(cat_name(c[0]))}</a></li>' for c in CATS)
            links.append(f'''<div class="nav-drop"><a class="nav-link{" active" if active==key else ""}" href="{rel(cur, tgt)}">{label}</a>
<button class="nav-drop-btn" type="button" aria-expanded="false" aria-controls="nav-treat-menu"><span class="sr-only">{L("Show treatment categories", "عرض فئات العلاج", "Tedavi kategorilerini göster")}</span><svg aria-hidden="true" width="12" height="12" viewBox="0 0 12 12"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
<div class="nav-menu" id="nav-treat-menu" hidden><p class="eyebrow">{L("8 medical categories", "8 فئات طبية", "8 tıbbi kategori")}</p><ul>{items}</ul><a class="menu-all" href="{rel(cur, tgt)}">{L("View the full treatments catalogue", "عرض دليل العلاجات الكامل", "Tüm tedavi kataloğunu görüntüleyin")} {arrow()}</a></div></div>''')
        else:
            links.append(f'<a class="nav-link{" active" if active==key else ""}" href="{rel(cur, tgt)}"{" aria-current=\"page\"" if active==key else ""}>{label}</a>')
    mob = "".join(f'<a class="mnav-link" href="{rel(cur, t)}">{L(l, NAV_AR[k], NAV_TR[k])}</a>' for l, t, k in NAV)
    mob_cats = "".join(f'<a class="mnav-sub" href="{rel(cur, cat_dir(c[0]))}">{esc(cat_name(c[0]))}</a>' for c in CATS)
    vid = f'<a class="btn btn-ghost" href="{VIDEO_CONSULT_URL}">{L("Book Consultation", "احجز استشارة", "Görüşme Ayarlayın")}</a>' if VIDEO_CONSULT_URL else ""
    return f'''<body>
<a class="skip" href="#main">{L("Skip to main content", "انتقل إلى المحتوى الرئيسي", "Ana içeriğe geç")}</a>
<header class="header" id="top">
<div class="container header-inner">
<a class="brand" href="{rel(cur, "")}" aria-label="{att(SITE)} — {L("home", "الصفحة الرئيسية", "ana sayfa")}"><span class="brand-mark">threeeight35°</span><span class="brand-sub">{L("Medical Travel Agency", SITE_SUB_AR, SITE_SUB_TR)}</span></a>
<nav class="nav" aria-label="{L("Primary", "القائمة الرئيسية", "Ana menü")}">{"".join(links)}</nav>
<div class="header-cta">{lang_switch(cur, "lang-switch")}{vid}<a class="btn btn-navy" href="{rel(cur, "contact/#enquiry")}">{L("Enquire", "استفسر", "Bilgi Al")}</a></div>
{lang_switch(cur, "lang-switch lang-switch-mobile")}
<button class="burger" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="{L("Open menu", "فتح القائمة", "Menüyü aç")}"><span></span><span></span><span></span></button>
</div>
<nav class="mobile-nav" id="mobile-nav" aria-label="{L("Mobile", "قائمة الجوال", "Mobil menü")}" hidden>
<div class="container">{mob}<p class="eyebrow mnav-h">{L("Medical categories", "الفئات الطبية", "Tıbbi kategoriler")}</p>{mob_cats}{lang_switch(cur, "mnav-link mnav-lang")}<a class="btn btn-navy btn-block" href="{rel(cur, "contact/#enquiry")}">{L("Make an Enquiry", "أرسل استفسارك", "Talep Gönderin")}</a></div>
</nav>
</header>'''

def _star(cx, cy, r, points=7, inner=0.4):
    """Points of a star polygon (flag stars), first point straight up."""
    import math
    pts = []
    for i in range(points * 2):
        a = math.pi * i / points - math.pi / 2
        rr = r if i % 2 == 0 else r * inner
        pts.append(f"{cx + rr * math.cos(a):.2f},{cy + rr * math.sin(a):.2f}")
    return " ".join(pts)

# Flags for the WhatsApp menu, drawn inline (flag emoji show as plain letters on Windows).
# Australia: Union Jack canton, Commonwealth Star and Southern Cross at official positions (10080x5040 spec scaled to 60x30).
FLAG_AU = ('<svg class="wa-flag" viewBox="0 0 60 30" width="30" height="15" aria-hidden="true"><clipPath id="wa-au-c"><path d="M0,0h30v15H0z"/></clipPath>'
           '<clipPath id="wa-au-t"><path d="M15,7.5h15v7.5zv7.5H0zH0V0zV0h15z"/></clipPath><rect width="60" height="30" fill="#012169"/>'
           '<g clip-path="url(#wa-au-c)"><path d="M0,0L30,15M30,0L0,15" stroke="#fff" stroke-width="3"/><path d="M0,0L30,15M30,0L0,15" clip-path="url(#wa-au-t)" stroke="#C8102E" stroke-width="2"/>'
           '<path d="M15,0v15M0,7.5h30" stroke="#fff" stroke-width="5"/><path d="M15,0v15M0,7.5h30" stroke="#C8102E" stroke-width="3"/></g><g fill="#fff">'
           + "".join(f'<polygon points="{_star(x, y, r, p, i)}"/>' for x, y, r, p, i in
                     [(15, 22.5, 6.4, 7, 0.44), (45, 25, 2.9, 7, 0.44), (37.5, 13.1, 2.9, 7, 0.44), (45, 5, 2.9, 7, 0.44), (52.6, 10.7, 2.9, 7, 0.44), (48, 16.3, 1.3, 5, 0.4)])
           + '</g></svg>')
FLAG_AE = ('<svg class="wa-flag" viewBox="0 0 12 6" width="30" height="15" aria-hidden="true"><rect width="12" height="2" fill="#00732F"/>'
           '<rect y="2" width="12" height="2" fill="#fff"/><rect y="4" width="12" height="2" fill="#000"/><rect width="3" height="6" fill="#FF0000"/></svg>')
WA_ICON = ('<svg aria-hidden="true" width="{s}" height="{s}" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/>'
           '<path fill="currentColor" d="M16.6 14.2c-.3-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2c0 1.3.9 2.5 1 2.7.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.6-.3z"/></svg>')

def wa_float():
    """Floating WhatsApp button (every page): opens a small menu so the visitor picks the Australia & International or UAE & GCC line.
    Built on <details>, so it opens and closes without JavaScript; main.js only adds close-on-outside-tap."""
    greet = quote(L("Hello threeeight35°, I'd like to ask about medical travel coordination.", "مرحباً threeeight35°، أودّ الاستفسار عن تنسيق السفر العلاجي.", "Merhaba threeeight35°, tıbbi seyahat koordinasyonu hakkında bilgi almak istiyorum."))
    desks = [(FLAG_AU, L("Australia & International", "أستراليا والدول الأخرى", "Avustralya ve Uluslararası"), PHONE_AU), (FLAG_AE, L("UAE & GCC", "الإمارات ودول الخليج", "BAE ve Körfez"), PHONE_UAE)]
    links = "".join(f'<a class="wa-link" href="https://wa.me/{n.replace("+", "").replace(" ", "")}?text={greet}" rel="noopener noreferrer" target="_blank">{flag}'
                    f'<span class="wa-text"><span class="wa-desk">{esc(d)}</span><span class="wa-num" dir="ltr">{n}</span></span>'
                    f'<span class="wa-go">{WA_ICON.format(s=18)}</span><span class="sr-only">{L(" (opens WhatsApp in a new tab)", " (يفتح واتساب في علامة تبويب جديدة)", " (WhatsApp yeni sekmede açılır)")}</span></a>' for flag, d, n in desks)
    title = L("Chat with us on WhatsApp", "تواصل معنا عبر واتساب", "WhatsApp üzerinden bize yazın")
    return (f'<details class="wa-float"><summary class="wa-btn" aria-label="{title}"><span class="wa-badge">{WA_ICON.format(s=24)}</span>'
            f'<span class="wa-label"><strong>WhatsApp</strong><small>{L("Chat with us", "تحدّث معنا", "Bize yazın")}</small></span></summary>'
            f'<div class="wa-menu"><div class="wa-head"><p class="wa-title">{title}</p><p class="wa-sub">{L("Choose a contact line", "اختر خط التواصل", "Bir iletişim hattı seçin")}</p></div>{links}</div></details>')

def footer(cur):
    soc = "".join(f'<li><a href="{u}" rel="noopener noreferrer" target="_blank" aria-label="{att(SITE.split(" ")[0])} {L("on", "على", "–")} {n} {L("(opens in a new tab)", "(يفتح في علامة تبويب جديدة)", "(yeni sekmede açılır)")}">{n}</a></li>' for n, u in SOCIAL)
    cats = "".join(f'<li><a href="{rel(cur, cat_dir(c[0]))}">{esc(cat_name(c[0]))}</a></li>' for c in CATS)
    nav = [(L("Home", "الرئيسية", "Ana Sayfa"), ""), (L("Treatments Catalogue", "دليل العلاجات", "Tedavi Kataloğu"), "treatments/"), (L("Medical Travel Packages", "باقات السفر العلاجي", "Tıbbi Seyahat Paketleri"), "patient-packages/"),
           (L("How It Works", "كيف نعمل", "Nasıl Çalışır"), "how-it-works/"), (L("About Us", "من نحن", "Hakkımızda"), "about/"), (L("FAQs", "الأسئلة الشائعة", "SSS"), "faqs/"), (L("Contact & Enquiries", "التواصل والاستفسارات", "İletişim ve Talepler"), "contact/")]
    legal = [(L("Privacy Policy", "سياسة الخصوصية", "Gizlilik Politikası"), "privacy/"), (L("Terms & Conditions", "الشروط والأحكام", "Şartlar ve Koşullar"), "terms/"),
             (L("Medical Information Disclaimer", "إخلاء المسؤولية الطبية", "Tıbbi Bilgilendirme ve Sorumluluk Reddi"), "medical-disclaimer/"), (L("Editorial Policy", "السياسة التحريرية", "Yayın İlkeleri"), "editorial-policy/")]
    ln = lambda items: "".join(f'<li><a href="{rel(cur, t)}">{esc(l)}</a></li>' for l, t in items)
    notice = L(esc(NOTICE), f"<strong>{NOTICE_AR_TITLE}:</strong> {NOTICE_AR_BODY}", f"<strong>{NOTICE_TR_TITLE}:</strong> {NOTICE_TR_BODY}")
    return f'''<footer class="footer">
<div class="container">
<div class="footer-grid">
<div class="footer-brand"><p class="brand-mark brand-mark-lg">threeeight35°</p><p class="brand-sub">{L("Medical Travel Agency", SITE_SUB_AR, SITE_SUB_TR)}</p>
<p class="footer-tag">{L("Your Health Journey, Beyond Borders.", "رحلتك الصحية، بلا حدود.", "Sağlık Yolculuğunuz, Sınırların Ötesinde.")}</p>
<p class="footer-desc">{L("Personalised medical travel coordination connecting patients from Australia, the UAE and other international markets with independent healthcare providers in Türkiye.", "تنسيق شخصي للسفر العلاجي يربط المرضى من أستراليا والإمارات العربية المتحدة والأسواق الدولية الأخرى بمقدّمي رعاية صحية مستقلين في تركيا.", "Avustralya, BAE ve diğer uluslararası pazarlardaki hastaları Türkiye'deki bağımsız sağlık kuruluşlarıyla buluşturan kişiye özel tıbbi seyahat koordinasyonu.")}</p>
<p class="eyebrow eyebrow-on-dark">{L("AUSTRALIA · UAE · TÜRKİYE", "أستراليا · الإمارات · تركيا", "AVUSTRALYA · BAE · TÜRKİYE")}</p></div>
<div><h2 class="footer-h">{L("Navigate", "التصفح", "Gezinme")}</h2><ul>{ln(nav)}</ul></div>
<div><h2 class="footer-h">{L("Medical categories", "الفئات الطبية", "Tıbbi kategoriler")}</h2><ul>{cats}</ul></div>
<div><h2 class="footer-h">{L("Compliance &amp; legal", "الامتثال والشؤون القانونية", "Uyum ve Yasal Bilgiler")}</h2><ul>{ln(legal)}</ul>
<h2 class="footer-h footer-h2">{L("Contact", "التواصل", "İletişim")}</h2><ul class="contact-list">
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li>{L("Australia &amp; International", "أستراليا والدول الأخرى", "Avustralya ve Uluslararası")}: <a href="tel:{PHONE_AU.replace(" ","")}">{ltr(PHONE_AU)}</a></li>
<li>{L("UAE &amp; GCC", "الإمارات ودول الخليج", "BAE ve Körfez")}: <a href="tel:{PHONE_UAE.replace(" ","")}">{ltr(PHONE_UAE)}</a></li></ul>
<h2 class="footer-h footer-h2">{L("Follow", "تابعنا", "Takip Edin")}</h2><ul class="social-list">{soc}</ul></div>
</div>
<div class="footer-notice" role="note"><p>{notice}</p></div>
<div class="footer-base"><p>{L("© 2026 threeeight35° Medical Travel Agency. All rights reserved.", "© 2026 وكالة threeeight35° للسفر العلاجي. جميع الحقوق محفوظة.", "© 2026 threeeight35° Tıbbi Seyahat Acentesi. Tüm hakları saklıdır.")}</p><p>{L("ABN", "رقم الأعمال الأسترالي (ABN)", "Avustralya İşletme Numarası (ABN)")} {ABN}</p></div>
</div>
</footer>
{wa_float()}
<script src="{asset(cur, "assets/js/form-config.js")}"></script>
<script src="{asset(cur, "assets/js/main.js")}" defer></script>
</body>
</html>'''

def breadcrumb_html(cur, crumbs):
    items = []
    for i, (n, pth) in enumerate(crumbs):
        if i == len(crumbs) - 1: items.append(f'<li aria-current="page">{esc(n)}</li>')
        else: items.append(f'<li><a href="{rel(cur, pth)}">{esc(n)}</a></li>')
    return f'<nav class="crumbs" aria-label="{L("Breadcrumb", "مسار التنقل", "Sayfa yolu")}"><ol>{"".join(items)}</ol></nav>'

def breadcrumb_ld(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": page_url(p)} for i, (n, p) in enumerate(crumbs)]}

def webpage_ld(p, crumbs):
    return {"@context": "https://schema.org", "@type": "WebPage", "@id": abs_url(p.get("canon", p["path"])) + "#webpage",
            "url": abs_url(p.get("canon", p["path"])), "name": p["title"], "description": p["desc"], "inLanguage": L("en-AU", "ar", "tr"),
            "isPartOf": {"@type": "WebSite", "@id": BASE + "#website", "name": SITE, "url": BASE},
            "publisher": {"@id": BASE + "#organization"}}

ORG_LD = {"@context": "https://schema.org", "@type": "Organization", "@id": BASE + "#organization", "name": SITE, "url": BASE,
          "email": EMAIL, "telephone": PHONE_AU, "slogan": "Your Health Journey, Beyond Borders.",
          "logo": {"@type": "ImageObject", "url": abs_url("assets/img/brand/logo.png"), "width": 1259, "height": 290},
          "description": "Medical travel coordination service connecting patients from Australia, the UAE and other international markets with independent healthcare providers in Türkiye. Not a healthcare provider.",
          "identifier": {"@type": "PropertyValue", "propertyID": "ABN", "value": ABN},
          "areaServed": [{"@type": "Country", "name": "Australia", "identifier": "AU"}, {"@type": "Country", "name": "United Arab Emirates", "identifier": "AE"}],
          "knowsLanguage": ["en", "ar", "tr"],
          "sameAs": [u for _, u in SOCIAL], "founder": {"@id": BASE + "about/#founder"},
          "contactPoint": [{"@type": "ContactPoint", "contactType": "customer support", "telephone": PHONE_AU, "email": EMAIL, "areaServed": "AU"},
                           {"@type": "ContactPoint", "contactType": "customer support", "telephone": PHONE_UAE, "email": EMAIL, "areaServed": "AE"}]}
