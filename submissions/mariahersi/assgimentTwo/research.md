# Research Paper: Nutrition and Food Habits Dataset

## Title & Collection Method

*Title:* Nutrition and Food Habits of University Students
*Collection Method:* I designed a survey questionnaire and asked 10 students at my university about their daily meals, fluid intake, and consumption of fruits, vegetables, and snacks. Each student provided responses about the number of meals per day, frequency of consumption, portion sizes, water intake, and overall dietary quality.

---

## Description of Features & Labels

* *Features (X):*

  1. Age Group (categorical: 18–20, 21–23, 24–26)
  2. Meals per Day (categorical: 1 meal, 2 meals, 3 meals, 4 or more meals)
  3. Meal Frequency (categorical: Never, 1–2 days, 3–4 days, 5–6 days, Every day)
  4. Fruit Servings per Day (numeric)
  5. Vegetable Servings per Day (numeric)
  6. Snack Frequency (categorical: Never, 1 time, 2 times, 3 or more times)
  7. Water Intake per Day (categorical: Less than 1 liter, 1–1.5 liters, 1.5–2 liters, More than 2 liters)
  8. Sugary Drinks per Week (categorical: Never, 1–2 days/week, 3–4 days/week)
  9. Fast Food Consumption per Week (categorical: 0 days, 1–2 days, 3–4 days, 5 or more days)

* *Label (y):*

  * Overall Dietary Quality → Very low / Low / Okay / High / Very high

This makes the problem a classification task (predicting dietary quality).

---

## Dataset Structure

* *Rows:* 10 students (samples)
* *Columns:* 9 features + 1 label

### Sample Table (10 rows)

| Age Group | Meals/Day | Meal Frequency | Fruit Servings | Veg Servings | Snack Frequency | Water Intake  | Sugary Drinks | Fast Food | Dietary Quality |
| --------- | --------- | -------------- | -------------- | ------------ | --------------- | ------------- | ------------- | --------- | --------------- |
| 21–23     | 3 meals   | Every day      | 0              | 0            | 1 time          | 1–1.5 liters  | 1–2 days/week | 0 days    | Okay            |
| 21–23     | 2 meals   | 1–2 days       | 1 serving      | 0            | 2–3 times       | More than 2 L | 1–2 days/week | 1–2 days  | Okay            |
| 21–23     | 3 meals   | 5–6 days       | 2 servings     | 1 can/glass  | 2–3 times       | 1–1.5 liters  | 1–2 days/week | 3–4 days  | Low             |
| 21–23     | 2 meals   | 3–4 days       | 1 serving      | 2            | 4 or more times | Less than 1 L | 1–2 days      | –         | High            |
| 18–20     | 1 meal    | Never          | 2 servings     | 0            | 1 time          | 1–1.5 liters  | 1–2 days/week | 3–4 days  | High            |
| 18–20     | 2 meals   | Every day      | 1 serving      | 1 can/glass  | 1 time          | 1–1.5 liters  | 1–2 days/week | 3–4 days  | Okay            |
| 18–20     | 1 meal    | Never          | 0 servings     | 0            | Never           | Less than 1 L | Never         | 0 days    | Very low        |
| 24–26     | 4+ meals  | Every day      | 5+ servings    | 3 or more    | 4+ times        | More than 2 L | 3–4 days/week | 5+ days   | Very high       |
| 21–23     | 2 meals   | 3–4 days       | 1 serving      | 1 can/glass  | 1 time          | 1–1.5 liters  | 1–2 days/week | 3–4 days  | High            |
| 18–20     | 2 meals   | Every day      | 2 servings     | 1 can/glass  | Never           | 1.5–2 liters  | Never         | 0 days    | Very high       |

---

## Quality Issues

* *Missing values:* Some students skipped the fast food question.
* *Categorical text:* Meal frequency, water intake, and dietary quality must be encoded for ML.
* *Imbalance:* Only a few students are “Very low” quality; most are Okay/High.
* *Inconsistent reporting:* Some wrote “4+ meals” while others wrote “or more meals.”

---

## Use Case

This dataset can be used to train a classification model to predict whether a student’s dietary quality is low, okay, or high based on their nutrition habits.

* Possible algorithms: Decision Tree, Random Forest, Logistic Regression.
* It could help nutritionists or universities identify students who may need dietary guidance.