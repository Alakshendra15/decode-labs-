# Project 2 – Exploratory Data Analysis (EDA)

## 1. Project Overview

This project performs Exploratory Data Analysis (EDA) on an order dataset to understand patterns, trends, distributions, relationships, and unusual observations in the data.

The analysis focuses on descriptive statistics, categorical analysis, product performance, payment methods, referral sources, coupon usage, order status, time trends, outliers, and correlations.

## 2. Dataset Overview

- **Records:** 1,200 orders
- **Columns:** 14
- **Date range:** January 1, 2023 to June 30, 2025
- **Numerical variables:** Quantity, UnitPrice, ItemsInCart, TotalPrice
- **Categorical variables:** Product, PaymentMethod, OrderStatus, ReferralSource, CouponCode
- **Missing values:** CouponCode contains 309 missing records; all other columns have complete records.

## 3. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- OpenPyXL
- Visual Studio Code

## 4. EDA Methodology

The following steps were performed:

1. Loaded the Excel dataset using Pandas.
2. Inspected dataset dimensions, data types, and missing values.
3. Calculated descriptive statistics including count, mean, median, minimum, maximum, and standard deviation.
4. Analyzed categorical variables using frequency counts.
5. Examined the distribution of TotalPrice.
6. Compared product order volume, revenue, average order value, and average quantity.
7. Analyzed revenue by payment method.
8. Analyzed revenue and order value by referral source.
9. Compared coupon categories and orders where no coupon was recorded.
10. Analyzed order status by order count, revenue, and average order value.
11. Analyzed monthly revenue trends.
12. Detected TotalPrice outliers using the IQR method.
13. Examined correlations among numerical variables.

## 5. Key Statistical Findings

| Metric | Result |
|---|---:|
| Total orders | 1,200 |
| Average Quantity | 2.95 |
| Median Quantity | 3.00 |
| Average Unit Price | 356.41 |
| Median Unit Price | 364.21 |
| Average Items in Cart | 5.49 |
| Median Items in Cart | 5.00 |
| Average Order Value | 1,053.97 |
| Median Order Value | 823.62 |
| Maximum Order Value | 3,456.40 |

The mean TotalPrice is higher than the median TotalPrice, indicating that relatively high-value orders influence the average order value.

## 6. Product Performance

- **Chair** generated the highest total revenue: **195,620.11**.
- **Printer** was a very close second with **195,612.61** in revenue.
- **Laptop** had the highest average order value: **1,110.56**.
- **Phone** had the lowest order count (156) and the lowest average order value (972.58).

This shows that the product with the highest order volume or total revenue is not necessarily the product with the highest average order value.

## 7. Payment Method Analysis

- **Credit Card** generated the highest revenue: **263,847.63**.
- Credit Card also had the highest average order value: **1,127.55**.
- Online payments had the highest number of orders: **258**.

Therefore, order volume and revenue rankings are not identical across payment methods.

## 8. Referral Source Analysis

- **Instagram** generated the highest number of orders: **259**.
- Instagram also generated the highest total revenue: **275,285.45**.
- **Facebook** had the highest average order value: **1,098.29**, despite having fewer orders than Instagram.

Instagram therefore appears strongest for order volume and total revenue in this dataset, while Facebook is associated with relatively higher-value orders.

## 9. Coupon Analysis

- **FREESHIP** had the highest number of recorded orders among coupon categories: **313**.
- FREESHIP also generated the highest revenue among the coupon categories: **335,036.99**.
- SAVE10 had an average order value of **1,065.87**.
- WINTER15 had the lowest average order value among the listed coupon categories: **1,035.90**.
- 309 records have no CouponCode recorded. For analysis, these were labeled "No Coupon"; this should not be interpreted as definitive proof that a customer did not use a coupon.

Coupon analysis shows association between coupon category and order value/revenue, but it does not establish causation.

## 10. Order Status Analysis

| Status | Orders | Revenue | Average Order Value |
|---|---:|---:|---:|
| Cancelled | 250 | 276,396.21 | 1,105.58 |
| Pending | 237 | 256,328.15 | 1,081.55 |
| Shipped | 235 | 246,159.58 | 1,047.49 |
| Returned | 247 | 243,277.70 | 984.93 |
| Delivered | 231 | 242,600.32 | 1,050.22 |

The most important observation is that **Cancelled orders have the highest associated order value**, with 250 orders representing 276,396.21 in TotalPrice. This warrants further investigation into cancellation reasons and potential financial impact.

The dataset does not provide enough information to classify this amount as actual lost revenue because refund/payment settlement information is not available.

## 11. Outlier Analysis

The IQR method was used to identify unusual TotalPrice values.

- Q1: **410.52**
- Q3: **1,578.475**
- IQR: **1,167.955**
- Upper outlier threshold: **3,330.4075**
- Detected outliers: **8**

All eight detected outliers have Quantity = 5 and TotalPrice above the upper threshold.

The outliers appear internally consistent with Quantity × UnitPrice. Therefore, they were retained rather than removed. They represent high-value orders that should be investigated rather than automatically treated as errors.

## 12. Correlation Analysis

| Variable Pair | Correlation |
|---|---:|
| UnitPrice – TotalPrice | 0.717 |
| Quantity – TotalPrice | 0.615 |
| Quantity – ItemsInCart | 0.650 |
| ItemsInCart – TotalPrice | 0.393 |
| Quantity – UnitPrice | 0.015 |
| UnitPrice – ItemsInCart | 0.001 |

The strongest relationship is between **UnitPrice and TotalPrice (0.717)**, followed by **Quantity and TotalPrice (0.615)**.

Quantity and UnitPrice have almost no linear relationship (0.015).

Correlation indicates association, not causation.

## 13. Business Recommendations

1. **Investigate cancellations:** Cancelled orders represent the highest associated order value. Analyze cancellation reasons, customer segments, products, and timing to understand the issue.
2. **Monitor high-value products:** Chair, Printer, and Laptop contribute strongly to revenue and should receive close attention in inventory and sales planning.
3. **Evaluate referral channels:** Instagram has the highest order volume and revenue, while Facebook has a higher average order value. Marketing performance should therefore be evaluated using both volume and value.
4. **Evaluate coupon effectiveness:** FREESHIP performs strongly by order count and revenue, but further analysis is needed to determine whether coupons actually cause higher sales.
5. **Investigate high-value outliers:** The eight outliers should be monitored for unusual customer behavior or order patterns, while retaining them because they are internally consistent.
6. **Use multiple KPIs:** Order count alone is insufficient. Revenue and average order value should be considered together when evaluating products, payment methods, marketing sources, and promotions.

## 14. Visualizations Created

The project generates the following charts:

- Total Price Distribution
- Total Price Boxplot
- Revenue by Product
- Orders by Order Status
- Monthly Revenue Trend
- Revenue by Payment Method
- Revenue by Referral Source
- Average Order Value by Coupon
- Correlation Heatmap
- Revenue by Order Status

## 15. How to Run

### Install dependencies

```bash
python -m pip install pandas numpy matplotlib seaborn openpyxl
```

### Run the analysis

```bash
python project2_.py
```

The script saves visualization files in the `charts/` directory.

## 16. Conclusion

The EDA transformed the order dataset into actionable analytical observations. The analysis identified differences between order volume and revenue, highlighted important product and marketing patterns, identified high-value order outliers, and revealed relationships among numerical variables.

The analysis can serve as a foundation for more advanced reporting, dashboard development, customer analysis, and predictive modeling.
