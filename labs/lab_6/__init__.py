from labs.lab_6.distance_functions import calculate_euclidean_distance
from labs.lab_6.knn import KNN


def run():
    data = {
        0: [(1, 12), (2, 5), (3, 6), (3, 10), (3.5, 8), (2, 11), (2, 9), (1, 7)],
        1: [(5, 3), (3, 2), (1.5, 9), (7, 2), (6, 1), (3.8, 1), (5.6, 4), (4, 2), (2, 5)]
    }

    p = (6, 7)
    model = KNN(3, data, calculate_euclidean_distance)
    print(f"The value classified to unknown point is: {model.classify(p)}")
    print(f"The value regressed to unknown point is: {model.regress(p)}")