import numpy as np
import pandas as pd


def eqn(val):
    return val * np.log10(val)


def e_feat(feat_val_grp: pd.DataFrame, label: str):
    total = len(feat_val_grp)
    return - sum([eqn(len(i) / total) for n, i in feat_val_grp.groupby(label)])


def e(feat_grp, label, total_count):
    return sum([(len(val) / total_count) * e_feat(val, label) for n, val in feat_grp])


def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


def build_decision_tree(df: pd.DataFrame, label, visited=None, tree: dict = None):
    if visited is None:
        visited = []
    feature = get_min_entropy_feature(df, label)
    if tree is None:
        tree = {feature: {}}
    if len(df[label].unique()) == 1:
        return df[label].unique()[0]
    if feature not in visited:
        visited.append(feature)
        feat_val_groups = df.groupby(feature)
        tree[feature] = {i: {} for i, grp in feat_val_groups}
        for i, feat_val in feat_val_groups:
            tree[feature].update({i: build_decision_tree(feat_val, label, visited, tree[feature][i])})
    return tree


def get_min_entropy_feature(df, label):
    entropy_values = dict(sorted({f: e(df.groupby(f), label, len(df)) for f in df}.items(), key=lambda x: x[1]))
    del entropy_values[label]
    feature = min(entropy_values, key=entropy_values.get)
    return feature
