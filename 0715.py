from time import sleep
import os, sys

class Product:
    _name = None
    _price = None

    def init(self, name, price):
        self._name = name
        self._price = price

    def info(self):
        print(f"{self._name}: {self._price}$", end="")


class DiscountedProduct(Product):
    _discount = None

    def init(self):
        super(DiscountedProduct, self).init(name, price)
        self._discount = price * 15 // 100

    def info(self):
        super().info()
        print(f" (скидка {self._discount}$ 15%)")


name = None
price = None
numbers = []

for i in range(10):
    numbers.append(i)

while True:
    name = input("Продукт: ")
    for i in numbers:
        if str(i) in name:
            print("Пиши название товара!")
            sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            os.execl(sys.executable, sys.executable, *sys.argv)
    break

while True:
    try:
        price = int(input("Цена: "))
        break
    except ValueError:
        print("Это не цена!")
        sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        os.execl(sys.executable, sys.executable, *sys.argv)

product = Product(name, price)
discountedproduct = DiscountedProduct()
print()
discountedproduct.info()