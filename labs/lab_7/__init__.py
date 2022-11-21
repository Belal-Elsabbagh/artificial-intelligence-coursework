import pandas as pd

from labs.lab_7.decision_tree import build_decision_tree


def run():
    df = pd.read_csv('labs/content/drug200.csv')
    tree = build_decision_tree(df, 'Drug')
