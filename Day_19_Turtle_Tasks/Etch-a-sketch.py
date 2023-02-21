from turtle import Turtle, Screen

pointer = Turtle()
screen = Screen()

def forward():
    pointer.forward(10)

def back():
    pointer.back(10)

def turnLeft():
    pointer.left(30)

def turnRight():
    pointer.right(30)

def clear():
    pointer.clear()
    pointer.penup()
    pointer.setx(0)
    pointer.sety(0)
    pointer.pendown()

screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=back)
screen.onkey(key='a', fun=turnLeft)
screen.onkey(key='d', fun=turnRight)
screen.onkey(key='space', fun=clear)












screen.exitonclick()