
# E-Commerce Dataset Cleaning Report

## 1. Project Overview

**Assignment:** WE INTERN WEEK 1 - Data Science Internship  
**Project:** Global E-Commerce Sales Data Analysis  
**Dataset:** Global E-Commerce Sales  
**Tools Used:** Python, Pandas, VS Code

## 2. Dataset Overview

The original dataset contains 2,000 rows and 15 columns covering order details, customer information, product categories, quantities, prices, discounts, sales, shipping costs, profit, and payment methods.

The original dataset has been preserved separately from the cleaned dataset.
### Dataset Column Classification

The dataset contains 15 columns, classified into the following data types:

| Column Name | Data Type | Description |
|---|---|---|
| Order_ID | Identifier (String) | Unique order identifier |
| Order_Date | Date | Date of the order |
| Customer_Name | Text | Customer name |
| Customer_Segment | Categorical | Customer segment |
| Country | Categorical | Country information |
| Region | Categorical | Sales region |
| Product_Category | Categorical | Product category |
| Product_Name | Categorical | Product name |
| Quantity | Integer | Number of units ordered |
| Unit_Price | Float | Price per unit |
| Discount_Percent | Integer | Discount percentage |
| Total_Sales | Float | Total sales amount |
| Shipping_Cost | Float | Shipping cost |
| Profit | Float | Profit amount |
| Payment_Method | Categorical | Payment method used |

**Note:** In the original CSV file, `Order_Date` is stored as a string. It was converted to a datetime data type during the cleaning process.

## 3. Missing Value Analysis

The initial inspection identified zero missing values across all columns.

**Decision:** No missing-value imputation or row removal was required.

## 4. Duplicate Analysis

The initial inspection identified zero fully duplicated rows. Further validation found 2,000 unique Order IDs and zero repeated Order IDs.

**Decision:** No rows were removed due to duplicates.

## 5. Data Validation

A comprehensive validation process was performed on the cleaned dataset.

### Validation Results

| Validation Check | Result |
|---|---:|
| Total records | 2,000 |
| Total columns | 15 |
| Missing required columns | 0 |
| Missing values | 0 |
| Blank text values | 0 |
| Leading/trailing whitespace values | 0 |
| Fully duplicated rows | 0 |
| Repeated Order IDs | 0 |
| Invalid order dates | 0 |
| Non-numeric values in numeric columns | 0 |
| Quantity less than or equal to zero | 0 |
| Unit price less than or equal to zero | 0 |
| Discounts outside 0–100% | 0 |
| Sales formula mismatches (tolerance 0.02) | 0 |
| Rows not comparable for sales formula | 0 |
| Category/text formatting inconsistencies | 0 |
| Unexpected product categories | 0 |

### Category Consistency

The following categorical columns were reviewed:

- Customer_Segment
- Country
- Region
- Product_Category
- Product_Name
- Payment_Method

No leading/trailing whitespace or capitalization inconsistencies were detected in these columns.

All four expected product categories were found:

- Furniture
- Technology
- Clothing & Accessories
- Office Supplies

No unexpected product categories were identified.

### Date and Numeric Validation

No invalid order dates or non-numeric values were detected.

All quantity, unit price, and discount validation checks passed.

### Sales Formula Validation

The Total_Sales values matched the expected calculation within a tolerance of 0.02:

`Total_Sales = Quantity × Unit_Price × (1 − Discount_Percent / 100)`

No formula mismatches were found.

### Delivery Status

Delivery Status standardization was not applicable because the dataset does not contain a Delivery_Status column.

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
