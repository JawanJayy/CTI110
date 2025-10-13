# Your Name
# Date
# P2HW2 – Grades List
# This program takes grades from 6 modules, stores them in a list, and calculates:
# the lowest grade, highest grade, total, and average. All results are formatted clearly.

# Pseudocode:
# 1. Ask the user to enter grades for Modules 1 to 6 (as float)
# 2. Store these grades in a list
# 3. Calculate the lowest grade using min()
# 4. Calculate the highest grade using max()
# 5. Calculate the sum of grades using sum()
# 6. Calculate the average by dividing the sum by number of items
# 7. Display all results formatted as shown in the image

# Step 1: Get grades from user
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Step 2: Store grades in a list
grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# Step 3: Perform calculations
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Step 4: Display results
print("\n------------Results------------")
print(f"Lowest Grade:     {lowest}")
print(f"Highest Grade:    {highest}")
print(f"Sum of Grades:    {total}")
print(f"Average:          {average:.2f}")
print("--------------------------------")
