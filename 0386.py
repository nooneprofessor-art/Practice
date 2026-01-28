import turtle
joe = turtle.Turtle()
window = turtle.Screen()
joe.hideturtle()
joe.speed(100)
colors = ["red", "blue", "green", "brown"]

def object(angle = 3, length = 20):
    n_angle = 360 / angle
    for i in range(100):
        window.bgcolor(colors[i % 4])
        joe.color(colors[i % 4])
        joe.fd(length)
        joe.left(n_angle)
        
def move(x, y):
    joe.up()
    joe.setposition(x, y)
    joe.down()
    object()

window.onclick(move)
window.listen()
window.mainloop()

# hideturtle() делает перо невидимым на холсте.