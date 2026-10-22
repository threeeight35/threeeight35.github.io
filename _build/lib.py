# -*- coding: utf-8 -*-
import hashlib, html, json, os, re, glob
from PIL import Image
from content import *

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMGDIR = os.path.join(ROOT, "assets", "img")

def typo(s): return s.replace("'", "’")
def esc(s): return typo(html.escape(s, quote=False))
def att(s): return html.escape(s, quote=True)

def rel(cur, target):
    """relative URL from page dir `cur` ('' or 'a/b/') to site-relative `target` ('' , 'x/', 'x/#id', 'assets/..')"""
    depth = len([p for p in cur.strip("/").split("/") if p])
    pre = "../" * depth
    out = pre + target
    return out if out else "./"

def abs_url(path): return BASE + path

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
    og_alt = "Sunset over the Istanbul skyline and waterway, with domed mosques and a ferry below an aeroplane in the sky."
    pre = ""
    if p.get("hero"):
        ws = widths("16_health_journey_istanbul")
        srcset = ", ".join(f"{rel(cur, f'assets/img/16_health_journey_istanbul-{w}.webp')} {w}w" for w in ws)
        pre = f'<link rel="preload" as="image" imagesrcset="{srcset}" imagesizes="(min-width: 960px) 52vw, 100vw" fetchpriority="high">\n'
    fonts = "".join(f'<link rel="preload" as="font" type="font/woff2" href="{rel(cur, "assets/fonts/"+f)}" crossorigin>\n'
                    for f in ("plus-jakarta-sans-latin-400-normal.woff2", "playfair-display-latin-600-normal.woff2"))
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False, separators=(",", ":"))}</script>' for j in p.get("jsonld", []))
    return f'''<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{att(p["title"])}</title>
<meta name="description" content="{att(p["desc"])}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{can}">
<meta name="theme-color" content="#0b1f3b">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{att(SITE)}">
<meta property="og:locale" content="en_AU">
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
<link rel="icon" href="{rel(cur, "favicon.ico")}" sizes="48x48">
<link rel="icon" type="image/png" href="{rel(cur, "assets/img/brand/icon-192.png")}" sizes="192x192">
<link rel="apple-touch-icon" href="{rel(cur, "assets/img/brand/apple-touch-icon.png")}">
{ld}
</head>'''

def header(cur, active):
    links = []
    for label, tgt, key in NAV:
        if key == "treatments":
            items = "".join(f'<li><a href="{rel(cur, cat_dir(c[0]))}">{esc(c[2])}</a></li>' for c in CATS)
            links.append(f'''<div class="nav-drop"><a class="nav-link{" active" if active==key else ""}" href="{rel(cur, tgt)}">Treatments</a>
<button class="nav-drop-btn" type="button" aria-expanded="false" aria-controls="nav-treat-menu"><span class="sr-only">Show treatment categories</span><svg aria-hidden="true" width="12" height="12" viewBox="0 0 12 12"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
<div class="nav-menu" id="nav-treat-menu" hidden><p class="eyebrow">8 medical categories</p><ul>{items}</ul><a class="menu-all" href="{rel(cur, tgt)}">View the full treatments catalogue →</a></div></div>''')
        else:
            links.append(f'<a class="nav-link{" active" if active==key else ""}" href="{rel(cur, tgt)}"{" aria-current=\"page\"" if active==key else ""}>{label}</a>')
    mob = "".join(f'<a class="mnav-link" href="{rel(cur, t)}">{l}</a>' for l, t, k in NAV)
    mob_cats = "".join(f'<a class="mnav-sub" href="{rel(cur, cat_dir(c[0]))}">{esc(c[2])}</a>' for c in CATS)
    vid = f'<a class="btn btn-ghost" href="{VIDEO_CONSULT_URL}">Book Consultation</a>' if VIDEO_CONSULT_URL else ""
    return f'''<body>
<a class="skip" href="#main">Skip to main content</a>
<header class="header" id="top">
<div class="container header-inner">
<a class="brand" href="{rel(cur, "")}" aria-label="{att(SITE)} — home"><span class="brand-mark">threeeight35°</span><span class="brand-sub">Medical Travel Agency</span></a>
<nav class="nav" aria-label="Primary">{"".join(links)}</nav>
<div class="header-cta">{vid}<a class="btn btn-navy" href="{rel(cur, "contact/#enquiry")}">Enquire</a></div>
<button class="burger" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu"><span></span><span></span><span></span></button>
</div>
<nav class="mobile-nav" id="mobile-nav" aria-label="Mobile" hidden>
<div class="container">{mob}<p class="eyebrow mnav-h">Medical categories</p>{mob_cats}<a class="btn btn-navy btn-block" href="{rel(cur, "contact/#enquiry")}">Make an Enquiry</a></div>
</nav>
</header>'''

