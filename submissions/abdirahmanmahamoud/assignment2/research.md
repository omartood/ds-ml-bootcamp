# Research Paper: Lifestyle Habits and Health Status Dataset

## 1. Title & Collection Method

**Title:** _Lifestyle Habits and Their Effect on Health Status_

**Collection Method:**  
This dataset consists of **50 samples (rows)** collected from **49 community members and one sample from myself**. The data was gathered through **direct interviews, observation, and manual data collection**. Participants were asked about lifestyle habits such as sleep, tea/coffee consumption, exercise, and healthy eating.

---

## 2. Description of Features & Label

The dataset contains **6 features (X)** and **1 label (y):**

- **Age (X1):** The age of the participant (integer, years).
- **SleepHours (X2):** Average hours of sleep per day.
- **TeaCoffeePerDay (X3):** Number of cups of tea/coffee consumed daily.
- **ExerciseDays (X4):** Number of days the participant exercises per week.
- **HealthyMeals (X5):** Number of healthy meals consumed weekly.
- **MealsPerDay (X6):** Number of meals consumed per day.
- **HealthStatus (y):** Health status (categorical: _Good, Average, Poor_).

---

## 3. Dataset Structure

- **Rows:** 50 samples (49 participants + 1 myself).
- **Columns:** 7 (6 features + 1 label).

### Sample Table (10 Rows):

| Age | SleepHours | TeaCoffeePerDay | ExerciseDays | HealthyMeals | MealsPerDay | HealthStatus |
| --- | ---------- | --------------- | ------------ | ------------ | ----------- | ------------ |
| 22  | 5          | 2               | 7            | 1            | 2           | Average      |
| 15  | 8          | 0               | 0            | 0            | 3           | Average      |
| 18  | 4          | 3               | 1            | 0            | 3           | Poor         |
| 65  | 8          | 2               | 0            | 3            | 3           | Good         |
| 14  | 7          | 0               | 1            | 1            | 3           | Average      |
| 47  | 6          | 1               | 0            | 2            | 2           | Good         |
| 24  | 4          | 4               | 2            | 0            | 3           | Poor         |
| 17  | 3          | 0               | 0            | 2            | 3           | Good         |
| 38  | 7          | 1               | 2            | 1            | 3           | Average      |
| 21  | 9          | 0               | 1            | 6            | 2           | Good         |

---

## 4. Quality Issues

During data collection, several issues were identified that require **preprocessing**:

1. **Missing Values:** Some participants skipped questions, resulting in rows with missing values.
2. **Categorical Labels:** HealthStatus is textual (_Good, Average, Poor_), requiring **encoding** (e.g., 0, 1, 2).
3. **Imbalance:** Certain labels (e.g., _Poor_) have fewer samples than others, which could affect model performance.
4. **Human Error:** Possible mistakes in reported values such as sleep hours, tea/coffee cups, or exercise frequency.
5. **Different Scales:** Features such as _Age_ and _ExerciseDays_ are on different scales, requiring **normalization/scaling**.

---

## 5. Use Case for Machine Learning

This dataset can be effectively used for **Machine Learning projects**:

- **Classification:**

  - Predicting _HealthStatus (Good, Average, Poor)_ based on lifestyle habits.
  - Suitable algorithms: _Logistic Regression, Random Forest, SVM, Neural Networks_.

- **Clustering:**

  - Grouping people with similar lifestyle habits (e.g., high sleep vs low sleep groups).

- **Regression (optional):**
  - Predicting values like sleep hours or exercise days based on age and other lifestyle factors.

---

## 6. Conclusion

This dataset of 50 samples highlights the relationship between age, sleep, tea/coffee consumption, exercise, healthy meals, and daily meals with overall health status. Despite quality issues (missing values, imbalance, human error), it provides a **solid foundation for building Machine Learning models**.

The main goal is to understand how lifestyle habits relate to overall health, which could lead to future health solutions and community awareness programs.
