num = 10
print("До функции:", num)

def xxx():
    global num
    num *= num

xxx()
print("После функции:", num)