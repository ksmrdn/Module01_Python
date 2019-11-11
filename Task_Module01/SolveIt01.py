# 01
# Solve it 1
import math
x = 4
y = 3
z = 2
v = ((x+y*z)/(x*y))
w = pow(v,z)
print(w)
print("%.2f"%w)
print(round(w,2))
print(math.floor(w))
print(math.ceil(w))

# Solve it 2
num1 = int(input("Fill your number here: "))
print (f'Your number is {num1}')
print(f'Kuadrat dari {num1} = {pow(num1,2)}')

# Solve it 3
TotalDays = int(input("How many days you want to add : "))
W = (TotalDays/7)
M = (TotalDays/30)
Y = (TotalDays/360)
print(f'{round(TotalDays,2)} same with {round(W,2)} weeks, {round(M,2)} months, or {round(Y,2)} yaers')

# Solve it 4
tU = 49
rA = 0.4
rB = 1
A = (rA*(tU/(rA+rB)))
B = tU - A
print(f'Umur Andi sanat ini adalah {int(A)} dan umur Budi saat ini adalah {int(B)}')
ftr = int(input("Masukkan berapa tahun mendatang: "))
print(f'Umur Andi di {int(ftr)} tahun mendatang adalah {int(A+ftr)}')
print(f'Umur Andi di {int(ftr)} tahun mendatang adalah {int(B+ftr)}')

# Solve it 5
kampus = 'Purwadhika Startup & Coding School berada di BSD GOP 9 menjadi salah satu Startup & Coding School tertua di Indonesia'

# jumlah huruf
print(len(kampus.replace(' ','')))
print(len(kampus))
print('\n')

# mengidentifikasi letak karakter
print(kampus.index(' '))
print('\n')

# mengidentifikasikan jumlah karakter 1
print(kampus.lower().count('g'))
print(kampus.lower().count('c'))
print('\n')

# Solve it 6
S = 120
A = 60
B = 40
V = A+B
hour = 9
hour1 = S/V
menit = S%V
Wpapasan = hour+hour1
print(f'Mobil A dan B akan berpapasan pada pukul {round(Wpapasan)} lewat {menit} menit')