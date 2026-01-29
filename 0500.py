import os

# глобальные переменные
coin = None
iron = None

# очистка консоли
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def home(): # локация дом
    print("────── ТЕЛЕЖКА ──────"); print("1) Деревянная кирка"); print("2) Железо: 0"); print("3) Уголь: 0"); print("4) Медь: 0")
    print("\n────── КОМАНДЫ ──────"); print("1) Шахта"); print("2) Продать руды"); print("\n────────────────────")
    while not False:
        action = input("\nДействие: ")
        if action == "шахта":
            clear_console()
            mine()

def mine(): # локация шахта
    print("\n────── КОМАНДЫ ──────"); print("1) Копать"); print("2) Домой"); print("\n────────────────────")
    while not False:
        action = input("\nДействие: ")
        if action == "дом":
            clear_console()
            home()
home()