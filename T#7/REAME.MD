# Sistem Manajemen Data Presensi Mahasiswa

Aplikasi ini adalah program berbasis terminal (CLI) sederhana untuk mengelola, mengevaluasi, dan memperbarui data kehadiran serta tugas mahasiswa. Program ini menggunakan pendekatan pemrograman berorientasi objek (OOP) di Python agar struktur datanya rapi dan mudah dikembangkan.

---

## Kebutuhan Sistem dan Versi Python

Program ini dibuat dan berjalan dengan baik pada spesifikasi berikut:
* **Python Version:** Python 3.10 atau versi di atasnya.
    * *Catatan:* Program ini menggunakan fitur `match-case` (Pattern Matching) yang baru tersedia sejak Python versi 3.10. Jika Anda menggunakan versi di bawahnya, program akan memicu error.

---

## Penjelasan Library yang Digunakan

Program ini memanfaatkan tiga pustaka utama untuk mengolah data dan mempercantik tampilan terminal:

1.  **Pandas (`import pandas as pd`)**
    Digunakan untuk membuat dan mengelola tabel data (DataFrame). Pandas mempermudah proses pencarian indeks data berdasarkan nama mahasiswa, serta mengubah nilai pada baris dan kolom tertentu secara instan.
2.  **NumPy (`import numpy as np`)**
    Meskipun di dalam kode saat ini belum dieksploitasi secara intensif, library ini umumnya digunakan untuk mendukung operasi komputasi array performa tinggi dan manipulasi data numerik yang terintegrasi dengan Pandas.
3.  **Tabulate (`from tabulate import tabulate`)**
    Berperan penting dalam mengubah data tabel mentah dari Pandas menjadi bentuk tabel grafis bergaris (`grid`) di terminal, sehingga data lebih enak dibaca oleh pengguna.

---

## Fitur-Fitur Utama Aplikasi

Aplikasi ini dilengkapi dengan empat fitur utama yang dapat diakses secara dinamis oleh pengguna melalui menu:

1.  **Menampilkan DataFrame (Menu 1):** Menampilkan seluruh data tabel mahasiswa saat ini dalam bentuk tabel grid yang rapi, bergaris, dan terstruktur.
2.  **Menampilkan Hasil Rincian Evaluasi (Menu 2):** Menampilkan ringkasan penilaian per individu secara vertikal, lengkap dengan status keaktifan dan predikat kedisiplinan yang sudah diformat sejajar menggunakan spasi statis.
3.  **Update/Perbaiki Kesalahan Data (Menu 3):** Mengubah data komponen spesifik (Kehadiran saja, Tugas saja, atau Keduanya sekaligus) untuk mahasiswa tertentu, yang kemudian memicu sistem untuk menghitung ulang status dan keterangan mereka secara otomatis.
4.  **Keluar dari Sistem (Menu 4):** Menghentikan perulangan menu utama secara paksa dan menutup program dengan aman.

---

## Penjelasan Alur dan Isi Source Code

Kode program dibungkus ke dalam sebuah kelas bernama `DataManusia` yang memiliki fungsi-fungsi utama sebagai berikut:

* **`__init__` (Inisialisasi):** Wadah untuk mengenalkan variabel dasar seperti Nama, Kehadiran, Tugas, Status, Keterangan, dan DataFrame (`df`).
* **Struktur Data Awal (`df = pd.DataFrame(...)`):** Berisi data bawaan pabrik (default) dari 8 orang mahasiswa sebagai contoh awal manipulasi data sistem.
* **`display_dataFrame`:** Berfungsi mencetak tabel utama mahasiswa ke terminal menggunakan format grid dari library Tabulate.

### Penjelasan Percabangan (If-Else dan Match-Case)
Program ini mengombinasikan dua jenis struktur percabangan untuk mengambil keputusan berdasarkan kondisi data atau input pengguna:

1.  **Struktur Match-Case:**
    * **`status_target`:** Digunakan untuk memeriksa string nilai Kehadiran. Jika bernilai "Tinggi", program langsung mengembalikan status "Aktif". Jika "Rendah", mengembalikan status "Tidak Aktif". Tanda `case _:` berfungsi seperti `else`, yaitu menangkap nilai di luar dua pilihan tersebut sebagai data tidak valid.
    * **Menu Update & Menu Utama:** Membaca angka string yang diinput oleh pengguna untuk melompat ke blok kode yang sesuai dengan nomor menu pilihan (1, 2, 3, atau 4).

2.  **Struktur If-Else:**
    * **`bonuses_tugas`:** Digunakan untuk mengecek dua kondisi sekaligus menggunakan operator logika `and`. Sistem memeriksa **if (jika)** Tugas bernilai "Lengkap" **dan** Kehadiran bernilai "Tinggi", maka mahasiswa berhak mendapatkan keterangan "Mahasiswa Disiplin". Jika salah satu atau kedua kondisi tersebut tidak terpenuhi, blok **else (selain itu)** akan berjalan dan memberikan keterangan "Tidak memenuhi syarat kriteria".
    * **Validasi Nama di `update_data`:** Menggunakan `if` untuk memastikan nama yang diinput pengguna terdaftar di dalam tabel sebelum melakukan manipulasi. Jika nama tidak ada, program memunculkan pesan error dan langsung berhenti (`return`).
    * **Validasi Format Nilai di `update_data`:** Menggunakan `if-else` pada Menu Opsi 3 untuk memastikan input data kombinasi yang dikirim berbentuk objek `tuple` atau `list`. Jika benar, data dipecah; jika salah, blok `else` akan menampilkan pesan error format salah.

* **`display_results`:** Menampilkan rincian evaluasi per individu secara vertikal. Fungsi ini menggunakan perintah `.ljust(17)` pada label teks agar susunan teks dan tanda titik dua (`:`) berbaris lurus rapi ke bawah di terminal.
* **Menu Utama (`if __name__ == "__main__":`):** Bagian yang pertama kali dieksekusi saat file dijalankan. Menggunakan perulangan `while True` agar program terus berjalan menampilkan 4 pilihan menu utama sampai pengguna memilih menu nomor 4 (Keluar).

---

## Cara Menjalankan Program

Ikuti langkah-langkah berikut untuk menjalankan program di komputer Anda:

### Langkah 1: Install Library yang Diperlukan
Sebelum memutar program, Anda harus memasang library Pandas dan Tabulate terlebih dahulu lewat terminal atau command prompt. Ketik perintah berikut:

```bash
pip install pandas tabulate