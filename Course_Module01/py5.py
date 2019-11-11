Biodata = {
    'Nama': 'Rachmad',
    'Usia': 21,
    'Lahir': 'Mojokerto',
    'Sudah_Menikah': 'False',
    'Kesukaan': 'Kamu',
    'Hobby': ['Kuliner','Basket','Jogging'],
    'Kendaraan':['Jalan Kaki', 'Mio J','Mercikel'],
    'Alamat':{
        'Jalan': 'Semarang',
        'Blok': 'A 28',
        'RT': 4,
        'RW': 4,
        'Keluruhan': 'Bubutan',
        'Geo':{
            'Lat': 653.9,
            'Long': 9272
        }
    }
}
print(Biodata['Nama'])
print(Biodata['Usia'])
print(Biodata['Lahir'])
print(Biodata['Sudah_Menikah'])
print('\n')
print(Biodata.get('Nama'))
print(Biodata.get('Usia'))
print(Biodata.get('Lahir'))
print(Biodata.get('Sudah_Menikah'))
print(Biodata.get('job', 'Pengacara'))
# print(Biodata['job']) -> Akan error
print(Biodata.get('Kesukaan', 'Bukan Kamu'))
print(type(Biodata))
Biodata['name'] = 'Kusumardana'
print(Biodata.get('Hobby'))
print(Biodata['Hobby'][1])
print(Biodata['Alamat']['Geo']['Lat'])
Biodata.update({'No.KTP':357813070298005})
print(Biodata)
print(list(Biodata))
print(list(Biodata.keys())) #atribut dat
print(list(Biodata.values()))

days = {'senin': 'monday', 'selasa': 'tuesday','rabu': 'wednesday','kamis':'thrusday',
   'jumat':'friday', 'sabtu':'saturday', 'minggu': 'sunday'}

#id-eng
indo = input('Ketik nama hari: ')
print(f'Bahasa inggris dari {indo.upper()} adalah {days.get(indo.lower(), "Invalid")}')

#eng-id
ind = list(days)
eng = list(days.values())
eng1 = input('Type the day: ')
ind1 = ind[eng.index(eng1.lower())]
print(f'Bahasa indonesia dari {eng1.lower()} adalah {ind1, "Invalid"}')

jomblo = True
nganggur = False

if jomblo and nganggur:
    print('Anda kebangetan')
elif jomblo and not nganggur:
    print('Iya jomblo tok!')
elif not jomblo and nganggur:
    print('Anda bucin')
else:
    print('Anda Bahagia')

nilai = 98
if 72<= nilai <= 100:
    print("Lulus gaes!")
elif 40 <= nilai < 72:
    print("Remidi gaes!")
elif nilai < 40:
    print("Tidak lulus!") 

x = {1: True, 2: False}
print(list(x.items()))

days = {'senin': 'monday', 'selasa': 'tuesday','rabu': 'wednesday','kamis':'thrusday',
         'jumat':'friday', 'sabtu':'saturday', 'minggu': 'sunday'}
ind = list(days)
eng = list(days.values()) 
x = input("Hari apa/ What is the day: ")
if x.lower() in ind:
    engDay = eng[ind.index(x.lower())]
    print(f'Bahasa inggris dari {x.lower()} adalah {engDay}')
else:
    idHari = ind[eng.index(x.lower())]
    print(f'Bahasa indonesia dari {x.lower()} adalah {idHari}')