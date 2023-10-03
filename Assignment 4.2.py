def computepay(h_worked, h_rate):
    if h_worked > 40:
        regular_pay = 40 * h_rate
        overtime_hours = h_worked - 40
        overtime_pay = overtime_hours * 1.5 * h_rate
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = h_worked * h_rate
    return total_pay

try:
    h_worked = float(input("Enter the number of hours worked: "))
    h_rate = float(input("Enter the hourly rate: "))
    if h_worked >= 0 and h_rate >= 0:
        salary = computepay(h_worked, h_rate)
        print(f"Total salary: ${salary:.2f}")
    else:
        print("Error: Hours worked and hourly rate must be non-negative numbers.")
except ValueError:
    print("Error, please enter numeric input")