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
