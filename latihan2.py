'''
Nama        : Firda Citra Aulia Zahramadan
NIM         : 2601439
Mata Kuliah : Dasar Pemrograman

menghitung nilai siswa sejumlah 5 siswa, dihitung nilai rata rata nya
'''
totalNilai = 0
print("======== MENGHITUNG NILAI RATA-RATA MAHASISWA ==========")
for i in range(10):
    nilai_mhs = int(input(f"Masukkan nilai ke-{i + 1}: "))
    totalNilai = totalNilai + nilai_mhs
    rataRata = totalNilai/10
print(rataRata)


