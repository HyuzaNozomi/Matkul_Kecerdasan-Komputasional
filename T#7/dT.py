import pandas as pd
import numpy as np
from tabulate import tabulate

class DataManusia:
    # Inisialisasi atribut
    def __init__(self,Nama=None, Kehadiran=None, Tugas=None, Status=None, Keterangan=None, df= None):
        self.Nama = Nama
        self.Kehadiran = Kehadiran
        self.Tugas = Tugas
        self.Status = Status
        self.Keterangan = Keterangan
        self.df = df  
        
    # Data sistem presensi
    df = pd.DataFrame({
        'Nama': [
            'Andi', 'Budi', 'Citra', 'Deni', 
            'Hana', 'Ocha', 'Samny', 'Mei'
        ],
        'Kehadiran' : [
            "Tinggi", 'Rendah', "Tinggi", "Rendah",
            "Tinggi", "Tinggi", "Tinggi", "Tinggi"
        ],
        "Tugas": [
            "Lengkap", "Tidak Lengkap", "Tidak Lengkap", "Lengkap",
            "Lengkap", "Lengkap", "Lengkap", "Lengkap"
        ],
        "Status": [
            "Aktif", "Tidak Aktif", "Aktif", "Tidak Aktif",
            "Aktif", "Aktif", "Aktif", "Aktif"
        ],
        "Keterangan": [
            "Mahasiswa Disiplin", "Mahasiswa Tidak Disiplin", "Mahasiswi Disiplin", "Mahasiswa Tidak Disiplin",
            "Mahasiswi Disiplin", "Mahasiswi Disiplin", "Mahasiswa Disiplin", "Mahasiswi Disiplin"
        ]
    })

    # Menampilkan DataFrame
    def display_dataFrame(self):
        print(tabulate(self.df, headers='keys', tablefmt='grid', showindex=False))

    # Menentukan nilai status target
    def status_target(self, Kehadiran, Status):
        match Kehadiran:
            case "Tinggi":
                return "Aktif"
            case "Rendah":
                return "Tidak Aktif"
            case _:
                return "Kehadiran tidak valid"

    # Bonus jika tugas lengkap
    def bonuses_tugas(self, Tugas, Kehadiran):
        if Tugas == "Lengkap" and  Kehadiran == "Tinggi":
            return "Mahasiswa Disiplin"
        else:
            return "Tidak memenuhi syarat kriteria"

    # Update data
    def update_data(self, Nama, Menu, NewNilai):
        if Nama not in self.df['Nama'].values:
            print(f"\n[Error] Nama '{Nama}' tidak ditemukan!")
            return

        idx = self.df[self.df['Nama'] == Nama].index[0]

        #proses update
        match Menu:
            case "1":
                self.df.at[idx, 'Kehadiran'] = NewNilai
                print(f"\nSukses Mengubah Kehadiran {Nama} menjadi {NewNilai}.")
            case "2":
                self.df.at[idx, "Tugas"] = NewNilai
                print(f"\nSukses Mengubah Tugas {Nama} menjadi {NewNilai}.")
            case "3": 
                if isinstance(NewNilai, tuple) or isinstance(NewNilai, list):
                    self.df.at[idx, 'Kehadiran'] = NewNilai[0]
                    self.df.at[idx, 'Tugas'] = NewNilai[1]
                    print(f"\nSukses Mengubah Kehadiran ({NewNilai[0]}) & Tugas ({NewNilai[1]}) untuk {Nama}.")
                else:
                    print("\nError Format nilai baru untuk opsi 3 harus kombinasi (Kehadiran, Tugas).")
                    return
            case _:
                print("\nError Opsi menu update tidak valid!")
                return
    
        #Update display (Sekarang sejajar dengan match Menu di dalam fungsi update_data)
        hadir_skrg = self.df.at[idx, 'Kehadiran']
        tugas_skrg = self.df.at[idx, 'Tugas']
        status_lama = self.df.at[idx, 'Status']
        self.df.at[idx, 'Status'] = self.status_target(hadir_skrg, status_lama)
        self.df.at[idx, 'Keterangan'] = self.bonuses_tugas(tugas_skrg, hadir_skrg)
        print("Kolom 'Status' dan 'Keterangan' berhasil diperbarui.")
    

    # Menampilkan hasil
    def display_results(self):
        # Tampilkan DataFrame
        self.display_dataFrame()

        # Tampilkan hasil presensi
        print("\n" + "-" * 81)
        for _, row in DataManusia.df.iterrows():
            nama = row['Nama']
            hadir = row['Kehadiran']
            tugas = row['Tugas']
            status = row['Status']

            status_target = self.status_target(hadir, status)
            bonus = self.bonuses_tugas(tugas, hadir)

            # Label teks
            lbl_nama    = "Nama".ljust(17)
            lbl_hadir   = "Kehadiran".ljust(17)
            lbl_tugas   = "Tugas".ljust(17)
            lbl_status  = "Status".ljust(17)
            lbl_target  = "Status Target".ljust(17)
            lbl_bonus   = "Bonus".ljust(17)

            # cetak
            print(f"\n{lbl_nama}: {nama}")
            print(f"{lbl_hadir}: {hadir}")
            print(f"{lbl_tugas}: {tugas}")
            print(f"{lbl_status}: {status}")
            print(f"{lbl_target}: {status_target}")
            print(f"{lbl_bonus}: {bonus}")


if __name__ == "__main__":
    mhs = DataManusia()
    mhs.df = DataManusia.df.copy()
    
    while True:
        print("\n" + "-"*40 + " MENU SISTEM DATA MANUSIA " + "-"*40)
        print("1. Tampilkan DataFrame")
        print("2. Tampilkan Hasil Rincian Evaluasi")
        print("3. Update/Perbaiki Kesalahan Data")
        print("4. Keluar")

        pilih_Menu = input("Pilih Menu (1-4) hanya angka yet!: ")

        match pilih_Menu:
            case "1":
                mhs.display_dataFrame()
            case "2":
                mhs.display_results()
            case "3":
                print("\n--- Pilih MY_Menu ---")
                nama_target = input("Masukkan Nama Mahasiswa yang mau diupdate: ")
                
                print("Komponen yang ingin diperbaiki:")
                print("1. Hanya Kehadiran")
                print("2. Hanya Tugas")
                print("3. Keduanya (Kehadiran & Tugas)")
                menu_update = input("Pilih komponen (1-3): ")

                match menu_update:
                    case "1":
                        nilai = input("Masukkan Kehadiran baru (Tinggi/Rendah): ")
                        mhs.update_data(nama_target, menu_update, nilai)
                    case "2":
                        nilai = input("Masukkan Tugas baru (Lengkap/Tidak Lengkap): ")
                        mhs.update_data(nama_target, menu_update, nilai)
                    case "3":
                        kh = input("Masukkan Kehadiran baru (Tinggi/Rendah): ")
                        tg = input("Masukkan Tugas baru (Lengkap/Tidak Lengkap): ")
                        mhs.update_data(nama_target, menu_update, (kh, tg))
                    case _:
                        print("Error Pilihan komponen salah.")
            case "4":
                print("\nTerima kasih! Keluar dari sistem.")
                break
            case _:
                print("\nPeringatan Pilihan tidak valid, PILIH YANG BENAR YET!, Silahkan Coba Lagi.")