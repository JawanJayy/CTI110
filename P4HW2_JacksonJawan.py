# Jawan Jackson
# November 9, 2025
# P4HW2 - Pay Calculation for Multiple Employees
# This program calculates an employee’s gross pay, overtime pay, and regular pay
# for multiple employees entered by the user. It continues until the user enters "Done".
# Finally, it displays totals for all employees: overtime, regular pay, and gross pay.

# ---------------------------------------------------------
# Pseudocode:
# ---------------------------------------------------------
# 1. Initialize totals for overtime, regular pay, gross pay, and employee count.
# 2. Ask the user for the employee's name.
# 3. While the user does not enter "Done":
#    a. Ask for hours worked and pay rate.
#    b. Calculate overtime hours (if any) and regular hours.
#    c. Calculate overtime pay (1.5 × pay rate × overtime hours).
#    d. Calculate regular pay (pay rate × regular hours).
#    e. Calculate gross pay (regular pay + overtime pay).
#    f. Display pay information for this employee.
#    g. Add amounts to totals and increment employee count.
#    h. Ask for another employee name or "Done" to terminate.
# 4. When done, display total employees, total overtime pay, total regular pay, and total gross pay.
# ---------------------------------------------------------

# Initialize totals
total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

# Input first employee name
employee_name = input("Enter employee's name or 'Done' to terminate: ")

# Sentinel loop
while employee_name.lower() != "done":
    # Input hours and pay rate
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    print(f"\nEmployee name:   {employee_name}\n")

    # Calculate overtime
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    # Display results for this employee
    print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
    print("-" * 70)
    print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:.2f}\n")

    # Add to totals
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # Ask for next employee
    employee_name = input("Enter employee's name or 'Done' to terminate: ")

# Display totals
print(f"\nTotal number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
