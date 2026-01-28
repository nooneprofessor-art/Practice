words = "YEAH", "YO", "YEAH", "YO"
print(words)

def up(el):
    return el.lower()

result = map(up, words)
result = list(result)

print(result)