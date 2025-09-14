# Student Lifestyle and Social Media Survey

## 1. Title & Collection Method
**Title:** Student Lifestyle and Social Media Usage Dataset  
**Collection Method:**  
The dataset was collected through a self-designed survey/questionnaire distributed among classmates. The survey asked students about their daily habits including sleep, study, social media usage, caffeine intake, and mood. Data collection ensured diversity in age, gender, and daily routines, capturing realistic student behaviors.

---

## 2. Description of Features & Labels
The dataset contains the following variables:

| Feature (X)       | Description                                | Type        |
|------------------|--------------------------------------------|------------|
| Age               | Age of the student in years                | Numeric    |
| Gender            | Male/Female                                | Categorical|
| Sleep Hours       | Average hours of sleep per night           | Numeric    |
| Study Hours       | Average hours spent studying per day       | Numeric    |
| Coffee/Tea Intake | Number of cups of coffee/tea consumed daily| Numeric    |
| Mood              | General mood of the student (Happy/Neutral/Sad) | Categorical |

**Label (y):** Social Media Hours — numeric. Can be used for regression. Mood can be used for classification if needed.

---

## 3. Dataset Structure
- **Rows (samples):** 100  
- **Columns (features + label):** 7  

**Sample Table (10 rows):**

| Age | Gender | Sleep Hours | Study Hours | Social Media Hours | Coffee/Tea | Mood |
|-----|--------|------------|------------|------------------|-----------|------|
| 20  | Male   | 7          | 5          | 4                | 1         | Neutral |
| 19  | Female | 8          | 6          | 5                | 2         | Neutral |
| 26  | Male   | 3          | 12         | 6                | 6         | Happy |
| 20  | Female | 8          | 6          | 3                | 1         | Neutral |
| 22  | Male   | 5          | 3          | 4                | 1         | Neutral |
| 19  | Female | 8          | 6          | 3                | 1         | Happy |
| 23  | Female | 6          | 3          | 5                | 1         | Neutral |
| 21  | Female | 4          | 3          | 6                | 1         | Happy |
| 22  | Female | 7          | 5          | 3                | 1         | Happy |
| 21  | Female | 6          | 5          | 4                | 2         | Sad |

---

## 4. Quality Issues
- The dataset has some realistic data challenges:
- Missing values (NaN): Present in Sleep Hours, Coffee/Tea intake, and Social Media Hours for a few students.
- Outliers: Extreme values such as 24 hours on social media, 0 hours sleep, or very high coffee intake.
- Typographical inconsistencies: Some numeric entries were originally in text form (e.g., “8hr”, “6:00”), later cleaned.
- Imbalance: Mood distribution is roughly balanced but may need adjustment for classification tasks.
- These quality issues make the dataset ideal for practicing preprocessing in machine learning.

---

## 5. Use Case
- **Regression:** predict social media hours from lifestyle features.  
- **Classification:** predict mood from numeric features.  
- **Clustering:** group students by lifestyle patterns.  
- **Data Preprocessing Practice:** handling missing values, outliers, encoding categorical variables, scaling.  

**Summary:**  
The dataset  contains 100 samples, 7 columns, missing values, and outliers. Suitable for regression, classification, and clustering tasks.
