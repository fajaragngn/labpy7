# Lab 3
## Latihan 1
![latihan1](assets/img/lab3/1.png)

![code-1](assets/img/code/code-1.png)

Penjelasan:


Output:

![latihan1.1](assets/img/lab3/1.1.png)

## Latihan 2
![latihan2](assets/img/lab3/2.png)

![code-2](assets/img/code/code-2.png)

Penjelasan:
* ``import random`` berfungsi untuk memanggil library random, dimana random berfungsi untuk menentukan pilihan secara acak
* ``nilai = int(input('Masukan nilai n : '))`` untuk menginputkan nilai berupa integer
* range() berfungsi menghasilkan list
* masukkan ``i = random.uniform (.0,.5)`` di gunakan untuk menampilkan bilangan float random, lalu masukkan a+=1 untuk memberi nomer pada bilangan float.
* ``print('data ke :',a,'==>', i)`` untuk menampilkan output data

Output:

![latihan2.2](assets/img/lab3/2.2.png)

# Modul Praktikum 2
## Latihan 1: Membuat program menentukan nilai akhir

![code-1-2](assets/img/code/code-1-2.png)

Penjelasan:
* Masukkan nilai yang sudah di tentukan oleh variabel, seperti ``nama, uts, uas,tugas``
* untuk ``akhir = (int(tugas) * .2) + (int(uts) * .4) + (int(uts) * .4)``
* ``if akhir > 80:`` Jika nilai akhir diatas 80, maka ``huruf = 'A'``
* ``elif akhir > 70:`` dan jika nilai akhir diatas 70, maka ``huruf = 'B'``
* ``elif akhir > 50:`` dan jika nilai akhir diatas 50, maka ``huruf = 'C'``
* ``elif akhir > 40:`` dan jika nilai akhir diatas 40, maka ``huruf = 'D'``
* ``else:`` selain itu maka ``huruf = 'E'``
* cetak nilai akhir ``print``


Output:

![latihan1-modul2](assets/img/praktikum-2/1.png)

## Latihan 2: Membuat program menampilkan status gaji karyawan

![code-2-2](assets/img/code/code-2-2.png)

Penjelasan:
* ``gaji = int(input("Masukkan gaji:"))`` masukkan jumlah gaji
* ``if gaji > 3000000:`` jika gaji diatas 3jt, maka ``print ("Gaji sudah diatas UMR")`` jika tidak, maka ``else: print("Gaji belum UMR")`` dan juga pengkondisian yang lainnya
* maka data akan di cetak sesuai data yang di isi

Output:

![latihan2-modul2](assets/img/praktikum-2/2.png)

## Latihan 3: penggunaan kondisi OR program membandingkan 3 input bilangan, apabila penjumlahan 2 bilangan hasilnya sama dengan bilangan lainnya, maka cetak pernyataan “BENAR”

![code-2-2](assets/img/code/code-3-2.png)

Penjelasan:
* ``a = int(input('Masukkan bilangan A: '))`` Masukkan bilangan A pada saat runtime, lakukan juga pada bilangan B dan C
* ``if a+b == c or b+c == a or c+a == b:`` jika a+b = c atau b+c = a atau c+a = b maka ``print('benar')``
* selain itu maka ``else: print('salah')``

Output:

![latihan3-modul2](assets/img/praktikum-2/3.png)

## Tugas Praktikum 2
![soal-praktikum-modul2](assets/img/praktikum-2/praktikum.png)

![code-3-2](assets/img/code/code-3.png)

Penjelasan:
* ``A = int(input('Masukkan bilangan pertama: '))`` masukkan nilai bilangan pertama, dan lakukan juga pada bilangan kedua dan ketiga pada saat runtime
* ``if A > B and A > C:`` jika A lebih besar dari B dan A lebih besar dari C maka ``print('Nilai', A, 'terbesar dari 3 bilangan yang di inputkan')``
* ``elif B > A and B > C:`` dan jika B lebih besar dari A dan B lebih besar dari C maka ``print('Nilai', B, 'terbesar dari 3 bilangan yang di inputkan')``
* ``else:`` selain itu maka ``print('Nilai', C, 'terbesar dari 3 bilangan yang di inputkan')``

Output:

![tugas-praktikum-modul2](assets/img/praktikum-2/5.png)

Flowchart
![flowchart-praktikum-modul2](assets/img/praktikum-2/fc-maks.png)

# Modul Praktikum 3
## Latihan 1
![latihan1-modul3](assets/img/praktikum-3/1.png)

![code-1-3](assets/img/code/code-1-3.png)

Penjelasan:
* ``import random`` berfungsi untuk memanggil library random, dimana random berfungsi untuk menentukan pilihan secara acak
* ``nilai = int(input('Masukan nilai n : '))`` untuk menginputkan nilai berupa integer
* range() berfungsi menghasilkan list
* masukkan ``i = random.uniform (.0,.5)`` di gunakan untuk menampilkan bilangan float random, lalu masukkan a+=1 untuk memberi nomer pada bilangan float.
* ``print('data ke :',a,'==>', i)`` untuk menampilkan output data

Output:

![latihan2.2](assets/img/lab3/2.2.png)

## Latihan 2
![latihan2-modul3](assets/img/praktikum-3/2.png)

![code-2-3](assets/img/code/code-2-3.png)

Penjelasan:
* Integer max = 0

* fungsi perulangan ``while true`` hingga menampilkan perulangan sampai batas tertentu.

* Memasukan bilangan integer pada "a"

* Menggunakan fungsi ``if`` jika max kurang dari nilai a, maka max sama dengan a

* Mengunakan fungsi ``if`` jika nilai a adalah 0 maka fungsi ``break`` artinya perulangan berhenti jika menulis nilai 0

* Mencetak nilai paling terbesar setelah ``break``, sehingga menampilkan nilai terbesar diantara bilangan tersebut dalam perulangan.

Output:

![latihan-2-out-modul3](assets/img/praktikum-3/2.1.png)


## Tugas Praktikum 3
![program-1-modul3](assets/img/praktikum-3/3.png)

![code-3-3](assets/img/code/code-3-3.png)

Penjelasan:
* Variabel ``a = 100.000.000`` modal awal

* Menggunakan fungsi looping for pada nilai x 1-9 untuk menampilkan bulan 1 sampai bulan 8.

* Menggunakan fungsi ``if``, untuk menghitung laba bulan 1 sampai 8

* Bulan pertama dan kedua laba adalah 0

* Bulan ke 3 dan ke 4 mendapat laba 1% sehingga modal di kali 1% = keuntungan

* Bulan ke 5 mendapatkan laba 5%, sehingga modal dikali 5% = keuntungan

* Bulan ke 8 mendapatkan laba 2% sehingga keuntungan menurun dari bulan sebelumnya, modal dikali 2% = keuntungan.

* Menghitung jumlah total laba dengan menjumlah keuntungan dari bulan ke 1 sampai bulan 8, hasilnya adalah total keuntungan yang didapat ``total=b+b+c+c+d+d+d+e``

* ``print("\Total : ",total)``, untuk menampilkan hasil keseluruhan laba dari bulan pertama sampai bulan kedelapan.

Output:

![program-1-out-modul3](assets/img/praktikum-3/3.1.png)
