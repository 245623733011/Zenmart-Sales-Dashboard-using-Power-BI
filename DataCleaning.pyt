import pandas as pd
import numpy as np

df = pd.read_csv("zenmart_sales_dataset.csv")

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df.select_dtypes(include=['object']).columns

df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df['DayName'] = df['Date'].dt.day_name()

df['Product Category'] = df['Product Category'].str.strip().str.title()
df['Payment Method'] = df['Payment Method'].str.strip().str.title()
df['City'] = df['City'].str.strip().str.title()

df['Revenue'] = df['Quantity'] * df['Unit Price']
df['Profit'] = df['Revenue'] * 0.10

df = df.drop_duplicates()

df.to_csv("zenmart_sales_cleaned.csv", index=False)