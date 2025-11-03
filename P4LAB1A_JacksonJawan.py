# P4LAB1a_JacksonJawan.py
# Author: Jawan Jackson
# CTI 110 - P4LAB1a: Shapes
# This program draws a square and a triangle using turtle graphics.

import turtle

# Create the turtle
t = turtle.Turtle()
t.pensize(3)
t.color("blue")

# Draw a square using a for loop
for i in range(4):
    t.forward(100)
    t.right(90)

# Move to a new position so the triangle doesn’t completely overlap
t.penup()
t.goto(-50, -50)
t.pendown()
t.color("green")

# Draw a triangle using a while loop
sides = 0
while sides < 3:
    t.forward(100)
    t.left(120)
    sides += 1

# Hide turtle and finish
t.hideturtle()
turtle.done()

