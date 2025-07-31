from turtle import Turtle, Screen

toyo = Turtle()

#while True:
number = 3
calc_factor = 360 / number

for _ in range(number):
    toyo.forward(50)
    toyo.left(calc_factor)
number += 1

for _ in range(number):
    toyo.forward(50)
    toyo.left(calc_factor)
    number += 1

















my_own_screen = Screen()
my_own_screen.exitonclick()