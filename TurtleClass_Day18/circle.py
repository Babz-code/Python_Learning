import turtle, random

t = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

t.speed("fastest")

for _ in range(100):
    t.color(random_color())
    t.circle(100)
    t.setheading(t.heading() + 10)

























my_own_screen = turtle.Screen()
my_own_screen.exitonclick()