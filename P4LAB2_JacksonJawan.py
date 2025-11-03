# P4LAB2_JacksonJawan.py
# Author: Jawan Jackson
# CTI 110 - P4LAB2: Multiplication Table
# This program displays a multiplication table for a non-negative integer.
# It also checks for negative input and uses both a while and a for loop.

def main():
    run_again = "yes"

    # While loop controls repetition
    while run_again.lower() == "yes":
        print()
        number = int(input("Enter an integer: "))

        # Handle negative input
        if number < 0:
            print("\nThis program does not handle negative numbers.\n")

        else:
            print()
            # Display multiplication table using for loop
            for i in range(1, 13):
                # Formatting to align equal signs nicely
                print(f"{number} * {i:<2} = {number * i}")
            print()

        # Ask user if they want to run the program again
        run_again = input("Would you like to run the program again? ").lower()

    print("\nExiting program...")

# Run main
main()
