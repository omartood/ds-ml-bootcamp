Research Paper: AI & Technology Usage Habits Dataset  
1. Title and Data Collection Method  

Title: AI & Technology Usage Habits of University Students  

Collection Method:  

The dataset was collected using a survey questionnaire distributed to 63 university students. 
Each participant provided responses about their,age,hours of sleep, daily technology use, AI 
adoption, device availability, and academic performance. The survey f ocused on understanding 
how technology habits affect academic outcomes. 

2. Dataset Features and Labels  

Features (X):  

• Age (numeric):  
• Sleep Hours per Day (numeric): Average hours of sleep per day.  
• Daily AI Tool Usage (numeric): Average hours per day using AI tools (e.g., ChatGPT, 
Grammarly, coding assistants).  
• Social Media Usage (numeric): Hours spent on platforms like Facebook, TikTok, or 
Instagram.  
• Study Hours per Day (numeric): Average daily hours dedicated to studying.  
• Device Ownership (categorical): Type of primary device used (Laptop, Smartphone, 
Tablet).  
Label (y):  

• Academic Result (classification): Excellent/ Good/ Average/ Poor  
This makes the problem a classification task, predicting a student’s academic result (Excellent, 
Good, Average, or Poor) based on their AI and technology usage Patts . 
Dataset Structure  
• Rows: 63 students (samples)  
• Columns: 7 (6 features + 1 label)  
 
 
 Sample 15-row data :
| Age Range | Sleep Hours | AI Usage | Social Media | Coding Hours | Device     | Performance |
| --------- | ----------- | -------- | ------------ | ------------ | ---------- | ----------- |
| 21–23     | 7–8         | 1–3 hrs  | 3–4 hrs      | 7–10 hrs     | Laptop     | Good        |
| 21–23     | 7–8         | 1–3 hrs  | 3–4 hrs      | 4–6 hrs      | Laptop     | Good        |
| 21–23     | 6–7         | 4–6 hrs  | 3–4 hrs      | 1–3 hrs      | Laptop     | Excellent   |
| 18–20     | 6–7         | 1–3 hrs  | 3–4 hrs      | 1–3 hrs      | Laptop     | Good        |
| 18–20     | 7–8         | 4–6 hrs  | 3–4 hrs      | 4–6 hrs      | Laptop     | Average     |
| 18–20     | 6–7         | 7–10 hrs | 5–6 hrs      | 1–3 hrs      | Laptop     | Excellent   |
| 18–20     | 5–6         | 1–3 hrs  | <1 hr        | 1–3 hrs      | Smartphone | Good        |
| 18–20     | 7–8         | 4–6 hrs  | 3–4 hrs      | 1–3 hrs      | Laptop     | Good        |
| 24–26     | <5          | 1–3 hrs  | >6 hrs       | 1–3 hrs      | Laptop     | Poor        |
| 18–20     | 5–6         | 1–3 hrs  | 5–6 hrs      | 1–3 hrs      | Laptop     | Average     |
| 18–20     | 5–6         | 1–3 hrs  | 1–2 hrs      | 1–3 hrs      | Smartphone | Excellent   |
| 21–23     | 7–8         | 4–6 hrs  | 3–4 hrs      | 1–3 hrs      | Laptop     | Good        |
| >26       | 7–8         | 4–6 hrs  | 3–4 hrs      | 7–10 hrs     | Laptop     | Excellent   |
| 21–23     | 6–7         | 4–6 hrs  | 1–2 hrs      | 4–6 hrs      | Laptop     | Good        |
| 21–23     | >8          | 1–3 hrs  | 3–4 hrs      | 0 hrs        | Smartphone | Poor        |


 
Quality Issues : 
• Categorical text: Age groups, device, and performance labels must be encoded for ML.  
• Imbalance: More students reported “Good”, "average" or “Excellent” performance 
compared to “Poor”.  

Use Case :

This dataset can be used to train a classification model to predict a student’s academic performance based on their technology and AI usage habits.  

Possible algorithms:  Logistic Regression, Decision Tree, Random Forest.  

Educators can use this to:  
• Understand how technology habits affect performance.  
• Identify patterns (e.g., high social media + low sleep → poorer performance).  
• Provide guidance to students on balancing AI, social media, and study time. 
 
 

