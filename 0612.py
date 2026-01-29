l = [7, 4, 5, 8, 9]
print(l)
c = tuple(l)
print(c)
m = set(l)
print(m)
f = frozenset(l)
print(f)

from random import randint as r
print(5 in m)
print(8 in l)
print(3 in c)
def f(G):
    for i in range(8):
        G.append(r(0, 10))
    return G
l1, l2 = [], []
l1 = f(l1)
l2 = f(l2)
    
print(l1); print(l2)
m1, m2 = set(l1), set(l2)
print(m1 & m2)