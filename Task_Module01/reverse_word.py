#Membuat kata terbalik dengan for loop
def reverse(s):
    kal = "" 
    for i in s: 
	    kal = i + kal
    return kal
s = "Dunia Terbalik"
print (f'The original string is : {s}') 
print (f'The reversed string is : {reverse(s)}')
print('\n')

#Membuat kata terbalik dengan slicing
a = "Dunia Terbalik"
ax = a[::-1]
print(f'The original string is : {a}')
print(f'The reversed string is : {ax}')
print('\n')

#Membuat huruf terbalik dalam beberapa kata dalam satu kalimat 
kalimat = 'Dunia Terbalik Begitu Saja'
i = 0
# kalimat = (' '.join(kalimat.split()))
splits = kalimat.split()
print(kalimat)
print(splits)
print(type(splits))
mem = ""
while i <= len(splits)-1: 
# print(splits[0][::-1])
    rev = splits[i][::-1]
    i += 1
    mem += rev + ' '
print(mem.strip())
print(type(mem))