import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
csv_file = BASE_DIR / "data" / "products.csv"

df = pd.read_csv(csv_file)
df.columns = df.columns.str.strip()

print("Available Categories:")
print(df["Category"].unique())

category = input("\nEnter Category: ")

result = df[df["Category"].str.lower() == category.lower()]
result = result.sort_values(by="Rating", ascending=False)

if result.empty:
    print("No products found!")
else:
    print("\nRecommended Products:")
    print(result[["Product_name", "Brand", "Price", "Rating"]])
