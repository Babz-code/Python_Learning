from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(900, 600)
my_screen.bgcolor("black")
my_screen.title("Welcome to TY's Pong")
my_screen.tracer(0)


r_paddle = Paddle((430, 0))
l_paddle = Paddle((-430, 0))
my_ball = Ball()


my_screen.listen()
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")
my_screen.onkey(l_paddle.go_up, "w")
my_screen.onkey(l_paddle.go_down, "s")


my_score = Scoreboard()


is_game_on = True
while is_game_on:
    time.sleep(my_ball.timer_number)
    my_screen.update()
    my_ball.move_ball()

    #Detect wall collision
    if my_ball.ycor() > 300 or my_ball.ycor() < -300:
        my_ball.bounce_y()

    #Detect collision with paddle
    if my_ball.distance(r_paddle) < 50 and my_ball.xcor() > 410 or my_ball.distance(l_paddle) < 50 and my_ball.xcor() < -410:
        my_ball.bounce_x()

    #Detect when ball goes beyond paddles
    if my_ball.xcor() > 450:
        my_ball.reset_ball()
        my_score.add_to_l_score()

    if my_ball.xcor() < -450:
        my_ball.reset_ball()
        my_score.add_to_r_score()













my_screen.exitonclick()
