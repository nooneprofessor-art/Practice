from random import randint as r

class C:
    def init(self, x = r(2, 10), y = r(2, 10), z = r(2, 10), d = r(2, 10)):
        print(x, y, z, d, sep="|")
        res = (x + y + z + d) // 4
        print(f"Среднее значение: {res}")

c = C()