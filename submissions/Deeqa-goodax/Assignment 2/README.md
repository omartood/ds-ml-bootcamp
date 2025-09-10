# Lifestyle Habits and Productivity Dataset

## 📌 Project Overview
This project explores how **daily lifestyle habits** (study hours, sleep, phone usage, work hours, relaxation) affect a person’s **productivity score** (rated 1–10).  
The dataset was collected using a **Google Form survey** with **50 participants**.

The goal is to analyze this dataset and prepare it for use in **Machine Learning** models, particularly **regression tasks**.

---

## 📊 Dataset Details
- **Rows (Samples):** 50 participants  
- **Columns (Features + Label):** 6  
- **Features (X):**
  - Study Hours per Day
  - Sleep Hours per Day
  - Phone/Social Media Usage
  - Work Hours
  - Relaxation Hours
- **Label (y):**
  - Productivity Score (1–10)

---

## 🛠️ Quality Issues
- Inconsistent formats (e.g., `6`, `6hours`, `6-7 hours`)  
- Typos (e.g., `4hpurs`)  
- Categorical ranges instead of numeric values (`2-3 hours`)  
- Small dataset (50 rows, needs more for robust ML models)

---

## 🚀 Use Case
This dataset can be used to train **regression models** to predict productivity based on lifestyle habits.  
Possible algorithms:
- Linear Regression  
- Random Forest  
- Gradient Boosting  

**Applications:**  
- Students can identify how habits affect their performance.  
- Educators can detect at-risk students early.  
- Workplaces can analyze the effect of work-life balance on productivity.

---

## 📈 Insights (from initial analysis)
- Higher **study** and **sleep** hours → better productivity.  
- Excessive **phone/social media usage** → lower productivity.  
- Balanced **relaxation** helps maintain productivity.  

---

## 🔮 Future Work
- Clean and preprocess the dataset (handle ranges, typos, categorical encoding).  
- Collect **100+ more samples** for stronger predictions.  
- Add more features (diet, exercise, stress levels).  
- Train and compare multiple regression models.  

---

## 📂 Repository Structure