import turtle as t
from turtle import Screen
import random

# set up turtle
timmy = t
timmy.speed(15)
timmy.colormode(255)  # set range of color mode to 255
Screen().bgcolor('black')  # set background color


def random_color():
    """"these function returns a random color using RGB"""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return red, green, blue


# Angela's version
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())  # for each iteration set random color
        timmy.circle(100)  # Draw circle with a radius of 100
        timmy.setheading(timmy.heading() + size_of_gap)  # rotate by each iteration by the specified gap size.


# call draw spirograph method
draw_spirograph(5)

# Wait the user input before closing the window.
Screen().exitonclick()

# Mi versión
# for _ in range(100):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.right(10)
#
# Screen().exitonclick()
