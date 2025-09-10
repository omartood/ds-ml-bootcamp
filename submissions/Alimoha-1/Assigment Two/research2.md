# Research Paper: Blood Type Dataset

## Title & Collection Method

**Title:** Blood Type and Demographic Dataset  
**Collection Method:** Data was collected from **53 individuals** by recording their **name, age, gender, and blood type**. The information was gathered through a **questionnaire** and direct self-registration.

---

## Description of Features & Labels

* **Features (X):**
  1. **Name** (categorical – full name)
  2. **Age** (numeric – person’s age)
  3. **Gender** (categorical – Male/Female)

* **Label (y):**
  * **Blood Type** → (A+, A-, B+, B-, AB+, AB-, O+, O-)

This makes it a **classification task** (predicting blood type based on age and gender).

---

## Dataset Structure

* **Rows:** 53 individuals (samples)  
* **Columns:** 4 (3 features + 1 label)

### Sample Table (10 rows)

| Name                | Age | Gender | Blood Type |
|---------------------|-----|--------|------------|
| Ali                 | 20  | Male   | O-         |
| Xikmah Abdullahi    | 20  | Female | O+         |
| Abdi                | 20  | Male   | O+         |
| Yusuf               | 22  | Male   | O+         |
| Mohamed             | 21  | Male   | O+         |
| Mubarik             | 17  | Male   | O+         |
| Abu Malik           | 29  | Male   | B+         |
| Zaydalli            | 19  | Male   | O+         |
| Cumar Ismacil Muuse | 26  | Male   | B+         |
| Cabdi Salaan Barkhad| 19  | Male   | A+         |

---

## Quality Issues

* **Duplicate entries:** For example, *Azad Daahir Daud* and *Mabruuka Shucayb* appear more than once.  
* **Inconsistent capitalization:** Some names are lowercase, others are uppercase.  
* **Possible age outliers:** The youngest entry is **10 years old**, which may affect dataset balance.  
* **Gender typos:** Some entries wrote “MAle” instead of “Male.”

---

## Use Case

This dataset can be useful for:

* **Machine Learning:** Training a **classification model** to predict **blood type** using features like age and gender.  
* **Healthcare Planning:** Assisting in **blood bank management** by identifying individuals with rare blood types (e.g., O-).  
* **Data Cleaning Practice:** Good for practicing **data preprocessing** (removing duplicates, fixing typos, encoding categorical data).

---
-