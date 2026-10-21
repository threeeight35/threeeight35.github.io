/* Enquiry form back-end configuration (public values only — NEVER put passwords, SMTP credentials or API secrets here).
   Set `endpoint` to the HTTPS URL given by your form-delivery service (for example Formspree, Web3Forms, Getform, Formspark,
   or your own server endpoint) that forwards submissions to hello@threeeight35.com.
   Until `endpoint` is set, the form validates but DOES NOT send, and shows an honest "not connected" message — never a fake success. */
window.T35_FORM = {
  endpoint: "https://threeeight35-form-backend.vercel.app/api/enquiry",              // e.g. "https://formspree.io/f/xxxxxxx"  — TECHNICAL CONFIGURATION REQUIRED
  method: "POST",
  turnstileSiteKey: "",      // optional: Cloudflare Turnstile PUBLIC site key (spam control). Leave empty if the service provides its own.
  fallbackEmail: "hello@threeeight35.com",
  fallbackPhoneAU: "+61 426 499 822"
};
