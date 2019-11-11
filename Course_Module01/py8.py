def Star(x):
    star = ''    
    for i in range(x):
        star = ' * ' * i
        print(star)
Star(5)

def rStar(x):
    star = ''    
    for i in range(x):
        star = ' * ' * (x-i)
        print(star)
rStar(5)

print('\n')
def nStar(x):
    star = ''    
    for i in range(1, x+1):
        star += str(i) + ' '
        print(star)
nStar(5)

def uStar(x): 
    h = x+1
    for i in range(1, h):
        star = ''
        for j in range(1, (h-i)):
            star += str(j) + ' '
        print(star)
uStar(5)

def xStar(x):
    star = ''    
    for i in range(5, 0, -1):
        star += str(i) + ' '
        print(star)
xStar(5)

