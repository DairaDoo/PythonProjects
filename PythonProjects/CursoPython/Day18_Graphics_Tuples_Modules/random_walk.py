import turtle as t
from turtle import Screen
import random


def turtle_moves(turtle):
    positions_to_move = ['north', 'south', 'east', 'west']
    chosen_move = random.choice(positions_to_move)

    if chosen_move == 'north':
        turtle.setheading(90)
    elif chosen_move == 'south':
        turtle.setheading(270)
    elif chosen_move == 'east':
        turtle.setheading(0)
    else:  # west
        turtle.setheading(180)
    turtle.forward(22)


# our turtle characteristics
timmy = t
t.colormode(255)  # set range of the color mode to 255
timmy.shapesize(1)
timmy.pensize(15)
timmy.speed("fastest")
Screen().bgcolor('black')


def random_color():
    """"these function returns a random color using RGB"""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return [red, green, blue]


# for each iteration change color and call function.
for _ in range(200):
    timmy.color(random_color())
    turtle_moves(timmy)

Screen().exitonclick()
