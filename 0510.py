def f1():
    def f2():
        def f3():
            def f4():
                def f5():
                    return 1
                return f5() + 1
            return f4() + 1
        return f3() + 1
    return f2() + 1

num = f1()
print(num)