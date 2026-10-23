# -*- coding: utf-8 -*-
import html, os, sys, csv, shutil, re
sys.path.insert(0, os.path.dirname(__file__))
import pages, pages2
from pages2 import *
from lib import *

out = ROOT
OLD_PREFIX = "medical-travel-agency/"   # the site's address before it moved to the domain root
# clear generated html (keep assets, _build)
for d in ["treatments","patient-packages","how-it-works","about","faqs","contact","privacy","terms","medical-disclaimer","editorial-policy","medical-travel-turkiye-from-australia",OLD_PREFIX.strip("/"),"ar"]+[s[1].strip("/") for s in SPOKES]:
    shutil.rmtree(os.path.join(out, d), ignore_errors=True)
for f in ("index.html","404.html","sitemap.xml","robots.txt","llms.txt"):
    if os.path.exists(os.path.join(out, f)): os.remove(os.path.join(out, f))

build_home(); build_directory()
for c in CATS: build_category(c)
for sid in TREAT: build_treatment(sid)
build_packages(); build_how(); build_about(); build_faqs(); build_contact()
build_privacy(); build_terms(); build_disclaimer(); build_editorial(); build_geo()

# Arabic versions of the core pages (lib.AR_PAGES), written under ar/
set_lang("ar")
build_home(); build_directory()
for c in CATS: build_category(c)
for sid in TREAT: build_treatment(sid)
build_packages(); build_how(); build_about(); build_faqs(); build_contact()
build_privacy(); build_terms(); build_disclaimer()
set_lang("en")
assert {p["en_path"] for p in PAGES if p["path"].startswith("ar/")} == AR_PAGES

