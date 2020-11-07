# Lab 3
## Latihan 1
![latihan1](assets/img/lab3/1.png)

```
for row in range(0, 10):
    for col in range(0, 10):
        num = row + col
        if num < 10:
            empty = "  "
        else:
            if num < 100:
                empty  = " "
        print(empty, num, end = '')
    print()
```
Penjelasan:
* ``for row in range(0, 10):`` ``for col in range(0, 10):`` Variabel row / col berfungsi untuk menampung baris dan kolom, dan fungsi range() berfungsi untuk membuat list dengan area dari 0-10
* 

Output:

![latihan1.1](assets/img/lab3/1.1.png)

![latihan2](assets/img/lab3/2.png)

```
import random
nilai = int(input('Masukan nilai n : '))
a = 0
for x in range (nilai):
    i = random.uniform(.0,.5)
    a+=1
    print('data ke :',a,'==>', i)
```
Penjelasan:
* ``import random`` berfungsi untuk memanggil library random, dimana random berfungsi untuk menentukan pilihan secara acak
* ``nilai = int(input('Masukan nilai n : '))`` untuk menginputkan nilai berupa integer
* range() berfungsi menghasilkan list

Output:

![latihan2.2](assets/img/lab3/2.2.png)

# Modul Praktikum 2
## Latihan 1: Membuat program menentukan nilai akhir
```
nama = input('masukkan nama: ')
uts = input('masukkan nilai uts: ')
uas = input('masukkan nilai uas: ')
tugas = input('masukkan nilai tugas: ')
akhir = (int(tugas) * .2) + (int(uts) * .4) + (int(uts) * .4)
keterangan = ('TIDAK LULUS', 'LULUS')[akhir > 60.0]
if akhir > 80:
    huruf = 'A'
elif akhir > 70:
    huruf = 'B'
elif akhir > 50:
    huruf = 'C'
elif akhir > 40:
    huruf = 'D'
else:
    huruf = 'E'

print("\nNama :",nama) 
print("Nilai UAS :",uas) 
print("Nilai UTS :",uts) 
print("Nilai akhir :",akhir) 
print("\nNilai huruf :",huruf) 
print("keterangan :",keterangan) 

```
Output:

![latihan1-modul2](assets/img/praktikum-2/1.png)

## Latihan 2: Membuat program menampilkan status gaji karyawan

```
gaji = int(input("Masukkan gaji:"))
berkeluarga = (False, True)[input("Sudah berkeluarga? (Y/T)") == "Y"]
punya_rumah = (False, True)[input("Punya rumah? (Y/T)") == "Y"]
if gaji > 3000000:
 print ("Gaji sudah diatas UMR")
 if berkeluarga:
     print ("Wajib ikutan asuransi dan menabung untuk pensiun")
 else:
     print("Tidak perlu ikutan asuransi")
 if punya_rumah:
     print("Wajib bayar pajak rumah")
 else:
     print("tidak wajib bayar pajak rumah")
else:
    print("Gaji belum UMR")
```
Output:

![latihan2-modul2](assets/img/praktikum-2/2.png)

## Latihan 3: penggunaan kondisi OR program membandingkan 3 input bilangan, apabila penjumlahan 2 bilangan hasilnya sama dengan bilangan lainnya, maka cetak pernyataan “BENAR”

```
a = int(input('Masukkan bilangan A: '))
b = int(input('Masukkan bilangan B: '))
c = int(input('Masukkan bilangan C: '))
if a+b == c or b+c == a or c+a == b:
    print('benar')
else: print('salah')
```
Output:

![latihan3-modul2](assets/img/praktikum-2/3.png)

## Tugas Praktikum 2
![soal-praktikum-modul2](assets/img/praktikum-2/praktikum.png)

```
A = int(input('Masukkan bilangan pertama: '))
B = int(input('Masukkan bilangan kedua: '))
C = int(input('Masukkan bilangan ketiga: '))

if A > B and A > C:
    print('Nilai', A, 'terbesar dari 3 bilangan yang di inputkan')
elif B > A and B > C:
    print('Nilai', B, 'terbesar dari 3 bilangan yang di inputkan')
else:
    print('Nilai', C, 'terbesar dari 3 bilangan yang di inputkan')
```
Output:

![tugas-praktikum-modul2](assets/img/praktikum-2/5.png)

Flowchart
![flowchart-praktikum-modul2](assets/img/praktikum-2/fc-maks.png)

# Modul Praktikum 3
## Latihan 1
![latihan1-modul3](assets/img/praktikum-3/1.png)

```
import random
nilai = int(input('Masukan nilai n : '))
a = 0
for x in range (nilai):
    i = random.uniform(.0,.5)
    a+=1
    print('data ke :',a,'==>', i)
```
Penjelasan:
* ``import random`` berfungsi untuk memanggil library random, dimana random berfungsi untuk menentukan pilihan secara acak
* ``nilai = int(input('Masukan nilai n : '))`` untuk menginputkan nilai berupa integer
* range() berfungsi menghasilkan list

Output:

![latihan2.2](assets/img/lab3/2.2.png)

## Latihan 2
![latihan2-modul3](assets/img/praktikum-3/2.png)

## Tugas Praktikum 3
![program-1-modul3](assets/img/praktikum-3/3.png)

```
a= 100000000
for x in range (1,9):
    if (x>=1 and x<=2):
        b=a*0
        print("laba bulan ke-",x,": ",b)
    if (x>=3 and x<=4):
        c=a*0.1
        print("laba bulan ke-",x,": ",c)
    if (x>5 and x<=7):
        d=a*0.5
        print ("laba bulan ke-",x,": ",d)
    if (x==8):
        e=a*0.2
        print("Laba bulan ke-",x,": ",e)
total=b+b+c+c+d+d+d+e
print("\Total : ",total)
```
Output:

![program-1-out-modul3](assets/img/praktikum-3/3.1.png)
