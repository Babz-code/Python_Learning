# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('hirst.jpg', 20)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)

import turtle as t, random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)
color_palette = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]

x = -250
y = -200

paint = 0

while paint < 10:
    tim.teleport(x, y)
    tim.speed("fastest")
    for _ in range(1, 11):
        rand_color = random.choice(color_palette)
        tim.color(rand_color)
        tim.dot(20)
        tim.penup()
        tim.forward(50)

    y += 50
    paint += 1















my_screen = Screen()
my_screen.exitonclick()