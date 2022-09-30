"""
Write a Python function to check whether a number is perfect or
not.

Input/Output Scenario:
Please enter a number: 28
28 is a perfect number
Please enter a number: 9
9 is not a perfect number
"""


def get_divisors(num: int) -> list[int]:
    divisors = []
    for i in range(1, num - 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def is_perfect_number(num: int) -> bool:
    return sum(get_divisors(num)) == num


def test():
    print("Question 1")
    print(is_perfect_number(9))
    print(is_perfect_number(28))
