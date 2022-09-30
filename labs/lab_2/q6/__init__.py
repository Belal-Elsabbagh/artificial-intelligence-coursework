"""
Write a Python program that accepts a separator and a
separated sequence of words as input and prints the words in a
hyphen-separated sequence after sorting them alphabetically.

Input/Output Scenario:
Please enter the separator: ,
Please enter the sequence: Topics,Intelligence,Artificial,Selected
The ordered sequence is Artificial-Intelligence-Selected-Topics
"""


def sort_separated_string(separator: str, sequence: str):
    values = sequence.split(separator)
    return "-".join(sorted(values))


def test():
    print("Question 6")
    seq = "Topics,Intelligence,Artificial,Selected"
    sep = ","
    print(sort_separated_string(sep, seq))
