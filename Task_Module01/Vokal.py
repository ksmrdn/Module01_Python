#Mengganti Semua Huruf vokal tanpa replace
vocal = list('aiueo')
print(vocal)

def ubah(kalimat):
    StringAwal = ''
    for i in kalimat:
        if i in vocal:
            i = 'o'
            StringAwal += i
        else:
            StringAwal += i
    print(StringAwal)
ubah(input('Ini adalah sebuah kalimat percobaan: ').lower())

def ubahvokal(kata):
    output = ''
    for Huruf in kata:
        if Huruf in 'aiueo':
            output = output + output
        else:
            output= output + Huruf
    return output
print(ubahvokal('Mimi'))

#function 11
def vocal2(kal):
    if 'a' or 'i' or 'u' or 'e' in kal:
        print(kal.replace('a','o'))
        print(kal.replace('i','o'))
        print(kal.replace('u','o'))
        print(kal.replace('e','o'))
    else:
        print(kal)
vocal2(str(input('Masukkan sebuah kata: ')))

def vocal1(kal):
   kal = kal.lower()
   kal = kal.replace('a','o')
   kal = kal.replace('i','o')
   kal = kal.replace('u','o')
   kal = kal.replace('e','o')
   print(kal)
vocal1(str(input('Masukkan sebuah kata: ')))