import turtle
joe = turtle.Turtle()
joe.speed(100)
colors = ("brown", "orange")

for i in range(1000):
    joe.color(colors[i % 2])
       joe.forward(3)
       joe.left(3)
       joe.circle(200)

# color() - заливает цветом объект.