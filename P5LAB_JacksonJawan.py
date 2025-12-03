#Jawan Jackson
#20251130
#P5LAB - Accessing Self-Checkout Change Dispenser
#This program simulates a self-checkout machine that calculates and dispenses change using dollars and coins.

import random

def disperse_change(change):
    """Takes a float value and prints the dollars and coins needed to make that amount of change."""

    # Convert change to cents to avoid floating-point errors
    cents = int(round(change * 100))

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    print()
    print(f"{dollars} Dollars")
    print(f"{quarters} Quarters")
    print(f"{dimes} Dimes")
    print(f"{nickels} Nickels")
    print(f"{pennies} Pennies")


def main():
    # Generate a random amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed}")

    # Get user payment
    cash = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change
    change = round(cash - amount_owed, 2)

    print(f"Change is: ${change}")

    # Call the change-dispersing function
    disperse_change(change)


# Call the main function
main()
