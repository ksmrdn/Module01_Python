#KonversiNilai
nilai = 98
if 72<= nilai <= 100:
    print("Lulus gaes!")
elif 40 <= nilai < 72:
    print("Remidi gaes!")
elif nilai < 40:
    print("Tidak lulus!") 
print("========================================")

#Ganjil-Genap
nilai1 = 37
if nilai1 % 2 == 0:
    print("Bilangan Genap")
else:
    print("Bilangan Ganjil")

#function 5
def gangen(x): 
    if int(x % 2 == 0): 
        print(f'{x} = Bilangan Genap.')
    else:
        print(f'{x} = Bilangan Ganjil.')
gangen(int(input('Ketikkan angka: ')))

#default parameter
def kali(x):
    if (x<2):
        return 1
    else:
        return (x*tiga())
def  tiga():
    return 3
print(kali(5))

