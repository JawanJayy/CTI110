# Jawan Jackson
# 9/28/2025
# P1HW2 - Travel Expenses
# This program asks the user for a budget, travel destination, and expenses,
# then calculates and displays the remaining balance.

# Pseudocode:
# 1. Ask user to enter budget
# 2. Ask user to enter travel destination
# 3. Ask user how much they will spend on gas
# 4. Ask user how much they will spend on accommodation
# 5. Ask user how much they will spend on food
# 6. Add all expenses together
# 7. Subtract total expenses from budget
# 8. Display results in a formatted way

# Program code
print("This program calculates and displays travel expenses")
print()

budget = float(input("Enter Budget: "))
print()

destination = input("Enter your travel destination: ")
print()

gas = float(input("How much do you think you will spend on gas? "))
print()

accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()

food = float(input("Last, how much do you need for food? "))
print()

# Calculate total and remaining balance
expenses = gas + accommodation + food
remaining = budget - expenses

# Display results
print("------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()

print(f"Fuel: {gas}")
print(f"Accomodation: {accommodation}")
print(f"Food: {food}")
print()

print(f"Remaining Balance: {remaining}")
