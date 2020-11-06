## Lab 3
## Latihan 1
![latihan 1](assets/img/lab-3/1.png)

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
