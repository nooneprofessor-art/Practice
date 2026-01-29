num1, num2 = 0, 0

def f():
    global num1, num2
    num1 = int(input("Число: "))
    num1 += num2
    num2 = num1
    print(num1)
    f()

f()