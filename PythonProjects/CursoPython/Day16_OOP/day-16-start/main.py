# turtle graphics documentation site: docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen  # We import turtle module that allows us to use graphics.

timmy = Turtle()  # Create an object of Turtle Class.
timmy.color("green", "blue")  # We change the color of the turtle.
timmy.shape("turtle")
timmy.forward(100)  # We move the turtle forward.
my_screen = Screen()  # Another class from turtle module that brings us the window when the turtle is going show up.
print(my_screen.canvheight)

my_screen.exitonclick()  # Keeps screen until user clicks, this is a method from Screen class.


# Use PyPi to get packages with code created by other people to achieve a goal. Difference between package and
# module:
#   A Module is a single file containing python code. Modules are used to organize code in a single file,
#   making it easier to read and use. A Package is a collections of modules created by other people.

#   Packages are like folders or directories that contain multiple Python files (modules). They are used to keep
#   related code organized and structured within a project.

# The Package is others people code or modules inside a package while a module is a single python file.

# from prettytable import PrettyTable  # import package
#
# table = PrettyTable()  # we create an object of PrettyTable class.
#
# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])
#
# print(table)
#
# # Other way of creating the table.
# otherTable = PrettyTable()  # we create another object ot PrettyTable.
#
# otherTable.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
# otherTable.add_column("Types", ["Electric", "Water", "Fire"])
#
# otherTable.align = "l"
#
# print(otherTable)
