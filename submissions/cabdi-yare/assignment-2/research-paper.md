# Research Paper: Student Reading Habits Dataset

## 1. Title & Collection Method

*Title:* Student Reading Habits and Reading Level Dataset  

*Collection Method:*  
The dataset was obtained from students in my University class and some of my close friends.  
I asked them about their reading habits — their age, book type preferences, how many hours per week they read, their library visits, and in what format they read (Paper, E-book, Both).  
I received some answers in person and took notes on the others informally.

---

## 2. Description of Features & Label

*Features (X):*  
- *Age* → Numeric, age of the person.  
- *Book Type* → Categorical (Fiction, Academic, Non-fiction, Comics).  
- *Hours Reading* → Numeric, hours spent reading per week.  
- *Library Visits* → Numeric, times visited library per week.  
- *Reading Format* → Categorical (Paper, E-book, Both).  

*Label (y):*  
- *Reading Level* → Categorical: High, Medium, Low  

➡ This is a *classification task* (predicting reading level).

---

## 3. Dataset Structure

- *Rows:* 53 students/friends (samples)  
- *Columns:* 6 (5 features + 1 label)  

*Sample Table (10 rows):*

| Age | Book Type   | Hours Reading | Library Visits | Reading Format | Reading Level |
|-----|-------------|---------------|----------------|----------------|---------------|
| 18  | Fiction     | 4             | 1              | E-book         | Medium        |
| 19  | Academic    | 7             | 3              | Paper          | High          |
| 20  | Non-fiction | 2             | 0              | Both           | Low           |
| 21  | Fiction     | 5             | 2              | Paper          | Medium        |
| 22  | Academic    | 8             | 4              | E-book         | High          |
| 18  | Non-fiction | 3             | 1              | Both           | Low           |
| 19  | Fiction     | 6             | 2              | Paper          | Medium        |
| 20  | Academic    | 9             | 5              | E-book         | High          |
| 21  | Non-fiction | 1             | 0              | Both           | Low           |
| 22  | Fiction     | 7             | 3              | Paper          | Medium        |

---

## 4. Quality Issues

- Missing values: Some students did not provide all details.  
- Inconsistent text: e.g., E-book, ebook, Ebook.  
- Duplicates: Some ages or responses repeat.  

---

## 5. Use Case

- *Classification:* Predict reading level (High, Medium, Low) based on reading habits.  
- *Clustering:* Group students by reading patterns or preferences.  
- *Regression (optional):* Predict hours spent reading from other features.  

This dataset can help teachers understand students’ reading habits and identify 
students who might need extra help.