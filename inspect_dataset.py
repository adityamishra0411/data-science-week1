import pandas as pd

# Load the original dataset
df = pd.read_csv("data/global_ecommerce_sales.csv")

# Validate order dates
dates = pd.to_datetime(df["Order_Date"], errors="coerce")

print("Total records:", len(df))
print("Invalid dates:", dates.isna().sum())
print("Quantity <= 0:", (df["Quantity"] <= 0).sum())
print("Unit price <= 0:", (df["Unit_Price"] <= 0).sum())

print(
    "Discount outside 0-100:",
    (~df["Discount_Percent"].between(0, 100)).sum()
)

print("Negative profit rows:", (df["Profit"] < 0).sum())