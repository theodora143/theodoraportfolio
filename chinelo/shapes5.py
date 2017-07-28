from turtle import *
import math


# Cynthia
t = Turtle()

# Set Up your screen and starting position.
setup(1000,800)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

color = input("color")

t.pencolor(color)
#start of square
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)

t.penup()

# Set Up your screen and starting position.
setup(1800,800)
x_pos = 20
y_pos = 20
t.setposition(x_pos, y_pos)

t.pendown()

t.forward(20)
t.left(120)
t.forward(20)
t.left(120)
t.forward(20)


t.penup()
# Close window on click.
exitonclick()
