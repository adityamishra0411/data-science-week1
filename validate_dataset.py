
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_ecommerce_sales.csv")

print("DATASET VALIDATION REPORT")
print("=" * 40)

# Check blank or whitespace-only text values
text_columns = df.select_dtypes(include="str").columns
blank_counts = {
    col: df[col].astype(str).str.strip().eq("").sum()
    for col in text_columns
}

print("\nBlank text values by column:")
print(pd.Series(blank_counts))

# Check Order_ID uniqueness
print("\nUnique Order_ID values:", df["Order_ID"].nunique())
print("Repeated Order_ID rows:", df["Order_ID"].duplicated().sum())

# Review category and region values
for column in ["Product_Category", "Region", "Payment_Method"]:
    print(f"\nUnique values in {column}:")
    print(sorted(df[column].dropna().unique()))

# Review negative-profit records
negative_profit = df[df["Profit"] < 0]

print("\nNegative-profit records:", len(negative_profit))
print("Total profit across negative-profit records:",
      round(negative_profit["Profit"].sum(), 2))

print("\nValidation checks completed.")
