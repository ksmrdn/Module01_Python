# x = ['Andi', 'Koko', 'Redo']
# for i in x:
#     print(i)

# x = [[1,2,3],[4,5,6],[7,8,9]]
# for i in x:
#     for j in i:
#         print(j)

# for i in range(5):
#     for j in range(7,9):
#         print(i, 'dan', j)

#a ^ b = c
a = 4  #jadi bilangan yang dikali dan pengali
b = 2  #jadi jumlah perkalian
for i in range(b-1):
    for j in range(a,b):
        a *= a
print(a)

def pangkat(a,b):
    out = 1 
    for i in range(b):
        out *= a
    print(out)
pangkat(4,2)

def pangkat1(c,d):
    if(d == 1):
        return c
    else:
        return c*pangkat1(c, d-1)
print(pangkat1(2,3))

def pangkat2(q,w):
    r = q
    for i in range(w-1):
        r *= q
    print(r)
pangkat2(4,2) 

import math
print(math.factorial(3))

#0! = 1
#1! = 1
#2! = 2x1 = 2
#3! = 3x2x1 = 6
def faktorial(a):
    e = 1
    for b in range(1, a+1):
        e *= b
    return e
print(faktorial(3))

def faktorial1(x):
    if x <= 2:
        return x
    else: 
        return x * faktorial1(x-1)
print(faktorial1(4))