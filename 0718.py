class T:
    def init(self, a, b):
        self.num = a
        self.word = b
        m = set(self.word)
        for i in range(self.num):
            print(m)

    def f(self):
        print(1)


class O(T):

    def init(self):
        print("init2")

    def init(self):
        print("init")

    def init(self):
        a, b, = int(input("::")), input("::")
        super(O, self).init(a, b)

    def f(self):
        super().f()
        print(1)


o = O()
o.f()