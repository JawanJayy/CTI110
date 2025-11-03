# P4LAB1b_JacksonJawan.py
# Author: Jawan Jackson
# CTI 110 - P4LAB1b: Initials (JJ)
# This program draws the initials "JJ" using turtle graphics.

import turtle

# Set up the turtle
t = turtle.Turtle()
t.pensize(6)
t.color("darkblue")

# --- Draw first J ---
t.penup()
t.goto(-120, 0)   # Move to starting position for first J
t.pendown()

t.forward(60)     # Top line of J
t.backward(30)    # Move halfway back
t.right(90)
t.forward(100)    # Downward stroke
t.left(90)
t.circle(15, 180) # Bottom curve of J

# --- Move to position for second J ---
t.penup()
t.goto(60, 0)
t.setheading(0)
t.pendown()

# --- Draw second J ---
t.forward(60)     # Top line
t.backward(30)
t.right(90)
t.forward(100)    # Downward stroke
t.left(90)
t.circle(15, 180) # Bottom curve

# Finish up
t.hideturtle()
turtle.done()
