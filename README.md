# MNIST Rakam Tanıma ve Tahmin Arayüzü 🎨🔢

Bu proje, popüler MNIST veri setini kullanarak el yazısı rakamları (0-9) tanıyan bir Derin Öğrenme (Deep Learning) modelidir. Proje sadece model eğitimini kapsamakla kalmaz, aynı zamanda kullanıcıların kendi çizdikleri veya yükledikleri rakamları test edebilecekleri interaktif bir web arayüzü sunar.

## 🚀 Özellikler

* **Yapay Sinir Ağı Modeli:** TensorFlow/Keras kullanılarak oluşturulmuş, 128 ve 64 nöronlu gizli katmanlara sahip model mimarisi.
* **Akıllı Görüntü İşleme:** Arayüze yüklenen görseller otomatik olarak OpenCV ile gri tonlamaya çevrilir ve 28x28 boyutlandırılır. Beyaz arka planlı görseller modelin daha iyi anlaması için otomatik olarak tersine (invert) çevrilir.
* **Gradio Web Arayüzü:** İki farklı kullanım seçeneği sunar:
  * **Resim Yükle:** Kendi cihazınızdaki bir rakam görselini (.png, .jpg) yükleyerek test edebilirsiniz.
  * **Çizim Yap:** Entegre çizim tahtası üzerinden anlık olarak farenizle rakam çizip modelin tahminini görebilirsiniz.

## 📸 Ekran Görüntüleri

### Resim Yükleme Ekranı
![Resim Yükleme Arayüzü]
<img width="1919" height="791" alt="Image" src="https://github.com/user-attachments/assets/02313aa4-2506-4a3b-aaf6-76d3ef0844ab" />


### Canlı Çizim ve Tahmin Ekranı
![Çizim Yapma Arayüzü]
<img width="1919" height="836" alt="Image" src="https://github.com/user-attachments/assets/9da615ba-333a-4d1d-b2b9-0df32c198870" />

## 🛠️ Kullanılan Teknolojiler

* **Python 3.x**
* **TensorFlow & Keras:** Model oluşturma ve eğitme
* **Gradio:** Kullanıcı arayüzü (UI) geliştirme
* **OpenCV (cv2):** Görüntü işleme ve boyutlandırma
* **Pandas & NumPy:** Veri işleme ve manipülasyon
* **Scikit-Learn:** Veri setini eğitim ve test olarak ayırma
* **Matplotlib:** Eğitim başarısı (Accuracy) grafiklerini görselleştirme

## 💻 Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Repoyu bilgisayarınıza klonlayın:
   ```bash
   git clone <repo_url_niz>
   cd <repo_klasor_adi>
