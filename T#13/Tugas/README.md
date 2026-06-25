# Q-Learning AI: Agen Taksi Pintar (Taxi-v4)

Pernahkah kamu membayangkan bagaimana caranya mengajari sebuah program komputer untuk menjadi supir taksi yang handal? Kode ini adalah jawabannya!

Proyek ini menggunakan algoritma **Q-Learning** (sebuah cabang dari *Reinforcement Learning*) untuk mengajari sebuah Agen AI (Kecerdasan Buatan) cara menjemput dan mengantar penumpang di lingkungan simulasi **Taxi-v4** dari library Gymnasium.

Pendekatannya mirip seperti melatih hewan peliharaan: kita memberikan **hadiah (reward)** jika dia melakukan hal yang benar, dan **hukuman (penalty)** jika dia melakukan kesalahan.

---

## 🛠️ Prasyarat (Yang Dibutuhkan)

Sebelum menjalankan kode ini, pastikan kamu sudah menginstal beberapa "peralatan" (library) Python berikut di komputermu:

* `numpy` (Untuk perhitungan matematika dan tabel memori)
* `gymnasium` (Dunia simulasi taksinya)
* `matplotlib` (Untuk menggambar grafik hasil belajar)

Cara installnya:

```bash
pip install numpy gymnasium matplotlib

```
---

## 🔬 Bedah Kode: Memahami Cara Kerjanya

Mari kita bongkar *source code* tersebut bagian per bagian agar kamu paham apa yang sebenarnya dilakukan oleh komputer:

### 1. Persiapan Alat (Import Library)

```python
import numpy as np
import gymnasium as gym
import random
import matplotlib.pyplot as plt

```

Di sini kita menyiapkan alat-alatnya. `numpy` untuk membuat tabel memori (matematika), `gymnasium` untuk memanggil simulasi taksinya, `random` untuk membuat AI bergerak acak (saat tahap coba-coba), dan `matplotlib` untuk menggambar grafik di akhir.

### 2. Membangun Fungsi Training

```python
def train_taxi_agent(total_episodes):
    env = gym.make("Taxi-v4")
    state_size = env.observation_space.n
    action_size = env.action_space.n
    q_table = np.zeros((state_size, action_size))

```

Fungsi `train_taxi_agent` ini adalah "sekolah" bagi si taksi.

* Kita membuat arena taksi (`env`).
* Kita menghitung ada berapa kemungkinan posisi/kondisi (`state_size`) dan berapa banyak gerakan yang bisa dilakukan seperti maju, mundur, ambil penumpang (`action_size`).
* Lalu, kita membuat **Q-Table**, yaitu buku catatan kosong berisi angka nol yang nantinya akan diisi dengan skor/nilai pengalaman AI.

### 3. Pengaturan Karakter AI (Hyperparameters)

```python
    learning_rate = 0.8          
    discount_rate = 0.95         
    epsilon = 1.0                
    ...

```

Bagian ini mengatur "otak" si AI.

* `learning_rate`: Seberapa cepat AI percaya pada informasi baru dibanding memori lamanya.
* `discount_rate`: Fokus AI pada hadiah di masa depan, bukan cuma hadiah instan.
* `epsilon`: Tingkat keacakan. Dimulai dari `1.0` (100% bergerak ngawur/coba-coba) agar AI mengeksplorasi peta. Nanti nilai ini akan terus dikurangi (`decay_rate`) agar AI mulai serius menggunakan ingatannya.

### 4. Siklus Belajar AI (Looping)

```python
    for episode in range(total_episodes):
        state_info = env.reset()
        ...
        while not done:

```

Ini adalah proses pengulangannya. Jika kita set `total_episodes` 1000, AI akan bermain 1000 kali. Setiap kali mulai (`episode` baru), posisi taksi dan penumpang diacak ulang (`env.reset()`). Selama game belum selesai atau *game over* (`while not done`), taksi akan terus bergerak.

### 5. Dilema AI: Coba-coba atau Gunakan Ingatan? (Eksplorasi vs Eksploitasi)

```python
            exploration_rate_threshold = random.uniform(0, 1)
            if exploration_rate_threshold > epsilon:
                action = np.argmax(q_table[state, :])
            else:
                action = env.action_space.sample()

```

Di setiap langkah, komputer mengocok angka acak dari 0 sampai 1.

* Jika angkanya lebih besar dari `epsilon` (ingat, epsilon akan makin kecil seiring waktu), AI akan melihat Q-Table dan memilih jalan terbaik yang sudah ia ketahui (**Eksploitasi**).
* Jika lebih kecil, AI akan bergerak asal-asalan untuk mencari pengalaman baru (**Eksplorasi**).

### 6. AI Bergerak dan Menerima Hadiah/Hukuman

```python
            step_result = env.step(action)
            ...
            new_state, reward, done, truncated, info = step_result

```

AI melakukan gerakan yang dipilihnya tadi (`env.step`). Lingkungan simulasi kemudian memberikan respons: posisi baru taksi (`new_state`), poin yang didapat (`reward` - positif jika benar, negatif jika nabrak/salah), dan status apakah game sudah selesai (`done`).

### 7. Otak Utama Pembelajaran (Persamaan Bellman)

```python
            q_table[state, action] = q_table[state, action] * (1 - learning_rate) + \
                learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))

```

