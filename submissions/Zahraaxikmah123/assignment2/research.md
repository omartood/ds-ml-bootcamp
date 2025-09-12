# 📝 Research Paper: Food & Coffee Preferences Dataset

## Title & Collection Method

**Title:** Food & Coffee Preferences and Their Impact on Productivity  
**Collection Method:** I designed a Google Form survey and shared it with university students and other friends. The survey collected **71 responses** within two days. Questions covered eating habits, coffee consumption, spending patterns, and productivity levels. The dataset is **self-collected**, not from any pre-made repository.

---

## Description of Features & Label

**Features (X):**

1. **Age** (numeric)  
2. **Coffee Consumption** (binary: Yes/No)  
3. **Cups of Coffee per Day** (numeric)  
4. **Preferred Coffee Type** (categorical: Espresso, Cappuccino, Latte, etc.)  
5. **Sugar Usage in Coffee** (categorical: Yes/No)  
6. **Daily Spending on Food/Drinks** (numeric, $USD)  
7. **Favorite Meal of the Day** (categorical: Breakfast, Lunch, Dinner, Snacks)  

**Label (y):**

* **Productivity Rating (1–5)** → A self-reported measure of how productive the person feels daily.  

---

## Dataset Structure

* **Rows:** 71 participants  
* **Columns:** 8 (7 features + 1 label)  

### Sample Table (10 rows)

| Age | Coffee Consumption | Cups of Coffee | Preferred Coffee Type | Sugar Usage | Daily Spending | Favorite Meal | Productivity Rating |
|-----|--------------------|----------------|-----------------------|-------------|----------------|---------------|----------------------|
| 20  | Yes                | 2              | Iced coffee           | Yes         | 3              | Lunch         | 3 |
| 20  | Yes                | 1              | Black coffee          | Yes         | 5              | Lunch         | 1 |
| 25  | Yes                | 1              | Cappuccino            | Yes         | 0.5            | Breakfast     | 1 |
| 23  | Yes                | 1              | Black coffee          | Yes         | 2              | Dinner        | 2 |
| 21  | Yes                | 1              | Latte                 | Yes         | 2              | Lunch         | 1 |
| 18  | Yes                | 1              | Black coffee          | Yes         | 3              | Lunch         | 3 |
| 28  | Yes                | 1              | Other                 | Yes         | 2              | Lunch         | 3 |
| 23  | No                 | —              | —                     | Yes         | 0.25           | Snacks        | 1 |
| 20  | Yes                | 1              | Black coffee          | Yes         | 2              | Breakfast     | 1 |
| 24  | Yes                | 1              | Iced coffee           | Yes         | 10             | Lunch         | 1 |

---

## Quality Issues

* **Missing values:** Some rows have missing data (e.g., Age, Cups of Coffee, Preferred Coffee Type).  
* **Categorical encoding needed:** Coffee Consumption, Preferred Coffee Type, Sugar Usage, and Favorite Meal must be encoded before modeling.  
* **Outliers:** Daily Spending can contain extreme values (e.g., `1000`) which must be handled.
* **Imbalance:** Productivity values are skewed (more low ratings than high ratings).  
* **Inconsistent entries:** Cups of Coffee sometimes uses values like `"4+"` instead of numeric.  

---

## Use Case

This dataset can be applied to a **regression task** predicting productivity levels based on coffee and spending habits.  

* Possible models: **Linear Regression, Random Forest Regressor, Gradient Boosting**  

It can also be applied to **classification**, e.g., predicting **High vs. Low productivity**.  

* Possible models: **Logistic Regression, Random Forest Classifier, Gradient Boosting Classifier**  

It can also be used for **clustering**, e.g., segmenting people into groups:  

* Coffee-heavy consumers with high productivity  
* Non-coffee consumers with low productivity  
* Balanced consumers with medium productivity  

---

## Conclusion

This dataset of 71 samples highlights the relationship between **coffee consumption, spending habits, and productivity levels**. Despite quality issues (missing values, outliers, imbalance, inconsistent entries), it provides a solid foundation for building Machine Learning models.  

The main goal is to understand how **coffee and food preferences** affect daily productivity. These insights could lead to practical applications such as **personalized marketing for cafés**, improved academic productivity strategies, and **awareness of lifestyle impacts on performance**.