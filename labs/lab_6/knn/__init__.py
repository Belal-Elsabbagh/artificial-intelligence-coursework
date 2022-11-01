from statistics import mode

import numpy as np


class KNN:
    dataset: dict[int:list] = None
    distance_function = None
    k = 1

    def __init__(self, k, dataset, distance_function):
        self.k = k
        self.dataset = dataset
        self.distance_function = distance_function

    def __calculate_distances_from_point(self, _object):
        distances = []
        for group, features in self.dataset.items():
            for point in features:
                distances.append((self.distance_function(point, _object), group))
        return distances

    def get_neighbor_labels(self, _object):
        distances = sorted(self.__calculate_distances_from_point(_object))
        return [i[1] for i in distances[:self.k]]

    def classify(self, _object):
        return mode(self.get_neighbor_labels(_object))

    def regress(self, _object):
        return np.mean(self.get_neighbor_labels(_object))
