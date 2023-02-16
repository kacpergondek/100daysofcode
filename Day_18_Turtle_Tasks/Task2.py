# This task required me to create a dashed line

import turtle
pointer = turtle.Turtle()

for _ in range (100):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)


screen = Screen()
screen.exitonclick()