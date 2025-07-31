from turtle import Turtle, Screen

toyo = Turtle()
number = 3
num = 0

ison = True
while ison:
    toyo.forward(50)
    yes_oh = 360 / number
    toyo.left(yes_oh)
    num += 1

    if num == number:
        number += 1
        num = 0

    if number == 10:
        ison = False
















my_own_screen = Screen()
my_own_screen.exitonclick()