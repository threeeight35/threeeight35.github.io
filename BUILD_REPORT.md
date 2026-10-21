# threeeight35° Medical Travel Agency — Build Report (v11 build, 21 October 2026)

Site root = `https://threeeight35.com/medical-travel-agency/`. Static HTML/CSS/JS, no framework, no build step needed to deploy (the Python generator in `_build/` is optional and only needed to regenerate pages).

## 1–2. Files created / replaced
All files are new. `index.html` replaces the old single-page app; the legacy "13 specialties / 105 procedures", package-fee inclusions, "accredited" claims, cost estimator, fake-success form and `social-preview.jpeg` reference are NOT carried forward.

## 3. Folder structure
```
index.html                       home (SUP-01)
404.html  sitemap.xml  robots.txt  .nojekyll  README.md  BUILD_REPORT.md
assets/css/styles.css            assets/js/main.js   assets/js/form-config.js
assets/fonts/                    self-hosted Playfair Display + Plus Jakarta Sans (woff2)
assets/img/*.webp / *.jpg        responsive derivatives (real conversions)
assets/img/source/               original supplied PNG/JPEG files, untouched
treatments/index.html            directory (SUP-02)
treatments/<category>/index.html            8 category pages (CAT-01…08)
treatments/<category>/<slug>/index.html    70 treatment pages (TRT-…)
patient-packages/ how-it-works/ about/ faqs/ contact/ privacy/ terms/ medical-disclaimer/ editorial-policy/
medical-travel-turkiye-from-australia/      GEO-AU-01 + 7 spoke folders (GEO-AU-02…08)
_build/                          generator (build.py, lib.py, components.py, pages*.py, content.py), v11_records.json, pages-register.csv
```
## 4–6. Pages generated
97 HTML pages (+404): 1 home, 1 directory, **8 category pages, 70 treatment pages (78/78 matched to Version 11 URLs, IDs and canonicals)**, 5 commercial/trust pages (packages, how-it-works, about, faqs, contact), 4 legal/trust pages, 1 GEO hub, 7 GEO spokes. Every page carries `data-cms-id`. `_build/pages-register.csv` lists every page with CMS ID, URL, indexability, status.

## 7. SEO / GEO implemented
Unique title + meta + canonical on every page (canonicals are self-referencing and unchanged even on noindex pages); one H1 per page; breadcrumbs (HTML + BreadcrumbList JSON-LD); WebPage JSON-LD; Organization + Person (founder) on Home/About only; Open Graph/Twitter using the hero image (1200×630 derivative of `16_health_journey_istanbul.png`); `sitemap.xml` (indexable pages only); en-AU; answer-first Q&A on hub/spokes; treatment → category → GEO-AU-01 → Contact path on every treatment page; related links from v11 "Related pages". No MedicalWebPage, ratings, reviews, FAQPage or LocalBusiness markup.

### Indexing policy (amended after independent QA — matches generated HTML, pages-register.csv and sitemap.xml exactly)
Only pages with **no clinical, editorial, legal or business approval outstanding** are indexable. Totals across 97 pages: **3 `index,follow`, 94 `noindex,follow`** (the 404 page is also noindex).

| Indexable (in sitemap.xml) | Why cleared |
|---|---|
| Home (SUP-01), Treatments directory (SUP-02), About (SUP-03) | Built from v11-approved copy; no approval flag outstanding. Home/directory meta descriptions were written by the build (v11 gives none) — tighten if you wish. |

| `noindex,follow` (not in sitemap) | Reason recorded in the register column `index_gate_reason` |
|---|---|
| 8 category pages (CAT-01…08) | Clinical review pending |
| 70 treatment pages | Clinical review pending (7 are also HELD: EYE-05, EYE-06, HEA-05, IVF-07, GEN-03, GEN-04, GEN-05) |
| GEO-AU-01 hub and 7 spokes (GEO-AU-02…08) | Derived copy/metadata; editorial approval required |
| How It Works, FAQs, Editorial & Medical Review Policy | Derived from v11 statements; editorial approval required |
| Medical Information Disclaimer | Derived copy; legal review recommended; editorial approval required |
| Patient Packages | Legal/consumer-law review recommended; page metadata derived |
| Contact & Enquiry | Form back-end not configured; consent wording awaiting legal approval |
| Privacy, Terms | Legal review pending |

