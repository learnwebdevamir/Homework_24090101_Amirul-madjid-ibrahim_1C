#MENGHITUNG ABSENSI KETERLAMBATAN MAHASISWA SAAT MASUK KE KELAS

print("IDENTITAS MAHASISWA")

nama = str(input("MASUKKAN NAMA MAHASISWA: "))
prodi = str(input("MASUKKAN NAMA PRODI: "))
nim = int(input("MASUKKAN NIM: "))
kelas = str(input("MASUKKAN NAMA KELAS: "))

print("INFORMASI PERKULIAHAN HARI SENEN")
matkul_ke1 = str(input("KONSEP TEKNOLOGI INFORMASI, JAM DIMULAI: "))
masuk = int(input("SELISIH BERAPA MENIT: "))
status = "TIDAK TERLAMBAT" if masuk <30 else "TERLAMBAT"
print(status)

matkul_ke2 = str(input("KALKULUS, JAM DIMULAI: "))
masuk2 = int(input("SELISIH BERAPA MENIT: "))
status1 = "TIDAK TERLAMBAT" if masuk2 <30 else "TERLAMBAT"
print(status1)

