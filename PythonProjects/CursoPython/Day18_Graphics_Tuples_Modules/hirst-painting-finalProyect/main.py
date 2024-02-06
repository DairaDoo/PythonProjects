# list of colors in image
# TODO 1: how to draw dots with turtle module, it will have 10 from each side
# TODO 2: each circle needs to be about 20 inside and spaces apart about 50 paces
import turtle as t
from turtle import Screen
import random

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
              (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
              (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
              (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]


def chooseColor(colorList):
    return random.choice(color_list)


# turtle info
tom = t
tom.hideturtle()
tom.colormode(255)
counter = 1
choose_direction = 10

tom.penup()
tom.setheading(222)
tom.forward(300)
tom.pendown()
tom.setheading(0)


def choose_moves(direction_p, turtle_obj):
    """"Choose were to move, left or right"""
    turtle_obj.dot(20, chooseColor(color_list))
    if direction_p % 20 == 0:
        turtle_obj.right(90)
        turtle_obj.forward(50)
        turtle_obj.right(90)
    else:
        turtle_obj.left(90)
        turtle_obj.forward(50)
        turtle_obj.left(90)


while counter <= 10:
    tom.penup()
    for i in range(9):
        tom.dot(20, chooseColor(color_list))
        tom.forward(50)
    choose_moves(choose_direction, tom)
    choose_direction += 10
    counter += 1

Screen().exitonclick()
