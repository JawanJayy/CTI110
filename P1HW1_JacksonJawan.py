# Jawan Jackson
# 09/28/2025
# P1HW1 – Exponents and Math Expressions
# This program asks the user for numbers, calculates exponent results,
# and performs addition and subtraction, then displays the results.

print("-----Calculating Exponenets----")

# Exponent calculation
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent
print(f"\n{base} raised to the power of {exponent} is {result} !!")

print("\n-----Addition and Subtraction----")

# Addition and subtraction
start = int(input("\nEnter a starting integer: "))
to_add = int(input("Enter an integer to add: "))
to_subtract = int(input("Enter an integer to subtract: "))

final_result = start + to_add - to_subtract
print(f"\n{start} + {to_add} - {to_subtract} is equal to {final_result}")
