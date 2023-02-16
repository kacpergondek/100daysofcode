# This task required me to draw 8 shapes, each with smaller angles than the last one
import turtle
import random
pointer = turtle.Turtle()

counter = 3
turtle.colormode(255)
for _ in range (8):
    r = random.randint(0,254)
    g = random.randint(0,254)
    b = random.randint(0,254)
    angle = 360 / counter
    fullRotation = 360
    rotation = 0
    pointer.pencolor(r,g,b)
    while rotation < fullRotation:
        pointer.forward(100)
        pointer.right(angle)
        rotation += angle
    counter += 1

screen = turtle.Screen()
screen.exitonclick()

    