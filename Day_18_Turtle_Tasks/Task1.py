# This task requires me to draw a square with turtle 
from turtle import *
pointer = Turtle()


counter = 0
while counter < 4:
    pointer.forward(100)
    pointer.right(90)
    counter += 1
    
screen = Screen()
screen.exitonclick()