def footer(cur):
    soc = "".join(f'<li><a href="{u}" rel="noopener noreferrer" target="_blank" aria-label="{att(SITE.split(" ")[0])} on {n} (opens in a new tab)">{n}</a></li>' for n, u in SOCIAL)
    cats = "".join(f'<li><a href="{rel(cur, cat_dir(c[0]))}">{esc(c[2])}</a></li>' for c in CATS)
    nav = [("Home", ""), ("Treatments Catalogue", "treatments/"), ("Medical Travel Packages", "patient-packages/"), ("How It Works", "how-it-works/"),
           ("About Us", "about/"), ("FAQs", "faqs/"), ("Contact & Enquiries", "contact/")]
    legal = [("Privacy Policy", "privacy/"), ("Terms & Conditions", "terms/"), ("Medical Information Disclaimer", "medical-disclaimer/"), ("Editorial Policy", "editorial-policy/")]
    ln = lambda L: "".join(f'<li><a href="{rel(cur, t)}">{esc(l)}</a></li>' for l, t in L)
    return f'''<footer class="footer">
<div class="container">
<div class="footer-grid">
<div class="footer-brand"><p class="brand-mark brand-mark-lg">threeeight35°</p><p class="brand-sub">Medical Travel Agency</p>
<p class="footer-tag">Your Health Journey, Beyond Borders.</p>
<p class="footer-desc">Personalised medical travel coordination connecting patients from Australia, the UAE and other international markets with independent healthcare providers in Türkiye.</p>
<p class="eyebrow eyebrow-on-dark">AUSTRALIA · UAE · TÜRKİYE</p></div>
<div><h2 class="footer-h">Navigate</h2><ul>{ln(nav)}</ul></div>
<div><h2 class="footer-h">Medical categories</h2><ul>{cats}</ul></div>
<div><h2 class="footer-h">Compliance &amp; legal</h2><ul>{ln(legal)}</ul>
<h2 class="footer-h footer-h2">Contact</h2><ul class="contact-list">
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li>Australia: <a href="tel:{PHONE_AU.replace(" ","")}">{PHONE_AU}</a></li>
<li>United Arab Emirates: <a href="tel:{PHONE_UAE.replace(" ","")}">{PHONE_UAE}</a></li></ul>
<h2 class="footer-h footer-h2">Follow</h2><ul class="social-list">{soc}</ul></div>
</div>
<div class="footer-notice" role="note"><p>{esc(NOTICE)}</p></div>
<div class="footer-base"><p>© 2026 threeeight35° Medical Travel Agency. All rights reserved.</p><p>ABN {ABN}</p></div>
</div>
</footer>
<script src="{asset(cur, "assets/js/form-config.js")}"></script>
<script src="{asset(cur, "assets/js/main.js")}" defer></script>
</body>
</html>'''

def breadcrumb_html(cur, crumbs):
    items = []
    for i, (n, pth) in enumerate(crumbs):
        if i == len(crumbs) - 1: items.append(f'<li aria-current="page">{esc(n)}</li>')
        else: items.append(f'<li><a href="{rel(cur, pth)}">{esc(n)}</a></li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'

def breadcrumb_ld(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": abs_url(p)} for i, (n, p) in enumerate(crumbs)]}

def webpage_ld(p, crumbs):
    return {"@context": "https://schema.org", "@type": "WebPage", "@id": abs_url(p.get("canon", p["path"])) + "#webpage",
            "url": abs_url(p.get("canon", p["path"])), "name": p["title"], "description": p["desc"], "inLanguage": "en-AU",
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
