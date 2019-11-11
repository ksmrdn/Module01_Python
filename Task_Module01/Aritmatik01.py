#Solve it extra
numHeads = int(input("Total of animals are "))
totLegs = int(input("Total of animals legs are "))
LegsA = int(input("Animal A legs are "))
LegsB = int(input("Animal B legs are "))
numB = (totLegs-(numHeads*LegsB))/LegsB
numB = (totLegs - (LegsA*numHeads))/(LegsB - LegsA)
print(f'Total of A are {int(numHeads-numB)} and B are {int(numB)}')

#soal ekstra 2
ThnLampau = -19
selisihdariAndi0 = - 1/2
selisihdariAndi1 = 19
rasio0 = 4
rasio1 = 7
y = (ThnLampau*rasio1) + (selisihdariAndi0*(rasio0*rasio1))
Ibu = y/(rasio0-rasio1)
Andi = selisihdariAndi1+Ibu/7
IbuLahirkan = Ibu - Andi
print(f'Umur Ibu sekarang {int(Ibu)}')
print(f'Umur Andi sekarang {int(Andi)}')
print(f'Umur Ibu saat melahirkan Andi {int(IbuLahirkan)}')

#Soal ekstra 3
tU = 50
rasioAyah = 6
rasioAndi = 1
tahunlalu = 4
# Ayah - 4 = 6*(Andi -4)
# Ayah = 6*((tU - Ayah)-24) + 4
# Ayah = 6*tU - 6*Ayah - 24 + 4
# 7*Ayah = 6*tU - 20
# Ayah = (6*tU - 20)/7
Ayah = (rasioAyah*tU-rasioAyah*tahunlalu+tahunlalu)/(rasioAyah+rasioAndi)
Andi = tU - Ayah
print(f'Umur Ayah adalah {int(Ayah)} dan umur Andi adalah {int(Andi)}')

import math
numHeads = 13
totLegs = 32
LegsG = 4 
LegsC = 2
numChicks = (totLegs-(numHeads*LegsC))/LegsC
print(f'Total of chickens are {numHeads-numChicks} and goats are {numChicks}')

numHeads = 13
totLegs = 52
LegsG = 4 
LegsC = 4
numCows = ((totLegs-(numHeads*LegsC))/LegsC)
print(f'Total of Goats are {numHeads-numCows} and cows are {numCows}')

numHeads = int(input("Total of animals are "))
totLegs = int(input("Total of animals legs are "))
LegsA = int(input("Animal A legs are "))
LegsB = int(input("Animal B legs are "))
numB = (totLegs-(numHeads*LegsB))/LegsB
print(f'Total of A are {int(numHeads-numB)} and B are {int(numB)}')