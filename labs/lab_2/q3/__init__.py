"""
Write a Python program to convert a given list of tuples to a list of
lists

Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3,
4, 2]]
"""


def to_list_of_lists(list_of_tuples: list[tuple]):
    return [list(tup) for tup in list_of_tuples]


def test():
    print("Question 3")
    list_of_tuples = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
    print(to_list_of_lists(list_of_tuples))

