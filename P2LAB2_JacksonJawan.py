# Jawan Jackson
# 2025-10-05
# P2LAB2
# This program uses a dictionary to store vehicle MPG data and calculates
# how many gallons of gas are needed for a given distance.

# Create the dictionary
car_mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

# Get and print the keys
keys = car_mpg.keys()
print(keys)

# Prompt user for vehicle
vehicle = input("Enter a vehicle to see it's mpg: ")

# Get and display MPG for that vehicle
mpg = car_mpg[vehicle]
print(f"\nThe {vehicle} gets {mpg} mpg.")

# Prompt for number of miles
miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

# Calculate and display gallons needed
gallons = miles / mpg
print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
