# -*- coding: utf-8 -*-
# Turkish text for the treatment pages (served under /tr/treatments/...). Mirrors the English built from v11 records
# and treatment_guides.py: same rules (planning and coordination only, no clinical advice or timeframes).

# Topic phrase per treatment, used in the lead, "what to understand", category cards and search description.
FOCUS_TR = {
 **{sid: "bireysel değerlendirme ve planlama" for sid in ["AES-01","AES-02","AES-03","AES-04","AES-05","AES-06","AES-07","AES-08","AES-09","AES-10","AES-11","AES-12","AES-13","AES-14","AES-15","AES-16","AES-17"]},
 "HAI-01": "FUE tekniği, donör bölge planlaması ve FUE ile DHI karşılaştırması",
 "HAI-02": "DHI tekniğinin ne olduğu ve FUE'den farkı",
 "HAI-03": "Safir FUE'nin ne olduğu ve standart FUE ile ilişkisi",
 "HAI-04": "donör bölge planlaması, sakal tasarımı ve alıcı bölge",
 "HAI-05": "kaş tasarımı, kılların çıkış yönü ve donör bölge planlaması",
 "HAI-06": "saç çizgisi tasarımı ve yeniden yapılandırma planlaması",
 "DEN-01": "implant değerlendirmesi, tedavi aşamaları ve ziyaret sayısı",
 "DEN-02": "tam çene implant planlaması ve All-on-4 ile All-on-6 karşılaştırması",
 "DEN-03": "tam çene implant planlaması ve All-on-6 ile All-on-4 karşılaştırması",
 "DEN-04": "kapsamlı diş restorasyonunun aşamalı planlaması ve seyahat planı",
 "DEN-05": "porselen kaplama değerlendirmesi ve alternatifler",
 "DEN-06": "lamina değerlendirmesi ve porselen kaplamalarla karşılaştırması",
 "DEN-10": "bütüncül estetik diş planlaması",
 "DEN-11": "cerrahi olmayan beyazlatma seçenekleri, sınırları ve diş hekimi değerlendirmesi",
 "DEN-09": "kronlara genel bakış, malzemeler ve ne zaman tercih edildikleri",
 "DEN-07": "zirkonyum kron malzeme seçimi ve alternatifler",
 "DEN-08": "E-Max kron malzeme seçimi ve alternatifler",
 "DEN-13": "restoratif dolgu seçenekleri ve ek tedavinin ne zaman gerekebileceği",
 "DEN-12": "kanal tedavisi planlaması ve sonrasında restorasyon",
 "DEN-14": "diş eti değerlendirmesi ve tedavi yolları",
 "DEN-15": "diş çekimi planlaması ve gerektiğinde diş yerine koyma seçenekleri",
 "EYE-01": "LASIK değerlendirmesi ve lensle görme düzeltme seçenekleriyle karşılaştırması",
 "EYE-04": "refraktif cerrahi seçenekleri",
 "EYE-03": "lensle görme düzeltme ve LASIK ile karşılaştırması",
 "EYE-02": "katarakt değerlendirmesi, lens planlaması ve takip",
 "BAR-01": "tüp mide ameliyatı ve gastrik bypass ile karşılaştırması",
 "BAR-02": "gastrik bypass ve tüp mide ameliyatı ile karşılaştırması",
 "BAR-03": "önceki bir obezite ameliyatından sonra değerlendirme",
 "IVF-03": "tedavi öncesi doğurganlık değerlendirmesi ve gerekli kayıtlar",
 "IVF-01": "tüp bebek sürecinin tamamı ve Türkiye'ye seyahat koordinasyonu",
 "IVF-02": "mikroenjeksiyonun (ICSI) doğurganlık tedavisindeki yeri ve tüp bebekle karşılaştırması",
 "IVF-04": "embriyo transferi aşaması ve takip",
 "IVF-05": "yumurta dondurma süreci, saklama ve ileride kullanıma ilişkin konular",
 "IVF-06": "embriyo dondurma süreci, saklama ve ileride kullanıma ilişkin konular",
 "HEA-01": "genel sağlık taramasının kapsamı, sonuçlar ve dönüşünüzden sonraki takip",
 "HEA-02": "kapsamlı sağlık taramasının kapsamı",
 "HEA-03": "yönetici sağlık taramasının kapsamı",
 "HEA-08": "sağlık taraması etrafındaki ayrıcalıklı koordinasyon düzenlemeleri; bunlar klinik üstünlük ölçüsü değildir",
 "HEA-04": "kalp ve damar taramasının kapsamı, sonuçlar ve takip",
 "HEA-06": "erkeklere yönelik sağlık değerlendirmesi ve taramalarının kapsamı",
 "HEA-07": "kadınlara yönelik sağlık değerlendirmesi ve taramalarının kapsamı",
 "GEN-01": "fıtık onarımı ve cerrahi yönteme göre planlama",
 "GEN-02": "planlı safra kesesi ameliyatı ve cerrahi yönteme göre planlama",
 "GEN-06": "sindirim sistemi cerrahisi hizmetleri",
 "GEN-07": "karın cerrahisi ve karın germe ameliyatından farkı",
 "GEN-08": "tek bir ameliyat değil, bir cerrahi yöntem olarak laparoskopi",
}

