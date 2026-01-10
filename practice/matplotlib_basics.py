# Line plot 
import matplotlib.pyplot as plt

sales = [120000, 80000, 100000, 50000, 90000]
days = ["Day 1", "Day 2","Day 3","Day 4","Day 5"]

plt.plot(days, sales)
plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Daily sales trend")

plt.show()

# Bar graph
region = ["Lahore", "Karachi", "Islamabad"]
total_sales = [170000, 170000, 100000]

plt.bar(region, total_sales)
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.title("Total sales by region")

plt.show()

# Visualization from pandas

import pandas as pd

df = pd.read_csv("data/sales.csv")

region_sales = df.groupby("region")["sales"].sum()

region_sales.plot(kind = "bar", title = "Sales by region (Pandas)")

plt.show()