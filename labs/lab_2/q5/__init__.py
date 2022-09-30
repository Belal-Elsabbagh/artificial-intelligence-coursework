"""
Write a Python program to sort the dictionary once by key.
"""


def sort_dict_by_key(data: dict):
    sorted_keys = sorted(data)
    new_dict = {}
    for i in sorted_keys:
        new_dict[i] = data[i]
    return new_dict


def test():
    print("Question 5")
    test_data = {
        2: 100000,
        1: 3,
        3: 4,
        5: 5,
        7: 1,
    }
    print(sort_dict_by_key(test_data))
