
import turtle, time
from random import *
joe = turtle.Turtle()
window = turtle.Screen()
window.setup(600, 600)
window.bgcolor("black")

def objects(angle):
    x = randint(-400, 400)
    y = randint(-400, 400)
    length = randint(20, 30)
    joe.up()
    joe.setposition(x, y)
    joe.down()
    joe.begin_fill()
    for i in range(9):
        joe.left(angle)
        joe.fd(length)
    joe.end_fill()

for i in range(30):
    joe.color("yellow")
    window.bgcolor("black")
    joe.speed(100)
    objects(200)

time.sleep(5)

# Thank you for visiting my code, please subscribe 🫡