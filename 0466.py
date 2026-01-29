# Переменые
play_game = False
line = "-" * 30
dot = "•   •   •   •   •   •   •   •"
action_home = None
action_tree = None
action_shop = None
tree = 0
coin = 0

print("• ИГРА ДРОВОСЕК •", end="\n\n")

print("Добро пожаловать в мою мини-игру, это первый пет-проект, строго не суди:)")

while True:
    name = input("\nСначала узнаем твое имя: напиши от 3 до 10 букв: ")
    if len(name) >= 3 and len(name) <= 10:
        while True:
            id_player = int(input("\nТеперь напиши свой id из 4 цифр: "))
            if id_player < 10000 and id_player > 1000: # первая проверка
                print(0)
            elif 5 == 5: # вторая проверка
                print(0)
            else:
                continue
        print("\nПриятной игры " + name + "!", end="\n\n")
        break
    
# 19 пробелов для id
# 19 - len(name) = пробелы для id
# id - 4 цифр

time_name = True
if time_name == True:
    print("name:                   id0000")
    time_name = False
print(line)

while True:
    
    if play_game == True:
        print("\n", line, sep="")
        for i in range(10):
            print(dot)
        print(line)
        print("name: nobody\t\tid0000")
        print(line)
    play_game = True
    
    print("|КОМАНДЫ|   |ДОМ|")
    print("• Рынок")
    print("• Лес", end="\n\n")
    
    print("|ИНВЕНТАРЬ|")
    print("• Топор ур. 1")
    print("• Дерево:", tree)
    print("• Монеты:", coin)
    
    print(line)
    
    loop = True
    while loop:
        action_home = input("|Действие >>> ")
        
        # это локация лес
        if action_home == "Лес" or action_home == "лес":
        
            print("\n", line, sep="")
            for i in range(10):
                print(dot)
            print(line)
            print("name: nobody\t\tid0000")
            print(line)
        
            print("|КОМАНДЫ|   |ЛЕС|")
            print("• Рубить")
            print("• Домой")
        
            while loop:
                action_tree = input("\n|Действие >>> ")
                if action_tree == "Рубить" or action_tree == "рубить" or action_tree == "Рубит" or action_tree == "рубит":
                    while loop:
                        print("\n+ 1 дерево")
                        tree +=1
                        action_tree = input("\n|Действие >>> ")
                        if action_tree == "Рубить" or action_tree == "рубить" or action_tree == "Рубит" or action_tree == "рубит":
                            continue
                        elif action_tree == "домой" or action_tree == "Домой" or action_tree == "Дом" or action_tree == "дом":
                            loop = False
                        else:
                            break
                elif action_tree == "домой" or action_tree == "Домой" or action_tree == "Дом" or action_tree == "дом":
                    loop = False
                else:
                    continue
                    
        # это локация рынок
        if action_home == "Рынок" or action_home == "рынок":
        
            print("\n", line, sep="")
            for i in range(10):
                print(dot)
            print(line)
            print("name: nobody\t\tid0000")
            print(line)
        
            print("|КОМАНДЫ|   |РЫНОК|")
            print("• Продать дерево")
            print("• Домой")
        
            while loop:
                action_shop = input("\n|Действие >>> ")
                if action_shop == "Продать дерево" or action_shop == "продать дерево" or action_shop == "продать дерев":
                    if tree > 0:
                        while True:
                           print("\n+ " + str(tree * 5) + " монета (продано " + str(tree) + " дерево)")
                           coin += tree * 5
                           tree = 0
                           break