from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
my_food = Food()
score = ScoreBoard()

screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food turtle
    if snake.head.distance(my_food) <= 15 :
        my_food.refresh()
        snake.increase_length()
        score.update_score()

    # Detect collision with Wall
    if snake.head.xcor() > 290 or snake.head.ycor()  > 290 or  snake.head.xcor() -1 < -290 or snake.head.ycor() < -290:
        score.game_over()
        is_game_on = False
    # Detect collision with tail

    slice_new_boxes = snake.new_boxes[1:]

    for box in slice_new_boxes:

        if snake.head.distance(box) < 10:
            score.game_over()
            is_game_on = False

screen.exitonclick()