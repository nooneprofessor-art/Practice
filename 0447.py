x = 0

while True:
    x += 1
    
    for i in range(1):
        print("=" * 10)
        if x < 10:
            print("Цикл #" + str(x))
    
    if x == 10:
        break
    else:
        for i in range(1, 10):
            print(i)