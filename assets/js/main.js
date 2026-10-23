/* threeeight35° — progressive enhancement only. The site is fully readable without JavaScript. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  /* messages follow the page language (Arabic pages live under /ar/ with <html lang="ar">, Turkish under /tr/ with <html lang="tr">) */
  var LANG = document.documentElement.lang, AR = LANG === "ar", TR = LANG === "tr";
  var t = function (en, ar, tr) { return AR ? ar : TR ? tr : en; };

  /* mobile navigation */
  var burger = $(".burger"), mnav = $("#mobile-nav");
  if (burger && mnav) {
    burger.addEventListener("click", function () {
      var open = burger.getAttribute("aria-expanded") === "true";
      burger.setAttribute("aria-expanded", String(!open));
      burger.setAttribute("aria-label", open ? t("Open menu", "فتح القائمة", "Menüyü aç") : t("Close menu", "إغلاق القائمة", "Menüyü kapat"));
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

  /* floating WhatsApp menu: close when tapping elsewhere or pressing Escape */
  var wa = $(".wa-float");
  if (wa) {
    document.addEventListener("click", function (e) { if (wa.open && !wa.contains(e.target)) wa.open = false; });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && wa.open) { wa.open = false; $(".wa-btn", wa).focus(); } });
  }
  /* language menus: close when tapping elsewhere or pressing Escape */
  $$(".lang-menu").forEach(function (m) {
    document.addEventListener("click", function (e) { if (m.open && !m.contains(e.target)) m.open = false; });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && m.open) { m.open = false; $(".lang-btn", m).focus(); } });
  });

  /* treatment directory search */
  var input = $("[data-dir-search]");
  if (input) {
    var items = $$(".tlist li"), cats = $$(".dir-cat"), status = $("#tsearch-status"), reset = $("[data-dir-reset]");
    var run = function () {
      var q = input.value.trim().toLowerCase(), shown = 0;
      items.forEach(function (li) { var m = !q || li.getAttribute("data-search").indexOf(q) > -1; li.hidden = !m; if (m) shown++; });
      cats.forEach(function (c) { c.hidden = !$$(".tlist li:not([hidden])", c).length; });
      status.textContent = q ? t("Showing " + shown + " of " + items.length + " treatments", "عرض " + shown + " من أصل " + items.length + " علاجاً", items.length + " tedaviden " + shown + " tanesi gösteriliyor") : t("Showing all treatments", "عرض جميع العلاجات", "Tüm tedaviler gösteriliyor");
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

  /* phone number: shown and required only for WhatsApp, SMS or phone-call contact */
  var contact = $("#f-contact"), phone = $("#f-phone"), phoneField = $("#phone-field");
  var phoneLabels = { "WhatsApp": t("WhatsApp number *", "رقم واتساب *", "WhatsApp numarası *"), "SMS": t("Mobile number for SMS *", "رقم الجوال للرسائل النصية *", "SMS için cep telefonu numarası *"), "Phone call": t("Phone number *", "رقم الهاتف *", "Telefon numarası *") };
  function togglePhone() {
    var label = phoneLabels[contact.value];
    phoneField.hidden = !label; phone.disabled = !label; phone.required = !!label;
    if (label) $("label", phoneField).textContent = label;
    else setErr("f-phone", "");
  }
  contact.addEventListener("change", togglePhone); togglePhone();

  if (cfg.turnstileSiteKey) {
    var s = document.createElement("script"); s.src = "https://challenges.cloudflare.com/turnstile/v0/api.js"; s.async = true; s.defer = true;
    document.head.appendChild(s);
    var w = document.createElement("div"); w.className = "cf-turnstile"; w.setAttribute("data-sitekey", cfg.turnstileSiteKey);
    $("#captcha-slot").appendChild(w);
  }

  function setErr(id, msg) {
    var f = $("#" + id), e = $("#e-" + id);
    var field = f.closest(".field"), help = f.getAttribute("data-describedby");
    if (msg) { e.textContent = msg; e.hidden = false; field.classList.add("invalid"); f.setAttribute("aria-invalid", "true"); f.setAttribute("aria-describedby", (help ? help + " " : "") + "e-" + id); }
    else { e.hidden = true; e.textContent = ""; field.classList.remove("invalid"); f.removeAttribute("aria-invalid"); if (help) f.setAttribute("aria-describedby", help); else f.removeAttribute("aria-describedby"); }
    return !msg;
  }
  function validate() {
    var ok = true, first = null;
    function chk(id, test, msg) { var v = test(); if (!setErr(id, v ? "" : msg)) { ok = false; if (!first) first = $("#" + id); } }
    var email = $("#f-email").value.trim();
    chk("f-name", function () { return $("#f-name").value.trim().length >= 2; }, t("Please enter your full name.", "يُرجى إدخال اسمك الكامل.", "Lütfen adınızı ve soyadınızı girin."));
    chk("f-email", function () { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email); }, t("Please enter a valid email address.", "يُرجى إدخال بريد إلكتروني صالح.", "Lütfen geçerli bir e-posta adresi girin."));
    chk("f-country", function () { return $("#f-country").value.trim().length >= 2; }, t("Please enter your country of residence.", "يُرجى إدخال بلد إقامتك.", "Lütfen yaşadığınız ülkeyi girin."));
    chk("f-contact", function () { return !!$("#f-contact").value; }, t("Please choose a preferred contact method.", "يُرجى اختيار وسيلة التواصل المفضّلة.", "Lütfen tercih ettiğiniz iletişim yöntemini seçin."));
    if (!phone.disabled) chk("f-phone", function () { var v = phone.value.trim(), d = v.replace(/\D/g, ""); return /^\+?[\d\s().-]+$/.test(v) && d.length >= 8 && d.length <= 15; }, t("Please enter a phone number we can reach you on, including your country code.", "يُرجى إدخال رقم هاتف يمكننا التواصل معك عليه، مع رمز الدولة.", "Lütfen size ulaşabileceğimiz bir telefon numarasını ülke koduyla birlikte girin."));
    chk("f-cat", function () { return !!cat.value; }, t("Please choose a treatment category, or “Not sure yet”.", "يُرجى اختيار فئة العلاج، أو «لم أحدّد بعد».", "Lütfen bir tedavi kategorisi veya “Henüz karar vermedim” seçeneğini seçin."));
    chk("f-consent", function () { return $("#f-consent").checked; }, t("Please confirm the privacy acknowledgement to continue.", "يُرجى تأكيد الإقرار بالخصوصية للمتابعة.", "Devam etmek için lütfen gizlilik onayını işaretleyin."));
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
    var tel = AR ? '<span dir="ltr">' + (cfg.fallbackPhoneUAE || cfg.fallbackPhoneAU) + '</span>' : cfg.fallbackPhoneAU;
    if (!cfg.endpoint) {
      show("bad", t("<strong>Your enquiry has not been sent.</strong> Online enquiries are not connected yet. Please email " + mail + " or call " + tel + " (Australia desk). Please don’t include medical records or payment details.",
                    "<strong>لم يُرسَل استفسارك.</strong> الاستفسارات عبر الإنترنت غير متاحة حالياً. يُرجى مراسلتنا على " + mail + " أو الاتصال على " + tel + " (مكتب الإمارات). يُرجى عدم إرسال سجلات طبية أو بيانات دفع.", "<strong>Talebiniz gönderilmedi.</strong> Çevrim içi talepler henüz bağlı değil. Lütfen " + mail + " adresine e-posta gönderin veya " + tel + " numarasını arayın (Avustralya ve Uluslararası hattı). Lütfen tıbbi kayıt veya ödeme bilgisi eklemeyin."));
      return;
    }
    submit.disabled = true; submit.textContent = t("Sending…", "جارٍ الإرسال…", "Gönderiliyor…");
    fetch(cfg.endpoint, { method: cfg.method || "POST", body: JSON.stringify(Object.fromEntries(new FormData(form).entries())), headers: { "Content-Type": "application/json", Accept: "application/json" } })
      .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r; })
      .then(function () { form.reset(); filterProcs(); togglePhone(); show("ok", t("<strong>Thank you — your enquiry has been received.</strong> A coordinator will respond using your preferred contact method.", "<strong>شكراً لك، لقد استلمنا استفسارك.</strong> سيتواصل معك أحد المنسّقين عبر وسيلة التواصل التي اخترتها.", "<strong>Teşekkürler, talebiniz bize ulaştı.</strong> Bir koordinatör, tercih ettiğiniz iletişim yöntemiyle size dönüş yapacaktır.")); })
      .catch(function () { show("bad", t("<strong>Your enquiry could not be sent.</strong> Please try again, or email " + mail + " or call " + tel + ".", "<strong>تعذّر إرسال استفسارك.</strong> يُرجى المحاولة مرة أخرى، أو مراسلتنا على " + mail + " أو الاتصال على " + tel + ".", "<strong>Talebiniz gönderilemedi.</strong> Lütfen tekrar deneyin ya da " + mail + " adresine e-posta gönderin veya " + tel + " numarasını arayın.")); })
      .then(function () { submit.disabled = false; submit.textContent = t("Send enquiry", "إرسال الاستفسار", "Talebi gönder"); });
  });
})();
