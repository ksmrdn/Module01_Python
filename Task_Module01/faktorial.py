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