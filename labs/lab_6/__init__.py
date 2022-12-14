import json

import pandas as pd

from labs.lab_6.distance_functions import *
from labs.lab_6.knn import KNN


def tiny_test():
    data = {
        0: [(1, 12), (2, 5), (3, 6), (3, 10), (3.5, 8), (2, 11), (2, 9), (1, 7)],
        1: [(5, 3), (3, 2), (1.5, 9), (7, 2), (6, 1), (3.8, 1), (5.6, 4), (4, 2), (2, 5)]
    }
    point = (6, 7)
    test_knn(data, point, 4)


def exam_test():
    data = {
        77: [(5, 45)],
        47: [(5.11, 26)],
        55: [(5.6, 30)],
        59: [(5.9, 34)],
        72: [(4.8, 40)],
        60: [(5.8, 36), (5.8, 28), (5.5, 38)],
        40: [(5.3, 19)],
        45: [(5.5, 23)],
        58: [(5.6, 32)],
    }
    point = (5.1, 40)
    test_knn(data, point, 3)


def test_knn(data, point, k):
    knn_test_models = [
        KNN(k, data, calculate_euclidean_distance),
        KNN(k, data, calculate_manhattan_distance),
        KNN(k, data, calculate_minkowski_distance),
    ]

    test_results = json.dumps({
        'algorithm': f'{k}-NearestNeighbors',
        'point_to_test': point,
        'results': [test_model(m, point) for m in knn_test_models]
    }, indent=4)
    print(test_results)


def test_model(model, point):
    return {
        'distance_function': model.distance_function.__name__,
        'classified_category': model.classify(point),
        'regressed_value': model.regress(point),
    }


def run():
    df = pd.read_csv('labs/content/Iris.csv', dtype={'Species': 'category'}, index_col='Id')
    species = df.groupby('Species')
    df_dict = {key: species.get_group(key).values.tolist() for key in species.groups.keys()}
    data = {group: [i[:-1] for i in values] for group, values in df_dict.items()}
    k = 4
    p = (5.9, 3.0, 5.1, 1.8)
    test_knn(data, p, k)
