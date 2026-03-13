import pandas as pd
import numpy as np

# Veriyi oku
train_df = pd.read_csv('train_mnist.csv')


y = train_df['label'].values
x = train_df.drop(['label', 'Unnamed: 0', 'id'], axis=1).values

print("Veri yüklendi. X boyutu:", x.shape)

# Pikselleri 0-1 arasına sıkıştırıyoruz
x = x.astype('float32') / 255.0  #Standart scaler yapmak yerine bölerek yaptı çünkü piksellerin hepsi aynı birimde 0-255 arasında değerlermiş
print("İlk pikselin değeri (Normalizasyon sonrası):", x[0, 150])

from tensorflow.keras.utils import to_categorical

# Rakamları (0-9) 10 elemanlı kategorik bir yapıya çeviriyoruz
y = to_categorical(y, num_classes=10)

# Kontrol edelim
print("İlk resmin yeni cevap formatı:", y[0])
#One Hot Encoding yaptık ama kensor kütüphanesiyle çünkü zaten numerik değerleri 1 ve 0 ile kategorikleştirdik

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=6)

print("Eğitim seti boyutu:", x_train.shape)
print("Test seti boyutu:", x_test.shape)


from keras.models import Sequential
from keras.layers import Dense

# 1. Model iskeletini oluşturuyoruz
model = Sequential()

# 2. Giriş Katmanı ve İlk Gizli Katman
# 784 girişi alıp 128 nörona bağlıyoruz. 'relu' şu an en popüler aktivasyon fonksiyonudur.
model.add(Dense(units=128, kernel_initializer='uniform', activation='relu', input_dim=784))

# 3. İkinci Gizli Katman (Raporun için bunu ekleyip çıkartarak deney yapabilirsin)
model.add(Dense(units=64, kernel_initializer='uniform', activation='relu'))

# 4. Çıkış Katmanı
# 10 nöron (0-9 arası rakamlar için). 'softmax' bize olasılık verir (%90 budur gibi).
model.add(Dense(units=10, kernel_initializer='uniform', activation='softmax'))

# 5. Modeli Derleme (Öğrenme stratejisi)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

print("Model mimarisi başarıyla oluşturuldu ve derlendi.")


# Modeli eğitmeye başlıyoruz
# verbose=1 sayesinde eğitimin gidişatını (accuracy artışını) anlık göreceksin
history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test), verbose=1)

print("Eğitim tamamlandı!")

import matplotlib.pyplot as plt

# Başarı (Accuracy) Grafiği
plt.plot(history.history['accuracy'], label='Eğitim Başarısı')
plt.plot(history.history['val_accuracy'], label='Test Başarısı')
plt.title('Model Başarı Grafiği')
plt.ylabel('Doğruluk (Accuracy)')
plt.xlabel('Epoch (Tur)')
plt.legend()
plt.show()

import gradio as gr
import cv2
import numpy as np

def tahmin_et(img):
    # Gradio'dan gelen görüntüyü kontrol et
    if img is None:
        return "Resim bulunamadı"
        
    # Görüntü bir sözlük yapısında gelebilir (çizim alanı için)
    if isinstance(img, dict):
        img = img['composite']
    
    # 1. Adım: Gri Tonlama
    if len(img.shape) == 3:
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        img_gray = img

    # 2. Adım: Boyutlandırma (28x28)
    img_resized = cv2.resize(img_gray, (28, 28))
    
    # 3. Adım: Akıllı Renk Kontrolü (Invert)
    # MNIST siyah arka plan sever. Eğer resmin köşesi beyazsa (255), 
    # bu bir beyaz kağıttır ve renkleri tersine çevirmemiz gerekir.
    if img_resized[0,0] > 127: 
        img_final = cv2.bitwise_not(img_resized)
    else:
        img_final = img_resized
        
    # 4. Adım: Normalizasyon ve Şekillendirme
    img_input = img_final.reshape(1, 784).astype('float32') / 255.0
    
    # Tahmin
    tahmin = model.predict(img_input)
    return int(np.argmax(tahmin))

# Arayüzü hem çizim hem yükleme yapacak şekilde kuruyoruz
with gr.Blocks() as demo:
    gr.Markdown("# Ömer'in MNIST Rakam Tanıyıcısı")
    
    with gr.Tab("Resim Yükle"):
        image_input = gr.Image(label="PNG/JPG Dosyası Yükle")
        upload_button = gr.Button("Tahmin Et")
        upload_output = gr.Label(label="Sonuç")
        upload_button.click(tahmin_et, inputs=image_input, outputs=upload_output)
        
    with gr.Tab("Çizim Yap"):
        sketch_input = gr.Sketchpad(label="Buraya Rakam Çiz")
        sketch_button = gr.Button("Tahmin Et")
        sketch_output = gr.Label(label="Sonuç")
        sketch_button.click(tahmin_et, inputs=sketch_input, outputs=sketch_output)

demo.launch(share=True)







