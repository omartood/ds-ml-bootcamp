
# Short Research Paper: Sleep & Productivity Dataset

## Title & Collection Method

**Title:** Sleep & Productivity Dataset for Lifestyle Analysis  

**Collection Method:**  
The dataset records daily habits related to sleep and screen usage to analyze their effect on personal productivity. Data can be collected through self-tracking (using apps like Google Fit, Apple Health, or manual logs) or surveys of classmates/friends. Each record corresponds to one day for one person. The dataset has at least 50 rows (observations) and 6 columns (5 features + 1 label).

---

## Description of Features & Labels

**Input Features (X):**  

- **Age** – Numeric variable (in years).  
- **Gender** – Categorical (Male/Female/Other).  
- **Sleep Hours** – Numerical (total hours of sleep per night).  
- **Wake-up Time** – Time of day (morning/evening).  
- **Daily Screen Time** – Numerical (hours spent on phone/computer).  

**Output Label (y):**  

- **Productive Day** – Binary (Yes = had a productive day, No = not productive).  

This can be collected through self-assessment surveys (e.g., “Did you feel productive today?”).

---

## Dataset Structure

The dataset contains **50 rows and 6 columns**. Each row represents one day of recorded data for one person.  

**Sample Table (5 rows):**  

| Age | Gender | Sleep Hours | Wake-up Time | Daily Screen Time | Productive Day |
| --- | ------ | ----------- | -------------| ----------------- | --------------- |
| 22  | Male   | 7.5         | 7:30 AM      | 4.2               | Yes             |
| 21  | Female | 5.0         | 9:00 AM      | 6.5               | No              |
| 23  | Male   | 8.0         | 6:45 AM      | 3.0               | Yes             |
| 20  | Female | 6.0         | 8:15 AM      | 7.0               | No              |
| 24  | Male   | 7.0         | 7:00 AM      | 4.5               | Yes             |

---

## Quality Issues

1. **Missing Values:** Some participants may forget to record sleep hours or screen time.  
2. **Inconsistent Wake-up Times:** Some may log in different formats (e.g., “07:30,” “7:30 AM”).  
3. **Self-Reporting Bias:** Productivity is subjective, and answers may not be fully accurate.  
4. **Class Imbalance:** If most people feel “productive,” the dataset might lack enough “No” labels.  
5. **Duplicate Entries:** Same day may be recorded twice if the survey is filled incorrectly.  

---

## Use Case

This dataset is suitable for multiple machine learning tasks:  

- **Classification** – Predict if a person will have a productive day (Yes/No) based on their sleep and screen habits.  
- **Regression** – Estimate productivity score (if collected on a scale from 1–10).  
- **Clustering** – Group individuals into “healthy sleepers,” “night owls,” and “high screen-time users.”  

**Example Project:**  
A classification model could predict “Will today be a productive day?” based on inputs like sleep hours, wake-up time, and screen time. Such insights could help students and workers optimize their daily routines for better productivity.  

---

## Conclusion

The Sleep & Productivity dataset provides an insightful connection between lifestyle habits and personal outcomes. While it may contain missing values and subjective labels, it is practical for exploring classification models and lifestyle-based prediction systems. This dataset encourages the study of real-world challenges in data preprocessing, behavior prediction, and productivity optimization.
