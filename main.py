import pandas as pd
from sales import sales_by_region

df = pd.read_csv("data/superstore.csv")

result = sales_by_region(df)

print(result)