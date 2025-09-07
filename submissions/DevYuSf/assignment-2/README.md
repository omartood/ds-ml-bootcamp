### Assignment 2 – Collecting Real Data

My dataset is about student exam performance. I collected the exam scores of 52 students across different subjects.

**Purpose of the Data**

The purpose of this dataset is to determine the academic status of each student:

- **Graduated:** A student who has marks in all 5 subjects (Windows10, MS-Word, MS-PPT, MS-Excel, and MS-Access).

- **Going to Graduate:** A student who has marks in at least 4 subjects.

- **Intermediate:** A student who has marks in 2 or 3 subjects.

- **Beginner:** A student who has marks in only 0 or 1 subject.

This categorization helps me as a teacher to evaluate students’ progress and readiness.

**Dataset Description**

The dataset consists of 7 columns:

- ***ID*** → Student ID

- ***Name*** → Student’s full name

- ***Windows10*** → Exam score in Windows 10

- ***Ms-Word*** → Exam score in Microsoft Word

- ***Ms-PPT*** → Exam score in Microsoft PowerPoint

- ***Ms-Excel*** → Exam score in Microsoft Excel

- ***Ms-Access*** → Exam score in Microsoft Access

**Why this data?**

I am the teacher who teaches these subjects, and these 52 students are part of my class. This dataset is a real sample of my students’ results (not the entire class).

**Type of Machine Learning Problem**

This dataset is best suited for a classification problem, because the output (student status: Graduated */ Going to Graduate / Intermediate / Beginner*) is a **category/label,** not a continuous number.

If I want to predict students’ marks in a subject (for example, predict MS-Word score based on other scores), then that would be a **regression problem.** But since my main purpose is to classify students into categories, this dataset is for **classification.**
