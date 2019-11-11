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