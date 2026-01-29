from random import randint as r

word = "Dad, Mom"
x = r(0, 1)
if x == True:
    word = word.upper()
else:
    word = word.lower()
print(word)

print("Upper") if x == 1 else print("lower")
print(word.isupper()); print(word.islower())

list = word.split(", ")
print(list)
list.extend(["sister", "cat"])
print(list)
word = "_|_".join(list)
print(word)
sis = word[12:-6]
ca = word[21:]
print(sis, ca)
list = word.split("_|_")
print(list)
for i in range(len(list) - 2):
    list.pop()
print(list)
sis_up = sis.upper()
ca_up = ca.upper()
list.extend([sis_up, ca_up])
print(list)
new_word = " -> ".join(list)
print("\n")
fam = "my family: ".capitalize() + new_word
print(fam.find("A"))
print(fam.find("S"))
print(fam)
print(fam[36])
print(fam[25])