max = 0
while True:
    a = int(input('Masukkan bilangan: '))
    if max < a :
        max = a
    if a == 5:
        break
print('Bilangan terbesar adalah =', max)