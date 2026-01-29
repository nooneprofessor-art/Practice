a, b, c = 2, 2, 2

def f():
    global a, b, c
    a -=1; b += 1; c -= 1
    return a, b, c

a, b, c = f()

print(a, b, c)