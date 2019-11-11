num1 = 9
num2 = 6
def BesarKecil(num1, num2):
    if num1 > num2:
        Besar = num1
        Kecil = num2
    else:
        Besar = num2
        Kecil = num1
    return Besar, Kecil

def KPK(num1, num2):
    Besar, Kecil = BesarKecil(num1, num2)
    kelipatanBesar = 0
    if Besar % Kecil == 0:
        print(f'KPK dari bilangan {Besar} dan {Kecil} adalah {Besar}')
    else:
        for i in range(1, Kecil+1):   
            kelipatanBesar += Besar
            if kelipatanBesar % Kecil  == 0:
                print(f'KPK dari bilangan {Besar} dan {Kecil} adalah {kelipatanBesar}')
                break
KPK(num1,num2)