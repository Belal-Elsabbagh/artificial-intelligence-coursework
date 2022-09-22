"""
Write a program which prints all the divisors
of a number.

Expected Input/Output script:
Enter number: 21
The divisors are 3, 7
"""


def run_q():
    number = int(input("Enter number: "))
    divisors = []
    for i in range(2, number - 1):
        if number % i == 0:
            divisors.append(i)
    print(f"Divisors: {divisors}")
