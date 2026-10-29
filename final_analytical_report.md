
# Global E-Commerce Sales Analysis
## WE INTERN — Week 1 Data Science Project

### 1. Project Overview

This project analyzes a Global E-Commerce Sales dataset using Python. The main objectives are to inspect the data, clean and validate it, calculate important sales KPIs, create visualizations, and identify useful business insights.

### 2. Objectives

- Inspect the dataset and understand its structure.
- Identify missing values, duplicate records, and invalid data.
- Prepare a cleaned dataset for analysis.
- Calculate important business KPIs.
- Analyze sales by category, product, region, month, and customer segment.
- Create charts and a dashboard mockup.
- Provide business insights and recommendations.

### 3. Dataset Description

The dataset used in this project is Global E-Commerce Sales.

- Original dataset: `data/global_ecommerce_sales.csv`
- Cleaned dataset: `data/cleaned_ecommerce_sales.csv`
- Total records: 2,000
- Total columns: 15
- Analysis period: January 2023 to December 2025

Important columns include Order_ID, Order_Date, Customer_Segment, Country, Region, Product_Category, Product_Name, Quantity, Unit_Price, Discount_Percent, Total_Sales, Shipping_Cost, Profit, and Payment_Method.

### 4. Data Cleaning and Validation

The dataset was inspected and validated using Python and Pandas.

| Validation Check | Result |
|---|---:|
| Original records | 2,000 |
| Records after cleaning | 2,000 |
| Missing values | 0 |
| Duplicate rows | 0 |
| Repeated Order IDs | 0 |
| Invalid dates | 0 |
| Non-positive quantities | 0 |
| Non-positive unit prices | 0 |
| Discounts outside 0–100 | 0 |
| Sales formula mismatches | 0 |

The Order_Date column was converted into a date format. The cleaned dataset was saved separately, and the original dataset was preserved.

No rows were removed because the validation checks did not identify records requiring removal.

A total of 272 records had negative profit, with a combined profit of -953.39. These records were retained for further business analysis.

### 5. Key Performance Indicators (KPIs)

| KPI | Result |
|---|---:|
| Total Revenue | 484,559.34 |
| Total Orders | 2,000 |
| Average Order Value | 242.28 |
| Total Units Sold | 7,115 |
| Total Profit | 158,872.32 |

The Average Order Value (AOV) was calculated by dividing total revenue by the number of unique orders.

### 6. Product Category Analysis

| Product Category | Revenue |
|---|---:|
| Furniture | 256,274.68 |
| Technology | 139,518.22 |
| Clothing & Accessories | 69,375.63 |
| Office Supplies | 19,390.81 |

Furniture generated the highest revenue, followed by Technology.

### 7. Product Analysis

The highest-revenue product was Standing Desk Converter, generating revenue of 46,614.22.

Other high-revenue products included Ergonomic Office Chair and Corner L-Shaped Desk.

These findings can help identify products that deserve further sales, inventory, and profitability analysis.

### 8. Regional Sales Analysis

| Region | Revenue | Orders |
|---|---:|---:|
| Europe | 137,006.20 | 503 |
| North America | 133,876.38 | 578 |
| Asia Pacific | 121,707.51 | 520 |
| South America | 46,051.13 | 191 |
| Middle East & Africa | 45,918.12 | 208 |

Europe generated the highest revenue, while North America recorded the highest number of orders.

### 9. Monthly Sales Analysis

- Highest monthly revenue: June 2025 — 18,068.09.
- Lowest monthly revenue: February 2025 — 7,337.28.
- Highest monthly order count: December 2023 — 78 orders.

Monthly revenue varied across the analysis period. Further investigation would be needed to determine the reasons for these fluctuations.

### 10. Customer Segment Analysis

| Customer Segment | Revenue | Orders |
|---|---:|---:|
| Consumer | 256,287.74 | 1,006 |
| Corporate | 146,050.39 | 623 |
| Home Office | 82,221.21 | 371 |

The Consumer segment generated the highest revenue and recorded the largest number of orders.

### 11. Data Visualizations and Dashboard

The project includes the following visualizations:

1. `outputs/revenue_by_category.png` — Bar chart comparing category revenue.
2. `outputs/monthly_sales_trend.png` — Line chart showing monthly revenue.
3. `outputs/revenue_share_by_category.png` — Pie chart showing category revenue shares.
4. `outputs/dashboard_mockup.png` — Dashboard containing revenue by category, monthly trends, regional revenue, and key KPIs.

### 12. Business Recommendations

- Review inventory and sales performance for the Furniture category.
- Investigate ways to increase revenue in regions with lower sales.
- Examine monthly revenue fluctuations before planning future campaigns.
- Develop targeted marketing strategies for different customer segments.
- Investigate negative-profit records, especially in Office Supplies.
- Review product costs, discounts, and shipping expenses to understand profitability.

### 13. Tools and Technologies

- Python
- Pandas
- Matplotlib
- Seaborn
- Visual Studio Code
- CSV datasets
- Markdown documentation

### 14. Project Limitations

This analysis is based on the supplied dataset. The reasons behind monthly sales fluctuations and negative-profit records cannot be confirmed from the summary statistics alone.

The dataset does not specify a currency unit, so the report presents monetary values without a currency symbol.

### 15. Conclusion

The project successfully completed dataset inspection, cleaning, validation, KPI calculation, detailed sales analysis, visualization, and dashboard creation.

The analysis identified Furniture as the leading category by revenue, Europe as the leading region by revenue, and Consumer as the leading customer segment by revenue.

The resulting dataset, charts, dashboard, and reports provide a foundation for further business analysis and decision-making.

---

**Project:** WE INTERN — Week 1 Data Science Project  
**Dataset:** Global E-Commerce Sales
