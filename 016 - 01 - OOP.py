# Spyder Editor
# Created on Sun Nov 14 11:14:34 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Intermediate
# 016 - 01 - OOP

#   An object or a module consists of two parts:
#   what it has: attributes which are variables
#   what it does: methods which are functions
#
#   A class is a blueprint and objects are generated from it.
#
#   class names are usually Pascal case, for example: CarBlueprint().
#   in contrast with variable names which are separated by underscore.
#
#   turtle is a pre-installed class
#   Turtle() and Screen() are classes of turtle

import turtle
from turtle import Screen


#   packages differ from modules. They contain many files and codes.
#   check pypi.org for packages.
#   prettytable is a simple library to create ASCII table format.
#
#   To install in Anaconda
#   first I logged in anaconda.org
#   then search for prettytable and find it in conda-forge
#   finally use code below:
#   conda install -c conda-forge prettytable
#   as Pycharm uses anaconda package manager it is also available there.
#   Check File -> Settings -> project -> python interpreter

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

javad = turtle.Turtle()
print(javad)
javad.shape("turtle")
javad.color('chartreuse', 'coral')
javad.back(200)
javad.forward(200)

#   alternatively:
#   from turtle import Turtle
#   javad = Turtle()

# Some functions of turtle
javad.color('blue', 'black')
javad.shape("circle")
javad.begin_fill()
# star
while True:
    javad.forward(300)
    javad.left(170)
    if abs(javad.pos()) < 1:
        break
javad.end_fill()
# Triangle
javad.color('red', 'pink')
javad.begin_fill()
while True:
    javad.forward(200)
    javad.left(120)
    if abs(javad.pos()) < 1:
        break
javad.end_fill()
# Square
javad.color('green', 'yellow')
javad.begin_fill()
while True:
    javad.forward(100)
    javad.left(90)
    if abs(javad.pos()) < 1:
        break
javad.end_fill()

my_screen = Screen()
print(my_screen.canvheight)
# method below lets to show the screen until we click. otherwise it is closed very fast and can't be seen.
my_screen.exitonclick()