paths = set()
for p in PAGES:
    assert p["path"] not in paths, p["path"]; paths.add(p["path"])
    d = os.path.join(out, p["path"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(p["html"])

# 404 (absolute asset URLs because it may be served from any depth)
n = dict(path="", title="Page not found | threeeight35° Medical Travel Agency", desc="This page could not be found.", robots="noindex,follow", canon="")
h404 = head(n).replace('href="./assets', 'href="' + BASE + 'assets').replace('href="assets', 'href="' + BASE + 'assets')
body404 = header("", "") + '\n<main id="main" tabindex="-1"><section class="page-head"><div class="container"><p class="eyebrow">404</p><h1>Page not found</h1><p class="lead">The page you are looking for is not available. Try the treatments catalogue or make an enquiry.</p><div class="btn-row"><a class="btn btn-navy" href="' + BASE + '">Home</a><a class="btn btn-outline-navy" href="' + BASE + 'treatments/">Treatments</a></div></div></section></main>\n' + footer("")
html404 = (h404 + body404)
# make every relative link absolute for the 404 page
html404 = re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#)([^"]*)"', lambda m: f'{m.group(1)}="{BASE}{m.group(2).lstrip("./")}"', html404)
open(os.path.join(out, "404.html"), "w", encoding="utf-8").write(html404)

# sitemap (indexable only) + robots
urls = [p for p in PAGES if p["indexable"]]
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in sorted(urls, key=lambda x: x["path"]):
    sm.append(f'<url><loc>{BASE}{p["path"]}</loc><lastmod>{BUILD_DATE}</lastmod></url>')
sm.append("</urlset>")
open(os.path.join(out, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")
open(os.path.join(out, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
open(os.path.join(out, ".nojekyll"), "w").write("")

# Redirects from the site's former address (https://threeeight35.com/medical-travel-agency/...) to the same page at the domain root.
# GitHub Pages has no server-side redirects; an instant refresh plus canonical is treated by search engines as a permanent redirect.
for p in PAGES:
    if p["path"].startswith("ar/"): continue   # Arabic pages are new; they never had an old address
    new = BASE + p["path"]
    d = os.path.join(out, OLD_PREFIX.strip("/"), p["path"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(
        f'<!DOCTYPE html>\n<html lang="en-AU"><head><meta charset="utf-8"><title>{html.escape(p["title"])}</title>'
        f'<meta http-equiv="refresh" content="0; url={new}"><link rel="canonical" href="{new}"></head>'
        f'<body><p>This page has moved to <a href="{new}">{new}</a>.</p></body></html>\n')

# llms.txt (llmstxt.org format); links follow the same HELD_FROM_INDEX gate as the sitemap
KEY_PAGES = [("", "Home", "overview of the service, packages and how the journey works"),
             ("treatments/", "Treatments catalogue", "8 medical categories and the treatment pages within each"),
             ("patient-packages/", "Patient packages", "package prices, inclusions and who pays for what"),
             ("how-it-works/", "How it works", "the coordination journey from first enquiry to follow-up"),
             ("about/", "About", "the business, its coordination role and founder"),
             ("faqs/", "FAQs", "common questions about packages, treatment and travel"),
             ("contact/", "Contact", "enquiry form and Australia, UAE and Istanbul contacts"),
             ("medical-travel-turkiye-from-australia/", "Medical travel to Türkiye from Australia", "practical guide for Australian patients"),
             ("medical-disclaimer/", "Medical information disclaimer", "limits of the information on this site"),
             ("privacy/", "Privacy policy", "how personal information is handled"),
             ("terms/", "Terms & conditions", "terms for coordination services")]
cleared = {p["path"] for p in PAGES if p["indexable"]}
llms = [f"# {SITE}", "",
        f"> Independent medical travel coordination service connecting patients from Australia, the UAE and other international markets with independent healthcare providers in Türkiye. {SITE.split(' ')[0]} is not a healthcare provider.", "",
        "## What we do",
        "- Coordinate the non-clinical side of medical travel to Türkiye: provider introductions, consultations and quotations, accommodation, private transfers in Istanbul and support in English, Arabic and Turkish during the stay.",
        "- Markets: Australia and other international markets (Australia & International contact line), and the United Arab Emirates and GCC (UAE & GCC contact line), with a coordinator supporting patients during their stay in Istanbul.",
        "- Languages: English, Arabic and Turkish.", "",
        "## Not a healthcare provider",
        NOTICE.split(": ", 1)[1],
        "Medical treatment is quoted by and paid directly to the independent clinic or hospital.", "",
        "## Coordination packages (prices in Australian dollars)"]
for pk in PACKAGES:
    fixed = "" if pk["price"].startswith("From") else " (fixed price)"
    guests = pk["guests"].replace("you and", "the patient and", 1)
    llms.append(f"- {pk['name']}: {pk['price']}{fixed}. Includes medical travel coordination, accommodation for {pk['nights']} for {guests}, and private transfers in Istanbul. {pk['audience']}." + (f" {pk['note'].replace('you accept', 'the patient accepts')}" if pk.get("note") else ""))
llms += ["",
         "Not included in any package: medical treatment and international flights. Extra nights the patient chooses are paid directly to the hotel; a longer stay advised by the treating clinician is quoted separately. Patients who prefer to arrange their own accommodation or transport receive a revised quote. A written, itemised proposal is provided before the patient proceeds.", "",
         "## Contact",
         f"- Email: {EMAIL}", f"- Australia: {PHONE_AU}", f"- United Arab Emirates: {PHONE_UAE}", f"- ABN: {ABN}", "",
         "## Key pages"]
llms += [f"- [{name}]({BASE}{path}): {note}" for path, name, note in KEY_PAGES if path in cleared]
if "ar/" in cleared:
    llms += ["", "## العربية (Arabic)",
             f"- [threeeight35° بالعربية]({BASE}ar/): Arabic versions of the home, packages, how it works, about, FAQs, contact, treatments catalogue, category and treatment pages, privacy, terms and medical disclaimer"]
open(os.path.join(out, "llms.txt"), "w", encoding="utf-8").write("\n".join(llms) + "\n")

# register
with open(os.path.join(out, "_build", "pages-register.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["cms_id", "type", "path", "canonical_url", "indexable", "robots", "cms_status", "index_gate_reason", "build_notes", "seo_title", "meta_description"])
    for p in sorted(PAGES, key=lambda x: x["path"]):
        w.writerow([p["id"], p["kind"], "/" + p["path"], BASE + p["path"], "yes" if p["indexable"] else "no", p.get("robots", "index,follow"), p["status"], p["gate"], p.get("notes", ""), p["title"], p["desc"]])
# self-check: robots meta in generated HTML must equal register and sitemap
for p in PAGES:
    assert ('content="index,follow' in p["html"]) == p["indexable"], p["path"]
assert len(PAGES) - len(urls) == sum(p["id"].removesuffix("-AR") in HELD_FROM_INDEX for p in PAGES)   # held pages, in both languages
print("pages:", len(PAGES), "indexable:", len(urls))
