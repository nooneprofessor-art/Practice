try:
    num = int(input("Number: "))
except ValueError:
    print("oh")

counter = 0
for i in range(1, num):
    if num % i == 0:
        counter += 1

print(counter)
