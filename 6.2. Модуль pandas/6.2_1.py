import pandas as pd
import re


def length_stats(text: str):
    words = sorted(set(re.findall(r"[a-zа-я]+", text.lower())))

    return pd.Series([len(word) for word in words], index=words)
