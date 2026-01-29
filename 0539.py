list = []
print("Список:", list, end="\n\n")

num = int(input("Сколько ячеек в список добавить: "))

for i in range(num):
    list.append("пустая ячейка")

print("\nСписок: ", list, sep="")

list.clear()
print("\nОчищенный список: ", list, sep="")