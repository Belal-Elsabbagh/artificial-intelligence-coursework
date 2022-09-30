"""
Write a Python function that takes a list and returns a new list
with unique elements of the first list.

Input/Output Scenario:
Please enter a sample list: [1,2,3,3,3,4,4,5]
The unique list: [1, 2, 3, 4, 5]
"""


def get_unique_list(original_list: list) -> list:
    unique_list = []
    for i in original_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


def test():
    print("Question 2")
    print(get_unique_list([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6, 7]))
