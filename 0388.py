import turtle
joe = turtle.Turtle()
window = turtle.Screen()
window.setup(500, 500)
joe.speed(100)

def block():
    for i in range(10):
        joe.fd(50)
              joe.left(200)
        joe.reset()

def move(x, y):
    joe.up()
    joe.setposition(x, y)
    joe.down()
    block()

window.onclick(move)
window.listen()
window.mainloop()

# reset() - для очистка рисунка, сброса.