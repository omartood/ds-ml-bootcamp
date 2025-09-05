# 📝 Research Paper: Food & Coffee Preferences Dataset

## Title & Collection Method

**Title:** Food & Coffee Preferences and Their Impact on Productivity  
**Collection Method:** I designed a Google Form survey and shared it with university students and other friends. The survey collected **71 responses** within two days. Questions covered eating habits, coffee consumption, spending patterns, and productivity levels. The dataset is **self-collected**, not from any pre-made repository.

---

## Description of Features & Labels

**Features (X):**

1. **Age** (numeric)  
2. **Gender** (categorical: Male, Female, Other)  
3. **Eating Out Frequency per Week** (numeric/categorical)  
4. **Favorite Food Type** (categorical: Somali food, Fast food, etc.)  
5. **Favorite Meal of the Day** (categorical: Breakfast, Lunch, Dinner)  
6. **Coffee Consumption** (binary: Yes/No)  
7. **Cups of Coffee per Day** (numeric)  
8. **Preferred Coffee Type** (categorical: Espresso, Cappuccino, etc.)  
9. **Daily Spending on Food/Drinks** (numeric, $USD)  
10. **Sugar Usage in Coffee** (categorical: None, Low, Medium, High)

**Label (y):**

* **Productivity Rating (1–5)** → A self-reported measure of how productive the person feels daily.

---

## Dataset Structure

* **Rows:** 71 participants  
* **Columns:** 12 (11 features + 1 label)

### Sample Table (10 rows)

| Age | Gender | Eating Out Frequency | Favorite Food Type   | Favorite Meal     | Coffee Consumption | Cups of Coffee | Coffee Type   | Sugar Usage | Drink  | Daily Spending | Productivity |
|-----|--------|----------------------|-------------|----------|--------|------|---------------|-------|--------|----------|--------------|
| 20  | Female | 1–2 times            | Somali food | Lunch    | Yes    | 2    | Iced coffee   | Yes   | Water  | 3        | 3            |
| 20  | Female | Never                | Fast food   | Lunch    | Yes    | 1    | Black coffee  | Yes   | Water  | 5        | 1            |
| 25  | Male   | Never                | Somali food | Breakfast| Yes    | 1    | Cappuccino    | Yes   | Tea    | 0.5      | 1            |
| 23  | Male   | Never                | Somali food | Dinner   | Yes    | 1    | Black coffee  | Yes   | Tea    | 2        | 2            |
| 21  | Female | Never                | Fast food   | Lunch    | Yes    | 1    | Latte         | Yes   | Water  | 2        | 1            |
| 18  | Female | Never                | Somali food | Lunch    | Yes    | 1    | Black coffee  | Yes   | Water  | 3        | 3            |
| 28  | Male   | 1–2 times            | —           | Lunch    | Yes    | 1    | Other         | Yes   | Energy drinks | 2        | 3            |
| 23  | Male   | 1–2 times            | Fast food   | Snacks   | No     | 0    | —             | —     | Tea    | 0.25     | 1            |
| 20  | Female | Never                | Somali food | Breakfast| Yes    | 1    | Black coffee  | Yes   | Water  | 2        | 1            |
| 24  | Female | 1–2 times            | Somali food | Lunch    | Yes    | 1    | Iced coffee   | Yes   | Tea    | 10       | 1            |

---

## Quality Issues

* **Missing values:** The “Food Type” column has a missing value (row 7 shows `—`).  
* **Categorical text:** Columns like Gender, Food Type, Meal, Coffee Type, Drink, Sugar need encoding.  
* **Imbalance:** Productivity values are mostly `1`, which could lead to imbalance if modeling productivity.  
* **Inconsistent entries:** Eating Out Frequency uses `1–2 times` and `Never` inconsistently; Coffee Type has variations like `Black coffee`, `Iced coffee`, `Latte`, `Other`, or `—`.  
* **Inconsistent units:** Spending contains both decimals (e.g., `0.25`) and whole numbers; units should be standardized.  

---

## Use Case

This dataset can be applied to a **regression task** predicting productivity levels based on food and coffee habits.  

* Possible models: **Linear Regression, Random Forest Regressor, Gradient Boosting**.  

It can also be applied to **classification**, e.g., predicting **High vs. Low productivity** based on features like coffee consumption, and daily spending.  

* Possible models: **Logistic Regression, Random Forest Classifier, Gradient Boosting Classifier**.  

It can also be applied to **clustering**, e.g., segmenting people into groups:

* Coffee-heavy spenders with high productivity  
* Non-coffee consumers with low productivity  
* Balanced eaters with medium productivity 

**Practical Impact:**  

* Cafés and food businesses could use these insights to improve **personalized marketing**.  
* Universities could study the relationship between coffee/drinking habits and **academic productivity**.  

👉 This project shows the real-life connection between lifestyle and performance, making it both **fun and useful**. ☕📊

## Conclusion

This dataset of 71 samples highlights the relationship between age, gender, eating habits, coffee consumption, daily spending, and productivity levels. Despite quality issues (missing values, imbalance, inconsistent entries), it provides a solid foundation for building Machine Learning models.

The main goal is to understand how lifestyle habits, particularly food and coffee preferences, relate to daily productivity. These insights could lead to practical applications such as personalized marketing for cafés, improved academic productivity strategies, and awareness of lifestyle impacts on performance.