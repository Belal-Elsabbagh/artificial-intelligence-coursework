import math


def _calculate_euclidean_distance(_a: list, _b: list):
    return math.sqrt(sum([(i - j) ** 2 for i, j in zip(_a, _b)]))


def _calculate_manhattan_distance(_a: list, _b: list):
    return sum([abs(i - j) for i, j in zip(_a, _b)])


def _calculate_minkowski_distance(_a: list, _b: list, _exp=2):
    return sum([abs(i - j) ** _exp for i, j in zip(_a, _b)]) ** (1/_exp)


euclidean = _calculate_euclidean_distance
manhattan = _calculate_manhattan_distance
minkowski = _calculate_minkowski_distance
