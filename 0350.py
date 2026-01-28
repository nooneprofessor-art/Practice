dict = {"a": "python", "b": "c++", "c": "java", "d": "ruby", "e": "css"}

v = dict.items()
num = 0

for x, y in v:
    num += 1
    print(num, x + ": " + y)