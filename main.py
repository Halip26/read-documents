# Membaca isi file "check.txt"
with open("check.txt", "r") as f:
    print(f.read())

# Menulis konten ke file "check2.txt"
with open("check2.txt", "w") as f:
    f.write("Sekarang file baru ada. Dengan informasi")

# Membaca isi file "check2.txt"
with open("check2.txt", "r") as f:
    print(f.read())

# Menambahkan teks ke file "check2.txt"
with open("check2.txt", "a") as f:
    f.write("Now the new file is there. We are appending text in file.")

# Membaca isi file "check2.txt" lagi
with open("check2.txt", "r") as f:
    print(f.read())

# Membaca dua baris pertama dari file "check.txt"
with open("check.txt", "r") as f:
    print(f.readline())
    print(f.readline())

# Membaca semua baris dari file "check.txt"
with open("check.txt", "r") as f:
    print(f.readlines())

# Membuat file kosong "myfile.txt"
with open("myfile.txt", "x"):
    pass
