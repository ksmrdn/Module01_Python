#Membuat class
#Berisi mean, median, modus
#Tanpa menggunakan import statistic
#obj dibuat pada file py lain

#Mean = sum(variable)/len(variable)
#Median jika banyak bilangan ganjil --> sort --> indeks[len(variable)/2+0.5]
       #jika banyak bilangan genap --> sort --> (indeks[len(variable)/2] + indeks[len(variable)/2]+1) / 2
#Modus menggunakan count i
# import math
# x = [3, 4, 5, 6, 1, 9, 10, 2, 8, 7, 7]
# self.mean = sum(x)/len(x)
# y = list(sorted(x))
# print(y)

# if len(y)%2 != 0:
    # med = [int[len(y)/2]]
# else:
#     med0 = y[len(y)/2])
#     med1 = y[(len(y)/2)+1]
#     med = int((med0+med1)/2)
#     print(med)

# for i in x:
    
print('==============================================================================')
from functools import reduce
class statistik:
    def rata2(self, x):
        totMean = reduce(lambda a, b: a+b, x)
        return totMean/len(x)
    def nilaiTengah(self, x):
        x.sort()
        if len(x)%2 != 0:
            iTengah = [int(len(x)/2)]
        else:
            iTengah = [int(len(x)/2)-1, int(len(x)/2)]
        aTengah = list(map(lambda a: x[a], iTengah))
        totMed = reduce(lambda x,y: x+y, aTengah)
        return totMed/len(aTengah)
    def modus(self, x):
        x = sorted(x)
        print(x)
        print(type(x))
        xs = list(set(x))
        print(xs)
        most = list(map(x.count, xs))
        print(most)
        maxm = max(most)
        print(maxm)
        t = most.index(maxm)
        print(t)
        print(xs[t])
# objM = statistik()
# print(objM.rata2)

stats = statistik()
print(stats.rata2([3,6,7,1,4,2,10,7,3,1,7]))
print(stats.nilaiTengah([3,6,7,1,4,2,10,7,3,1,7]))
print(stats.modus([3,6,7,1,4,2,10,7,3,1,7]))