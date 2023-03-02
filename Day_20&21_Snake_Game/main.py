from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("lightblue")
screen.title('Snek')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score.PrintScore()

while True:
    screen.update()
    time.sleep(0.05)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 10:
        score.clear()
        score.IncreaseScore()
        score.PrintScore()
        food.refresh()
        snake.extend_snake()

    #Detect collision with wall
    if snake.head.xcor() < -400 or snake.head.xcor() > 400 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
        score.GameOver(screen)

    #Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.GameOver(screen)


screen.exitonclick()