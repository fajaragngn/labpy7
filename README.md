# Lab 3
## Latihan 1
![latihan1](assets/img/lab/1.png)

```
#bilangan bertingkat(nested)
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

![latihan1.1](assets/img/lab/1.1.png)

![latihan2](assets/img/lab/2.png)

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

![latihan2.2](assets/img/lab/2.2.png)

# Modul Praktikum 2
## Latihan 1: Membuat program menentukan nilai akhir
```
#Membuat program menentukan nilai akhir
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