from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal') 

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/home/kacper/Pobrane/Day_25/Snake_Game_Updated/highscore.txt") as file:
            self.high_score = file.read()

    def PrintScore(self):
        self.penup()
        self.hideturtle()
        self.setpos(0,280)
        self.write((f"Score: {self.score} High Score: {self.high_score}") ,True, align=ALIGNMENT,font=FONT)

    def IncreaseScore(self):
        self.score += 1
        if self.score > int(self.high_score):
            self.high_score = self.score

    def resetScore(self):
        self.score = 0
        self.clear()
        self.PrintScore()
        
    def saveHighScore(self):
        with open("/home/kacper/Pobrane/Day_25/Snake_Game_Updated/highscore.txt", mode='w') as file:
            file.write(str(self.high_score))

