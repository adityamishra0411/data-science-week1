
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_ecommerce_sales.csv")

# Convert order dates to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# 1. Product category analysis
print("REVENUE BY CATEGORY")
print("=" * 40)
category_analysis = (
    df.groupby("Product_Category")
    .agg(
        Revenue=("Total_Sales", "sum"),
        Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum")
    )
    .sort_values("Revenue", ascending=False)
)
print(category_analysis.round(2))

# 2. Top 10 products by revenue
print("\nTOP 10 PRODUCTS BY REVENUE")
print("=" * 40)
product_analysis = (
    df.groupby("Product_Name")
    .agg(
        Revenue=("Total_Sales", "sum"),
        Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum")
    )
    .sort_values("Revenue", ascending=False)
    .head(10)
)
print(product_analysis.round(2))

# 3. Regional sales analysis
print("\nREVENUE BY REGION")
print("=" * 40)
region_analysis = (
    df.groupby("Region")
    .agg(
        Revenue=("Total_Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .sort_values("Revenue", ascending=False)
)
print(region_analysis.round(2))

# 4. Monthly sales trends
print("\nMONTHLY SALES TRENDS")
print("=" * 40)
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

monthly_analysis = (
    df.groupby("Month")
    .agg(
        Revenue=("Total_Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .sort_index()
)
print(monthly_analysis.round(2))

# 5. Negative-profit analysis
print("\nNEGATIVE-PROFIT ANALYSIS")
print("=" * 40)
loss_df = df[df["Profit"] < 0].copy()

print("Loss-making records:", len(loss_df))
print("Combined profit of loss-making records:",
      round(loss_df["Profit"].sum(), 2))

print("\nLoss-making records by category:")
print(
    loss_df.groupby("Product_Category")
    .agg(
        Loss_Records=("Order_ID", "count"),
        Combined_Profit=("Profit", "sum")
    )
    .sort_values("Combined_Profit")
    .round(2)
)

# 6. Customer segment analysis
print("\nCUSTOMER SEGMENT ANALYSIS")
print("=" * 40)
segment_analysis = (
    df.groupby("Customer_Segment")
    .agg(
        Revenue=("Total_Sales", "sum"),
        Profit=("Profit", "sum"),
        Customers=("Customer_Name", "nunique"),
        Orders=("Order_ID", "nunique")
    )
    .sort_values("Revenue", ascending=False)
)
print(segment_analysis.round(2))
