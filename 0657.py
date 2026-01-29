from random import randint as r

l1 = []; l2 = []; l3 = []

class Lst:
        
        def init(self, i="Запуск."):
                print(i)
        
        def add_el(self, x):
                for i in range(8):
                        x.append(r(10, 20))
                print(x)
        
        def els(self, a, b, c):
                for i in a:
                        if i not in b:
                                c.append(i)
                print(c)
                
lst = Lst()
lst.add_el(l1)
lst.add_el(l2)
lst.els(l1, l2, l3)