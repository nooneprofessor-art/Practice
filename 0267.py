def maxmimal(a):
    l1 = max(a)
    return l1
    
def max_min(a, b, c, d):
    print(max(a, b, c, d))
    print(min(a, b, c, d))
    
    
list1 = [3, 7, 1, -4, 9, 0, -2]
max1 = maxmimal(list1)
print("Первый список: " + str(max1))

list2 = [56, 12, 89, 54, 39, 34]
max2 = maxmimal(list2)
print("Второй список: " + str(max2))

list3 = [45.6, 23.9, 60.2, 11.1, 99.9, 10.6, 41.50]
max3 = maxmimal(list3)
print("Третьи список: "+ str(max3))

list4 = [23, 4, 6.4, 53, 17.9, 3, 21]
max4 = maxmimal(list4)
print("Четвертый список: " + str(max4))

print("\nНахождение мин/макс числа:")

max_min(max1, max2, max3, max4)






