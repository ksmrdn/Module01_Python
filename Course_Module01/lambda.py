#lambda function --> function x {return x * x}
#satu expression saja 
#satu line
x = lambda a : a
print(x(2))
print('==============================================================================')

y = lambda a,b,c : a+b+c
print(y(4,7,1))
print('==============================================================================')

z = lambda a,b,c : a/b+c
print(z(10,5,1))
print('==============================================================================')

#lambda in function 
def myFunction(b):
    return lambda a : a**b #--> a = notasi angka, b = notasi berpangkat 
pangkat0 = myFunction(0)
pangkat5 = myFunction(5)
pangkat11 = myFunction(11)

print(pangkat0(120))
print(pangkat5(5))
print(pangkat11(42))
print('==============================================================================')

x = lambda a: True if a%2 == 0 else False
print(x(7))

def k(a):
    if a%2 == 0:
        return True
    else:
        return False
print(k(7))
print('==============================================================================')

x = lambda a: print(a)
x('This is lambda expression. '*2)
print('==============================================================================')

#map
#mengeksekusi sebuah spesifik function untuk setiap element varibale yg ditreble (str, list)

def l(a):
    return len(a)
a = ['Brotoseno', 'Poliandri', 'Seseno']
x = map(l, a)
print(list(x))
print('==============================================================================')
#bilangan berpangkat 2
r = [2, 4, 6, 8, 10]
def myFunction1(w):
    return w**2
i = map(myFunction1, r)
print(list(i))

e = map(lambda a: a**2, r)
print(list(e))

d = []
for t in r:
    d.append(t**2)
print(d)

w = list(map(pow, [2,3],[4,5]))
print(w)
print('==============================================================================')

f = range(11)
def kurangLima(x):
    if x < 5:
        return False
    else:
        return True
y = filter(kurangLima, f)
print(list(y))

n = filter(lambda a: True if a >= 5 else False, f)
print(list(n))
print('==============================================================================')

h = [1, 2+2, 6, 7, 10, 12-1, 86]
j = [3+1, 5, 7, 9, 12-2, 24, 867]
k = list(filter(lambda a: a in h, j))
print(k)
print('==============================================================================')

#reduce semua element dipakai
j = [1,2,3,4]
hasil = 1
for i in j:
    hasil *= i
print(hasil)

from functools import reduce
res0 = reduce(lambda a, b: a*b, j)
print(res0)

kata = ['Tahu','Bulat','500-an']
print(" ".join(kata) + '.')

from functools import reduce
pair0 = reduce(lambda a, b: a + b, kata)
print(pair0 + '.')
print('==============================================================================')

#lambda in lambda
num = [1,2,3,4]
ab = list(map(lambda a: a*2, filter(lambda a: a>3, num)))
cd = list(filter(lambda a: a>3, map(lambda a: a*2, num)))
print(ab, cd)
print('==============================================================================')

#list 1-100 --> angka genap --> x2 --> total
num1 = list(range(2,102,2))
print(num1)
ab = list(map(lambda a: a*2, num1))
print(ab)
from functools import reduce
tot1 = reduce(lambda a, b: a+b, ab)
print(tot1)

# #list 0-100
# num2 = list(range(1,101))
# print(num2)
# ac = list(filter(lambda a: ,num2))
# print(ac)