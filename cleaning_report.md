
# E-Commerce Dataset Cleaning Report

## 1. Project Overview

**Assignment:** WE INTERN WEEK 1 - Data Science Internship  
**Project:** Global E-Commerce Sales Data Analysis  
**Dataset:** Global E-Commerce Sales  
**Tools Used:** Python, Pandas, VS Code

## 2. Dataset Overview

The original dataset contains 2,000 rows and 15 columns covering order details, customer information, product categories, quantities, prices, discounts, sales, shipping costs, profit, and payment methods.

The original dataset has been preserved separately from the cleaned dataset.

## 3. Missing Value Analysis

The initial inspection identified zero missing values across all columns.

**Decision:** No missing-value imputation or row removal was required.

## 4. Duplicate Analysis

The initial inspection identified zero fully duplicated rows. Further validation found 2,000 unique Order IDs and zero repeated Order IDs.

**Decision:** No rows were removed due to duplicates.

## 5. Data Validation

The following checks were performed:

| Validation Check | Result |
|---|---:|
| Invalid order dates | 0 |
| Quantity less than or equal to zero | 0 |
| Unit price less than or equal to zero | 0 |
| Discounts outside 0–100% | 0 |
| Blank text values | 0 |
| Repeated Order IDs | 0 |
| Sales formula mismatches (tolerance 0.02) | 0 |

The Total_Sales values matched the expected calculation within a tolerance of 0.02:

Quantity × Unit Price × (1 − Discount Percent / 100)

## 6. Negative Profit Review

A total of 272 records contain negative profit, with a combined profit value of -953.39 across those records.

Negative profit is not automatically a data-quality error. These records were retained for further business analysis rather than removed without justification.

## 7. Cleaning Decisions

- Loaded the original dataset without modifying the source file.
- Checked missing values and duplicate records.
- Validated dates, quantities, unit prices, discount percentages, and sales calculations.
- Converted Order_Date to a datetime data type in the cleaned dataset.
- Saved the cleaned dataset separately as `data/cleaned_ecommerce_sales.csv`.
- Removed zero rows because the checks did not identify any rows requiring removal.

## 8. Final Dataset Summary

| Metric | Result |
|---|---:|
| Original rows | 2,000 |
| Cleaned rows | 2,000 |
| Rows removed | 0 |
| Missing values remaining | 0 |
| Duplicate rows remaining | 0 |

## 9. Conclusion

The dataset passed the performed missing-value, duplicate, and numeric validation checks. No rows needed to be removed based on these checks.

The cleaned dataset is ready for further exploratory analysis, KPI calculations, visualization, and business insight generation.

These results describe the checks performed; they do not guarantee that every possible data-quality issue has been ruled out.
