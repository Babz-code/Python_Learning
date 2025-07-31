import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

my_player = Player()
my_car = CarManager()
my_scoreboard = Scoreboard()

screen.listen()
screen.onkey(my_player.move_up,"Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    my_car.create_cars()
    my_car.move_forward()

    for cars in my_car.all_cars:
        if cars.distance(my_player) < 20:
            game_is_on = False
            my_scoreboard.game_over()

    if my_player.ycor() > 280:
        my_player.player_starting_pos()
        my_car.increase_speed()
        my_scoreboard.increase_level()



screen.exitonclick()