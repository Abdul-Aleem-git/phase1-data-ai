import pandas as pd
import numpy as np

# Creating a dirty data set 

data = {
    "name": ["Ali", "Sara", "Ahmed", "Sara", None],
    "age": [25, np.nan, 30, 28, 40],
    "salary": [50000, 60000, None, 60000, 70000],
    "department": ["IT", "HR", "IT", "HR", "Finance"]
}

df = pd.DataFrame(data)

print("Original Data Frame")
print(df)

# Detecting Missing values

print("\nDetecting Missing Values(True=Missing)")
print(df.isna())

# Counting missing values

print("\nCounting missing values")
print(df.isna().sum())

# Droping missing values i.e dropna()

df_dropped=df.dropna()

print("\nAfter dropping null values")
print(df_dropped)

# Filling missing values

df_filled = df.copy()

df_filled["age"] = df_filled["age"].fillna(df_filled["age"].mean())
df_filled["salary"] = df_filled["salary"].fillna(df_filled["salary"].median())
df_filled["name"] = df_filled["name"].fillna("Unknown")

print("\nAfter filling null values")
print(df_filled)

print("\nDuplicated rows")
print(df_dropped.duplicated())

# Remove duplicates
df_no_duplicates = df_filled.drop_duplicates()

print("\nAfter removing duplicates")
print(df_no_duplicates)

#Fixing data types
print("\nData types before")
print(df_no_duplicates.dtypes)

#Making age as integer
df_no_duplicates["age"] = df_no_duplicates["age"].astype(int)

print("\nData types after fixing")
print(df_no_duplicates.dtypes)
