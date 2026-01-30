import random

coal = iron = gold = copper = 0

print(f"Уголь: {coal}")
print(f"Железо: {iron}")
print(f"Золото: {gold}")
print(f"Медь: {copper}")
print("- " * 10)

coal += random.randint(1, 10)
iron += random.randint(1, 10)
gold += random.randint(1, 10)
copper += random.randint(1, 10)

print(f"Уголь: {coal}")
print(f"Железо: {iron}")
print(f"Золото: {gold}")
print(f"Медь: {copper}")