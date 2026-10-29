
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_ecommerce_sales.csv")

# Calculate key sales KPIs
total_revenue = df["Total_Sales"].sum()
total_orders = df["Order_ID"].nunique()
average_order_value = total_revenue / total_orders if total_orders else 0
total_units_sold = df["Quantity"].sum()
total_profit = df["Profit"].sum()

# Find the top-selling category by revenue
category_revenue = df.groupby("Product_Category")["Total_Sales"].sum()
top_category = category_revenue.idxmax()
top_category_revenue = category_revenue.max()

# Find the top product by revenue
product_revenue = df.groupby("Product_Name")["Total_Sales"].sum()
top_product = product_revenue.idxmax()
top_product_revenue = product_revenue.max()

# Display the KPI summary
print("E-COMMERCE SALES KPI SUMMARY")
print("=" * 40)
print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value (AOV): {average_order_value:,.2f}")
print(f"Total Units Sold: {total_units_sold:,}")
print(f"Total Profit: {total_profit:,.2f}")

print("\nTOP CATEGORY BY REVENUE")
print(f"Category: {top_category}")
print(f"Revenue: {top_category_revenue:,.2f}")

print("\nTOP PRODUCT BY REVENUE")
print(f"Product: {top_product}")
print(f"Revenue: {top_product_revenue:,.2f}")

print("\nCATEGORY REVENUE BREAKDOWN")
print(category_revenue.sort_values(ascending=False).round(2))
