# Research Paper: Social Media Usage and Academic Performance

## **Title**

**Social Media Usage and Academic Performance Dataset**

---

## **Abstract**

This study presents a dataset collected from **102 undergraduate students** to analyze the relationship between social media usage, study habits, lifestyle, and academic performance. The dataset includes **daily social media hours, preferred platform, study hours, sleep hours, group study participation, and self-reported GPA**. The academic performance is classified as **High (GPA ≥ 3.0)** or **Low (GPA < 3.0)**. This dataset can be used for machine learning models to predict at-risk students and support academic guidance.

---

## **Collection Method**

I conducted a **structured survey** among 102 undergraduate students. Each participant was asked about:

* Daily social media usage,
* Preferred social media platform,
* Study habits (study hours per day),
* Sleep hours per day,
* Participation in group study, and
* **Self-reported GPA**, which was later used to classify **Academic Performance**:
  * High = GPA ≥ 3.0
  * Low = GPA < 3.0

The responses were manually recorded and organized into a dataset with **102 rows and 6 columns**.

**Note:** Since GPA was self-reported, there is a potential **self-reporting bias**.

---

## **Description of Features & Label**

### **Features (X):**

1. **Social Media Hours per Day (numeric)** → Daily time spent on social media.
2. **Preferred Platform (categorical)** → Facebook, TikTok, Instagram, Twitter, YouTube.
3. **Study Hours per Day (numeric)** → Daily study hours.
4. **Sleep Hours per Day (numeric)** → Average sleep hours per day.
5. **Group Study (categorical: Yes/No)** → Whether the student studies with peers.

### **Label (y):**

* **Academic Performance (binary classification)** → High / Low.
  * High = GPA ≥ 3.0
  * Low = GPA < 3.0

This is a **classification problem** suitable for supervised machine learning.

---

## **Dataset Structure**

* **Rows (samples):** 102 students
* **Columns:** 6 (5 features + 1 label)

### **Sample (10 students):**


| Social Media Hours | Platform | Study Hours | Sleep Hours | Group Study | Academic Performance |
| ------------------ | -------- | ----------- | ----------- | ----------- | -------------------- |
| 3.2                | Twitter  | 3.2         | 6.9         | No          | Low                  |
| 4.1                | TikTok   | 2.6         | 6.8         | No          | Low                  |
| 3.6                | TikTok   | 3.1         | 7.5         | Yes         | Low                  |
| 5.1                | YouTube  | 2.2         | 7.3         | No          | Low                  |
| 3.7                | Facebook | 4.1         | 7.6         | Yes         | High                 |
| 2.0                | TikTok   | 2.7         | 7.7         | No          | High                 |
| 6.1                | YouTube  | 1.8         | 5.7         | No          | Low                  |
| 4.6                | YouTube  | 2.0         | 6.5         | No          | Low                  |
| 2.5                | —       | 4.2         | 8.1         | Yes         | High                 |
| 5.5                | Facebook | 3.3         | 7.2         | No          | Low                  |

---

## **Class Distribution**

* **High Performance:** 70 students (≈68.6%)
* **Low Performance:** 32 students (≈31.4%)

**Imbalance Issue:** The dataset is skewed toward “High” performance, which may bias machine learning models.

---

## **Quality Issues**

1. **Missing values:** Some students skipped the “Preferred Platform” question.
2. **Categorical encoding:** “Platform” and “Group Study” need encoding before ML (e.g., one-hot or label encoding).
3. **Imbalance:** High vs Low class distribution may require oversampling (SMOTE) or class weighting.
4. **Self-reporting bias:** Study hours, social media hours, and GPA are self-reported and may not be fully accurate.

---

## **Use Case**

This dataset can be applied in machine learning to:

* **Predict academic performance** based on social media behavior, study habits, and lifestyle.
* **Identify at-risk students** for early intervention and support.
* **Assist educators and counselors** in providing guidance on time management and study strategies.

### **Potential ML Algorithms:**

* Logistic Regression
* Decision Tree / Random Forest
* Support Vector Machine (SVM)
* Gradient Boosting

**Preprocessing Recommendations:**

* Encode categorical features (Preferred Platform, Group Study)
* Normalize numeric features (social media hours, study hours, sleep hours)
* Handle missing values appropriately
* Address class imbalance for better model performance
