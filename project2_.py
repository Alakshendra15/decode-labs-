import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Dataset for Data Analytics.xlsx")

print(df.head())
print(df.shape)
print(df.info())

# -----------------------------------------
# 2. DESCRIPTIVE STATISTICS
# -----------------------------------------

numeric_columns = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

print("\n===== DESCRIPTIVE STATISTICS =====")

print(df[numeric_columns].describe())

print("\n===== MEAN =====")
print(df[numeric_columns].mean())

print("\n===== MEDIAN =====")
print(df[numeric_columns].median())

print("\n===== COUNT =====")
print(df[numeric_columns].count())

# -----------------------------------------
# 3. CATEGORICAL DATA ANALYSIS
# -----------------------------------------

categorical_columns = [
    "Product",
    "PaymentMethod",
    "OrderStatus",
    "ReferralSource",
    "CouponCode"
]

print("\n===== CATEGORICAL DATA =====")

for column in categorical_columns:
    print(f"\n--- {column} ---")
    print(df[column].value_counts(dropna=False))

    # -----------------------------------------
# 4. DATE RANGE
# -----------------------------------------

print("\n===== DATE RANGE =====")

print("Minimum Date:", df["Date"].min())
print("Maximum Date:", df["Date"].max())

# -----------------------------------------
# 5. MISSING VALUES
# -----------------------------------------

print("\n===== MISSING VALUES =====")

print(df.isnull().sum())

# -----------------------------------------
# 6. TOTAL PRICE DISTRIBUTION
# -----------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(x=df["TotalPrice"], kde=True)

plt.title("Distribution of Total Order Price")
plt.xlabel("Total Price")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.savefig("charts/total_price_distribution.png")
plt.close()

# -----------------------------------------
# 11. PRODUCT PERFORMANCE ANALYSIS
# -----------------------------------------

product_analysis = df.groupby("Product").agg(
    Orders=("OrderID", "count"),
    Total_Revenue=("TotalPrice", "sum"),
    Average_Order_Value=("TotalPrice", "mean"),
    Average_Quantity=("Quantity", "mean")
).sort_values("Total_Revenue", ascending=False)

print("\n===== PRODUCT PERFORMANCE =====")
print(product_analysis)

# -----------------------------------------
# 12. PAYMENT METHOD ANALYSIS
# -----------------------------------------

payment_analysis = (
    df.groupby("PaymentMethod")
    .agg(
        Orders=("OrderID", "count"),
        Total_Revenue=("TotalPrice", "sum"),
        Average_Order_Value=("TotalPrice", "mean")
    )
    .sort_values("Total_Revenue", ascending=False)
)

print("\n===== PAYMENT METHOD ANALYSIS =====")
print(payment_analysis)

plt.figure(figsize=(9, 6))

sns.barplot(
    x=payment_analysis.index,
    y=payment_analysis["Total_Revenue"]
)

plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Revenue")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("charts/revenue_by_payment_method.png")

plt.close()

# -----------------------------------------
# 13. REFERRAL SOURCE ANALYSIS
# -----------------------------------------

referral_analysis = (
    df.groupby("ReferralSource")
    .agg(
        Orders=("OrderID", "count"),
        Total_Revenue=("TotalPrice", "sum"),
        Average_Order_Value=("TotalPrice", "mean")
    )
    .sort_values("Total_Revenue", ascending=False)
)

print("\n===== REFERRAL SOURCE ANALYSIS =====")
print(referral_analysis)

plt.figure(figsize=(9, 6))

sns.barplot(
    x=referral_analysis.index,
    y=referral_analysis["Total_Revenue"]
)

plt.title("Revenue by Referral Source")
plt.xlabel("Referral Source")
plt.ylabel("Total Revenue")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("charts/revenue_by_referral_source.png")

plt.close()

# -----------------------------------------
# 14. COUPON ANALYSIS
# -----------------------------------------

coupon_data = df.copy()

coupon_data["CouponCode"] = coupon_data["CouponCode"].fillna("No Coupon")

coupon_analysis = (
    coupon_data.groupby("CouponCode")
    .agg(
        Orders=("OrderID", "count"),
        Total_Revenue=("TotalPrice", "sum"),
        Average_Order_Value=("TotalPrice", "mean")
    )
    .sort_values("Total_Revenue", ascending=False)
)

print("\n===== COUPON ANALYSIS =====")
print(coupon_analysis)

plt.figure(figsize=(9, 6))

sns.barplot(
    data=coupon_analysis.reset_index(),
    x="CouponCode",
    y="Average_Order_Value"
)

plt.title("Average Order Value by Coupon")
plt.xlabel("Coupon Code")
plt.ylabel("Average Order Value")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("charts/average_order_value_coupon.png")

plt.close()

# -----------------------------------------
# 15. OUTLIER ANALYSIS
# -----------------------------------------

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["TotalPrice"] < lower_limit) |
    (df["TotalPrice"] > upper_limit)
]

print("\n===== OUTLIER ANALYSIS =====")

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

print("Number of Outliers:", len(outliers))

print("\n===== OUTLIER RECORDS =====")

print(
    outliers[
        [
            "OrderID",
            "Date",
            "Product",
            "Quantity",
            "UnitPrice",
            "TotalPrice"
        ]
    ]
)

# -----------------------------------------
# 16. CORRELATION ANALYSIS
# -----------------------------------------

correlation_data = df[
    [
        "Quantity",
        "UnitPrice",
        "ItemsInCart",
        "TotalPrice"
    ]
]

correlation_matrix = correlation_data.corr()

print("\n===== CORRELATION MATRIX =====")

print(correlation_matrix)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Correlation Between Numerical Variables")

plt.tight_layout()

plt.savefig("charts/correlation_heatmap.png")
plt.close()

# -----------------------------------------
# 17. ORDER STATUS REVENUE ANALYSIS
# -----------------------------------------

status_analysis = (
    df.groupby("OrderStatus")
    .agg(
        Orders=("OrderID", "count"),
        Total_Revenue=("TotalPrice", "sum"),
        Average_Order_Value=("TotalPrice", "mean")
    )
    .sort_values("Total_Revenue", ascending=False)
)

print("\n===== ORDER STATUS REVENUE ANALYSIS =====")
print(status_analysis)

plt.figure(figsize=(9, 6))

sns.barplot(
    data=status_analysis.reset_index(),
    x="OrderStatus",
    y="Total_Revenue"
)

plt.title("Revenue by Order Status")
plt.xlabel("Order Status")
plt.ylabel("Total Revenue")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("charts/revenue_by_order_status.png")

plt.close()