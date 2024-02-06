from turtle import Turtle as t, Screen
import random

timmy = t()

# Number of divisions for the circle
num_of_divisions = 3

Screen().bgcolor('black')

# Total angle of the circle
circle_angle = 360

#  color to choose
color_list = ["red", "green", "blue", "cyan", "magenta", "yellow", "orange", 'pink', 'violet', 'DarkOrchid',
              'CornflowerBlue']

# Loop until all the divisions are realized
while num_of_divisions <= 10:
    timmy.color(random.choice(color_list))
    # Draw a different segment for each division
    for _ in range(num_of_divisions):
        timmy.right(circle_angle / num_of_divisions)
        timmy.forward(100)

    # increment the value for each division
    num_of_divisions += 1

# Close the screen on click
Screen().exitonclick()
