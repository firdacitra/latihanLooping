'''
Nama        : Firda Citra Aulia Zahramadan
NIM         : 2601439
Mata Kuliah : Dasar Pemrograman

sistem login sederhana, tidak ada batas salah
username/password
Username: dasproRPL
Password: RPLfire!123

'''

usernameTrue = "dasproRPL"
passwordTrue = "RPLfire!123"

print("================= LOGIN ===================")
while True:
    username_input = input("Masukkan username: ")
    password_input = input("Masukkan password: ")

    if username_input == usernameTrue and password_input == passwordTrue:
        print("Login berhasil.")
        break
    else:
        print("username atau password salah! coba lagi")




