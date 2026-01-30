class B:
    a = 10
    b = 0
    c = 0

    def init(self, b, c):
        self.b = b
        self.c = c
        print(self.a, self.b, self.c)


class C(B):
    def init(self, a, b, c):
        super(C, self).init(b, c)
        self.a = a


c = C(20, 30, 40)