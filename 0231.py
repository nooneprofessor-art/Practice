alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
print(alphabet[:])
print(alphabet[2:4])
print(alphabet[4:7])
print(alphabet[:3])
print(alphabet[6:])
print(alphabet[3:5])

print("")

word = "absolutism"
print(word[:])
print(word[2:7])
print(word[6:9])
print(word[:3])
print(word[8:])
print(word[1:9])

# КАК РАБОТАЕТ СРЕЗЫ?

# 1. Первая цифра удаляет   элементы с начала, то есть в номер примере: [3:] forget -> get.

# 2. Вторая цифра наоборот оставляют первые цифры, остальные удаляются, то есть: [:4] friend -> frie

# 3. Если нет цифр, в списке ничего не изменится.