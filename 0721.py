class Animal:
    def sound(self):
        print("Животное издает звук.")


class Dog(Animal):
    def sound(self):
        print("Собака лает")


animal = Animal()
dog = Dog()

animals = [animal, dog]
for i in animals:
    i.sound()