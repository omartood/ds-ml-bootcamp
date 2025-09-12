# Research Paper: Student Well-being and Mental Health Dataset

## Title & Collection Method

**Title:** Student Well-being and Mental Health Dataset.

**Collection Method:** I designed an anonymous online **survey questionnaire using Google Forms.** I collected data from **57 students,** gathering information about their academic life, lifestyle habits, and mental well-being using a validated scale. This method was chosen to ensure confidentiality and to gather a mix of quantitative and categorical data.

---

## Description of Features & Labels

My dataset contains a mix of quantitative and categorical features. The primary objective is to use these features (**X**) to predict a student's level of depression (**y**).

### Features (X):

1.  `academic_pressure` (ordinal: a 1-5 scale)
2.  `cgpa` (numeric: a score likely out of 10)
3.  `study_satisfaction` (categorical: e.g., 'Satisfied', 'Neutral')
4.  `sleep_hours` (categorical: e.g., '4-6 hours', '6-8 hours')
5.  `dietary_habits` (categorical: e.g., 'Healthy', 'Unhealthy')
6.  `financial_stress` (ordinal: a 1-5 scale)
7.  `study_hours` (categorical: e.g., '5-10 hours', '11-15 hours')

### Label (y):

* `depression_level` → 'low', 'Medium', 'high' (or similar categories)

This makes the problem a **classification task**, as the goal is to predict a specific category.

---

## Dataset Structure

* **Rows:** 57 students (samples)
* **Columns:** 8 (7 features + 1 label)

### Sample Table (10 rows)

| academic_pressure | cgpa | study_satisfaction | sleep_hours | dietary_habits | financial_stress | study_hours | depression_level |
|---|---|---|---|---|---|---|---|
| 5 | 8 | Neutral | 4-6 hours | Healthy | 5 | Less than 5 hours | Medium |
| 1 | 8.2 | Satisfied | 4-6 hours | Healthy | 2 | More than 20 hours | low |
| 4 | 8.1 | Dissatisfied | 6-8 hours | Mixed | 2 | Less than 5 hours | low |
| 4 | 8.2 | Neutral | 4-6 hours | Healthy | 3 | 5-10 hours | low |
| 2 | 7.5 | Very Satisfied | 8-10 hours | Healthy | 1 | 11-15 hours | Medium |
| 3 | 7.8 | Neutral | 6-8 hours | Mixed | 2 | 5-10 hours | low |
| 1 | 9 | Very Satisfied | 8-10 hours | Healthy | 1 | 16-20 hours | low |
| 5 | 7.2 | Dissatisfied | 4-6 hours | Unhealthy | 4 | Less than 5 hours | Medium |
| 4 | 7.9 | Neutral | 6-8 hours | Mixed | 3 | 11-15 hours | low |
| 2 | 8.5 | Very Satisfied | 8-10 hours | Healthy | 2 | More than 20 hours | low |

---

## Quality Issues

* **Categorical text:** Features like `study_satisfaction`, `sleep_hours`, `dietary_habits`, and `study_hours` are in text format and must be encoded for a machine learning model.
* **Imbalance:** The number of students in the `low` depression category is likely much higher than in the `Medium` or `High` categories, resulting in an imbalanced dataset.
* **Inconsistent reporting:** The `cgpa` values should be checked for consistent formatting and scale.
* **Outliers:** There are several potential outliers in the `cgpa` column. Some students filled in values like **80, 90, and 78**, which are far outside the expected scale and may be due to data entry errors.

---

## Use Case

This dataset can be used to train a **classification model** to predict a student's **depression level** based on their lifestyle and academic habits. 

* Possible algorithms include Logistic Regression, Decision Tree, and Random Forest.
* The resulting model could be a valuable tool for university counseling services to identify students who may be at a **higher risk for depression** based on their habits. This could help them provide proactive support and resources.