# -*- coding: utf-8 -*-
"""Structured content taken from FINAL CMS Version 11 (display order, labels, support copy)."""

BASE = "https://threeeight35.com/medical-travel-agency/"
SITE = "threeeight35° Medical Travel Agency"
EMAIL = "hello@threeeight35.com"
PHONE_AU = "+61 426 499 822"
PHONE_UAE = "+971 544 144 203"
ABN = "31 329 961 078"
SOCIAL = [
    ("Instagram", "https://www.instagram.com/threeeight35medical/"),
    ("Facebook", "https://www.facebook.com/profile.php?id=61595762571004"),
    ("TikTok", "https://www.tiktok.com/@threeeight35medical?_r=1&_t=ZS-9AiyD5T8TR6"),
    ("YouTube", "https://www.youtube.com/@threeeight35medical"),
]
BUILD_DATE = "2026-10-21"

# (CMS id, folder slug, display name, image stem, image alt, intro)
CATS = [
 ("CAT-01","aesthetic-plastic-surgery","Aesthetic & Plastic Surgery","01_aesthetic_plastic_surgery",
  "A woman seated in a clinic setting while a practitioner’s gloved hands hold a fine instrument near her face.",
  "Surgical procedures affecting the face, breasts and body. Use this section to identify the specific procedure relevant to your concern, rather than treating aesthetic surgery as a single service."),
 ("CAT-02","hair-transplantation","Hair Transplantation","03_hair_transplantation",
  "Blue-gloved hands parting dark hair on a man’s scalp to examine the hairline.",
  "Hair-restoration techniques and site-specific transplantation. This section helps you tell FUE, DHI, Sapphire FUE and hairline-design questions apart, without any claim that one technique is better than another."),
 ("CAT-03","dental","Dental Treatments","04_dental_care",
  "A smiling woman in a dental chair while a gloved hand holds a dental mirror near her mouth.",
  "Restorative, implant, aesthetic and periodontal dental care. These pages focus on diagnosis, treatment staging, materials where relevant and the number of visits or trips that may be required."),
 ("CAT-04","eye-care","Eye Care & Vision Correction","05_eye_care",
  "A woman resting her chin on a slit-lamp eye examination device while a clinician looks through the instrument.",
  "Ophthalmic and refractive care. Specific treatment pages are separated from broader guide pages; the retinal and corneal pages are currently under specialist review."),
 ("CAT-05","bariatric-surgery","Bariatric & Weight-Loss Surgery","06_bariatric_surgery",
  "A woman in a black sports top and leggings holding a tape measure around her waist in a bright room with a city view.",
  "Metabolic and bariatric procedures, including primary and revision surgery. These pages focus on long-term follow-up, nutrition and continuity of care."),
 ("CAT-07","ivf-fertility","IVF & Fertility Treatments","12_ivf_fertility",
  "A gloved hand holding a pipette over a clear laboratory dish beneath a microscope.",
  "Fertility assessment and treatment stages. These pages separate IVF, ICSI, embryo transfer and preservation pathways; topics that involve legal and ethical requirements remain under review."),
 ("CAT-06","health-check-up","Health Check-Up & Preventive Screening","14_health_checkup",
  "A smiling doctor in a white coat with a stethoscope speaking with a patient across a desk.",
  "Diagnostic and screening services. These pages focus on scope, results, limitations and Australian follow-up."),
 ("CAT-08","general-surgery","General Surgery","13_general_surgery",
  "A surgical team in blue scrubs and masks operating beneath theatre lights.",
  "Specific general-surgery procedures plus broader guide pages. Umbrella terms are not presented as one standard operation, and specialist-scope pages remain under review."),
]
GROUPS = {
 "CAT-01": [("Facial Surgery",["AES-01","AES-02","AES-03","AES-04","AES-05","AES-06"]),
            ("Breast Surgery",["AES-07","AES-08","AES-09","AES-10"]),
            ("Body Contouring",["AES-11","AES-12","AES-13","AES-14","AES-15","AES-16","AES-17"])],
 "CAT-02": [(None,["HAI-01","HAI-02","HAI-03","HAI-04","HAI-05","HAI-06"])],
 "CAT-03": [("Dental Implants & Full-Mouth Restoration",["DEN-01","DEN-02","DEN-03","DEN-04"]),
            ("Cosmetic Dentistry",["DEN-05","DEN-06","DEN-10","DEN-11"]),
            ("Restorative Dentistry",["DEN-09","DEN-07","DEN-08","DEN-13","DEN-12"]),
            ("General Dentistry",["DEN-14","DEN-15"])],
 "CAT-04": [("Vision Correction",["EYE-01","EYE-04","EYE-03"]),
            ("Eye Surgery & Specialised Procedures",["EYE-02","EYE-05","EYE-06"])],
 "CAT-05": [(None,["BAR-01","BAR-02","BAR-03"])],
 "CAT-07": [("Fertility Assessment & Treatment",["IVF-03","IVF-01","IVF-02","IVF-04","IVF-07"]),
            ("Fertility Preservation",["IVF-05","IVF-06"])],
 "CAT-06": [("General Health Check-Ups",["HEA-01","HEA-02","HEA-03","HEA-08"]),
            ("Specialised Health Screening",["HEA-04","HEA-05","HEA-06","HEA-07"])],
 "CAT-08": [("Common Surgical Procedures",["GEN-01","GEN-02","GEN-03","GEN-04"]),
            ("Digestive & Abdominal Surgery",["GEN-05","GEN-06","GEN-07","GEN-08"])],
}
LABELS = {
 "AES-05":"Blepharoplasty (Eyelid Surgery)", "HAI-03":"Sapphire FUE Hair Transplant",
 "DEN-02":"All-on-4 Dental Implants","DEN-03":"All-on-6 Dental Implants",
 "IVF-01":"IVF (In Vitro Fertilisation)","IVF-02":"ICSI (Intracytoplasmic Sperm Injection)",
 "HEA-01":"General Health Check-Up","HEA-02":"Comprehensive Health Check-Up",
 "HEA-03":"Executive Health Check-Up","HEA-08":"VIP Health Check-Up",
 "HEA-06":"Men’s Health Check-Up","HEA-07":"Women’s Health Check-Up",
}
DISCLOSURE = ("Treatment and travel costs are separate. Medical treatment is quoted by and paid directly to the independent clinic or hospital. "
              "Accommodation and private transport costs are arranged and itemised separately. Your complete proposal, including confirmed inclusions and exclusions, "
              "is provided in writing before you proceed.")
NOTICE = ("Important Medical Coordination Notice: threeeight35° Medical Travel Agency is a medical travel and journey coordination service. We do not provide medical advice, "
          "diagnosis, treatment or clinical recommendations. Clinical assessments, treatment suitability decisions, medical procedures and clinical oversight are provided independently "
          "by appropriately licensed healthcare professionals and healthcare providers in Türkiye.")
PACKAGES = [
 dict(key="essential", name="Essential Care", price="A$4,950", kind="Fixed Medical Travel Coordination Package",
      audience="Positioned for individuals", stay="4–7 night stay profile"),
 dict(key="executive", name="Executive Wellness & Recovery", price="A$9,900", kind="Fixed Medical Travel Coordination Package",
      audience="Positioned for couples and longer or more involved journeys", stay="7–14 night stay profile"),
 dict(key="vip", name="VIP Bespoke Health Journey", price="From A$14,900", kind="Medical Travel Coordination Package",
      audience="Positioned for families, complex care, several procedures or family journeys", stay="10+ night stay profile",
      note="Because the scope is bespoke, the final threeeight35° coordination package price is confirmed in writing after the scope of the journey is established, before you accept."),
]
