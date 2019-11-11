import datetime as dt
i = dt.datetime.now()

hari = {
        'Monday' : 'Senin',
        'Tuesday' : 'Selasa',
        'Wednesday' : 'Rabu',
        'Thrusday' : 'Kamis',
        'Friday' : 'Jum\'at',
        'Saturday' : 'Sabtu',
        'Sunday' : 'Minggu'
}

bulan = {
        'January' : 'Januari',
        'February' : 'Pebruari',
        'Maret' : 'March',
        'April' : 'April',
        'May' : 'Mei',
        'June' : 'Juni',
        'July' : 'Juli',
        'August' : 'Agustus',
        'September' : 'September',
        'October' : 'Oktober',
        'November' :  'Nopember',
        'December' : 'Desember'
}

print(i)
print(i.strftime('%d')) #--> tanggal
print(i.strftime('%A')) #--> hari
print(hari[i.strftime('%A')]) #--> hari
print(i.strftime('%m')) #--> bulan
print(i.strftime('%B')) #--> nama bulan
print(bulan[i.strftime('%B')]) #--> nama bulan
print(i.strftime('%Y')) #--> tahun

# print(i.strftime('%H')) #--> 24 jam
# print(i.strftime('%I'+ ' %p')) #--> 12 jam + am/pm
# print(i.strftime('%M')) #--> min
# print(i.strftime('%S')) #--> sec

# print(i.strftime('%c'))
# print(i.strftime('%x'))
# print(i.strftime('%X'))