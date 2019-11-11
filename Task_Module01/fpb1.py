num1 = 6
num2 = 9
def BesarKecil(num1, num2):
    if num1 > num2:
        Besar = num1
        Kecil = num2
    else:
        Besar = num2
        Kecil = num1
    return Besar, Kecil

def FPB(num1, num2):
    Besar, Kecil = BesarKecil(num1, num2)
    for i in range(1, Kecil):   
        if Besar % Kecil == 0:
            print(f'FPB dari bilangan {Besar} dan {Kecil} adalah {Kecil}')
            break
        else:
            if Kecil % (Kecil-i) == 0 and Besar % (Kecil-i) == 0:
                Hasil = Kecil-i
                print(f'FPB dari bilangan {Besar} dan {Kecil} adalah {Hasil}')
                break
FPB(num1,num2)

