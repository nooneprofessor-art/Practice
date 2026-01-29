from random import randint as r

list1 = []; list2 = []; list3 = []

print("ПОКАЗЫВАЕТ СКОЛЬКО ЕСТЬ НУЛЕЙ\n")

for i in range(10):
    list1.insert(r(0, 9), r(0, 9))
print(list1, "\n>>> ", list1.count(0), sep="", end="\n\n")

for i in range(10):
    list2.append(r(0, 9))
print(list2, "\n>>> ", list2.count(0), sep="", end="\n\n")

counter = 10
nums = []
while not False:
    for i in range(r(1, 4)):
        nums.append(r(0, 9))
    if counter >= len(nums):
        for i in nums:
            list3.extend([i])
        counter -= len(nums)
        nums.clear()
    elif counter < len(nums):
        for i in range(10 - len(list3)):
            list3.extend([r(0, 9)])
        break
print(list3, "\n>>> ", list3.count(0), sep="", end="\n\n")

main_list = []
temporary_list = []
for i in list1:
    temporary_list.append(i)
for i in list2:
    temporary_list.append(i)
for i in list3:
    temporary_list.append(i)
for i in temporary_list:
    main_list.insert(r(0, 29), i)
print(main_list, "\n>>> ", main_list.count(0), sep="")