import pandas as pd

def top_10_customers(df):
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

    result = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    return result