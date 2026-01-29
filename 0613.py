info = {"name": None, "surname": None, "age": None, "city": None}
    
info["name"] = input("Твое имя: ")
info["surname"] = input("Твое фамилие: ")
info["age"] = input("Твой возраст: ")
info["city"] = input("Твой город: ")
print(f"Твой юзернейм: {info["name"].lower()}_{info["surname"].lower()}")

print()
for k, v in info.items():
    print(k.capitalize() + ": " + v.capitalize())

age = int(info["age"])
def check():
    global age
    if age < 14:
        print("\nДоступ запрещен!")
    elif age > 14 and age < 17:
        print("\nОграниченный доступ!")
    else:
        print("\nПолный доступ!")
check()