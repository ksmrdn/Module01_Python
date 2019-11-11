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
