# jawan Jackson
# 2025-10-05
# P2LAB1
# This program calculates and displays the diameter, circumference,
# and area of a circle based on the radius provided by the user.

import math

# Ask the user for the radius
radius = float(input("What is the radius of the circle? "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display the results with proper formatting
print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")
