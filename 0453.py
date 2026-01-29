list = [0]

counter1 = 14
while counter1 > 0:
    print(list)
    list.append(0)
    counter1 -= 1
    
counter2 = 0
while counter2 < 14:
    list.pop(0)
    print(list)
    counter2 += 1