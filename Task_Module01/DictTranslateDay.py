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