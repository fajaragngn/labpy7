# Latihan 3: penggunaan kondisi OR program membandingkan 3 input bilangan, 
# apabila penjumlahan 2 bilangan hasilnya sama dengan bilangan lainnya, 
# maka cetak pernyataan “BENAR”
a = int(input('Masukkan bilangan A: '))
b = int(input('Masukkan bilangan B: '))
c = int(input('Masukkan bilangan C: '))
if a+b == c or b+c == a or c+a == b:
    print('benar')
else: print('salah')