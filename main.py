import sys
from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
import sys

snake_screen = Screen()
snake_screen.setup(width=600, height=600)
snake_screen.bgcolor("black")
snake_screen.title("Asif's Snake Game")
snake_screen.tracer(0)

snake = Snake()
food = Food()
score_card = Scoreboard()

game_on = True
while game_on:
    snake_screen.update()
    time.sleep(0.1)

    snake_screen.listen()
    snake_screen.onkey(fun=snake.up, key="Up")
    snake_screen.onkey(fun=snake.down, key="Down")
    snake_screen.onkey(fun=snake.right, key="Right")
    snake_screen.onkey(fun=snake.left, key="Left")
    snake.move()


    if snake.head.distance(food) <= 15:
        food.refresh()
        score_card.update_score()
        snake.extend()

    if snake.head.xcor() <= -280 or snake.head.xcor() >= 280 or snake.head.ycor() <= -280 or snake.head.ycor() >= 250:
        game_on = False

    if snake.collision() == 1:
        game_on = False

score_card.game_over()

snake_screen.update()







snake_screen.exitonclick()