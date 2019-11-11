massa = float(input('Masukkan massa anda: '))
tinggi = float(input('Masukkan tinggi anda: '))
tinggi = float(tinggi/100)
print(f'Massa anda {massa} kg & tinggi anda {tinggi} m.')
IMT = float(massa/tinggi**2)
if IMT < 18.5:
    print(f'IMT = {round(IMT,4)}')
    print(f'Berat badan kurang.')
elif 18.5 <= IMT <= 24.9:
    print(f'IMT = {round(IMT,4)}')
    print(f'Berat badan ideal.')
elif 25.0 <= IMT <= 29.9:
    print(f'IMT = {round(IMT,4)}')
    print(f'Berat badan berlebih.')
elif 30.0 <= IMT <= 39.9:
    print(f'IMT = {round(IMT,4)}')
    print(f'Berat badan sangat berlebih.')
elif IMT > 39.9:
    print(f'IMT = {round(IMT,4)}')
    print(f'Obesitas')
else:
    print(f'Invalid input!')  