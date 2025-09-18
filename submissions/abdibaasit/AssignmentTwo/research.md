# Practical Assignment: Data Foundations for Machine Learning

## Title & Collection Method
**Title:** Water Supply Usage and Pricing Dataset  
**Collection Method:** I collected data from 60 households in my city for the past 6 months. Each household provided information on their water meter readings, prices paid, water source, and connection type.

---

## Description of Features & Labels

### Features (X)
1. **CustomerID** (numeric) – Unique ID for each household  
2. **WaterSource** (categorical) – Tap, Well, Borehole  
3. **ConnectionType** (categorical) – Residential, Commercial  
4. **PreviousMonthUsage** (numeric) – Water used in m³  
5. **PreviousMonthPrice** (numeric) – Price paid in USD  
6. **UnitPrice** (numeric) – Price per m³  
7. **AverageUsage** (numeric) – Average monthly usage in last 6 months  

### Label (y)
- **NextMonthPrice** (numeric) – Predicted price for next month  

This makes the problem a **regression task** (predicting a numeric value).

---

## Dataset Structure
- **Rows:** 60 households (samples)  
- **Columns:** 8 (7 features + 1 label)  

---

## Sample Table (10 rows)

| CustomerID | WaterSource | ConnectionType | PreviousMonthUsage | PreviousMonthPrice | UnitPrice | AverageUsage | NextMonthPrice |
|------------|------------|----------------|-----------------|------------------|-----------|-------------|----------------|
| 101        | Tap        | Residential    | 12              | 24               | 2         | 10          | 26             |
| 102        | Tap        | Residential    | 15              | 30               | 2         | 14          | 32             |
| 103        | Well       | Commercial     | 20              | 50               | 2.5       | 18          | 52             |
| 104        | Borehole   | Residential    | 10              | 20               | 2         | 12          | 22             |
| 105        | Tap        | Commercial     | 25              | 60               | 2.4       | 22          | 62             |
| 106        | Borehole   | Residential    | 18              | 36               | 2         | 16          | 38             |
| 107        | Well       | Residential    | 14              | 28               | 2         | 15          | 30             |
| 108        | Tap        | Commercial     | 30              | 72               | 2.4       | 28          | 75             |
| 109        | Borehole   | Residential    | 8               | 16               | 2         | 9           | 18             |
| 110        | Tap        | Residential    | 16              | 32               | 2         | 15          | 34             |

---

## Quality Issues
- **Missing values:** Some households did not provide usage data for all months.  
- **Categorical text:** WaterSource and ConnectionType must be encoded for ML.  
- **Inconsistent reporting:** Some households wrote "tap water" instead of "Tap".  

---

## Use Case
This dataset can be used to train a regression model to predict **NextMonthPrice** based on past usage and prices.  
Possible algorithms: Linear Regression, Decision Tree Regressor, Random Forest Regressor.  

It could help water supply companies predict household bills and detect unusual usage patterns.
