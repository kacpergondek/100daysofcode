#This task required me to create a spirograph

import turtle
import random
pointer = turtle.Turtle()
turtle.colormode(255)
pointer.width(1)
pointer.speed("fastest")
for _ in range (int(360/3)):
    r = random.randint(0,254)
    g = random.randint(0,254)
    b = random.randint(0,254)
    pointer.pencolor(r,g,b)
    pointer.circle(100)
    pointer.right(3)

screen = turtle.Screen()
screen.exitonclick()
