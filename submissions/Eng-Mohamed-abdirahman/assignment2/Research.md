# Research Paper: Customer Satisfaction Survey Dataset

## Title & Collection Method
**Title:** Customer Satisfaction Survey for Local Businesses  
**Collection Method:** I designed a survey questionnaire and collected responses from 120 customers who visited local businesses (restaurants, shops, and service providers) in Borama. Each customer provided feedback about their experience, service quality, pricing, and overall satisfaction.

---

## Description of Features & Labels

### Features (X):
- **Customer Age** (numeric, 18–65)  
- **Gender** (categorical: Male, Female)  
- **Type of Business Visited** (categorical: Restaurant, Retail, Service)  
- **Service Quality Rating** (numeric, 1–5)  
- **Product/Service Price Satisfaction** (numeric, 1–5)  
- **Frequency of Visits per Month** (numeric)  

### Label (y):
- **Overall Satisfaction → Satisfied / Not Satisfied**  

This makes the problem a **classification task** (predicting customer satisfaction).

---

## Dataset Structure
- **Rows:** 120 customers (samples)  
- **Columns:** 7 (6 features + 1 label)  

---

## Sample Table (10 rows)

| Age | Gender | Business Type | Service Quality | Price Satisfaction | Visits/Month | Overall Satisfaction |
|-----|--------|---------------|-----------------|-------------------|--------------|----------------------|
| 25  | Male   | Restaurant    | 4               | 5                 | 3            | Satisfied            |
| 32  | Female | Retail        | 3               | 2                 | 2            | Not Satisfied        |
| 41  | Male   | Service       | 5               | 4                 | 4            | Satisfied            |
| 22  | Female | Restaurant    | 2               | 3                 | 1            | Not Satisfied        |
| 29  | Male   | Retail        | 4               | 4                 | 5            | Satisfied            |
| 35  | Female | Service       | 3               | 3                 | 2            | Not Satisfied        |
| 27  | Male   | Restaurant    | 5               | 5                 | 6            | Satisfied            |
| 30  | Female | Retail        | 2               | 2                 | 1            | Not Satisfied        |
| 40  | Male   | Service       | 4               | 3                 | 3            | Satisfied            |
| 23  | Female | Restaurant    | 5               | 4                 | 4            | Satisfied            |

---

## Quality Issues
- **Missing values:** Some customers skipped the “Price Satisfaction” rating.  
- **Categorical encoding:** Gender and Business Type need to be encoded for ML.  
- **Imbalance:** 90 customers satisfied, 30 not satisfied (imbalanced dataset).  
- **Inconsistent responses:** Some customers wrote “Rest” instead of “Restaurant.”  

---

## Use Case
This dataset can be used to train a **classification model** to predict whether a customer is satisfied or not based on their demographics and business experience.

### Possible Algorithms:
- Logistic Regression  
- Decision Tree  
- Random Forest  

### Practical Application:
Local business owners can use the insights to improve service quality, adjust pricing strategies, and increase customer loyalty.

---
