
Sales Dataset Cleaning 

Data Cleaning Task: Cleaned and preprocessed a messy sales dataset using Python and Pandas. Removed missing values, eliminated duplicates, corrected inconsistent text formatting, and ensured data integrity for further analysis.

Task 1: Data Cleaning and Preprocessing

 📁 Project Overview
This project focuses on cleaning a deliberately messy version of a sales dataset to simulate real-world data cleaning challenges. It is useful for practicing handling dirty data including null values, inconsistent labels, and incorrect calculations.

---

 📊 Dataset Details
- File Name: `sales_data.csv` (raw), `cleaned_sales_data.csv` (cleaned)
- Records: Simulated retail transactions with intentionally introduced errors like:
  - Missing values in key fields
  - Inconsistent capitalization and formatting
  - Typos in categorical data
  - Duplicated rows
  - Incorrect totals

---

 🧹 Cleaning Steps Performed

The script performs the following data cleaning steps:

1. Loading the Dataset
   Imported using `pandas.read_csv()`.

2. Handling Missing Values
   - Removed rows with missing (NaN) values using `.dropna()`.

3. Removing Duplicates
   - Dropped exact duplicate rows using `.drop_duplicates()`.

4. Standardizing Text Columns
   - Cleaned `Payment Method` values by removing extra spaces and applying title case with `.str.strip().str.title()`.
   - Fixed known typos like `'Csh'` → `'Cash'`.

5. Fixing Data Types
   - Converted the `Date` column to `datetime` format using `pd.to_datetime()`.
   - Cast numeric fields (`Quantity`, `Price`) to appropriate types (`int`, `float`).

6. Recalculating Totals
   - Verified and corrected the `Total` column using:
     df['Total'] = df['Quantity'] * df['Price']
     

7. Exporting Cleaned Dataset
   - Saved the cleaned dataset as `cleaned_messy_sales_data.csv`.

---

🧪 Tools & Libraries
- Python 3
- Pandas

---

🚀 How to Run

1. Ensure `messy_sales_data.csv` is in the same directory as your script.
2. Run the cleaning script using:
   python clean_messy_data.py
   

---
