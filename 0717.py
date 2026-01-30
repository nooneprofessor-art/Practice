class T:
    def init(self, a=3, b="da"):
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
        # a, b, = int(input("::")), input("::")
        # super(O, self).init(a, b)
        pass

    def f(self):
        super().f()
        print(1)


t = T()
t.num = 5
t = T()
o = O()