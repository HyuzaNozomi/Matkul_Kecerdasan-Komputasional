Tentu, ini adalah draf `README.md` yang disusun secara profesional, terstruktur, dan mudah dipahami oleh dosen atau pembaca kode lainnya. Kamu bisa menyalin teks ini ke dalam file bernama `README.md` di folder proyekmu.

---

# Proyek: Q-Learning pada Environment Taxi-v4

Proyek ini merupakan implementasi algoritma **Q-Learning** untuk melatih agen kecerdasan buatan (*AI Agent*) agar dapat menyelesaikan tugas penjemputan dan pengantaran penumpang pada lingkungan simulasi `Taxi-v4` dari *Gymnasium*.

## Daftar Isi

1. [Deskripsi Proyek](https://www.google.com/search?q=%23deskripsi-proyek)
2. [Prasyarat](https://www.google.com/search?q=%23prasyarat)
3. [Struktur Kode](https://www.google.com/search?q=%23struktur-kode)
4. [Analisis Hyperparameter](https://www.google.com/search?q=%23analisis-hyperparameter)
5. [Cara Menjalankan](https://www.google.com/search?q=%23cara-menjalankan)

---

## Deskripsi Proyek

Tujuan utama dari proyek ini adalah melatih agen AI untuk mengoptimalkan rute dalam grid 5x5. Agen belajar melalui metode *trial-and-error* dengan memaksimalkan *reward* berdasarkan keputusan yang diambil. Proyek ini juga membandingkan efisiensi pembelajaran pada tiga durasi latihan (1000, 2000, dan 5000 episode).

## Prasyarat

Untuk menjalankan kode ini, pastikan sistemmu telah terinstal pustaka berikut:

* `numpy`: Untuk operasi matriks Q-Table.
* `gymnasium`: *Environment* standar untuk RL.
* `matplotlib`: Untuk visualisasi grafik hasil pembelajaran.

Instalasi dapat dilakukan via terminal:

```bash
pip install numpy gymnasium matplotlib

```

## Struktur Kode

Program ini terbagi menjadi tiga blok logika utama:

1. **Fungsi Training (`train_taxi_agent`)**: Mengelola logika Q-Learning, memperbarui nilai Q-Table berdasarkan *reward*, dan mengelola penurunan nilai *epsilon* (*decay*).
2. **Eksperimen Perbandingan**: Menjalankan fungsi training untuk 1000, 2000, dan 5000 episode guna mengukur kecepatan konvergensi agen.
3. **Visualisasi & Testing**:
* Menampilkan grafik perbandingan rata-rata *reward* per 100 episode.
* Melakukan demonstrasi pergerakan taksi (*Testing Agent*) setelah agen mencapai tingkat kematangan maksimal (5000 episode).



## Analisis Hyperparameter

Program ini menggunakan pengaturan (*tuning*) sebagai berikut:

* **Learning Rate (α) = 0.8**: Memberikan bobot tinggi pada informasi baru agar agen cepat belajar.
* **Discount Factor (γ) = 0.95**: Memastikan agen lebih memprioritaskan imbalan jangka panjang (kesuksesan *dropoff*).
* **Epsilon Decay = 0.005**: Memastikan transisi yang mulus dari fase eksplorasi (mencoba segalanya) ke fase eksploitasi (menggunakan jalur terbaik).

## Cara Menjalankan

1. Pastikan lingkungan *Python* sudah siap.
2. Salin kode ke dalam file Python (`.py`) atau cell Jupyter Notebook.
3. Jalankan sel tersebut. Grafik perbandingan akan muncul otomatis, diikuti dengan log pergerakan taksi dalam simulasi *testing* di akhir *output*.

---

### Penjelasan Mengapa README Ini Dibuat Seperti Ini:

* **Struktur Profesional:** Dosen biasanya menyukai README yang memiliki *Daftar Isi* agar mudah dinavigasi.
* **Analisis Teknis:** Penjelasan mengenai *Hyperparameter* menunjukkan bahwa kamu tidak sekadar "bisa menjalankan kode", tetapi juga mengerti *mengapa* angka-angka tersebut dipilih.
* **Kejelasan Alur:** Bagian *Struktur Kode* membantu dosen memahami alur logika program tanpa harus membaca baris demi baris kodenya terlebih dahulu.

Apakah ada bagian dari `README` ini yang ingin kamu tambah atau ubah?