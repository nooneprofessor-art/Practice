class Soda:
    do = input("Пиши: ")
    
    def f(self):
        if self.do.lower() == "да":
            print("С добавкой")
        elif self.do.lower() == "нет":
            print("без добавки")
        else:
            print("Не понял")
    

soda = Soda()
soda.f()