**Ini adalah jantung dari kodenya!** Saat taksi bergerak dari Titik A ke Titik B dan dapat poin, dia akan membuka buku catatannya (Q-Table) dan *meng-update* nilainya. Rumus ini intinya berkata: *"Skor lama saya di titik ini diperbarui dengan mencampurkan skor lama, hadiah yang baru saja saya dapat, ditambah tebakan skor maksimal yang bisa saya dapatkan di langkah selanjutnya."*

### 8. Evaluasi (Ujian Nasional)

```python
avg_rewards_1000, q_table_1000 = train_taxi_agent(1000)
avg_rewards_2000, q_table_2000 = train_taxi_agent(2000)
avg_rewards_5000, q_table_5000 = train_taxi_agent(5000)

```

Kode keluar dari fungsi dan mulai menjalankan *training* sebanyak tiga kali dengan durasi yang berbeda-beda. Buku catatan (Q-Table) terbaik dari masing-masing tes disimpan untuk dibandingkan. Setelah ini selesai, kode `plt.plot()` di bawahnya akan menggambar grafik berdasarkan hasil ini.

### 9. Pembuktian di Dunia Nyata (Testing Agen)

```python
env_test = gym.make("Taxi-v4", render_mode="ansi")
...
while not done:
    action = np.argmax(q_table_5000[state, :])
    ...

```


---

## 🧠 Bagaimana Cara AI Ini Belajar? (Penjelasan Kode)

Kode ini dibagi menjadi tiga bagian utama, ibarat **Sekolah**, **Ujian Nasional**, dan **Kerja Lapangan**. Berikut adalah penjelasan dengan "bahasa manusia":

### 1. Masa Sekolah (Proses Training)

Di dalam fungsi `train_taxi_agent`, AI kita dimasukkan ke dalam simulasi berulang-ulang (disebut *Episode*).

* **Buku Catatan (Q-Table):** AI dibekali sebuah tabel kosong bernama Q-Table. Setiap kali dia berada di suatu posisi dan mengambil tindakan, dia akan mencatat apakah tindakan itu menghasilkan poin bagus atau buruk.
* **Coba-coba vs Pengalaman (Eksplorasi vs Eksploitasi):** Awalnya, AI tidak tahu apa-apa, jadi dia akan bergerak secara **acak** (coba-coba/eksplorasi). Namun seiring berjalannya waktu, dia akan mulai mengandalkan **buku catatannya** untuk mengambil keputusan yang pasti menguntungkan (pengalaman/eksploitasi).
* **Mengingat Masa Depan (Persamaan Bellman):** Ini adalah rumus matematika di dalam kode yang memastikan AI tidak hanya mencari poin instan, tapi juga merencanakan rute terbaik untuk jangka panjang.

### 2. Ujian Nasional (Evaluasi dan Perbandingan)

Bagaimana kita tahu AI sudah pintar? Kode ini tidak hanya melatih satu AI, melainkan tiga AI sekaligus dengan "waktu sekolah" yang berbeda-beda:

* AI yang belajar selama **1.000 episode**
* AI yang belajar selama **2.000 episode**
* AI yang belajar selama **5.000 episode**

Setelah ketiganya selesai belajar, program akan memunculkan sebuah **Grafik Visualisasi**. Dari grafik ini, kita bisa melihat bahwa AI yang belajar lebih lama (5.000 episode) grafik poinnya akan lebih stabil dan tinggi dibandingkan yang belajarnya hanya sebentar.

### 3. Kerja Lapangan (Testing/Simulasi)

Setelah mengetahui bahwa agen yang belajar 5.000 episode adalah yang paling pintar, kita mempekerjakannya di dunia nyata!

* Di bagian akhir kode, AI (lulusan 5.000 episode) diuji coba untuk mengantar penumpang **tanpa boleh mencoba-coba lagi secara acak**.
* Dia murni menggunakan ingatannya (Q-Table) untuk mencari penumpang, menjemputnya, dan mengantarkannya ke tujuan seefisien mungkin.
* Kamu bisa melihat pergerakan taksi ini secara langsung di layar terminalmu (dicetak dalam bentuk teks langkah demi langkah).

---

## ⚙️ Kamus Istilah (Hyperparameters)

Jika kamu melihat bagian atas kode, ada beberapa angka yang disetting. Berikut adalah arti dari angka-angka tersebut:

* **Learning Rate (0.8):** Seberapa cepat AI menyerap informasi baru. Angka 0.8 berarti dia sangat cepat belajar dari kejadian baru dan sedikit melupakan masa lalu.
* **Discount Rate (0.95):** Pandangan masa depan AI. Angka 0.95 berarti AI sangat peduli pada hadiah jangka panjang (mengantar penumpang sampai tujuan), bukan sekadar hadiah kecil di depan mata.
* **Epsilon (1.0):** Tingkat "coba-coba". Dimulai dari 100% (benar-benar acak), dan lambat laun menurun (*decay*) hingga tersisa 1% saja saat dia sudah pintar.

---

## 🚀 Cara Menjalankan

1. Simpan kode Python tersebut (misalnya dengan nama `taxi_qlearning.py`).
2. Buka terminal atau *command prompt*.
3. Jalankan perintah:
```bash
python taxi_qlearning.py

```

4. Tunggu beberapa saat, sebuah grafik akan muncul.
5. Setelah grafik ditutup (*close*), lihat terminalmu untuk menonton AI menyetir taksi langkah demi langkah sampai selesai!
```
