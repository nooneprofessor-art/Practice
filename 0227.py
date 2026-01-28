length = int(input("Enter the length of the list: "))
print(length)

list = []
i = 0

while i < length:
    string = "\nElement " + str(i) + ": "
    el = input(string)
    print(el)
    list.append(el)
    i += 1
    
print("\n", list, sep="")