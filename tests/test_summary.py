import pandas as pd

from datakit_lite import summarize_table


def test_summarize_table_basic():
    df = pd.DataFrame(
        {
            "a": [1, 2, 3],
            "b": ["x", "y", None],
        }
    )

    summary = summarize_table(df)

    assert "name" in summary.columns
    assert len(summary) == 2

    a_row = summary[summary["name"] == "a"].iloc[0]
    assert a_row["non_null"] == 3
    assert a_row["missing_pct"] == 0.0
