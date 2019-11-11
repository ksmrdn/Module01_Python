num0 = 12
golongan = []
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
print(prima(num0))

if type(num0) == int:
    golongan.append('Bulat')
    if num0 >= 0:
        golongan.append('Cacah')
    if num0 > 0:
        golongan.append('Asli')
        if num0 % 2 == 0:
            golongan.append('Genap')
        elif num0 % 2 != 0:
            golongan.append('Ganjil')
if prima(num0) == True:
    golongan.append('Prima')
else:
    golongan.append('Komposit')  
if num0 < 0:
    golongan.append('Negatif')
elif num0 == 0:
    golongan.append('Nol')


print(golongan)

    