import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
csv_file = BASE_DIR / "data" / "products.csv"

st.title("🛍️ Product Recommendation System")

df = pd.read_csv(csv_file)
df["Price"] = pd.to_numeric(df["Price"])
df["Rating"] = pd.to_numeric(df["Rating"])

category = st.selectbox(
    "Select Category",
    df["Category"].unique()
)

budget = st.number_input(
    "Enter Maximum Budget",
    min_value=0,
    value=50000
)

min_rating = st.slider(
    "Minimum Rating",
    1.0,
    5.0,
    4.0
)

result = df[df["Category"] == category].copy()

result["Score"] = (
    result["Rating"] * 10
    - result["Price"] / 10000
)

result = result[result["Price"] <= budget]
result = result[result["Rating"] >= min_rating]

result = result.sort_values(
    by="Score",
    ascending=False
)

st.subheader("Recommended Products")
st.dataframe(
    result[[
        "Product_name",
        "Brand",
        "Price",
        "Rating",
        "Score"
    ]]
)
