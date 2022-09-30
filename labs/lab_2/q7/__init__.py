"""
Write a Python program to check whether a list contains a
sublist.
Input/Output Scenario:
Please enter a list: [12,5,6,11,21,13]
Please enter a sublist to be checked: [1,5,6]
[1,5,6] is not a sublist of [12,5,6,11,21,13]
"""


def two_lists_are_equal(l1, l2):
    return set(l1) == set(l2)


def is_sublist(original, sub_list):
    sub_len = len(sub_list)
    max_index = len(original) - sub_len
    for i in range(max_index):
        list_slice = original[i: i + sub_len]
        if two_lists_are_equal(list_slice, sub_list):
            return True
    return False


def test():
    print("Question 7")
    my_list = [12, 5, 6, 11, 21, 13]
    my_sub_list = [6, 11, 21]
    my_false_sub_list = [1, 5, 6]
    print(is_sublist(my_list, my_sub_list))
    print(is_sublist(my_list, my_false_sub_list))
