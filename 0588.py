def counter():
    count = 0
    def counter2():
        nonlocal count
        count += 1
        return count
    return counter2

c = counter()
print(c())
print(c())
print(c())