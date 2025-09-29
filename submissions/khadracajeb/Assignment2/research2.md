# Research Paper: Employee Performance Dataset

## 1. Title & Collection Method

**Title:** Employee Performance Dataset  

**Collection Method:**  
This dataset was collected using a survey questionnaire distributed to 50 employees from a large organization. Employees provided information about their daily work hours, tasks completed, job role, and attendance.  

Each employee answered questions regarding:

- **Daily Work Hours** – number of hours worked per day  
- **Tasks Completed per Day** – number of tasks completed each day  
- **Job Role** – position within the company (Manager, Developer, Accountant, Salesperson,Designer, HR Officer, etc.)  
- **Attendance %** – percentage of days attended  

---

## 2. Description of Features & Label

The dataset contains 4 features (X) and 1 label (y):
**Label (x):** 

- **Daily Work Hours (X1, numeric):** Number of hours worked per day  
- **Tasks Completed per Day (X2, numeric):** Number of tasks completed daily  
- **Job Role (X3, categorical):** Employee’s position (Manager, Developer, Accountant, Salesperson,Designer, HR Officer, etc.)  
- **Attendance % (X4, numeric, 0–100):** Percentage of days attended  

**Label (y):**  
- **Productivity Level:** High / Medium / Low  

**Task:** Classification — predicting whether an employee’s productivity is High, Medium, or Low based on work habits.  

---

## 3. Dataset Structure

- **Rows:** 50 employees (samples)  
- **Columns:** 5 (4 features + 1 label)  

**Sample Table (10 Employees):**

| Daily Work Hours | Tasks Completed | Job Role      | Attendance % | Productivity |
|-----------------|----------------|---------------|--------------|--------------|
| 8               | 7              | Developer     | 90           | High         |
| 7               | 5              | Manager       | 85           | Medium       |
| 6               | 3              | Accountant    | 70           | Low          |
| 9               | 8              | Salesperson   | 95           | High         |
| 7               | 4              | Salesperson   | 75           | Medium       |
| 10              | 9              | Developer     | 98           | High         |
| 6               | 2              | Accountant    | 60           | Low          |
| 8               | 6              | Salesperson   | 88           | Medium       |
| 7               | 3              | HR Officer    | 65           | Low          |
| 9               | 7              | Salesperson   | 92           | High         |

---

## 4. Quality Issues

During data collection, several issues were identified that may require preprocessing:
## 4. Quality Issues

- **Missing values:** Some employees did not answer all survey questions  
- **Categorical text:** Job Role and Productivity must be encoded for machine learning models  
- **Imbalance:** Some productivity levels (High, Medium, Low) have fewer samples, creating imbalance  
- **Inconsistent reporting:** Some employees reported tasks or hours incorrectly  

---

## 5. Use Case for Machine Learning


This dataset can be used to train a **classification model** to predict whether an employee is likely to have **High, Medium, or Low productivity** based on their work habits.

* Possible algorithms: Logistic Regression, Decision Tree, Random Forest.  
* It could help managers identify **low-performing employees** early and provide additional training or support.

---

## 6. Conclusion

This Employee Performance Dataset, containing 50 samples, provides insight into the relationship between daily work hours, tasks completed, job roles, attendance, and overall productivity.  

