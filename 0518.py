password = int(input("ПАРОЛЬ: "))
login = input("ЛОГИНИ: ")

def f1():
    global password, login
    numbers = password
    word = login
    def f2():
        nonlocal numbers, word
        print("\nВЕРНЫЙ ПАРОЛЬ") if numbers == 1234 else print("\nНЕ ВЕРНЫЙ ПАРОЛЬ!")
        print("ВЕРНЫЙ ЛОГИН") if word == "www" else print("НЕ ВЕРНЫЙ ЛОГИН!")
    f2()
f1()