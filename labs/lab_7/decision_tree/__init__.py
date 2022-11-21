import numpy as np
import pandas as pd


def e(val):
    return val * np.log10(val)


def e_feat(feat_val_grp: pd.DataFrame, label: str):
    total = len(feat_val_grp)
    return - sum([e(len(i)/total) for n, i in feat_val_grp.groupby(label)])


def get_entropy(feat_grp, label, total_count):
    return sum([(len(val)/total_count) * e_feat(val, label) for n, val in feat_grp])


def tree_util(df: pd.DataFrame, tree):
    return tree


def build_decision_tree(df: pd.DataFrame, lbl):
    entropy_values = dict(sorted({f: get_entropy(df.groupby(f), lbl, len(df)) for f in df}.items(), key=lambda i: i[1]))
    del entropy_values[lbl]
    tree = {}
    for feature, entropy in entropy_values.items():
        for i, val in df.groupby(feature):
            tree = tree_util(val, tree)

