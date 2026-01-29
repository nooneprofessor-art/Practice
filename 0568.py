d = {"HTML": "скелет СайТА", "CSS": "офорМЛение сайта", "JavaScript": "интеракТивность сайта"}

k = len(d.keys()) - 2
for keys in d.keys():
    print(str(k) + ". " + keys)
    k += 1

print()

v = len(d.values()) - 2
for values in d.values():
    print(str(v) + ". " + values.upper())
    v += 1

print()

i = len(d) - 2
for keys, values in d.items():
    print(str(i) + ". " + keys + ": " + values.lower())
    i += 1
    
print()

lk = []
for keys in d.keys():
    lk.append(keys)
print(lk)

print(lk[0].isupper())

#lk = lk[1].lower()

print(lk[1].islower())

cor = tuple(lk[2])
print(cor)
for i in cor:
    print(i, end="")

print()

print("|".join(cor).upper())
print("|".join(cor).lower())
print(cor.count("a"))
print(cor.count("c"))
print(d.popitem())
print(d.clear())
w = "kontiki"
print(w.find("i"))
word = "Cappy, Zack, Mita, Mike, Frap"
list = word.split(", ")
print(list)
print("-".join(list))