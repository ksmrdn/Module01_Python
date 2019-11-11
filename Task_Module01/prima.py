# Program python untuk menentukan bilangan prima atau tidak
# Meminta input bilangan dari user
num = int(input("Masukkan bilangan: "))
# bilangan prima harus lebih besar dari 1
if num > 1:
    for i in range(2,num):
        # print(i)
        if (num % i) == 0:
            print(num, "bukan bilangan prima")
            print(i, "kali", num//i, "=", num)
            break
    else:
        print(num,"adalah bilangan prima")
# bila bilangan kurang atau sama dengan satu
else:
    print(num, "bukan bilangan prima")
print('==============================================================================')

#bilangan prima memakai lambda
# num1 = list(filter(num, range(101)))

def prima(x):
    if x > 1:
        if x == 2:
            a = True
        else:
            for i in range(2,x):
                if x % i == 0:
                    a = False
                    break
            else:
                a  = True
    else:
        a = False
    return a
print(prima(5))
z = list(filter(prima,range(101)))
print(z)
print('==============================================================================')

primelist = lambda n : [x for x in range(2, n) if not 0 in map(lambda z : x % z, range(2,x))]
print(", ".join(map(str, primelist(100))))