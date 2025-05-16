import pandas as pd


def get_long(data: pd.Series, min_length=5):
    new = data.copy()
    return new[new >= min_length]
