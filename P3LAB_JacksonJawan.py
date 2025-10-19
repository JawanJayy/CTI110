# P3LAB_JacksonJawan
# This program converts a float dollar amount into the most efficient
# number of dollars, quarters, dimes, nickels, and pennies.

# Get user input
amount = float(input("Enter the amount of money as a float: $"))
0.000
# Convert to cents
cents = int(round(amount * 100))

# If amount is 0, print "No change"
if cents == 0:
    print("No change")
else:
    # Dictionary to hold coin values
    coins = {
        "Dollar": 100,
        "Quarter": 25,
        "Dime": 10,
        "Nickel": 5,
        "Penny": 1
    }

    for name, value in coins.items():
        count = cents // value
        cents %= value
        if count > 0:
            if count == 1:
                print(f"{count} {name}")
            else:
                # Add 's' for plural, with special case for 'Penny'
                plural_name = "Pennies" if name == "Penny" else name + "s"
                print(f"{count} {plural_name}")
