'''
Nama        : Firda Citra Aulia Zahramadan
NIM         : 2601439
Mata Kuliah : Dasar Pemrograman (1A)

Menginputkan sejumlah n diisi nama nama hewan
kemudian mencetak kembali hewan yang telah diinputkan
'''
no = 1
n = int(input("Masukkan jumlah hewan yang ingin diinputkan: "))
hewan = []
for i in range(n):
    nama_hewan = input(f"Masukkan nama hewan ke-{i + 1}: ")
    hewan.append(nama_hewan)

print("==================================================================================")
print("Hewan yang telah diinputkan:")
for h in hewan:
    print(f"Hewan ke {no} : {h}")