**To clear a page for indexing:** add its CMS ID to `CLEARED_FOR_INDEX` in `_build/pages.py` (single gate; sets the robots meta, sitemap and register together), then `cd _build && python3 build.py`. `build.py` asserts that robots meta, register and sitemap agree. Treat Patient Packages, Contact and the legal pages as commercial pages that you will probably want indexed soon after their reviews.

## 8–12. Items still needed
**BUSINESS INPUT REQUIRED**
- Video-consultation booking URL (SUP-13). Until set (`VIDEO_CONSULT_URL` in `_build/lib.py`) the "Schedule Video Consultation / Schedule Video Call / Book Consultation" buttons are **hidden** (no dead links).
- Desk operating hours (Mon–Sat times in SUP-11 are marked "reconfirm") — NOT published.
- Confirmed coordination-package inclusion lists per package — not in v11; pages say inclusions are listed in the written proposal. Stay profiles (4–7 / 7–14 / 10+ nights) are published as v11 documents them; reconfirm.
- Optional add-on prices (A$590 / A$250 / hotel at cost) and the "no clinic commission" statement — NOT published (v11 requires reconfirmation).
- Whether "Luxury 5-Star Hotels" / "Luxury VIP Cars" may be advertised for every booking, and the supplier payment flow (SUP-10 flags). Copy follows the approved v11 spec with its written-proposal test.
- Image rights/licences for all 12 images; approved hero crop (mobile uses `object-position`), founder photo approval.
- Confirm WhatsApp links (`wa.me/61426499822`, `wa.me/971544144203`, built from the phone numbers) work as intended.
- Logo file (none supplied): a text wordmark is used. Favicon / site icon (none supplied): none referenced.
- Slugs/titles/metas not defined in v11 (see "Derived content").
**CLINICIAN INPUT REQUIRED** — every treatment/category page: definition, suitability, risks, recovery, fitness-to-fly, comparison text; scope for the 7 HELD pages and 6 guide/hub pages. Reviewer name, credentials, jurisdiction, date, version.
**LEGAL INPUT REQUIRED** — final Privacy Policy (APP 8, retention); Terms incl. payment (50 % on acceptance, balance 14 days before travel), cancellation and refund (A$350 deduction) — NOT published; form consent checkbox wording (draft in `pages2.py` `FORM_CONSENT`); fertility/genetic-testing legal copy; consumer-law review of package pricing.
**SOURCE REQUIRED** — v11 has no claim-level source map. The only external source used is Smartraveller (medical tourism: basic travel insurance rarely covers medical tourism; check cover for complications and evacuation; research the destination; avoid unofficial facilities) on GEO hub/spokes, verified against smartraveller.gov.au on 21 Oct 2026.
**TECHNICAL CONFIGURATION REQUIRED** — enquiry form endpoint (below); root-level `robots.txt`; Search Console sitemap submission; final browser/device QA.

## Derived content (not in v11 — needs editorial approval)
v11 contains **no copy** for: How It Works, FAQs, Privacy, Terms, Medical Disclaimer, Editorial Policy, GEO-AU-01…08 body/metadata, category meta descriptions, or the directory/contact/packages page metas. These were written using only v11 statements (About, Packages, SUP-10…14, treatment-record text, global rules) and are flagged `derived` in the register. Proposed (not v11-approved) URLs: `/how-it-works/ /faqs/ /privacy/ /terms/ /medical-disclaimer/ /editorial-policy/` and the 7 GEO spoke slugs.

## v11 anomalies handled (please review)
- AES-14 SEO title is truncated in v11 ("…Different? in"); corrected to "…Different? | threeeight35°".
- CAT-03 H1/title "Dental in Türkiye" is kept exactly as v11 (grammatically awkward); navigation uses "Dental Treatments". Consider editing v11.
- v11 treatment/guide/held records contain editor instructions ("It should explain…", "Do not publish…", "Review gate"). These were converted to patient-facing wording or omitted; no internal text is shown.
- v11 held records' meta descriptions contain internal review wording; neutral metas used (EYE-05/06, HEA-05, IVF-07, GEN-03/04/05).
- v11 TECH-02 lists three social links; TECH-03/SUP-14 and your brief add YouTube. All four are used; LinkedIn is absent.
- v11 uses "│" in titles; "|" is used. Display-order spellings "Specialized/Fertilization" → Australian "Specialised/Fertilisation".
- Treatment-specific meta descriptions follow v11's pattern ("Research X in Türkiye: …"), which is templated; v11 asks for unique CMS metadata — rewrite after clinician review.

