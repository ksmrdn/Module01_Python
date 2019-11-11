import datetime as dt
x = dt.datetime.now()

print(x)
print(x.strftime('%d')) #--> tanggal
print(x.strftime('%A')) #--> hari
print(x.strftime('%m')) #--> bulan
print(x.strftime('%B')) #--> nama bulan
print(x.strftime('%Y')) #--> tahun

print(x.strftime('%H')) #--> 24 jam
print(x.strftime('%I'+ ' %p')) #--> 12 jam + am/pm
print(x.strftime('%M')) #--> min
print(x.strftime('%S')) #--> sec

print(x.strftime('%c'))
print(x.strftime('%x'))
print(x.strftime('%X'))