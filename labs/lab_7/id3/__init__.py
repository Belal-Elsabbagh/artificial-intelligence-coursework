import pandas as pd

from labs.lab_7.id3.entropy import max_info_gain_feature


def id3(df: pd.DataFrame, label: str):
    return _build_decision_tree(df, label, [], {})


def _build_decision_tree(df: pd.DataFrame, label: str, visited: list, tree: dict):
    feature = max_info_gain_feature(df, label)
    tree[feature] = {}
    if _label_has_one_unique_value(df, label):
        return _get_first_label_value(df, label)
    if feature not in visited:
        visited.append(feature)
        feat_val_groups = df.groupby(feature)
        tree[feature] = {i: {} for i, grp in feat_val_groups}
        for feat_val, sub_frame in feat_val_groups:
            tree[feature].update({feat_val: _build_decision_tree(sub_frame, label, visited, tree[feature][feat_val])})
    return tree


def _get_first_label_value(df, label):
    return df[label].unique()[0]


def _label_has_one_unique_value(df, label):
    return len(df[label].unique()) == 1