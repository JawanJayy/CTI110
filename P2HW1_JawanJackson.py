# Jawan Jackson
# 10/12/2025
# P2HW1 – Travel Expense Calculator
# This program asks the user for travel expenses and displays them in a formatted table

# Get user input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display results
print("\n------------Travel Expenses------------")
print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:.2f}")
print(f"{'Fuel:':20}${gas:.2f}")
print(f"{'Accomodation:':20}${accommodation:.2f}")
print(f"{'Food:':20}${food:.2f}")
print("----------------------------------------")
print(f"{'Remaining Balance:':20}${remaining_balance:.2f}")
