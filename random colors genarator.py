import turtle as t
from turtle import Screen
import random


t.colormode(255)

dots = t.Turtle()
def t_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t_colors = (r, g, b)
    return t_colors


dots.penup()
dots.setheading(215)
dots.fd(360)
dots.setheading(0)
num_of_count = 100

for count_dot in range(1, num_of_count):
    dots.fd(50)
    dots.dot(20, t_colors())

    if count_dot % 10 == 0:
        dots.setheading(90)
        dots.forward(50)
        dots.setheading(180)
        dots.forward(500)
        dots.setheading(0)
scr = Screen()
scr.exitonclick()