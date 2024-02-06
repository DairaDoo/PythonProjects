from turtle import Turtle as T, Screen

# timmy = T()
# timmy.color('black')
# timmy.shape('turtle')
#
# for _ in range(50):
#     timmy.forward(10)
#     timmy.color('white')
#     timmy.forward(10)
#     timmy.color('black')
#     timmy.left(7)
#
# Screen().exitonclick()


timmy2 = T()
timmy2.shape('turtle')

for _ in range(50):
    timmy2.forward(10)
    timmy2.penup()
    timmy2.forward(10)
    timmy2.pendown()
    timmy2.left(7)

Screen().bgcolor('Black')
Screen().exitonclick()



