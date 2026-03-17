import turtle
turtle.bgcolor("yellow")
turtle.setup(300,400)
polygon = turtle.Turtle()
num_sides = 6
side_length = 87
angle = 360/num_sides
polygon.color("turquoise")
polygon.begin_fill()
polygon.fillcolor("white")
polygon.end_fill()
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()
