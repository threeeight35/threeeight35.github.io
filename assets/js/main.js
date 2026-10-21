/* threeeight35° — progressive enhancement only. The site is fully readable without JavaScript. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* mobile navigation */
  var burger = $(".burger"), mnav = $("#mobile-nav");
  if (burger && mnav) {
    burger.addEventListener("click", function () {
      var open = burger.getAttribute("aria-expanded") === "true";
      burger.setAttribute("aria-expanded", String(!open));
      burger.setAttribute("aria-label", open ? "Open menu" : "Close menu");
      mnav.hidden = open;
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !mnav.hidden) { burger.click(); burger.focus(); }
    });
  }
  /* desktop treatments menu */
  var dbtn = $(".nav-drop-btn"), menu = $("#nav-treat-menu");
  if (dbtn && menu) {
    var close = function () { menu.hidden = true; dbtn.setAttribute("aria-expanded", "false"); };
    dbtn.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = !menu.hidden; menu.hidden = open; dbtn.setAttribute("aria-expanded", String(!open));
    });
    document.addEventListener("click", function (e) { if (!menu.contains(e.target)) close(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !menu.hidden) { close(); dbtn.focus(); } });
  }

  /* treatment directory search */
  var input = $("[data-dir-search]");
  if (input) {
    var items = $$(".tlist li"), cats = $$(".dir-cat"), status = $("#tsearch-status"), reset = $("[data-dir-reset]");
    var run = function () {
      var q = input.value.trim().toLowerCase(), shown = 0;
      items.forEach(function (li) { var m = !q || li.getAttribute("data-search").indexOf(q) > -1; li.hidden = !m; if (m) shown++; });
      cats.forEach(function (c) { c.hidden = !$$(".tlist li:not([hidden])", c).length; });
      status.textContent = q ? ("Showing " + shown + " of " + items.length + " treatments") : "Showing all treatments";
      reset.hidden = !q;
    };
    input.addEventListener("input", run);
    reset.addEventListener("click", function () { input.value = ""; run(); input.focus(); });
  }

  /* enquiry form */
  var form = $("#enquiry-form");
  if (!form) return;
  var cfg = window.T35_FORM || {};
  var statusBox = $("#form-status"), submit = $("#f-submit");
  var cat = $("#f-cat"), proc = $("#f-proc");
  var procOpts = $$("option[data-cat]", proc);

  function filterProcs() {
    var c = cat.value;
    procOpts.forEach(function (o) { var show = !c || c === "Not sure yet" || o.getAttribute("data-cat") === c; o.hidden = !show; o.disabled = !show; });
    $$("optgroup", proc).forEach(function (g) { g.hidden = !$$("option:not([hidden])", g).length; });
    if (proc.selectedOptions[0] && proc.selectedOptions[0].disabled) proc.value = "";
  }
  cat.addEventListener("change", filterProcs); filterProcs();

  if (cfg.turnstileSiteKey) {
    var s = document.createElement("script"); s.src = "https://challenges.cloudflare.com/turnstile/v0/api.js"; s.async = true; s.defer = true;
    document.head.appendChild(s);
    var w = document.createElement("div"); w.className = "cf-turnstile"; w.setAttribute("data-sitekey", cfg.turnstileSiteKey);
    $("#captcha-slot").appendChild(w);
  }

  function setErr(id, msg) {
    var f = $("#" + id), e = $("#e-" + id);
    var field = f.closest(".field");
    if (msg) { e.textContent = msg; e.hidden = false; field.classList.add("invalid"); f.setAttribute("aria-invalid", "true"); f.setAttribute("aria-describedby", "e-" + id); }
    else { e.hidden = true; e.textContent = ""; field.classList.remove("invalid"); f.removeAttribute("aria-invalid"); f.removeAttribute("aria-describedby"); }
    return !msg;
  }
  function validate() {
    var ok = true, first = null;
    function chk(id, test, msg) { var v = test(); if (!setErr(id, v ? "" : msg)) { ok = false; if (!first) first = $("#" + id); } }
    var email = $("#f-email").value.trim();
    chk("f-name", function () { return $("#f-name").value.trim().length >= 2; }, "Please enter your full name.");
    chk("f-email", function () { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email); }, "Please enter a valid email address.");
    chk("f-country", function () { return $("#f-country").value.trim().length >= 2; }, "Please enter your country of residence.");
    chk("f-contact", function () { return !!$("#f-contact").value; }, "Please choose a preferred contact method.");
    chk("f-cat", function () { return !!cat.value; }, "Please choose a treatment category, or “Not sure yet”.");
    chk("f-consent", function () { return $("#f-consent").checked; }, "Please confirm the privacy acknowledgement to continue.");
    if (first) first.focus();
    return ok;
  }
  function show(kind, html) {
    statusBox.className = "form-status " + kind; statusBox.innerHTML = html; statusBox.hidden = false; statusBox.focus();
  }
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    statusBox.hidden = true;
    if (!validate()) return;
    if ($("#f-hp").value) return; /* honeypot */
    var mail = '<a href="mailto:' + cfg.fallbackEmail + '">' + cfg.fallbackEmail + '</a>';
    if (!cfg.endpoint) {
      show("bad", "<strong>Your enquiry has not been sent.</strong> Online enquiries are not connected yet. Please email " + mail + " or call " + cfg.fallbackPhoneAU + " (Australia desk). Please don’t include medical records or payment details.");
      return;
    }
    submit.disabled = true; submit.textContent = "Sending…";
    fetch(cfg.endpoint, { method: cfg.method || "POST", body: JSON.stringify(Object.fromEntries(new FormData(form).entries())), headers: { "Content-Type": "application/json", Accept: "application/json" } })
      .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r; })
      .then(function () { form.reset(); filterProcs(); show("ok", "<strong>Thank you — your enquiry has been received.</strong> A coordinator will respond using your preferred contact method."); })
      .catch(function () { show("bad", "<strong>Your enquiry could not be sent.</strong> Please try again, or email " + mail + " or call " + cfg.fallbackPhoneAU + "."); })
      .then(function () { submit.disabled = false; submit.textContent = "Send enquiry"; });
  });
})();
