# Research Paper: Workout and Calories Burned Dataset

## Title & Collection Method

*Title:* Workout Patterns and Calories Burned Dataset  
*Collection Method:*  
The dataset was collected by tracking *daily exercise activities* of *50 participants* for one week. Each participant recorded details about their *exercise type, duration, intensity level, and body weight, along with the estimated **calories burned* during each session. Data was self-reported and cross-verified using fitness tracker apps where available.

---

## Dataset Description

The dataset explores the relationship between *exercise behavior* (type, duration, intensity, weight,age) and the corresponding *calories burned*. It is designed for use in predictive modeling, fitness analytics, and personalized workout recommendations.

### Features (X):

1. *Exercise Type* – Categorical (Running, Cycling, Push-ups, Squats)  
2. *Duration (minutes)* – Numeric (total time spent exercising)  
3. *Intensity Level* – Categorical (Low, Medium, High)  
4. *Body Weight (kg)* – Numeric (participant’s weight)  

### Label (y):

- *Calories Burned* – Numeric (continuous value in kcal)  

This makes the dataset suitable for a *regression task* (predicting calories burned).

---

## Dataset Structure

- *Rows (samples):* 12 participants  
- *Columns (variables):* 5 (4 features + 1 label)  

### Sample Records (12 rows)

|  | Exercise Type  | Duration| Repitation | Intensity | Age | Wieght(Kg) | Calories Burned |
|----|----------------|---------------------|------------|-----------|-----|------------|-----------------|
| 1  | Push-ups       | 20                  |            | Low       | 20  | 56         | 200             |
| 2  | Push-ups       | 20                  | 3          | Medium    | 18  | 50         | 210             |
| 3  | Push-ups       | 30                  | 10         | High      | 19  | 55         | 2               |
| 4  | Running        | 30                  | 1          | Medium    | 21  | 70         | 100             |
| 5  | Jump Rope      | 30                  | 3          | Medium    | 22  | 43         | 12              |
| 6  | Push-ups       | 20                  | 10         | Medium    | 18  | 58         | 2               |
| 7  | Running        | 40                  | 7          | Medium    | 25  | 56         | 3               |
| 8  | Squats         | 10                  |            | Medium    | 19  | 60         | 15              |
| 9  | Push-ups       | 20                  | 3          | Medium    | 21  | 54         | 32              |
| 10 | Push-ups       | 60                  | 100        | High      | 23  | 65         | 50              |
| 11 | Push-ups       | 20                  | 21         | Medium    | 20  | 58         | 1               |
| 12 | Maba sameeyo   | 0.1                 |            | Low       | 22  | 50         | 0.1             |
---

## Data Quality Issues

Based on the collected dataset, the following issues were identified:

### 1. Missing Values
- *Repetition* column has missing entries in rows *1, 8, and 12*.  
  - Example: Cardio exercises such as Running and Squats had no repetitions recorded.  
  - Row 12 ("Maba sameeyo") also has no repetition value.

### 2. Anomalies in Calories Burned
- Some calorie values are *unrealistically low* given the exercise type, duration, and weight.  
  - Row 3: Push-ups, 30 minutes, 10 reps → only *2 calories burned*.  
  - Row 7: Running, 40 minutes, 7 reps → only *3 calories burned*.  
  - Row 11: Push-ups, 20 minutes, 21 reps → only *1 calorie burned*.  
  - Row 12: Maba sameeyo, 0.1 minutes → *0.1 calories burned*.  

### 3. Inconsistent Exercise Names
- Row 12 includes "Maba sameeyo" (Somali for I didn’t do it), which is not a valid exercise type.  

### 4. Duration Formatting Issues
- Row 12 has a *decimal value (0.1 minutes = 6 seconds)*, which is inconsistent with the rest of the dataset (all integers).  

---

## Summary
The dataset contains *missing values, anomalies, and inconsistent labels. These issues need to be addressed during the **data cleaning and preprocessing stage* before training any machine learning model.

---

## Applications & Use Cases

This dataset is useful for building predictive models and fitness insights:

- *Regression algorithms:* Linear Regression, Random Forest Regressor, Gradient Boosting.  
- *Personalized fitness apps:* Predict calories burned based on activity type, duration, and weight.  
- *Health & wellness research:* Analyze the impact of intensity and exercise type on energy expenditure.  
- *Weight management tools:* Provide calorie burn estimates for diet and training planning.  

---

## Conclusion

The *Workout and Calories Burned Dataset* highlights the relationship between physical exercise patterns and energy expenditure. While limited by self-reporting bias and device variability, the dataset provides valuable input for *machine learning models*, fitness recommendation systems, and personalized health interventions.