# Endings of "what to understand", by the kind of treatment (matches the English endings).
UND_END_TR = {
 "surgical": "; önerilen işlemin amacı, mevcut alternatifler ve bireysel cerrahi değerlendirme gerektiren sorular.",
 "dental": "; tedavinin aşamalı bakım veya birden fazla ziyaret gerektirip gerektirmediği dahil. Tedavi sırası ve uygunluk diş hekimi değerlendirmesi gerektirir.",
 "eye": ". Herkese uyan tek bir göz işlemi yoktur; uygun seçenekleri göz muayenesi belirler.",
 "fertility": "; bu adımın doğurganlık tedavisi sürecindeki yeri. Uygunluk ve tedavi kararları klinik konulardır.",
 "checkup": "; hizmetin neleri kapsadığı, sonuçların nasıl bildirildiği ve olağan dışı sonuçları kimin takip ettiği.",
}

# "What to confirm before you travel" (four variants in the English).
CONFIRM_TR = {
 "surgical": "Tedaviyi yürütecek hekimi, önerilen işlemi, gerektiğinde anestezi ve sağlık kuruluşu düzenlemelerini, Türkiye'de beklenen kontrolleri, yanınızda götüreceğiniz kayıtları ve dönüşünüzden sonra ortaya çıkabilecek endişeler için planı teyit edin.",
 "dental": "Teşhisi veya tedavi hedefini, gereken kayıtları ya da röntgenleri, önerilen aşamaları, gerektiğinde kullanılacak malzemeleri, gerektiğinde geçici veya kalıcı protezleri, kontrol takvimini ve dönüşünüzden sonra ihtiyaç duyacağınız takibi teyit edin.",
 "eye": "Gereken muayeneleri, önerilen işlemi, alternatifleri, beklenen kontrol takvimini, dikkat edilmesi gereken belirtileri ve dönüşünüzden sonra göz takibinin nasıl süreceğini teyit edin.",
 "fertility": "Gereken kayıtları ve test sonuçlarını, değerlendirmelerin veya tedavi aşamalarının zamanlamasını, onam gerekliliklerini, gerektiğinde saklama veya laboratuvar düzenlemelerini ve dönüşünüzden sonra takibin nasıl süreceğini teyit edin.",
}

