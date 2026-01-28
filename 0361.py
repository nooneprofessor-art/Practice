from random import *
random_num = randint(15, 30)

age_jaba = lambda name, age: name + str(age) + " лет"

print(age_jaba("Жабе ", random_num))