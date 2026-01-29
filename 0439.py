i = True
num = 7

print("ИГРА: угадай цифру от 1 до 9 :)")

while i:
    num_player = int(input("Ввод: "))
    if num_player > 0 and num_player < 10:
        if num == num_player:
            print("Молодец, ты победил! Поздравляю!")
            i = False
        else:
            print("Попытайся снова :)", end="\n\n")
    else:
        print("Напоминаю, цифры от 1 до 9.", end="\n\n")
else:
    print("Конец игры...")