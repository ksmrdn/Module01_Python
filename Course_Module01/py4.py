x = 12
x = 14
x += 3 #x=x+3
x -= 3 #x=x-3
x *= 2 #x=x*2
x /= 2 #x=x/2
y = 7
print(x)
print('==============================================================================')

y = 'operasimiliter'
print(reversed(y))
print(list(reversed(y))) #membalik characters string dengan mengubah ke dalam variable list
print(y[::-2])
print('==============================================================================')

day = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
now = input("What day is today: ")
nextday = int(input("how many day before or after? "))
futureday = day.index(now)
whatday = nextday % len(day)
thenextday = day[(futureday+whatday)%7]
print(f'That day exactly {thenextday}')
print('==============================================================================')

day.append('senin')
print(day)
day.insert(3,'rabu')
print(day)
day.pop()
print(day)
day.remove('rabu')
print(day)
day.pop(4)
print(day)
day.reverse()
print(day)
day = day[::-1]
print(day)
num = [4,5,80,17,3,25,1]
day.sort()
print(num)
z = [1,2,3,4,5,6,7]
w = z[::2].copy()
print(z)
print(w)
print(z,w)
print(z+w)
print(w*2)
u = [[1,2,3],[4,5,6],[7,8,9]]
print(u[1][0])
a = [1,2,3,4,5,6,7,4]
print(a.index(3))
b = (1,2,3,4,5,6,7)

# tuple list
c = [(1,2,3),
     (4,['zeus'],6),
     (7,8,9)]
c[1][1][0]='Mamen'
print(c)

# set/himpunan
# 1.no indexing
# 2.duplicate elements not allowed
# 3.set mutable,elemennya immutable
# 4.add elemen jadi random
d = {1,2,3,1,2,3,1,3}
d.add('u')
d.add('o')
d.add(('a','v','g'))
print(d)
z=list(d)
print(z[0])

h = []
for e in d:
    h.append(e)
print(h)

d.update('miMI')
d.update([6,7,8])
d.update({'p','fruti'})
print(d)
d.remove('m')
print(d)
d.discard('owl')
print(d)
d.pop()
print(d)
d.clear()
print(d)
del d
print(d)

#irisan
k = list('indonesia')
l = list('indomie')
print(k)
print(l)
k = set(k)
l = set(l)
print(k.intersection(l))
print(k&l)
print(set.intersection(k,l))

#Union
print(k.union(l))
print(k|l)

#difference
print(k.difference(l))
print(l.difference(k))
print(k-l)
print(l-k)

#symmetric diff
print(k.symmetric_difference(l))
print(l.symmetric_difference(k))
print(k^l)
print(l^k)

#soal 1
P = {1,2,4,7,9,19}
Q = {5,12,16,17,7,9,19}
R = {3,8,19,6}
print(P&Q)
print(P&Q&R)

#soal 2
P = {-4,-3,-2,-1,0,1,2,3,4}
Q = {-7,-6,-5,-4,-3,-2,-1,0,1}
R = {-1,0,1,2,3,4,5,6,7}
S = {-9,-8,-7,-6,-5,-4,-3,-2,1,2,3,4,5,6,7,8,9}
print(P.union(Q))
print(P.union(R))
print(Q.union(R))
P = list(P)
Q = list(Q)
R = list(R)
P.sort()
Q.sort()
R.sort()
print(P)
print(Q)
print(R)

#frozenset
r = set([1,2,3])
s = frozenset([1,2,3,4,5,6,1,2,3])
r.remove(2)
r.add
print(type(r))
print(len(s))

#soal 3
S = {1,2,3,4,5,6,7,8,9,10}
A = {1,3,5,7}
B = {5,7,9}
print(f'S = {S}')
print(f'A = {A}')
print(f'B = {B}')
print(f'A n B = {A & B}')
print(f'A u B = {A | B}')
print(f'A n (A u B) = {A & (A|B)}')
print(f'B n (A u B) = {B & (A|B)}')
print(f'(A u B) n (A u B) = {(A|B)&(A|B)}')
print(f'(A n B) u (A u B) = {(A&B)|(A|B)}')