# Planning sections for the ten key treatments (Turkish versions of treatment_guides.GUIDES).
GUIDES_TR = {
 "DEN-01": [
  ("Diş implantı seyahatlerini planlamak",
   "Diş implantları çoğunlukla aşamalı olarak planlanır ve bazı planlar Türkiye'ye birden fazla seyahat gerektirebilir. Uçak bileti almadan önce sağlık kuruluşundan, planınızın kaç ziyaret "
   "gerektirdiğini, her ziyarette ne yapılacağını ve her seferinde İstanbul'da ne kadar kalmanız gerektiğini yazılı olarak açıklamasını isteyin. Koordinatörünüz de konaklamayı ve transferleri her ziyarete göre ayarlar."),
  ("İlk konsültasyonunuzdan önce hazırlamanız gerekenler", [
   "Varsa dişlerinizin yakın tarihli bir röntgeni veya tomografisi ve çekim tarihi.",
   "Kullandığınız ilaçların ve sağlık durumlarınızın listesi; web sitesi formu üzerinden değil, özel sağlık bilgisi süreci aracılığıyla sağlık kuruluşuna iletilir.",
   "Önceki implant, kron veya köprü gibi geçmiş diş tedavilerinizin kayıtları.",
   "Tercih ettiğiniz seyahat tarihleri ve size bir misafirin eşlik edip etmeyeceği."]),
  ("Sağlık kuruluşuna sorulacak sorular", [
   "Hangi implant sistemi ve protez malzemeleri öneriliyor ve neden?",
   "Fiyat teklifi geçici dişler, abutmentlar ve kalıcı kron ya da köprüler dahil tüm planı mı, yoksa yalnızca bir aşamayı mı kapsıyor?",
   "Bir aşamanın tekrarlanması veya düzeltilmesi gerekirse ne olur ve maliyeti nedir?",
   "Röntgenler ve implant ayrıntıları ülkenizdeki diş hekiminizle nasıl paylaşılacak?",
   "Döndükten sonra bir endişeniz olursa kiminle iletişime geçeceksiniz?"]),
  ("Döndükten sonra",
   "Diş implantları düzenli kontrol gerektirir. Seyahatten önce ülkenizdeki bir diş hekimine rutin takibi üstlenip üstlenmeyeceğini sorun ve sağlık kuruluşundan implant sisteminin ayrıntılarını ve "
   "diş hekiminizin ihtiyaç duyacağı kayıtları isteyin. Koordinatörünüz, İstanbul'dan ayrılmadan önce bu kayıtları toplamanıza yardımcı olabilir."),
 ],
 "HAI-01": [
  ("FUE saç ekimi seyahatini planlamak",
   "Birçok FUE planı işlem için tek bir ziyaret içerir; ancak bazı hastalara daha sonra ek bir seans önerilebilir. Konaklama sürenizi ve seyahatten önceki kontrolü tedaviyi yapan klinik belirler. "
   "Koordinatörünüzün konaklamanızı, transferlerinizi ve dönüş uçuşunuzu buna göre ayarlayabilmesi için planlanan takvimi yazılı olarak isteyin."),
  ("Hazırlamanız gerekenler", [
   "Saç çizginizin, tepe bölgenizin ve donör bölgenizin iyi ışıkta çekilmiş net fotoğrafları; klinik istediğinde özel sağlık bilgisi süreci aracılığıyla gönderilir.",
   "Saç dökülmesi için kullandığınız ilaçların ve önceki saç işlemlerinin ayrıntıları.",
   "İşlemden sonraki yolculuk için önden düğmeli, rahat giysiler ve klinik önerirse yumuşak bir şapka.",
   "Tercih ettiğiniz tarihler ve size bir misafirin eşlik edip etmeyeceği."]),
  ("Kliniğe sorulacak sorular", [
   "İşlemin her bölümünü kim yapacak: cerrah mı, yoksa onun gözetimindeki bir teknisyen ekibi mi?",
   "Kaç greft planlanıyor ve bu sayı nasıl belirlendi?",
   "Fiyat greft başına mı, yoksa tüm seans için mi; ilaçları, bakım ürünlerini ve kontrol ziyaretlerini kapsıyor mu?",
   "Klinik, işlemden sonraki günlerde yolculuk, uyku ve işe dönüş konusunda ne öneriyor?",
   "Klinik, döndükten sonra sizi nasıl takip edecek ve bir endişeniz olursa kiminle iletişime geçeceksiniz?"]),
  ("Döndükten sonra",
   "Saç ekiminden sonraki takip genellikle uzaktan yapılır. Kliniğe sonucun nasıl gelişmesini beklediklerini ve ilerlemenizi nasıl ve ne zaman takip edeceklerini sorun (örneğin belirlenen aralıklarla fotoğraflarla) "
   "ve kullanılan teknik ile greft sayısını içeren işlem kaydının bir kopyasını saklayın."),
 ],
 "AES-01": [
  ("Burun estetiği seyahatini planlamak",
   "Burun estetiği seyahati genellikle ameliyattan önce İstanbul'da bir konsültasyon, ardından işlemin kendisi ve dönüşünüzden önce en az bir kontrol ziyareti içerir. Seyahat edeceğiniz zaman dahil "
   "her adımın zamanlamasını tedaviyi yürüten cerrah belirler. Planlanan takvimi yazılı olarak isteyin ve cerrah onaylamadan değiştirilemeyen bir dönüş bileti almayın. Koordinatörünüz konaklamayı ve transferleri plana göre ayarlar."),
  ("Hazırlamanız gerekenler", [
   "Burnunuzun önden, iki yandan ve dörtte üç açıdan net fotoğrafları; cerrah istediğinde özel sağlık bilgisi süreci aracılığıyla gönderilir.",
   "Önceki burun ameliyatları, yaralanmalar veya nefes alma sorunlarının ayrıntıları.",
   "Cerrah için kullandığınız ilaçların ve takviyelerin listesi.",
   "Mümkünse size eşlik edecek bir misafir. Her paket en az bir misafirin konaklamasını içerir."]),
  ("Cerraha sorulacak sorular", [
   "İşlem estetik amaçlı mı, işlevsel amaçlı mı (nefes almayı iyileştirmek için), yoksa her ikisi mi planlanıyor?",
   "Hangi cerrahi yöntem öneriliyor ve neden?",
   "Seyahatten önce hangi kontroller gerekiyor ve fiyat teklifi hastanede kalışı, anesteziyi, atelin çıkarılmasını ve ilaçları kapsıyor mu?",
   "Ameliyattan sonra burna oturan gözlük takmak, uçakla seyahat veya spor gibi nelerden ve ne kadar süre kaçınmalısınız?",
   "Cerrah, döndükten sonra sizi nasıl takip edecek?"]),
  ("Döndükten sonra",
   "Cerrah, sonuç oturdukça ilerleyen aşamalarda fotoğraf görmek isteyebilir. Uzaktan takibin nasıl yapılacağı konusunda önceden anlaşın ve doktorunuza verebileceğiniz yazılı bir işlem özeti isteyin."),
 ],
 "BAR-01": [
  ("Tüp mide ameliyatı seyahatini planlamak",
   "Tüp mide süreci ameliyat öncesi değerlendirme ve tetkikleri, ardından ameliyatı, hastanede kalışı ve seyahat etmenize izin verilmeden önceki kontrolleri içerir. Her adımı tedaviyi yürüten ekip belirler. "
   "Takip ameliyattan çok sonra da sürdüğü için, rezervasyon yapmadan önce seyahatinizi ve ülkenizdeki bakımınızı birlikte planlayın."),
  ("Hazırlamanız gerekenler", [
   "Kilo geçmişiniz ve daha önceki kilo verme tedavilerinin ayrıntıları.",
   "Sağlık durumlarınızın ve kullandığınız ilaçların listesi; özel sağlık bilgisi süreci aracılığıyla gönderilir.",
   "Doktorunuzda bulunan yakın tarihli kan tahlilleri veya raporlar.",
   "Size eşlik edecek bir misafir. Executive Sağlık ve İyileşme ile VIP paketleri birden fazla misafirin konaklamasını içerir."]),
  ("Cerrahi ekibe sorulacak sorular", [
   "Hangi tetkikler Türkiye'de yapılacak, hangileri seyahatten önce yapılmalı?",
   "Fiyat teklifi tetkikler, ameliyat, hastanede kalış, ilaçlar ve beslenme desteği dahil tüm süreci kapsıyor mu?",
   "Ekip hastanede ve İstanbul'da kaç gece kalmanızı bekliyor ve seyahat tarihinize kim karar veriyor?",
   "Hangi beslenme ve takviye planını ne kadar süre uygulayacaksınız?",
   "Ekip döndükten sonra nasıl bir takip sunuyor ve bu, ülkenizdeki doktorunuzla nasıl uyumlu hale getiriliyor?"]),
  ("Döndükten sonra",
   "Uzun süreli takip ile beslenme ve takviye izlemi obezite cerrahisi bakımının bir parçasıdır. Seyahatten önce doktorunuzla ülkenizde takibinizi kimin üstleneceğini konuşun "
   "ve cerrahi ekipten doktorunuzun kullanabileceği yazılı bir taburcu özeti isteyin."),
 ],
 "DEN-02": [
  ("All-on-4 seyahatlerini planlamak",
   "All-on-4 tedavisi genellikle çekimler, implantların yerleştirilmesi ve sabit geçici bir köprü için ilk bir ziyareti, ardından diş hekimi iyileşmeden emin olduktan sonra kalıcı köprünün takılması için ikinci bir ziyareti içerir. "
   "İki seyahat arasındaki süreyi tedaviyi yürüten diş hekimi belirler. İki seyahat için bütçe yapabilmeniz ve koordinatörünüzün her birini ayarlayabilmesi için iki ziyaretin de yazılı planınızda açıklanmasını isteyin."),
  ("Konsültasyonunuzdan önce", [
   "Diş hekiminizde varsa panoramik röntgen veya 3B tomografi; böylece sağlık kuruluşu kemik hacmini erkenden değerlendirebilir.",
   "Her çenede sallanan, ağrıyan veya eksik dişlerin bir notu.",
   "Diş cerrahisini etkileyen sağlık durumları, sigara kullanımı ve ilaçların ayrıntıları; web sitesi formu üzerinden değil, özel sağlık bilgisi kanalı aracılığıyla gönderilir.",
   "Tek çene mi yoksa iki çene mi planladığınız; çünkü bu, her ziyaretin süresini değiştirir."]),
  ("Diş hekiminizle netleştirmeniz gerekenler", [
   "Geçici köprü aynı ziyarette mi takılacak ve onu kullanırken neler yiyebilirsiniz?",
   "Kalıcı köprü hangi malzemeden yapılacak (örneğin akrilik, kompozit veya zirkonyum) ve bu fiyatı nasıl etkiler?",
   "Fiyat teklifi her çeneyi ayrı ayrı gösteriyor mu; çekimleri, gerekirse kemik greftini, anesteziyi ve iki köprüyü kapsıyor mu?",
   "Bir implant kemikle kaynaşmazsa ne olur ve değiştirme maliyetini kim üstlenir?",
   "Ülkenizdeki bir diş hekiminin köprüyü ileride bakımını veya onarımını yapabilmesi için hangi parçalar ve implant markası kullanılıyor?"]),
  ("Ziyaretler arasında ve sonrasında ülkenizdeki bakım",
   "Tam çene köprüsü yıllar boyunca profesyonel temizlik ve kontrol gerektirir. Seyahatten önce ülkenizdeki bir diş hekiminin yurt dışında takılmış bir All-on-4 köprüsünün bakımını üstlenip üstlenmeyeceğini kontrol edin "
   "ve ona vermek üzere sağlık kuruluşundan implant markasını, parça listesini ve röntgenleri isteyin."),
 ],
 "DEN-05": [
  ("Porselen kaplama seyahatini planlamak",
   "Kaplamalar genellikle tek bir seyahatte tamamlanır: dişler hazırlanır, diş laboratuvarı kalıcı kaplamaları üretirken geçici kaplamalar takılır ve kalıcı kaplamalar aynı konaklama sırasında ikinci bir randevuda yapıştırılır. "
   "İstanbul'da ihtiyaç duyacağınız iş günü sayısı kliniğe ve laboratuvarına bağlıdır; bu nedenle uçuşlarınızı ayırtmadan önce bunu teyit edin."),
  ("Konsültasyonunuzdan önce", [
   "Gülüşünüzün önden ve yanlardan fotoğrafları ile varsa yakın tarihli diş röntgenleri.",
   "Tedavi ettirmek istediğiniz dişlerin listesi ve bunlar arasındaki kronlar, dolgular veya kanal tedavili dişler.",
   "Beğendiğiniz renk ve şeklin görselleri; birebir kopyalamak için değil, diş hekiminizle konuşmak için.",
   "Diş gıcırdatma veya sıkma geçmişiniz varsa, diş hekiminiz bunu bilmek isteyecektir."]),
  ("Diş hekiminizle netleştirmeniz gerekenler", [
   "Diş yüzeyinden ne kadar aşındırılacak ve bu geri alınabilir mi?",
   "Kaplamalar porselen mi kompozit mi ve hangi laboratuvar üretiyor?",
   "Kalıcı kaplamalar yapıştırılmadan önce deneme gülüşü veya geçici kaplamaları görüp onaylayacak mısınız?",
   "Döndükten sonra bir kaplama çatlar ya da düşerse garanti neleri kapsar?",
   "Gece plağına ihtiyacınız var mı ve fiyata dahil mi?"]),
  ("Kaplamalarınızın ülkenizdeki bakımı",
   "Kaplamalar, diş hekiminizdeki düzenli kontrollerle daha uzun ömürlü olur. Birinin değiştirilmesi gerekirse ülkenizdeki bir diş hekiminin eşleştirme veya onarım yapabilmesi için klinikten renk, malzeme ve tedavi edilen dişlerin kaydını isteyin."),
 ],
 "HAI-02": [
  ("DHI saç ekimi seyahatini planlamak",
   "DHI, önce kanal açmak yerine greftleri kalem benzeri bir aletle yerleştirir ve greft başına FUE'den daha uzun sürebilir. Kliniğe, planlanan greft sayısının kaç gün gerektirdiğini, "
   "işlemin bir günde mi yoksa iki günde mi yapılacağını ve ayrılmadan önceki kontrolün ne zaman olacağını sorun. Koordinatörünüz konaklamanızı ve transferlerinizi bu takvime göre ayarlar."),
  ("Seyahatten önce", [
   "Gün ışığında çekilmiş saç çizginizin, şakaklarınızın, tepe bölgenizin ve ense bölgenizin fotoğrafları.",
   "Ne zamandır saç döküldüğü ve şu anda hangi tedaviyi kullandığınız.",
   "Beğendiğiniz saç çizgisi biçimlerinin kısa bir listesi; klinikle gerçekçi biçimde konuşmak için.",
   "Başınızdan geçirilmeden giyilebilen rahat giysiler ve klinik önerirse dışarıda saçlı derinizi örtmek için bir plan."]),
  ("Kliniğinizle netleştirmeniz gerekenler", [
   "Saç tipiniz ve kapatılacak alan için neden FUE yerine DHI?",
   "Saç çizgisini kim tasarlıyor ve greftleri kim yerleştiriyor?",
   "Planlanan greft sayısı nedir ve fiyat sabit mi, greft başına mı?",
   "Klinik alıcı bölgeyi tıraş ediyor mu ve tercih etmezseniz seçenekler neler?",
   "Klinik, döndükten sonra ilerlemenizi nasıl ve ne kadar süre takip edecek?"]),
  ("Ülkenizden takip",
   "Klinik genellikle ilerlemenizi fotoğraflarla takip eder. Ayrılmadan önce fotoğraf takvimi üzerinde anlaşın, greft sayısını içeren işlem özetini saklayın ve saç dökülmesi için yeni bir ilaca başlamadan önce ülkenizdeki doktorunuza danışın."),
 ],
 "BAR-02": [
  ("Gastrik bypass seyahatini planlamak",
   "Gastrik bypass besinlerin emilim şeklini değiştirir; bu nedenle planlama ameliyatın ötesine geçer. Süreç genellikle ameliyat öncesi tetkikleri, ardından ameliyatı, hastanede birkaç günü "
   "ve cerrahi ekip seyahat etmenize izin vermeden önceki kontrolleri içerir. Seyahat tarihlerini kesinleştirmeden önce kan tahlilleri ve diyetisyen desteği dahil ülkenizdeki takibinizi ayarlayın."),
  ("Seyahatten önce", [
   "Doktorunuzdan diyabet, kolesterol veya vitamin düzeyleriyle ilgili sonuçlar dahil yakın tarihli kan tahlilleri.",
   "Reflü, önceki karın ameliyatları veya önceki kilo verme işlemlerinin ayrıntıları.",
   "Kullandığınız ilaçlar; bazılarının bypass sonrasında değiştirilmesi gerekebilir.",
   "Taburcu olduktan sonra otelde size eşlik edip yardımcı olacak biri. Her paket en az bir misafirin konaklamasını içerir."]),
  ("Cerrahi ekiple netleştirmeniz gerekenler", [
   "Sizin durumunuzda neden tüp mide veya başka bir seçenek yerine gastrik bypass?",
   "Uzun vadede hangi vitamin ve mineralleri almanız gerekecek ve ekip yazılı bir plan veriyor mu?",
   "Hastanede ne kadar kalacaksınız ve taburcu olmadan önce kaçak testi veya başka bir kontrol yapılıyor mu?",
   "Fiyat teklifi cerrahı, anesteziyi, hastanede kalışı, tetkikleri ve ilaçları kapsıyor mu?",
   "Döndükten sonra kan sonuçlarınızı ve beslenmenizi kim değerlendirecek ve ekiple nasıl iletişime geçeceksiniz?"]),
  ("Ülkenizde uzun süreli bakım",
   "Gastrik bypass sonrası yaşam düzenli kan tahlillerini ve ömür boyu takviyeleri içerir. Ülkenizdeki bir doktorun ameliyatınızdan haberdar olduğundan emin olun, ona taburcu özetini verin ve seyahat ederken takviye planınızın bir kopyasını yanınızda bulundurun."),
 ],
 "IVF-01": [
  ("Türkiye'ye tüp bebek seyahatini planlamak",
   "Bir tüp bebek döngüsü birkaç aşamadan geçer: tetkikler, yumurtalık uyarımı, yumurta toplama, laboratuvarda döllenme ve embriyo transferi. Yumurta toplamadan önceki bazı takipler zaman zaman ülkenizde yapılabilir; "
   "bu da İstanbul'da kalma süresini kısaltır. Kliniğe hangi aşamaların Türkiye'de yapılması gerektiğini, bunun kaç gün anlamına geldiğini ve tarihlerin ne kadar esnek olduğunu sorun; çünkü döngünün zamanlaması her zaman önceden belirlenemez."),
  ("Seyahatten önce", [
   "Her iki eşin yakın tarihli doğurganlık tetkik sonuçları; örneğin hormon düzeyleri, ultrason raporları ve semen analizi.",
   "Kullanılan ilaçlar ve döngü sayısı dahil, daha önceki doğurganlık tedavilerinin özeti.",
   "Klinik isterse evlilik cüzdanı ve kimlik belgeleri.",
   "Başlangıç tarihleri döngünüze göre değişebileceğinden esnek seyahat düzenlemeleri."]),
  ("Kliniğinizle netleştirmeniz gerekenler", [
   "Planladığınız tedavi Türk mevzuatına göre sizin için uygun mu? Türkiye'de doğurganlık tedavisine kimlerin erişebileceği ve donör yumurta, sperm veya embriyo kullanımı konusunda belirli kurallar vardır; bu nedenle kliniğin bunu yazılı olarak teyit etmesini isteyin.",
   "Hangi tetkikler ve takip ultrasonları ülkenizde yapılabilir, hangileri İstanbul'da yapılmalı?",
   "Fiyat uyarım ilaçlarını, yumurta toplamayı, laboratuvar çalışmasını, embriyo transferini ve dondurmayı kapsıyor mu?",
   "Döngü iptal edilirse veya transfer için uygun embriyo olmazsa ne olur ve ücretler nelerdir?",
   "Sonuçlar nasıl bildirilir ve döndükten sonra transfer sonrasında size kim destek olur?"]),
  ("Döndükten sonra",
   "Gebelik testi ve erken dönem bakım genellikle döndükten sonra yapılır. Seyahatten önce ülkenizdeki doktorunuzu tedavi planınızdan haberdar edin ve klinikten, saklanan embriyolar ve saklama ücretlerinin nasıl hesaplandığı dahil döngünün yazılı bir özetini isteyin."),
 ],
 "AES-07": [
  ("Göğüs büyütme seyahatini planlamak",
   "Göğüs büyütme genellikle bir konsültasyon ve boyut belirleme randevusu, ardından ameliyat ve seyahatten önce ameliyat sonrası bir kontrolü içeren tek bir seyahat olarak planlanır. Seyahat etmenin ne zaman uygun olduğuna cerrah karar verir. "
   "Cerrah önerirse konaklamanızı uzatabilmeniz için planlarınızda esneklik bırakın."),
  ("Seyahatten önce", [
   "Mevcut sütyen bedeniniz ve hayalinizdeki sonuç; cerrahla konuşmak için örnek görsellerle birlikte.",
   "Mamografi veya ultrason gibi yakın tarihli meme görüntülemeleri ve ailede meme hastalığı öyküsü.",
   "Gebelik, emzirme planları ve önceki meme işlemlerinin ayrıntıları.",
   "Önden kapanan destekleyici sütyenler veya kliniğe cerrahi sütyen sağlayıp sağlamadığını sorun."]),
  ("Cerrahınızla netleştirmeniz gerekenler", [
   "Hangi implant tipi, şekli ve üreticisi öneriliyor ve seri numaralarını içeren implant kartını alacak mısınız?",
   "Kesi nerede olacak ve implant kasın üstüne mi altına mı yerleştirilecek?",
   "Fiyat implantları, anesteziyi, hastanede kalışı, cerrahi sütyeni ve kontrol ziyaretlerini kapsıyor mu?",
   "Cerrahın revizyon politikası neleri ve ne kadar süre kapsıyor?",
   "Cerrah döndükten sonra sizi nasıl takip edecek ve sonraki yıllarda hangi kontroller öneriliyor?"]),
  ("Döndükten sonra",
   "İmplant kartınızı ve ameliyat notlarınızı güvenli bir yerde saklayın; ileride sizi tedavi edecek her doktorun bunlara ihtiyacı olacaktır. Ülkenizdeki doktorunuza implantlarla meme kontrollerinin nasıl yapıldığını sorun ve bir değişiklik fark ederseniz muayene ayarlayın."),
 ],
}

