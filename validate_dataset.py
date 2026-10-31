
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. LOAD CLEANED DATASET
# --------------------------------------------------

DATA_PATH = Path("data/cleaned_ecommerce_sales.csv")

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_PATH}. "
        "Run this script from the project root folder."
    )

df = pd.read_csv(DATA_PATH)

print("=" * 65)
print("GLOBAL E-COMMERCE SALES - DATASET VALIDATION REPORT")
print("=" * 65)

# --------------------------------------------------
# 2. CHECK REQUIRED COLUMNS
# --------------------------------------------------

required_columns = [
    "Order_ID", "Order_Date", "Customer_Name",
    "Customer_Segment", "Country", "Region",
    "Product_Category", "Product_Name", "Quantity",
    "Unit_Price", "Discount_Percent", "Total_Sales",
    "Shipping_Cost", "Profit", "Payment_Method"
]

print("\n1. DATASET STRUCTURE")
print("-" * 45)

missing_columns = [
    col for col in required_columns if col not in df.columns
]

print("Total rows:", len(df))
print("Total columns:", len(df.columns))
print("Missing required columns:", missing_columns)

if missing_columns:
    raise ValueError(
        "Validation stopped because required columns are missing."
    )

# --------------------------------------------------
# 3. MISSING VALUE ANALYSIS
# --------------------------------------------------

print("\n2. MISSING VALUE ANALYSIS")
print("-" * 45)

missing_counts = df.isna().sum()

print(missing_counts.to_string())
print("Total missing values:", int(missing_counts.sum()))

# --------------------------------------------------
# 4. BLANK AND WHITESPACE ANALYSIS
# --------------------------------------------------

print("\n3. BLANK AND WHITESPACE ANALYSIS")
print("-" * 45)

text_columns = [
    col for col in df.columns
    if pd.api.types.is_string_dtype(df[col].dtype)
]

blank_counts = {}
whitespace_counts = {}

for col in text_columns:
    values = df[col].astype("string")

    blank_counts[col] = int(
        values.str.strip().eq("").fillna(False).sum()
    )

    whitespace_counts[col] = int(
        values.ne(values.str.strip()).fillna(False).sum()
    )

print("Blank text values by column:")
print(pd.Series(blank_counts).to_string())

print("\nTotal blank text values:", sum(blank_counts.values()))

print("\nValues with leading/trailing spaces:")
print(pd.Series(whitespace_counts).to_string())

print(
    "Total values with leading/trailing spaces:",
    sum(whitespace_counts.values())
)

# --------------------------------------------------
# 5. DUPLICATE ANALYSIS
# --------------------------------------------------

print("\n4. DUPLICATE ANALYSIS")
print("-" * 45)

duplicate_rows = int(df.duplicated().sum())
repeated_order_ids = int(df["Order_ID"].duplicated().sum())

print("Fully duplicated rows:", duplicate_rows)
print("Unique Order_ID values:", int(df["Order_ID"].nunique()))
print("Repeated Order_ID rows:", repeated_order_ids)

# --------------------------------------------------
# 6. CATEGORY AND TEXT CONSISTENCY
# --------------------------------------------------

print("\n5. CATEGORY AND TEXT CONSISTENCY")
print("-" * 45)

categorical_columns = [
    "Customer_Segment",
    "Country",
    "Region",
    "Product_Category",
    "Product_Name",
    "Payment_Method"
]

formatting_issues = {}

for col in categorical_columns:
    values = df[col].dropna().astype("string")

    print(f"\nUnique values in {col}:")
    for value in sorted(values.unique().tolist()):
        print(" -", value)

    groups = {}

    for value in values:
        normalized = value.strip().casefold()
        groups.setdefault(normalized, set()).add(value)

    variants = {
        key: sorted(original_values)
        for key, original_values in groups.items()
        if len(original_values) > 1
    }

    if variants:
        formatting_issues[col] = variants
        print("Possible formatting inconsistencies:", variants)
    else:
        print("No spacing/capitalization inconsistencies detected.")

# --------------------------------------------------
# 7. PRODUCT CATEGORY VALIDATION
# --------------------------------------------------

print("\n6. PRODUCT CATEGORY VALIDATION")
print("-" * 45)

expected_categories = {
    "Furniture",
    "Technology",
    "Clothing & Accessories",
    "Office Supplies"
}

actual_categories = set(
    df["Product_Category"].dropna().astype("string").tolist()
)

unexpected_categories = sorted(
    actual_categories - expected_categories
)

print("Expected categories:", sorted(expected_categories))
print("Actual categories:", sorted(actual_categories))
print("Unexpected categories:", unexpected_categories)

# --------------------------------------------------
# 8. DATE VALIDATION
# --------------------------------------------------

