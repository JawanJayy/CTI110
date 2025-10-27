# P3HW2 - Salary
# Name: Jackson, Jawan
# Date: 10/26/2025
# Description: Program calculates an employee's gross pay including overtime.

# Pseudocode:
# 1. Ask for employee's name
# 2. Ask for number of hours worked
# 3. Ask for hourly pay rate
# 4. If hours > 40:
#       overtime hours = hours - 40
#       regular hours = 40
#       overtime pay = overtime hours * (payrate * 1.5)
#    Else:
#       regular hours = hours
#       overtime hours = 0
#       overtime pay = 0
# 5. regular pay = regular hours * payrate
# 6. gross pay = regular pay + overtime pay
# 7. Display name, hours worked, pay rate, overtime, overtime pay,
#    regular pay, and gross pay

# ---- Code starts here ----

# Input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

print("----------------------------------------")

# Overtime calculation
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    overtime_hours = 0
    regular_hours = hours_worked
    overtime_pay = 0

# Regular and gross pay
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Output
print(f"Employee name:  {employee_name}\n")
print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
print("---------------------------------------------------------------------------")
print(f"{hours_worked:<14.1f}{pay_rate:<11.1f}{overtime_hours:<10.1f}"
      f"{overtime_pay:<15.2f}${regular_pay:<13.2f}${gross_pay:.2f}")
