class Matic:

    def __init__(self):
        self.a = None
        self.b = None
        self.operate()

    def operate(self):
        while True:
            try:
                self.a = int(input("a:"))
                self.a = abs(self.a)
                break
            except ValueError:
                print("Ты написал не число.")
        while True:
            try:
                self.b = int(input("b:"))
                self.b = abs(self.b)
                if self.b == 0:
                    if self.a == 0:
                        print("Ноль нельзя!")
                    else:
                        break
                else:
                    break
            except ValueError:
                print("Ты написал не число.")

        self.nod()

    def nod(self):
        for i in range(min(self.a, self.b), 0 , -1):
            if self.a % i == 0 and self.b % i == 0:
                print(i)
                break
                
matic = Matic()
