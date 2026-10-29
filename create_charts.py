
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the chart style
sns.set_theme(style="whitegrid")

# Read the cleaned dataset
file_path = Path("data") / "cleaned_ecommerce_sales.csv"
df = pd.read_csv(file_path)

# Convert Order_Date into a date format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create a folder to save charts
output_folder = Path("outputs")
output_folder.mkdir(exist_ok=True)

# ---------------------------------
# 1. Bar Chart: Revenue by Category
# ---------------------------------

category_revenue = (
    df.groupby("Product_Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=category_revenue.index,
    y=category_revenue.values
)

plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()

plt.savefig(output_folder / "revenue_by_category.png", dpi=300)
plt.close()

# ---------------------------------
# 2. Line Chart: Monthly Sales Trend
# ---------------------------------

df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_revenue = (
    df.groupby("Month")["Total_Sales"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(12, 6))
plt.plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=60, ha="right")
plt.tight_layout()

plt.savefig(output_folder / "monthly_sales_trend.png", dpi=300)
plt.close()

# ---------------------------------
# 3. Pie Chart: Revenue Share
# ---------------------------------

plt.figure(figsize=(8, 8))
plt.pie(
    category_revenue.values,
    labels=category_revenue.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Revenue Share by Product Category")
plt.tight_layout()

plt.savefig(output_folder / "revenue_share_by_category.png", dpi=300)
plt.close()

# Show completion message
print("All 3 charts created successfully!")

print("Saved charts:")
print(output_folder / "revenue_by_category.png")
print(output_folder / "monthly_sales_trend.png")
print(output_folder / "revenue_share_by_category.png")

