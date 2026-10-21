# -*- coding: utf-8 -*-
import os, sys, csv, shutil, re
sys.path.insert(0, os.path.dirname(__file__))
import pages, pages2
from pages2 import *
from lib import *

out = ROOT
# clear generated html (keep assets, _build)
for d in ["treatments","patient-packages","how-it-works","about","faqs","contact","privacy","terms","medical-disclaimer","editorial-policy","medical-travel-turkiye-from-australia"]+[s[1].strip("/") for s in SPOKES]:
    shutil.rmtree(os.path.join(out, d), ignore_errors=True)
for f in ("index.html","404.html","sitemap.xml","robots.txt"):
    if os.path.exists(os.path.join(out, f)): os.remove(os.path.join(out, f))

build_home(); build_directory()
for c in CATS: build_category(c)
for sid in TREAT: build_treatment(sid)
build_packages(); build_how(); build_about(); build_faqs(); build_contact()
build_privacy(); build_terms(); build_disclaimer(); build_editorial(); build_geo()

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
open(os.path.join(out, "robots.txt"), "w").write(f"# NOTE: crawlers only read robots.txt at https://threeeight35.com/robots.txt. Merge these lines into the root file.\nUser-agent: *\nAllow: /medical-travel-agency/\n\nSitemap: {BASE}sitemap.xml\n")
open(os.path.join(out, ".nojekyll"), "w").write("")

# register
with open(os.path.join(out, "_build", "pages-register.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["cms_id", "type", "path", "canonical_url", "indexable", "robots", "cms_status", "index_gate_reason", "build_notes", "seo_title", "meta_description"])
    for p in sorted(PAGES, key=lambda x: x["path"]):
        w.writerow([p["id"], p["kind"], "/" + p["path"], BASE + p["path"], "yes" if p["indexable"] else "no", p.get("robots", "index,follow"), p["status"], p["gate"], p.get("notes", ""), p["title"], p["desc"]])
# self-check: robots meta in generated HTML must equal register and sitemap
for p in PAGES:
    assert ('content="index,follow' in p["html"]) == p["indexable"], p["path"]
assert len(urls) == len(CLEARED_FOR_INDEX)
print("pages:", len(PAGES), "indexable:", len(urls))
