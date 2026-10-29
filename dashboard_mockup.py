
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the dashboard style
sns.set_theme(style="whitegrid")

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_ecommerce_sales.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create output folder
output_folder = Path("outputs")
output_folder.mkdir(exist_ok=True)

# Calculate key performance indicators (KPIs)
total_revenue = df["Total_Sales"].sum()
total_orders = df["Order_ID"].nunique()
average_order_value = total_revenue / total_orders
total_profit = df["Profit"].sum()

# Revenue by category
category_revenue = (
    df.groupby("Product_Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Monthly revenue
df["Month"] = df["Order_Date"].dt.to_period("M")
monthly_revenue = (
    df.groupby("Month")["Total_Sales"]
    .sum()
    .sort_index()
)

# Regional revenue
region_revenue = (
    df.groupby("Region")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Create dashboard layout
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle(
    "GLOBAL E-COMMERCE SALES DASHBOARD",
    fontsize=18,
    fontweight="bold"
)

# Chart 1: Revenue by category
category_revenue.plot(
    kind="bar",
    ax=axes[0, 0],
    title="Revenue by Product Category"
)
axes[0, 0].set_xlabel("Product Category")
axes[0, 0].set_ylabel("Revenue")
axes[0, 0].tick_params(axis="x", rotation=20)

# Chart 2: Monthly sales trend
monthly_revenue.index = monthly_revenue.index.astype(str)
monthly_revenue.plot(
    kind="line",
    marker="o",
    ax=axes[0, 1],
    title="Monthly Revenue Trend"
)
axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Revenue")
axes[0, 1].tick_params(axis="x", rotation=60)

# Chart 3: Regional revenue
region_revenue.plot(
    kind="bar",
    ax=axes[1, 0],
    title="Revenue by Region"
)
axes[1, 0].set_xlabel("Region")
axes[1, 0].set_ylabel("Revenue")
axes[1, 0].tick_params(axis="x", rotation=20)

# Chart 4: KPI summary
axes[1, 1].axis("off")

kpi_text = (
    f"TOTAL REVENUE\n{total_revenue:,.2f}\n\n"
    f"TOTAL ORDERS\n{total_orders:,}\n\n"
    f"AVERAGE ORDER VALUE\n{average_order_value:,.2f}\n\n"
    f"TOTAL PROFIT\n{total_profit:,.2f}"
)

axes[1, 1].text(
    0.5,
    0.5,
    kpi_text,
    ha="center",
    va="center",
    fontsize=15,
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=1", facecolor="white")
)

plt.tight_layout(rect=[0, 0, 1, 0.95])

# Save dashboard image
dashboard_path = output_folder / "dashboard_mockup.png"
plt.savefig(dashboard_path, dpi=300, bbox_inches="tight")
plt.close()

print("Dashboard created successfully!")
print(f"Saved at: {dashboard_path}")
