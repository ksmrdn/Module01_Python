pw = '070298'
i = 1
u = 3
Lebih = False

#CODING TANPA LIMIT
# while inputuser != pw:
#     inputuser = input(f'Ketik password {(i)}: ')
#     if inputuser != pw:
#         print('Password Salah.')
#     else:
#         print('Password Benar.') 

# inputuser = input('Ketik password: ')

# if inputuser != pw:

#CODING DENGAN LIMIT 1
inputuser= input(f'Ketik password {(i)}: ')
# while inputuser != pw and not Lebih:
#     if i <= u:
#         print('Password salah.')
#         inputuser = input(f'Ketik password {(i+1)}: ')
#         i+=1
#     else:
#         Lebih = True
# if Lebih:
#     print('Password salah.')
#     print('Kesempatan Habis.')
# else:
#     print('Password Benar.') 

#CODING DENGAN LIMIT 2
state = False
while state == False:
    if inputuser == pw:
        print('Password Benar.')
        break
    elif inputuser != pw and u > 0:
        print('Password salah.')
        inputuser = input(f'Ketik Password {(i+1)}:')
        i+=1
        u -= 1
    else:
        print('Password salah. Kesempatan habis.')
        break
