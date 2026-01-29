num = 0

while True:
    def func():
        global num
        print(num += 1) # так нельзя, внутри принт писать присваивание
        
    v = input()
    if v == "1":
        func()
    else:
        break