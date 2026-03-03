import pandas as pd

def sales_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total sales grouped by region.
    """

    required_columns = {"Region", "Sales"}
    if not required_columns.issubset(df.columns):
        raise ValueError("Dataset must contain 'Region' and 'Sales' columns.")

    # Convert Sales to numeric (important fix)
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

    grouped_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
    )

    return grouped_sales