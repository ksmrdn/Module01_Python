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

class ini:
    def __init__ (self):
        self.tanggal = i.strftime('%d') #--> tanggal
        self.day = i.strftime('%A') #--> hari
        self.hari = hari[i.strftime('%A')] #--> hari
        self.months = i.strftime('%B') #--> nama bulan
        self.bulan = bulan[i.strftime('%B')] #--> nama bulan
        self.tahun = i.strftime('%Y') #--> tahun
waktu = ini()
       