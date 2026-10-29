
# Global E-Commerce Sales Analysis

**WE INTERN — Week 1 Data Science Project**

## Project Overview

This project analyzes a Global E-Commerce Sales dataset using Python. It covers data inspection, cleaning, validation, sales analysis, visualization, and business insights.

## Objectives

- Inspect and clean the dataset.
- Validate data quality.
- Calculate sales KPIs.
- Analyze product categories, products, regions, monthly sales, and customer segments.
- Create charts and a dashboard mockup.
- Document business insights and recommendations.

## Dataset

- **Original file:** `data/global_ecommerce_sales.csv`
- **Cleaned file:** `data/cleaned_ecommerce_sales.csv`
- **Records:** 2,000
- **Columns:** 15
- **Analysis period:** January 2023 – December 2025

## Key Results

| KPI | Result |
|---|---:|
| Total Revenue | 484,559.34 |
| Total Orders | 2,000 |
| Average Order Value | 242.28 |
| Total Units Sold | 7,115 |
| Total Profit | 158,872.32 |

*Note: The dataset does not specify a currency unit.*

## Tools and Technologies

- Python
- Pandas
- Matplotlib
- Seaborn
- Visual Studio Code

## Project Structure

```text
data-science-week1/
├── data/
│   ├── global_ecommerce_sales.csv
│   └── cleaned_ecommerce_sales.csv
├── outputs/
│   ├── revenue_by_category.png
│   ├── monthly_sales_trend.png
│   ├── revenue_share_by_category.png
│   └── dashboard_mockup.png
├── inspect_dataset.py
├── clean_dataset.py
├── validate_dataset.py
├── analyze_sales.py
├── analyze_details.py
├── create_charts.py
├── dashboard_mockup.py
├── cleaning_report.md
├── business_insights.md
├── final_analytical_report.md
└── README.md
```

## How to Run the Project

### 1. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install the required libraries

```powershell
python -m pip install pandas numpy matplotlib seaborn jupyter openpyxl
```

### 3. Run the analysis scripts

```powershell
python inspect_dataset.py
python clean_dataset.py
python validate_dataset.py
python analyze_sales.py
python analyze_details.py
python create_charts.py
python dashboard_mockup.py
```

Run the cleaning script before the analysis scripts if you need to regenerate the cleaned dataset.

## Visualizations

The `outputs/` folder contains:

1. Revenue by Product Category — bar chart.
2. Monthly Sales Trend — line chart.
3. Revenue Share by Category — pie chart.
4. Dashboard Mockup — sales KPIs, category revenue, monthly trends, and regional revenue.

## Documentation

- `cleaning_report.md` — data cleaning and validation decisions.
- `business_insights.md` — business observations and recommendations.
- `final_analytical_report.md` — complete analytical report.

## Conclusion

This project demonstrates a basic data science workflow, from inspecting and preparing data to analyzing sales performance and communicating findings through charts and reports.
