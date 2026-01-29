age = int(input())

if age > 10 and age < 20:
    print(not False)
elif age > 10 or age < 20:
    print(False, True)
else:
    print(False)

