
# Research Paper: Cholera Outbreak Data Collection in Laascaanood

## Title  
**Cholera Outbreak Data Collection in Laascaanood**

---

## Collection Method  
This dataset was collected through **observation and survey**. It represents cases of people affected by cholera in the city of Laascaanood. The dataset considers health-related features, environmental conditions, and demographics of the patients. Some values were filled in to complete the dataset for learning purposes, as real-world health data is not always fully available.  

---

## Features & Label  

- **Age** → numeric  
- **Gender** → categorical (Male/Female)  
- **Access_to_Clean_Water** → categorical (Yes/No)  
- **Sanitation_Level** → categorical (Low/Medium/High)  
- **Hospitalized** → categorical (Yes/No)  
- **Survival_Status (Label y)** → binary (1 = Survived, 0 = Not Survived)  

---

## Dataset Structure  
- **Rows:** 50 samples  
- **Columns:** 6 (5 features + 1 label)  

### Example Sample Table (10 rows)

| Age | Gender | Access_to_Clean_Water | Sanitation_Level | Hospitalized | Survival_Status |
|-----|--------|------------------------|------------------|--------------|-----------------|
| 23  | Male   | No                     | Low              | Yes          | 1 |
| 45  | Female | No                     | Low              | Yes          | 0 |
| 12  | Male   | Yes                    | Medium           | No           | 1 |
| 34  | Female | Yes                    | High             | No           | 1 |
| 67  | Male   | No                     | Low              | Yes          | 0 |
| 29  | Female | Yes                    | Medium           | Yes          | 1 |
| 55  | Male   | No                     | Low              | Yes          | 0 |
| 19  | Female | Yes                    | High             | No           | 1 |
| 41  | Male   | No                     | Low              | Yes          | 0 |
| 15  | Female | Yes                    | Medium           | No           | 1 |

---

## Data Quality Issues  
- **Missing values**: Some records (e.g., “Hospitalized”) may be incomplete.  
- **Categorical text**: Many features are categorical (Yes/No, Male/Female), requiring encoding into numeric values.  
- **Imbalanced dataset**: The majority of patients survived compared to those who did not.  
- **Typos/Inconsistencies**: Text values like “Male/Female” or “Yes/No” may have inconsistent spellings.  

---

## Use Case (ML Application)  
This dataset can be used for **classification tasks**:  
- **Goal**: Predict whether a patient will **survive (1)** or **not survive (0)** cholera based on age, access to clean water, sanitation, and hospitalization status.  
- Potential ML models: **Logistic Regression, Decision Trees, Random Forest, Support Vector Machines (SVM)**.  
- Practical benefit: Understanding how **clean water and sanitation** impact survival outcomes, which can help guide **public health policies**.  
