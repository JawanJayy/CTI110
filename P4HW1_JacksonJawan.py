# Jawan Jackson
# November 9, 2025
# P4HW1 – Score List and Grade Calculation
# This program collects multiple scores, validates them, 
# drops the lowest score, calculates the average, 
# and displays the results including a letter grade.

# ---------------------------------------------------------
# Pseudocode:
# ---------------------------------------------------------
# 1. Ask the user how many scores they want to enter.
# 2. Create an empty list to store the scores.
# 3. Use a loop to collect each score.
# 4. Inside the loop:
#    - Validate each score (must be 0–100).
#    - If invalid, display an error message and re-prompt.
# 5. After collecting all scores:
#    - Find the lowest score and display it.
#    - Create a modified list without the lowest score.
#    - Calculate and display the average of the modified list.
#    - Determine and display the letter grade.
# ---------------------------------------------------------

# Ask user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list to store scores
scores = []

# Loop to collect scores
for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))
    
    # Validate the score
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i + 1} again: "))
    
    # Add valid score to list
    scores.append(score)

# Process and display results
print("\n-------------Results-------------")
lowest_score = min(scores)
print(f"Lowest Score   : {lowest_score}")

# Remove lowest and create modified list
modified_list = scores.copy()
modified_list.remove(lowest_score)
print(f"Modified List  : {modified_list}")

# Calculate average
average = sum(modified_list) / len(modified_list)
print(f"Scores Average : {average:.2f}")

# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade          : {grade}")
print("----------------------------------")
