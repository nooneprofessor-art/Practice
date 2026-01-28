word = input()

list = ["#" + word for i in range(5)]

new_list = "".join(list)

for i in new_list:
    print(i)