s = {"Leo": 2005, "matrica": 2000, "RobiNzon": 2010}
    
counter = 0
for keys in s.keys():
    counter += 1
    print(counter, ". ", keys.capitalize(), sep="")
    
print()
    
counter = 0
for values in s.values():
    counter += 1
    print(counter, ". ", values, sep="")
    
s["Titanic"] = 2003

print(s)