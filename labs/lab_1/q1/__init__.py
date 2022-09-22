"""
Write a program to prompt the user for hours
and rate per hour to compute gross pay.
Consider that the factory gives the employee
1.5 times the hourly rate for hours worked
above 40 hours.

Expected Input/Output script:
Enter the total worked hours:
57
Enter the rate per hour:
2
The gross pay is 131
"""

MIN_HOURS = 40
BONUS_FACTOR = 1.5


def calculate_pay(hours: float, rate: float) -> float:
    if hours < MIN_HOURS:
        return hours * rate
    extra_hours = hours - MIN_HOURS
    return (BONUS_FACTOR * rate * extra_hours) + rate * MIN_HOURS


def run_q():
    worked_hours = int(input("Enter the total worked hours:"))
    pay_rate = int(input("Enter the rate:"))
    print(f"Pay = {calculate_pay(worked_hours, pay_rate)}")
