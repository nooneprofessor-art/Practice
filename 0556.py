from random import randint as r

list = []

for i in range(10):
    list.insert(r(0, 9), r(1, 5))

print(list)

list.remove(r(1, 5))

print("\n", list, sep="")