# Class = Cetakan object
class Mobil():
    Warna = 'merah'
    Tahun = 2012

#create object Mobil 1
mobil1 = Mobil()
print(mobil1)
print(type(mobil1))
print(mobil1.Warna)
print(mobil1.Tahun)
print('==============================================================================')

class X:
    def __init__(self, name, age):
        self.nama = name
        self.usia = age
    def pensiun(self):
        return 55 - self.usia

objX = X('Beni', 22)
print(objX.pensiun())
objY = X('Lolo', 24)
print(objY.pensiun())
print('==============================================================================')

class MobilCustom():
    def __init__(self, warna, tahun):
        self.color = warna
        self.year = tahun
mobil1 = MobilCustom('pink', 2014)
mobil2 = MobilCustom('red', 2006)

print(mobil1.color)
print(mobil2.year)
print('==============================================================================')

class MobilCustom1():
    def __init__(self, warna, tahun, model):
        self.color = warna
        self.year = tahun
        self.model = model
mobil3 = MobilCustom1('pink', 2014, 'X')
mobil4 = MobilCustom1('red', 2006, ['a','b'])

print(mobil3.color)
print(mobil4.year)
print(mobil4.model)
print('==============================================================================')

class MobilCustom2():
    def __init__(self, warna, tahun, model):
        self.color = warna
        self.year = tahun
        self.model = model

    def old(self):
        if self.year < 2010:
            return True
        else:
            return False

mobilA = MobilCustom2('Biru',1998,'CX')
print(mobilA.old())
print('==============================================================================')

class MobilCustom3():
    def __init__(self, warna, tahun, model):
        self.color = warna
        self.year = tahun
        self.model = model

    def old(self):
        if self.year < 2010:
            return True
        else:
            return False

    def tes(self):
        print(self.color, self.year, self.model, self.old())

mobilA = MobilCustom3('Biru',1998,'CX')
print(mobilA.old())
mobilA.tes()
print('==============================================================================')

class Mobil:
    def __init__(self, warna, seat):
        self.warna = warna
        self.seat = seat

class Car(Mobil): #Iheritance
    pass

mobilB = Mobil('Brown', 7)
carA = Car('Black', 10)
print(mobilB.warna, mobilB.seat)
print(carA.warna, carA.seat)
print('==============================================================================')

class Mobil1:
    def __init__(self, warna, seat):
        self.warna = warna
        self.seat = seat

class Car1(Mobil1): #Iheritance
    gps = True

mobilC = Mobil1('Brown', 7)
carB = Car1('Black', 10)
print(mobilC.warna, mobilC.seat)
print(carB.warna, carB.seat, carB.gps)
print('==============================================================================')

class Mobil2:
    def __init__(self, warna, seat):
        self.warna = warna
        self.seat = seat

class Car2(Mobil2): #Iheritance
    gps = True
    def __init__(self, soundsys):
        self.soundsys = soundsys

mobilD = Mobil1('Brown', 7)
carC = Car1('Black', 10)
print(mobilC.warna, mobilC.seat)
print(carB.warna, carB.seat, carB.gps)
print('==============================================================================')

class x:
    def __init__(self, nama, gelar):
        self.nama  = nama
        self.gelar = gelar
        
# class y(x):                             #--> 1
#     def __init__(self, nama, gelar):
#         x.__init__(self, nama, gelar)

# class y(x):                             #--> 2
#     pass

class y(x):                               #--> 3
    def __init__(self, nama, gelar, pt):
        super().__init__(nama,gelar)
        self.kampus = pt
        self.gender = 'Laki-laki' #--> Tidak perlu di taruh dalam atribut

objx = x('Arnold', 'A.Md')
objy = y('Redo','S.ST','ITS')
objz = objy
print(objx.gelar)
print(objy.kampus)
print(getattr(objy,'nama'))
print(hasattr(objy,'kampus'))
objy.hobby = 'Mancing Perkoro'
setattr(objy,'alamat','BSD')

# from pprint import pprint #--> 1
# pprint(vars(objy))
print(vars(objy)) #--> 2
print(vars(objz))
# print(objy.__dict__) #--> 3
delattr(objy,'hobby')
print(vars(objy))
print('==============================================================================')

class Z:
    nama = 'Rachmad'
    usia = '21'
objz = Z()
print(objz.nama)
print(objz.usia)

del Z.nama
# print(objz.usia, objz.nama)
print('==============================================================================')

class std:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

data = [
    {'nama': 'Andi', 'usia': '26'},
    {'nama': 'Budi', 'usia': '25'},
    {'nama': 'Caca', 'usia': '24'},
    {'nama': 'Deni', 'usia': '23'}
    ]

def createObj(e):
    nama = e['nama']
    vars()[nama] = std(e['nama'], e['usia'])
    return vars()[nama]
# dataNew = list(map(createObj, data))
# print(dataNew[0].nama)
# print(dataNew[0].usia)

dataNew = list(map(lambda e: std(e['nama'], e['usia']), data))
print(dataNew[0].nama)
print(dataNew[2].usia)
print('==============================================================================')

nama = 'jasjus'
vars()[nama] = 12345
print(jasjus)

class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
        self.keliling = self.sisi * 4
        self.luas = self.sisi ** 2
PersegiA = Persegi(4)
PersegiB = Persegi(5)
print(vars(PersegiB))
print('==============================================================================')

#Multilevel Inheritance
class a:
    def __init__(self, nama, gelar):
        self.nama  = nama
        self.gelar = gelar

class b(a):                            
    def __init__(self, nama, gelar, pt):
        a.__init__(self, nama, gelar)
        self.kampus = pt
        self.gender = 'Laki-laki' #--> Tidak perlu di taruh dalam atribut

class c(b):
    def __init__(self, nama, gelar, pt, semester):
        b.__init__(self, nama, gelar, pt)
        self.semester = semester

obja = a('Andai','A.Md')
objb = b('Uus','S.Sos','UNAIR')
objc = c('Hendro','M.Sc','Cambridge','3')
print(vars(obja))
print(vars(objb))
print(vars(objc))
print('==============================================================================')

#Multiple Inheritance
class Karnivora:
    def __init__(self): #--> tidak perlu pembubuhan atribut
        self.daging = True
        self.jenis = 'Karnivora'

class Herbivora:
    def __init__(self):
        self.tumbuhan = True
        self.jenis = 'Herbivora'

class Omnivora(Karnivora, Herbivora):
    def __init__(self): #--> nektar tidak perlu dimasukkan sebagi atribut
        Karnivora.__init__(self)
        Herbivora.__init__(self)
        self.nektar = True
        self.jenis = 'Omnivora'

objK = Karnivora()
objH = Herbivora()
objO = Omnivora()
print(Omnivora.__mro__)
print(vars(objK))
print(vars(objH))
print(vars(objO))
print('==============================================================================')