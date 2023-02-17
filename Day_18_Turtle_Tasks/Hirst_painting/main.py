import colorgram
import turtle
import random

no_of_colours = 10
colours = colorgram.extract('Day_18_Turtle_Tasks/Hirst_painting/image.jpg',no_of_colours)
colour_list = []

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    new_colour = (r,g,b)
    colour_list.append(new_colour)

print(colour_list)
pointer = turtle.Turtle()
turtle.colormode(255)
pointer.width(1)
pointer.speed("fastest")
y_cord = -340
pointer.hideturtle()
pointer.penup()
pointer.setx(-400)
pointer.sety(-340)
for _ in range (30):
    for _ in range(20):
        x = random.choice(colour_list)
        pointer.color(x)
        pointer.fillcolor(x)
        pointer.begin_fill()
        pointer.circle(20)
        pointer.end_fill()
        pointer.penup()
        pointer.forward(50)
        pointer.pendown()
    pointer.penup()
    y_cord += 50
    pointer.setx(-400)
    pointer.sety(y_cord)
    pointer.pendown()


screen = turtle.Screen()
screen.exitonclick()