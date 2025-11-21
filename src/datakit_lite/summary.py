"""Summary utilities for pandas DataFrames.

This module provides functions to generate summary statistics and metadata
for pandas DataFrames, including information about column types, missing
values, and unique value counts.
"""

import pandas as pd


def summarize_table(df: pd.DataFrame) -> pd.DataFrame:
    """Return a simple summary of a pandas DataFrame.

    Columns:
        name: column name
        dtype: pandas dtype
        non_null: count of non-null values
        total: total rows
        missing_pct: percent missing (0-100)
        unique: number of unique values
    """
    rows = []

    total = len(df)

    for col in df.columns:
        series = df[col]
        non_null = series.notna().sum()
        missing_pct = round((1 - non_null / total) * 100, 2)
        unique = series.nunique(dropna=True)

        rows.append(
            {
                "name": col,
                "dtype": str(series.dtype),
                "non_null": int(non_null),
                "total": int(total),
                "missing_pct": missing_pct,
                "unique": int(unique),
            }
        )

    return pd.DataFrame(rows)
