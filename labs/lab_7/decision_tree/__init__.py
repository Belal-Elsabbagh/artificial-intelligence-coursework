import numpy as np
import pandas as pd


def eqn(val):
    return val * np.log10(val)


def e_feat(feat_val_grp: pd.DataFrame, label: str):
    total = len(feat_val_grp)
    return - sum([eqn(len(i) / total) for n, i in feat_val_grp.groupby(label)])


def e(feat_grp, label, total_count):
    return sum([(len(val) / total_count) * e_feat(val, label) for n, val in feat_grp])


def tree_util(df: pd.DataFrame, label, tree):
    for i, val in df.groupby(label):
        tree = tree_util(val, label, tree)
    return tree


def build_decision_tree(df: pd.DataFrame, label, visited=None, tree: dict = None):
    if visited is None:
        visited = []
    entropy_values = dict(sorted({f: e(df.groupby(f), label, len(df)) for f in df}.items(), key=lambda x: x[1]))
    del entropy_values[label]
    if tree is None:
        tree = {f: {} for f in entropy_values}
    if len(df[label].unique()) == 1:
        return df[label].unique()[0]
    for feature, entropy in entropy_values.items():
        for i, feat_val in df.groupby(feature):
            if i in visited:
                continue
            visited.append(i)
            tree[feature].update({i: build_decision_tree(feat_val, label, visited, tree)})
    return tree
