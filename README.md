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

## Key Steps Performed

1. Inspected the original e-commerce dataset.
2. Checked missing values and duplicate records.
3. Cleaned and validated the dataset using Python and Pandas.
4. Calculated key sales performance indicators.
5. Analyzed category, product, regional, monthly, and customer-segment performance.
6. Created bar, line, and pie charts.
7. Designed a sales dashboard mockup.
8. Documented business insights and recommendations.

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

## Major Findings

- Furniture generated the highest category revenue of 256,274.68.
- Standing Desk Converter was the highest revenue-generating product, with 46,614.22.
- Europe recorded the highest regional revenue of 137,006.20.
- North America recorded the highest number of regional orders, with 578.
- The Consumer segment generated the highest revenue of 256,287.74.
- June 2025 recorded the highest monthly revenue of 18,068.09.
- A total of 272 records had negative profit and were retained for further analysis.

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

1. **Revenue by Product Category** — Bar chart.
2. **Monthly Sales Trend** — Line chart.
3. **Revenue Share by Category** — Pie chart.
4. **Dashboard Mockup** — Sales KPIs, category revenue, monthly trends, and regional revenue.

## Documentation

- `cleaning_report.md` — Data cleaning and validation decisions.
- `business_insights.md` — Business observations and recommendations.
- `final_analytical_report.md` — Complete analytical report.

## Conclusion

This project demonstrates a basic data science workflow, from inspecting and preparing data to analyzing sales performance and communicating findings through charts and reports.

The analysis identified Furniture as the leading category by revenue, Europe as the leading region by revenue, and Consumer as the leading customer segment by revenue.

The resulting dataset, charts, dashboard, and reports provide a foundation for further business analysis and decision-making.

## Author Details

- **GitHub Username:** [adityamishra0411](https://github.com/adityamishra0411)
- **GitHub Repository:** [Global E-Commerce Sales Analysis](https://github.com/adityamishra0411/data-science-week1)
