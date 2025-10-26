# 🌱 Toprak Nem Sensörü Web Uygulaması  

Bu proje, **Halkbank & Habitat Derneği Hackathonu** kapsamında geliştirilen bir **IoT + Web + Basit Makine Öğrenimi tabanlı Toprak Nem Takip Sistemi**dir.  
Amaç; sensör verilerini toplayarak web arayüzü üzerinden gerçek zamanlı izleme ve basit bir tahmine dayalı sulama önerisi sunmaktır.  

---

## 🎯 Proje Amacı  
- Tarımda **toprak nemi takibini** kolaylaştırmak  
- **Gerçek zamanlı sensör verilerini** web üzerinden görüntülemek  
- **Makine öğrenimi (Linear Regression)** ile basit sulama önerileri üretmek  
- IoT, Web ve Python teknolojilerinin **entegrasyonunu** göstermek  

---

## ⚙️ Uygulama Mantığı  
1. Sensör `/soil` endpoint’ine POST yöntemiyle nem verisi gönderir.  
   Örnek JSON:  
   ```json
   { "moisture": 450 }
   ```
2. Veriler `soil_data.csv` dosyasında saklanır.  
3. CSV dosyasındaki veriler **Pandas & Scikit-Learn** kullanılarak işlenir.  
4. **Linear Regression** modeliyle bir sonraki nem değeri tahmin edilir.  
5. Tahmine göre sistem şu önerileri üretir:  
   - `< 300` → 🌵 Toprak çok kuru → **Sulama yapılmalı**  
   - `300–700` → 🌱 Nem ideal  
   - `> 700` → 💧 Toprak fazla nemli → **Sulamadan kaçının**  
6. Flask üzerinden HTML sayfası render edilir.  
   - `/` → Ana sayfa (tahmin + öneri)  
   - `/moisture` → Son nem değeri (JSON)  
   - `/soil` → Sensör verisi alımı (POST)  
7. JavaScript, `/moisture` endpoint’inden düzenli aralıklarla veri çekerek sayfadaki değeri **canlı olarak günceller.**

---

## 🧠 Kullanılan Teknolojiler  
| Katman | Teknoloji |
|--------|------------|
| Backend | Python, Flask |
| Veri İşleme | Pandas, NumPy |
| Makine Öğrenimi | Scikit-Learn (Linear Regression) |
| Frontend | HTML, CSS, JavaScript |
| Veri Saklama | CSV (soil_data.csv) |

---

## 🌐 API Endpointleri  
| Endpoint | Yöntem | Açıklama |
|-----------|--------|----------|
| `/soil` | POST | Sensörden gelen nem verisini alır |
| `/moisture` | GET | Son ölçülen nem değerini döndürür |
| `/` | GET | Web arayüzünü ve tahmin sonuçlarını gösterir |

---

## 💡 Notlar  
- Linear Regression modeli yalnızca **gösterim amaçlıdır**.  
  Gerçek uygulamalarda daha fazla sensör verisi ve gelişmiş ML modelleri kullanılmalıdır.  
- Frontend tarafında **HTML, CSS ve JS** dosyaları ayrı tutulmuştur.  
  Bu sayede arayüz düzenli, temiz ve geliştirilebilir yapıdadır.  

---

