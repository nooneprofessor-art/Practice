class Factory:
    color = None
    material = None

    def init(self):
        pass

    def materials(self, color="белый", material="железо"):
        self.color = color
        self.material = material

    def build(self):
        print(f"Краска: {self.color}\nМатериал: {self.material}")


class Car(Factory):
    def creat(self):
        print(f"\nМашина создана из {self.material},\nа цвет {self.color}")


class Plane(Car):
    pass


fac = Factory()
car = Car()
plane = Plane()
plane.materials("красный", "титан")
plane.build()
print("-" * 10)
fac.materials();
fac.build()
print("-" * 10)
car.materials("зеленый");
car.build()