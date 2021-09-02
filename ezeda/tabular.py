"""Tabular data helpers."""
import numpy as np
import pandas as pd

from ezeda.helpers import trim


def summary(df):
    """Builds a summary of `df`.

    # Params
        df (pd.DataFrame): the pandas dataframe to be described.

    # Returns
        summary (pd.DataFrame): for each dataframe feature, it provides:
            - The feature's name.
            - Its data type.
            - The feature's minimum/maximum (range).
            - A random feature sample.
            - The percentage of missing values.
            - The distribution of feature values over its range.
                - For categorical features -> top `N` counts.
                - For numerical features -> the mean and 25%, 50%, 75%, 90%, 99%.
    """
    # Define numeric types
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    info = dict()
    cols = df.columns.tolist()
    for col in cols:
        dtype = str(df[col].dtypes)
        info["Feature"] = info.get("Feature", []) + [col]
        info["Type"] = info.get("Type", []) + [dtype]
        info["% missing"] = info.get("% missing", []) + [trim(df[col].isna().mean().item() * 100)]
        info["Min"] = info.get("Min", []) + [trim(df[col].min().item())]
        info["25%"] = info.get("25%", []) + [trim(df[col].quantile(.25).item()) if dtype in numerics else np.nan]
        info["50%"] = info.get("50%", []) + [trim(df[col].quantile(.50).item()) if dtype in numerics else np.nan]
        info["Mean"] = info.get("Mean", []) + [trim(df[col].mean().item()) if dtype in numerics else np.nan]
        info["75%"] = info.get("75%", []) + [trim(df[col].quantile(.75).item()) if dtype in numerics else np.nan]
        info["90%"] = info.get("90%", []) + [trim(df[col].quantile(.90).item()) if dtype in numerics else np.nan]
        info["Max"] = info.get("Max", []) + [trim(df[col].max().item())]
        fs = df[col].value_counts().iloc[:3]
        info["F"] = info.get("F", []) + [dict(zip([trim(e) for e in fs.index.tolist()],
                                                  [trim(e) for e in fs.values.tolist()]))]
        info["Sample"] = info.get("Sample", []) + [trim(df[col].sample().item())]
    return pd.DataFrame(data=info)
