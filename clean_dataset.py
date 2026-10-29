
import pandas as pd
from pathlib import Path

# Define file paths
input_path = Path("data/global_ecommerce_sales.csv")
output_path = Path("data/cleaned_ecommerce_sales.csv")

# Load the original dataset
df = pd.read_csv(input_path)

# Record the original dataset size
original_rows = len(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Order_Date to datetime format
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

# Remove rows with missing values or invalid dates
df = df.dropna()

# Save the cleaned dataset separately
df.to_csv(output_path, index=False)

# Display cleaning summary
print("Original rows:", original_rows)
print("Rows after cleaning:", len(df))
print("Rows removed:", original_rows - len(df))
print("Missing values remaining:", df.isnull().sum().sum())
print("Duplicate rows remaining:", df.duplicated().sum())
print("Date column type:", df["Order_Date"].dtype)
print("Cleaned dataset saved to:", output_path)
