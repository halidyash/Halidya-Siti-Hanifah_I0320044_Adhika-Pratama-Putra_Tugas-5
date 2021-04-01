#Soal 1
#Program menyapa pengunjung

print('Masukkan Nama Anda!')
x = input('Masukkan nama : ')
print('Masukkan jenis kelamin Anda!')
y = input('Masukkan jenis kelamin (p/l) : ')

#output
if y == 'l':
    print("Selamat Datang, Tuan", x, "!")
else:
    print("Selamat Datang, Nyonya", x, "!")
