import pandas as pd

from labs.lab_7.id3 import id3


def run():
    df = pd.read_csv('labs/content/tennis.csv')
    tree = id3(df, 'Play')
    print(tree)
