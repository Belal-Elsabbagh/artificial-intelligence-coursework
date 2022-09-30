"""
Write a Python program to find the key of the maximum value and
minimum value in a dictionary.
"""


def find_key_of_min_and_max_value(data: dict) -> dict:
    min_key = None
    max_key = None
    for key in data.keys():
        value = data.get(key)
        """
        The condition has to be in this exact order because after it evaluates the left-hand side and realises it is
        true, it ignores the right-hand side which avoids the program throwing an exception due to evaluating None. 
        """
        if min_key is None or value < min_key:
            min_key = key
        if max_key is None or value > max_key:
            max_key = key
    return {
        'max': max_key,
        "min": min_key
    }


def test():
    print("Question 4")
    test_data = {
        1: 100000,
        2: 3,
        3: 4,
        4: 5,
        5: 1,
    }
    print(find_key_of_min_and_max_value(test_data))
