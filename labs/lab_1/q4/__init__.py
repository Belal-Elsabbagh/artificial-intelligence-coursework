"""
Write a program which prompts user for a
number and prints the reverse of it.

Expected Input/Output script:
Enter number: 834
The reversed number is: 438
"""
BASE = 10


def run_q():
    number = int(input("Enter number: "))
    rev = 0
    while number != 0:
        digit = number % BASE
        rev = rev * BASE + digit
        number = int(number // BASE)
    print(rev)
