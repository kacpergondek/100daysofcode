from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=640,height=480)
user_input = screen.textinput(title="Bet", prompt="Enter a colour of the turtle that will win the race: ")
y_positions = [0, -30, 30, -60, 60, 90, -90]
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black']
racers = []
finishline_cord = 300

pointer = Turtle()
pointer.penup()
pointer.goto(x=finishline_cord, y=-400)
pointer.pendown()
pointer.left(90)
pointer.forward(1000)

for racer_index in range (0,7):
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(colours[racer_index])
    racer.goto(x=-300, y=y_positions[racer_index])
    racers.append(racer)

while True:
    for racer in racers:
        rand_distance = random.randint(0,10)
        racer.forward(rand_distance)
        racer_coord = racer.xcor()
        if racer_coord > (finishline_cord - 20):
            win_colour = racer.pencolor()
            if user_input == win_colour:
                print(f"Congrats! The {win_colour} has won the race")
                screen.exitonclick()
            else:
                print(f"{win_colour} has won the race")
                screen.exitonclick()

screen.exitonclick()
