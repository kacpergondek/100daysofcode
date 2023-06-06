from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal') 

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.text = "Score: "

    def PrintScore(self):
        self.penup()
        self.hideturtle()
        self.setpos(0,280)
        self.write((self.text + str(self.score)),True, align=ALIGNMENT,font=FONT)

    def IncreaseScore(self):
        self.score += 1

    def GameOver(self,screen):
        self.goto(0,0)
        self.pencolor('red')
        self.write("GAME OVER",align=ALIGNMENT, font=FONT)
        time.sleep(2)
        screen.bye()