print("\n7. DATE VALIDATION")
print("-" * 45)

parsed_dates = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

invalid_dates = int(parsed_dates.isna().sum())

print("Invalid order dates:", invalid_dates)

# --------------------------------------------------
# 9. NUMERIC VALIDATION
# --------------------------------------------------

print("\n8. NUMERIC VALIDATION")
print("-" * 45)

numeric_columns = [
    "Quantity",
    "Unit_Price",
    "Discount_Percent",
    "Total_Sales",
    "Shipping_Cost",
    "Profit"
]

numeric_data = {}
numeric_errors = {}

for col in numeric_columns:
    numeric_data[col] = pd.to_numeric(
        df[col], errors="coerce"
    )

    numeric_errors[col] = int(
        (df[col].notna() & numeric_data[col].isna()).sum()
    )

    print(
        f"{col} - Non-numeric values:",
        numeric_errors[col]
    )

quantity = numeric_data["Quantity"]
unit_price = numeric_data["Unit_Price"]
discount = numeric_data["Discount_Percent"]
sales = numeric_data["Total_Sales"]
profit = numeric_data["Profit"]

invalid_quantity = int(quantity.le(0).sum())
invalid_unit_price = int(unit_price.le(0).sum())

invalid_discounts = int(
    (discount.lt(0) | discount.gt(100)).sum()
)

print("\nQuantity less than or equal to zero:", invalid_quantity)
print("Unit price less than or equal to zero:", invalid_unit_price)
print("Discounts outside 0-100:", invalid_discounts)

# --------------------------------------------------
# 10. SALES FORMULA VALIDATION
# --------------------------------------------------

print("\n9. SALES FORMULA VALIDATION")
print("-" * 45)

expected_sales = (
    quantity * unit_price * (1 - discount / 100)
)

comparable_rows = (
    quantity.notna()
    & unit_price.notna()
    & discount.notna()
    & sales.notna()
)

sales_mismatches = int(
    (
        (
            sales[comparable_rows]
            - expected_sales[comparable_rows]
        ).abs() > 0.02
    ).sum()
)

not_comparable = int((~comparable_rows).sum())

print(
    "Sales formula mismatches (tolerance 0.02):",
    sales_mismatches
)
print("Rows not comparable for sales formula:", not_comparable)

# --------------------------------------------------
# 11. DELIVERY STATUS APPLICABILITY
# --------------------------------------------------

print("\n10. DELIVERY STATUS CHECK")
print("-" * 45)

if "Delivery_Status" in df.columns:
    print("Delivery_Status column found.")
    print(
        "Unique values:",
        sorted(df["Delivery_Status"].dropna().unique())
    )
else:
    print(
        "Not applicable: The dataset does not contain "
        "a Delivery_Status column."
    )

# --------------------------------------------------
# 12. NEGATIVE PROFIT REVIEW
# --------------------------------------------------

print("\n11. NEGATIVE PROFIT REVIEW")
print("-" * 45)

# Keep the mask and numeric Profit series separate.
# This avoids summing text columns from the full DataFrame.

negative_profit_mask = profit < 0

negative_profit_count = int(negative_profit_mask.sum())

negative_profit_total = float(
    profit.loc[negative_profit_mask].sum()
)

print("Negative-profit records:", negative_profit_count)

print(
    "Total profit across negative-profit records:",
    round(negative_profit_total, 2)
)

# --------------------------------------------------
# 13. FINAL VALIDATION SUMMARY
# --------------------------------------------------

print("\n" + "=" * 65)
print("FINAL VALIDATION SUMMARY")
print("=" * 65)

print("Total records:", len(df))
print("Total columns:", len(df.columns))
print("Missing required columns:", len(missing_columns))
print("Missing values:", int(missing_counts.sum()))
print("Blank text values:", sum(blank_counts.values()))
print(
    "Leading/trailing whitespace values:",
    sum(whitespace_counts.values())
)
print("Fully duplicated rows:", duplicate_rows)
print("Repeated Order IDs:", repeated_order_ids)
print("Invalid dates:", invalid_dates)
print("Invalid numeric values:", sum(numeric_errors.values()))
print("Invalid quantities:", invalid_quantity)
print("Invalid unit prices:", invalid_unit_price)
print("Invalid discounts:", invalid_discounts)
print("Sales formula mismatches:", sales_mismatches)
print("Rows not comparable for sales formula:", not_comparable)
print("Formatting issue groups:", len(formatting_issues))
print("Unexpected product categories:", len(unexpected_categories))
print("Negative-profit records:", negative_profit_count)
print("Combined negative-record profit:", round(negative_profit_total, 2))

print("\nValidation process completed.")
print("Review all results before making data corrections.")
