x = 'AbcdEFgHi'
print(x)
x = list(x)
print(x)
y = []
for i in x:
    # print(i)
    if i.isupper() == True:
        # print(i)
        i = i.lower()
        y.append(i)
    elif i.islower() == True:
        i = i.upper()
        y.append(i)
print(y)
x = ''.join(y)
print(x)
        