## 13. Connecting the enquiry form
The form (`/contact/`) validates client-side and posts `FormData` (fields: full_name, email, country, preferred_contact, treatment_category, specific_procedure, message, privacy_consent, `_gotcha` honeypot, `_subject`, `_page`) to `window.T35_FORM.endpoint` in `assets/js/form-config.js`. Empty endpoint ⇒ honest "not sent" message with email/phone fallback (never a fake success). Steps:
1. Create a form endpoint with a service that emails hello@threeeight35.com (e.g. Formspree, Web3Forms, Getform, Formspark) or your own server function; verify the destination mailbox.
2. Paste the **public** endpoint URL into `endpoint`. Never place passwords, SMTP credentials or API secrets in this file.
3. Enable the service's server-side validation, spam filtering and rate limiting; optionally set `turnstileSiteKey` (Cloudflare Turnstile public key) and enable verification on the service.
4. Allow the site origin (`https://threeeight35.com`) in the service's allowed domains.
5. Test: valid submission arrives; each required field; consent; category→procedure filter; failure state (disconnect network); mobile Safari. Success is shown only on an HTTP 2xx response.
6. Add the privacy-policy wording approved by legal and update `FORM_CONSENT`.

## 14. Before production
Resolve the items above (at minimum: form endpoint, legal review of Privacy/Terms and consent text, image rights, clinician sign-off before indexing treatment pages); merge `robots.txt` lines into `https://threeeight35.com/robots.txt`; run Lighthouse/axe on the live URL; test social previews (Facebook Sharing Debugger, LinkedIn not applicable); click-test the four social links and both WhatsApp links.

## 15. Deploying to GitHub Pages
Do not overwrite the live site until you have had this ZIP reviewed. Then: (1) in a branch of your existing repo, delete the old `index.html` and any old `images/`; (2) copy the contents of this ZIP into the folder that is served at `/medical-travel-agency/` (the repository root if the repo is the `medical-travel-agency` project site); keep `.nojekyll`; (3) commit and open a pull request; (4) check the Pages preview/staging URL (all paths are relative, so it works at any base); (5) merge; (6) submit `https://threeeight35.com/medical-travel-agency/sitemap.xml` in Search Console. Note: `assets/img/source/` holds the 45 MB originals; remove that folder from the deployed repo if you prefer to keep originals elsewhere (nothing links to it).

## Performance / accessibility notes
Hero preloaded and eager (`fetchpriority=high`), all other images lazy with width/height; fonts self-hosted (no Google Fonts calls); ~5.7 MB site excluding originals; contrast-checked palette (bronze text uses #8f663b on light backgrounds; navy text on bronze buttons); skip link, landmarks, focus-visible, labelled form fields with `aria-live` errors, 48 px tap targets, reduced-motion support.

## Amendment log (post-QA rebuild)
- Indexing gate centralised (`CLEARED_FOR_INDEX`); categories, GEO-AU-01, How It Works, FAQs, Editorial Policy, Medical Disclaimer, Packages and Contact moved to `noindex,follow`; sitemap regenerated with 3 URLs; register gained `index_gate_reason`.
- Unchanged: 70 treatment pages, 7 GEO spokes, Privacy, Terms (already noindex); image and page architecture; package pricing; agency/provider wording; social links; form architecture; **form endpoint left blank** (`assets/js/form-config.js`).
- Re-run QA on 98 HTML files: 0 broken links/assets, 0 canonical mismatches (canonical = production URL on all non-404 pages), 1 H1 per page, 0 duplicate titles/descriptions, robots meta = register = sitemap for all 97 pages, no placeholder/LinkedIn/legacy-count strings.
