class Car:
    def __init__(self, color, brand, type):
        self.color = color
        self.brand = brand
        self.type = type
        
    def site(self):
        print("Site: htts:car.org")
        print("Director: Mike")

my_car = Car("red", "bmw", "sedan")

print("|SHOP|\nColor: " + my_car.color + "\nBrand: " + my_car.brand + "\nType: " + my_car.type + "\n")

my_car.site()

# Объектно-ориентированное программирование (ООП) — это подход, при котором программа рассматривается как набор объектов, взаимодействующих друг с другом. У каждого есть свойства и поведение. Если постараться объяснить простыми словами, то ООП ускоряет написание кода и делает его более читаемым.