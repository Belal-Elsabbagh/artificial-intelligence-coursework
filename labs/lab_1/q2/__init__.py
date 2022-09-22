"""
Write a Python program to construct the
following pattern, using a nested for loop.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""

element = "* "


def run_q():
    for i in range(0, 5):
        print(element * (i + 1))
    for i in range(4, 0, -1):
        print(element * i)
