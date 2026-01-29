from random import randint as r

name1, name2, name3, name4 = "Элли", "Сара", "Виолетта", "Жасминн"
name = None
age = None

def ran_name():
    return r(1, 4)
name = ran_name()
    
def ran_age():
    return r(10, 30)
age = ran_age()

print("Имя: ", end="")
if name == 1:
    print(name1)
elif name == 2:
    print(name2)
elif name == 3:
    print(name3)
elif name == 4:
    print(name4)
print("Возраст: " + str(age))