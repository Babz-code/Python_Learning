from turtle import Turtle, Screen
from food import Food
import time

from scoreboard import Scoreboard
from snake import Snake

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("Welcome to Toyo's snake game")
my_screen.tracer(0)

not_ty_snake = Snake()
snake_food = Food()
my_score = Scoreboard()

my_screen.listen()
my_screen.onkey(not_ty_snake.up, "Up")
my_screen.onkey(not_ty_snake.down, "Down")
my_screen.onkey(not_ty_snake.left, "Left")
my_screen.onkey(not_ty_snake.right, "Right")


is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    not_ty_snake.move_snake()

    #Detect collision with food
    if not_ty_snake.head.distance(snake_food) < 15:
        snake_food.refresh_meal()
        my_score.add_to_score()
        not_ty_snake.extend_snake()

    #Detect collision with wall
    if not_ty_snake.head.xcor() > 280 or not_ty_snake.head.xcor() < -280 or not_ty_snake.head.ycor() > 280 or not_ty_snake.head.ycor() < -280:
        my_score.reset()
        not_ty_snake.reset_snake()

    #Detect collision with tail
    for seg in not_ty_snake.segment[1:]:
        if not_ty_snake.head.distance(seg) < 10:
            my_score.reset()
            not_ty_snake.reset_snake()








my_screen.exitonclick()