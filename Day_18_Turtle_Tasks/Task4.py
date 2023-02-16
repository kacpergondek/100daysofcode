# This task required me to create a random walk.
import turtle
import random
pointer = turtle.Turtle()
turtle.colormode(255)
pointer.width(10)
pointer.speed("fastest")
while True:
    r = random.randint(0,254)
    g = random.randint(0,254)
    b = random.randint(0,254)
    pointer.pencolor(r,g,b)
    rnd = random.randint(0,3)
    pointer.forward(50)
    pointer.right(rnd*90)


screen = turtle.Screen()
screen.exitonclick()
