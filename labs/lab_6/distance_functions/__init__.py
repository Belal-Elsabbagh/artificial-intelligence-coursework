import math


def calculate_euclidean_distance(_rec, _ref):
    return math.sqrt(sum([(i - j) ** 2 for i, j in zip(_rec, _ref)]))


def calculate_manhattan_distance(_rec, _ref):
    return sum([abs(i - j) for i, j in zip(_rec, _ref)])


def calculate_minkowski_distance(_rec, _ref, _exp=2):
    return sum([abs(i - j) ** _exp for i, j in zip(_rec, _ref)]) ** (1/_exp)