GUIDE_META_TR = {
 "DEN-01": "Türkiye'de diş implantı: seyahat sayısı, hazırlık, implant sistemleri ve fiyat teklifleriyle ilgili sorular, ülkenizdeki kontrollerin planlanması.",
 "HAI-01": "Türkiye'de FUE saç ekimi: konaklama planı, gereken fotoğraflar, greftler ve işlemi kimin yaptığıyla ilgili sorular, uzaktan takip.",
 "AES-01": "Türkiye'de burun estetiği: konsültasyon ve kontrol planlaması, hazırlık, cerraha sorulacak sorular ve dönüş sonrası takip.",
 "BAR-01": "Türkiye'de tüp mide ameliyatı: tetkik, ameliyat ve hastanede kalış planlaması, cerrahi ekibe sorular ve uzun süreli takip.",
 "DEN-02": "Türkiye'de All-on-4: iki seyahatin planlanması, gereken görüntüler, köprü malzemesi ve implantlarla ilgili sorular, ülkenizdeki bakım.",
 "DEN-05": "Türkiye'de porselen kaplama: tek seyahat takvimi, gereken fotoğraflar, diş hazırlığı, deneme gülüşü ve onarımla ilgili sorular.",
 "HAI-02": "Türkiye'de DHI saç ekimi: konaklama süresi, gereken fotoğraflar, FUE ile karşılaştırma, greft sayısı ve ülkenizden takip.",
 "BAR-02": "Türkiye'de gastrik bypass: tetkik, ameliyat ve konaklama planı, ömür boyu takviyeler, ekibe sorular ve dönüş sonrası bakım.",
 "IVF-01": "Türkiye'de tüp bebek: İstanbul'da yapılan aşamalar, tarih esnekliği, kayıtlar, yasal uygunluk ve fiyata dahil olanlar.",
 "AES-07": "Türkiye'de göğüs büyütme: seyahat planı, hazırlık, implantlar, yerleşim ve revizyon politikasıyla ilgili sorular, ülkenizdeki kontroller.",
}
