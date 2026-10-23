# Mikroklimatik Ölçümler ve IoT ile Fotovoltaik Güç Üretim Tahmini

[English](README.md) · [Mevcut durum](STATUS.md) · [Yol haritası](ROADMAP.md)

Bu çalışma, Ege Üniversitesinde panel seviyesindeki çevresel ve elektriksel ölçümleri eş zamanlı toplayacak otonom bir IoT istasyonu ile fotovoltaik güç üretim tahmin yöntemlerinin karşılaştırılmasını amaçlayan bir araştırma projesidir.

**Durum:** TÜBİTAK 1002-A desteği onaylanmıştır; proje geliştirme başlangıç aşamasındadır. Bu depoda teknik özet, önerilen mimari, gereksinimler, doğrulama planı ve sentetik veriyi denetleyen küçük bir başlangıç aracı bulunur. Henüz saha başarımı veya eğitilmiş model sonucu sunulmamaktadır.

## Projenin amacı

Bölgesel hava durumu verileri ile panelin bulunduğu noktada ölçülen mikroklimatik verilerin PV güç tahminine katkısı aynı deney düzeninde karşılaştırılacaktır. Ölçümden veri kaydına, veri kalitesinden tahmin modeline kadar izlenebilir bir sistem kurulması hedeflenmektedir.

## Önerilen sistem

![Önerilen sistem mimarisi](docs/media/architecture.svg)

Ana işlemci adayı ESP32 TTGO T-Call'dır. Sensör verilerinin uygun arayüzlerle okunması, RTC ile zaman damgalanması, microSD karta yerel kaydı ve hücresel bağlantıyla buluta aktarılması planlanmaktadır. Dokunmatik HMI, internet olmasa da yerel sistem durumunu gösterecektir. Web/mobil izleme ve Python ortamında model geliştirme ayrı katmanlardır.

## Sayısal tasarım hedefleri

Bu tablodaki değerler elde edilmiş sonuç değil, öneri belgesindeki hedeflerdir.

| Başlık | Hedef |
| --- | --- |
| Ham veri aralığı | 1 dakika |
| Temel çevresel değişkenler | Işınım, ortam sıcaklığı, panel sıcaklığı, bağıl nem, rüzgâr hızı |
| Ek değişkenler | Rüzgâr yönü ve türetilmiş güneşlenme göstergesi |
| Elektriksel değişkenler | DC gerilim, akım ve güç |
| Toplulaştırma | 10 dakika, 30 dakika, 1 saat |
| Veri toplama | En az 4 ay; hedef 6 ay |
| Veri bütünlüğü | En az %98 |
| Modbus testi | 72 saatte en az %99 geçerli işlem, en fazla %1 CRC hatası |
| Otonomi | Tasarım senaryosunda 5 güneşsiz gün |
| Tahmin ufukları | 1, 6, 12 ve 24 saat |
| 1/6 saat tahmin hedefi | nRMSE ≤%10, R² ≥0,95; önceden tanımlı düşük güç kuralıyla MAPE ≤%8 |
| 12/24 saat tahmin hedefi | nRMSE ≤%15, R² ≥0,90 |
| Referansla karşılaştırma | RMSE'de en az %15 bağıl iyileşme |

## Yöntem

Kronolojik eğitim/test ayrımı ve eğitim dönemi içinde ileri yürüyen doğrulama kullanılacaktır. Çoklu doğrusal regresyon, SVR ve standart YSA ile PSO/GWO/WOA/GA adaylarıyla optimize edilecek YSA modelleri ortak kurallarla karşılaştırılacaktır. Hangi algoritmanın daha iyi olduğu deneylerden sonra belirlenecektir.

Gelecekte ölçülmüş hava verisini geçmişte biliniyormuş gibi modele vermemek, test dönemini model seçimine karıştırmamak ve gece sıfıra yakın güç değerlerinde MAPE kuralını açıkça belirtmek değerlendirme planının parçalarıdır.

## Benim planlanan katkım

Proje yürütücüsü **Dr. Günnur Şen**'dir; akademik ekipte **Abdullah Elen** de yer almaktadır. Öneri belgesindeki iş dağılımına göre Emre Teltik'in görev alanları donanım/sensör entegrasyonu, gömülü veri toplama yazılımı, yerel HMI ve sistem performans testleridir. Bulut, veri hazırlama ve YSA geliştirme çalışmalarının tamamı tek kişiye ait olarak gösterilmemektedir. Ekip bilgisi [CONTRIBUTORS.md](CONTRIBUTORS.md) dosyasındadır.

## Depoda şu an ne çalışıyor

`tools/validate_telemetry.py`, sentetik CSV örneğindeki zaman damgalarını, birimleri, örnekleme boşluklarını ve bazı veri tutarlılığı kurallarını denetleyen yardımcı programdır. Fiziksel sensör sürücüsü veya tahmin modeli değildir. Çalıştırma açıklaması [tools/README.md](tools/README.md) dosyasındadır.

Gerçek ölçüm sonuçları geldikçe veri sürümü, deney koşulları ve kod sürümüyle eklenecektir. Tam başvuru formu ve kişisel bilgiler bu depoya dahil edilmemiştir.
