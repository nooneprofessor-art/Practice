list1 = [5, 3, 9, 4, 7, 4, 1]
list2 = [7, 5, 9, 5, 9, 0, 3]
list3 = list1 + list2
set_list = set(list3)

new_list = []

def function(setlist):
    for x in setlist:
        new_list.append(x)

function(set_list)

print(new_list)
