length = int(input("List length: "))
print(length, "\n")
list = []

for i in range(length):
    string = "Element: "
    a = input(string)
    print(a, "\n")
    list.append(a)
    
print("Your list:\n", list, sep="")
