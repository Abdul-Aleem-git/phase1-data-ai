import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv("data/sales_day7.csv")

print("First 5 rows:")
print(df.head())

# 2. Basic info
print("\nData Info:")
print(df.info())

# 3. Summary statistics
print("\nStatistical Summary:")
print(df.describe())

# 4. Total sales by region
region_sales = df.groupby("region")["sales"].sum()
print("\nTotal Sales by Region:")
print(region_sales)

# 5. Average sales by product
product_avg = df.groupby("product")["sales"].mean()
print("\nAverage Sales by Product:")
print(product_avg)

# 6. Visualization – Sales by Region
region_sales.plot(kind="bar", title="Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# 7. Visualization – Average Sales by Product
product_avg.plot(kind="bar", title="Average Sales by Product")
plt.xlabel("Product")
plt.ylabel("Average Sales")
plt.tight_layout()
plt.show()
