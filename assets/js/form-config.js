/* Enquiry form back-end configuration (public values only — NEVER put passwords, SMTP credentials or API secrets here).
   `endpoint` is the HTTPS URL of the form back-end that forwards submissions to hello@threeeight35.com.
   If `endpoint` is ever emptied, the form validates but DOES NOT send, and shows an honest "not connected" message — never a fake success. */
window.T35_FORM = {
  endpoint: "https://threeeight35-form-backend.vercel.app/api/enquiry",              // form back-end (Vercel); must allow the https://threeeight35.com origin (CORS)
  method: "POST",
  turnstileSiteKey: "",      // optional: Cloudflare Turnstile PUBLIC site key (spam control). Leave empty if the service provides its own.
  fallbackEmail: "hello@threeeight35.com",
  fallbackPhoneAU: "+61 426 499 822",
  fallbackPhoneUAE: "+971 544 144 203"   // shown on the Arabic pages
};
