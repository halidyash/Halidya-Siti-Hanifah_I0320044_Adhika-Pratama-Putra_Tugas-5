# Soal 2
# Program grading nilai
print('Masukkan Nama Anda!')
x = input('Masukkan nama : ')
# inputkan bilangan
print('Masukkan Nilai Anda!')
y = int(input('Masukkan nilai : '))
nilai = 'Halo, '+ str(x) + '!' + ' Nilai anda setelah dikonversi adalah '
print(" ")

#memeriksa grading nilai
if y >= 85:
    print(nilai + 'A')
elif y >= 80:
    print(nilai + 'A-')
elif y >= 75:
    print(nilai + 'B+')
elif y >= 70:
    print(nilai + 'B')
elif y >= 65:
    print(nilai + 'C+')
elif y >= 60:
    print(nilai + 'C')
else:
    print(nilai + 'E')
print()