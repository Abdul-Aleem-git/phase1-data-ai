import pandas as pd

df = pd.read_csv("data/sales.csv")

print("First Rows:")
print(df.head())

print("\nSummary:")
print(df.describe())

print("\nSales above 80000:")
print(df[df["sales"] > 80000])

print("\nTotal Sales by region")
print(df.groupby("region")["sales"].sum())

print("\nAverage Sales by region")
print(df.groupby("product")["sales"].mean())
