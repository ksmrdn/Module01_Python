#ex 1
angka1 = 10
while (angka1 <= 10):
    print(angka1)

angka2 = 0
while (angka2 <= 20):
    print(angka2)
    angka2 += 1 
#     # ^ step  ^
print('\n')

angka3 = 20
while (angka3 >= 1):
    print(angka3)
    angka3 -= 1 
#     # ^ step  ^
print('\n')


std = ['Sopo','Kowe','Iku','Seh']
index = 0
while index <= len(std)-1:
     print(std[index])
     index += 1

numb = list(range(1,11,1))
res = list()
index = 0
while index <= len(numb)-1:
    res.append(pow(numb[index],2))
    index += 1
print(res)

a = 1
while a < 10:
    if a == 5:
        break
    a += 1
print(a)

#PW 1
pw = '070298'
inputuser = ''
i = 1
u = 3
Lebih = False
while inputuser != pw:
    inputuser = input(f'Ketik password {(i)}: ')
    if inputuser != pw:
        print('Password Salah.')
    else:
        print('Password Benar.') 

#PW 2   
while inputuser != pw and not Lebih:
    if i <= u:
        inputuser = input(f'Ketik password {(i)}: ')
        i+=1
    else:
        Lebih = True
if Lebih:
    print('Kesempatan Habis.')
else:
    print('Password Benar.') 
        
#ex 2
listItem = list(range(1,11,2))
print(listItem)

for item in listItem:
    print(item)

#ex 3
listItem = list(range(0,21,2))
print(listItem)

for item in listItem:
    print(f'Nomor urut {item}')

#ex 4
z= ' '
for item in range(0,5):
    z += ' * '
print(z)
print('\n')

#ex 5
z= ''
for item in range(0,5):
    z += ' * \n'
print(z)
print('\n')

#ex 6
z= ''
for item in range(0,5):
    z += ' *  *  *  *  * \n'
print(z)
print('\n')

#ex 7
z= ''
for item in range(0,5):
    for item in range(0,5):
        z += ' * '
    z += '\n'
print(z)
print('\n')

# #ex 8
z = ' * ' * 5
for item in range(5):
    for item1 in range(5,+item):
        z += ' * '
    z += '\n'
print(z)

#ex 9
z = ''
for item in range (5):
    for item1 in range(0, item-1):
        z -= ' * '
    z += '\n'
print(z)

#default parameter
def kali(x):
    if (x<2):
        return 1
    else:
        return (x*tiga())
def  tiga():
    return 3
print(kali(5))

#for loop
kota = ['Jakarta', 'Solo', 'Surabaya']
i = 0
while i <= len<(kota)-1:
    print(kota[i])
    i += 1
print('\n')

for i in range(len(kota)):
    print(kota[i])

for i in range(1,10):
    print(i)
    if i == 7:
        break
    print(i)

for i in range(1,10):
    # print(i)
    if i == 7:
        continue
    print(i)

for i in range(1,11):
    if i % 2 == 0:
        print('WOW')
    else:
        print(i)

for i in range(1,16):
    if i % (3*5) == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


def fizzbuzz(i):
    for i in range(1,i+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
fizzbuzz(150)

x = [1,2,3,4,5,6,7]
#1
x.reverse()
print(x)

#2
print(x[::-1])

#3
print(list(reversed(x)))

#5
#Mengganti Semua Huruf vokal tanpa replace
vocal = list('aiueo')
print(vocal)

def ubah(kalimat):
    StringAwal = ''
    for i in kalimat:
        if i in vocal:
            i = 'o'
            StringAwal += i
        else:
            StringAwal += i
    print(StringAwal)
ubah(input('Ini adalah sebuah kalimat percobaan: ').lower())

x = [1,4,56,7,9,0]
y =['Sed', 'Dih', 'Sekali']
def balikposisi(mylist):
    hasil = []
    for i in range(len(mylist)):
        hasil.insert(0, mylist[i])
    return hasil
print(balikposisi(x))
print(balikposisi(y))

def balikposisi1(mylist):
    for i in range(round(len(mylist)/2)):
        asli = mylist[i]
        mylist[i] = mylist[len(mylist)-1-i]
        mylist[len(mylist)-1-i] = asli
    return mylist
print(balikposisi1(x))
print(balikposisi1(y))

def ubahvokal(kata):
    output = ''
    for Huruf in kata:
        if Huruf in 'aiueo':
            output = output + output
        else:
            output= output + Huruf
    return output
print(ubahvokal('Mimi'))

#Palindrome
#katak = katak -> TRUE
#koding = gnidok -> FALSE
def Palindrome(kata):
    kata2 = kata.reverse()
    for kata2 in kata:
        if kata2 == kata.reverse():
            print('Palindrome')
        else:
            print('Bukan Palindrome')
Palindrome(input('Masukkan kata: ').lower())

# function to check string is 
# palindrome or not 
def isPalindrome(str): 

# Run loop from 0 to len/2 
    def palindrome2(kata):
        for i in range(round(0, len(str)/2)): 
            isPalindrome = False
            if str[i] != str[len(str)-i-1]: 
                isPalindrome = True
            else:
                isPalindrome = False
                break
        return isPalindrome
    print(palindrome2('kokok'))
    print(palindrome2('jumali'))

x = 'hahah'
y = list(x[::-1])
y = ''.join(y)
def isParam(kata):
    if y == x:
        print('TRUE')
    else:
        print('FALSE')
isParam(x)

x = 'hahah'
def isPalindrome1(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False
print(isPalindrome1(x))

kalimat = 'Hai aku Lintang'
print(''.join(kalimat.split()))