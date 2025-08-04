import pandas as pd

# Load your CSV file
df = pd.read_csv("sales_data.csv")

# Check for Missing values
print(df.isnull().sum())
df = df.dropna()  

# Remove Duplicate Rows
df = df.drop_duplicates()

# Fix Inconsistent text Fields
df['Payment Method'] = df['Payment Method'].str.strip().str.title()
df['Payment Method'] = df['Payment Method'].replace({'Csh': 'Cash'})  

# convert Data types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # convert to date
df['Quantity'] = df['Quantity'].astype(int)
df['Price'] = df['Price'].astype(float)

# Recalculate Total
df['Total'] = df['Quantity'] * df['Price']

# Save the cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)
