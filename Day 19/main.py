import random
from turtle import Turtle, Screen

is_race_on = True

my_screen = Screen()
my_screen.setup(500, 400)
user_bet = my_screen.textinput("Make your bet", "Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_goto = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_range in range(0, 6):
    toyo = Turtle(shape="turtle")
    toyo.penup()
    toyo.color(colors[turtle_range])
    toyo.goto(-230, y_goto[turtle_range])
    all_turtle.append(toyo)

# if user_bet:
#     is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")


        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)









my_screen.exitonclick()