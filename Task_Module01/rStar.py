#  *  *  *  *  *
#  *  *  *  *
#  *  *  *
#  *  *
#  *

# segitiga siku terbalik
star = ''
for i in range(5):
    star = ' * ' * (5-i)
    print(star)

# segitiga siku * terbalik
for i in range(5):
    for j in range(5 - i):
        print(' * ', end='')
    print()
print("=============================================================")

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# segitiga siku terbalik isi angka
angka = ''
for i in range(5):
    angka = (str(i+1) + ' ') * (5-i)
    print(angka)
print("=============================================================")

# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# 0

# segitiga siku terbalik isi angka
for i in range(5):
    for j in range(5 - i):
        print(str(j)+' ', end='')
    print()
print("=============================================================")

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# segitiga siku terbalik isi angka
angka = ''
for i in range(5):
    angka = (str(i+1) + ' ') * (5-i)
    print(angka)
print("=============================================================")

# 5 => 5 4 3 2 1
# 4 => 5 4 3 2
# 3 => 5 4 3
# 2 => 5 4
# 1 => 5

# segitiga siku terbalik isi angka
angka = ''
for i in range(5, 0, -1):
    angka = angka + str(i)
for i in range(len(angka)):
    print(angka[:len(angka)-i])
print("=============================================================")

# 5 => 1 2 3 4 5
# 4 => 1 2 3 4
# 3 => 1 2 3
# 2 => 1 2
# 1 => 1

# segitiga siku terbalik banyak angka
angka = ''
for i in range(1, 6, +1):
    angka = angka + str(i)
for i in range(len(angka)):
    print(angka[:len(angka)-i]) #print baris
print("=============================================================")

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# segitiga siku terbalik isi angka
for i in range(5):
    for j in range(5 - i):
        print(str(j+1)+' ', end='')
    print()