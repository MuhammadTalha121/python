from turtle import *
import random

is_race_on = False
scr = Screen()

scr.setup(width=500, height=400)
user_bet = scr.textinput(title="Make Your Bet", prompt="Which turtle Will Win the Race: Enter a color")
colors = ["red", "green", "blue", "purple", "saddle brown", "black"]
positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=positions[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 250:
            is_race_on = False
            winnig_c = turtle.pencolor()
            if winnig_c == user_bet:
                print(f"you've won! the {winnig_c} turtle is the winner:")
            else:
                print(f"you've lose! the {winnig_c} turtle is the winner:")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

scr.exitonclick()

