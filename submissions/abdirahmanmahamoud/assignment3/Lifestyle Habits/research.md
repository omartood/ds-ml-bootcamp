# Research Paper: Lifestyle Habits and Their Effect on Health Status

## 1. Title & Dataset

**Title:** _Lifestyle Habits and Their Effect on Health Status_

**Dataset Source:**\
The dataset consists of information collected from 63 individuals of
different ages. It focuses on daily lifestyle habits such as sleep,
tea/coffee consumption, exercise, healthy meals, and meal frequency.

**Columns:**\

- **Age** -- Age of the individual\
- **SleepHours** -- Average hours of sleep per night\
- **TeaCoffeePerDay** -- Number of cups of tea/coffee consumed daily\
- **ExerciseDays** -- Days of exercise per week\
- **HealthyMeals** -- Number of healthy meals per day\
- **MealsPerDay** -- Total meals per day\
- **HealthStatus** -- Overall health condition (Poor, Average, Good)

---

## 2. Preprocessing & Cleaning

Several preprocessing steps were applied to prepare the dataset for
analysis:

1.  **Handling Missing Values:**
    - Age & SleepHours → filled with **median**\
    - TeaCoffeePerDay & ExerciseDays → filled with **0** (non-users)\
    - HealthyMeals → filled with **median**\
    - MealsPerDay → filled with **mode**\
    - HealthStatus → filled with **Average**
2.  **Duplicates:**
    - Removed duplicate rows.
3.  **Outlier Detection & Handling:**
    - Applied **IQR method** to detect and cap extreme values.
4.  **Encoding:**
    - HealthStatus mapped to numerical values: {Poor = 0, Average = 1,
      Good = 2}.
5.  **Feature Engineering:**
    - **Meals_to_SleepRatio** = MealsPerDay / SleepHours\
    - **Exercise_to_AgeRatio** = ExerciseDays / Age\
    - **Caffeine_to_Meals** = TeaCoffeePerDay / MealsPerDay
6.  **Scaling:**
    - Standardized all numeric features using **StandardScaler**,
      except HealthStatusEncoded.

---

## 3. Findings

- Individuals with **less sleep and higher caffeine intake** generally
  had poorer health status.\
- **Regular exercise** strongly correlated with better health.\
- **Healthy meals** and **balanced meal frequency** positively
  impacted overall health.\
- The data suggested that the balance of **sleep, exercise, and
  nutrition** plays a significant role in determining health outcomes.

---

## 4. Conclusion

This research highlights that daily lifestyle habits such as adequate
sleep, healthy eating, and regular exercise have a strong influence on a
person's overall health. Proper data preprocessing is crucial to ensure
reliable results before conducting deeper statistical analysis or
machine learning modeling.
