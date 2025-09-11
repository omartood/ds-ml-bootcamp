# Research Paper: Student Sleep per Night Dataset  

## Title & Collection Method  

**Title:** Student Sleep per Night Dataset  
**Collection Method:** A **survey questionnaire** was designed and distributed to **50 students** (from different grade levels, including University, High School forms, and lower classes). Each student provided information about their **age, gender, grade level, daily study hours, caffeine intake, screen time**, and their **average sleep hours per night**.  

---

## Description of Features & Label  

* **Features (X):**  

  1. **Age** – Numeric (years)  
  2. **Gender** – Categorical (Male / Female)  
  3. **Grade Level** – Categorical (University, Form 1–4, Class 6–8, etc.)  
  4. **Study Hours per Day** – Numeric (average daily hours studied)  
  5. **Caffeine Intake per Day** – Numeric (cups or equivalent units)  
  6. **Screen Time per Day** – Numeric (hours spent on screens)  

* **Label (y):**  

  * **Hours Slept per Night** – Numeric  

This makes the problem a **regression task**, where the goal is to predict the **average hours of sleep per night** based on demographic and lifestyle factors.  

---

## Dataset Structure  

* **Rows (Samples):** 50 students  
* **Columns:** 7 (6 features + 1 label)  

### Sample Table (10 rows)  

| Age | Gender | Grade Level | Study Hours | Caffeine Intake | Screen Time | Hours Slept |
|-----|--------|-------------|-------------|-----------------|-------------|-------------|
| 20  | Male   | University  | 2           | 1               | 4           | 8           |
| 19  | Female | University  | 4           | 2               | 7           | 6           |
| 21  | Male   | University  | 5           | 1               | 6           | 6           |
| 23  | Male   | University  | 5           | 0               | 6           | 8           |
| 18  | Female | University  | 3           | 1               | 8           | 7           |
| 23  | Male   | University  | 4           | 0               | 4           | 9           |
| 24  | Male   | University  | 6           | 1               | 3           | 8           |
| 21  | Male   | University  | 3           | 0               | 7           | 5           |
| 20  | Female | University  | 2           | 2               | 9           | 4           |
| 23  | Male   | University  | 4           | 0               | 5           | 6           |  

---

## Data Quality Issues  

1. **Inconsistent categorical values** – Some entries for *Grade Level* are written differently (e.g., "form 1", "Form 1", "class 8").  
2. **Case sensitivity** – Some entries in *Gender* are lowercase (e.g., "female" instead of "Female").  
3. **Sample size** – Only 50 records, which may limit model generalization.  
4. **Missing context** – Caffeine intake unit (cups vs. mg) was not standardized.  

---

## Use Case  

This dataset can be used to train a **regression model** to predict **student sleep duration per night**.  

* Possible algorithms: **Linear Regression, Random Forest Regressor, Gradient Boosting**.  
* Potential applications:  
  - Understand how **study load, caffeine use, and screen time** affect student sleep.  
  - Provide insights for **health professionals and educators** to encourage better sleep hygiene.  
  - Support interventions for students struggling with **sleep deprivation**.  
---