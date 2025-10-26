# 🌱 Toprak Nem Sensörü Web Uygulaması

Bu proje, **IoT + Web + Basit Makine Öğrenimi** kombinasyonu ile geliştirilmiş bir **Toprak Nem Takip Sistemi**dir. Hackathon sürecinde, toprak sensöründen veri alıp web üzerinden görüntüleme ve basit tahmin yapma amaçlı tasarlanmıştır.  

Sensör verisi toplanır, CSV dosyasında saklanır, Linear Regression ile basit bir tahmin yapılır ve tahmine dayalı sulama önerisi web arayüzünde gösterilir. Ayrıca gerçek zamanlı veri izleme için ayrı bir endpoint ve JavaScript tabanlı dashboard vardır.

---

## 🎯 Proje Amacı
- Tarımda toprak nemi takibi ve sulama önerisi sağlamak  
- Gerçek zamanlı nem verisini web arayüzü üzerinden izlemek  
- Basit makine öğrenimi ile tahmin yapmak ve öneri üretmek  
- Hackathon kapsamında IoT, Web ve Python entegrasyonunu göstermek  

---
🌐 API Endpointleri

/soil (POST) → Sensörden gelen nem verisini alır. JSON: { "moisture": 450 }

/moisture (GET) → Son ölçülen nem değerini JSON olarak döndürür

/ (GET) → Web arayüzü, tahmin ve öneri ile birlikte son nem değerini gösterir.

---

🧠 Kullanılan Teknolojiler

Python → Backend ve veri işleme

Flask → Web framework

Pandas & NumPy → CSV okuma ve veri işlemleri

Scikit-Learn → Linear Regression tahmini

HTML, CSS, JavaScript → Web arayüzü ve canlı veri güncelleme

---

🔧 Uygulama Mantığı

Sensör /soil endpoint’ine POST ile nem değerini gönderir

soil_data.csv dosyasında tüm nem değerleri saklanır

CSV verileri okunur, Linear Regression ile bir sonraki değer tahmini yapılır

Tahmine göre sulama önerisi üretilir:

< 300 → Toprak çok kuru, sulama yapın

300–700 → Nem ideal

700 → Toprak fazla nemli, sulamadan kaçının

HTML sayfası Flask tarafından render edilir, JS ile /moisture endpoint’i düzenli aralıklarla çekilir ve anlık değer güncellenir

