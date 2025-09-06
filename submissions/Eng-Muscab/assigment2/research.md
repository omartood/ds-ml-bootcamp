Research Paper: Dataset on Smartphone Usage and Addiction
Author: Moscab Bashir Hassan

1. Title & Collection Method
   Title: "Behavioral Dataset Linking Smartphone Application Usage to Self-Reported Addiction"

Collection Method: This dataset was collected via a custom-designed digital survey created using Google Forms. The form was distributed anonymously through social media channels and personal networks to gather data from a varied demographic. The survey was designed to quantify time spent on different smartphone activities (social media, gaming) and during critical periods (night usage), and to directly capture the respondent's self-perceived level of addiction.

2. Description of Features & Labels
   This dataset is structured for a classification task in machine learning. The objective is to predict whether a person believes they are addicted to their smartphone based on their usage patterns and demographics.

Features (Input Variables X):

Name: (To be Removed). A unique identifier for respondent privacy. This feature will be dropped for ML as it does not contribute to predictive patterns.

Age: Continuous numerical variable. The respondent's age in years.

Sex: Categorical binary variable. Biological sex of the respondent (Male/Female).

DailyUsageHours: Continuous numerical variable. Total self-reported average daily screen time in hours.

SocialMediaHours: Continuous numerical variable. Average daily hours spent specifically on social media apps.

GamingHours: Continuous numerical variable. Average daily hours spent on mobile games.

NightUsage: Continuous numerical variable. Self-reported usage after 10:00 PM in hours.

SleepHours: Continuous numerical variable. Average total sleep per night in hours.

Label (Output Variable y):

Addiction: Categorical binary variable. The target label based on the direct question: "Do you believe you are addicted to your smartphone?" (Yes/No). This is a clear binary classification label.

3. Dataset Structure
   The collected dataset consists of 63 samples (rows) and 9 original variables (columns): 8 features and 1 label. After removing the Name column, the final dataset for ML will have 62 samples and 8 columns.

Sample Table (First 10 Rows):

Name Age Sex DailyUsageHours SocialMediaHours GamingHours NightUsage SleepHours Addiction
Mohamed 22 Female 7.5 4.0 0.5 2.0 6.0 Yes
Ali 19 Male 5.0 2.0 2.0 1.5 7.5 No
Aisha shamow 34 Male 3.0 1.5 0.0 0.5 8.0 No
Guuleyd osmaan 17 Female 9.0 5.5 1.0 3.0 5.0 Yes
Ahmed hassan 28 Female 6.0 3.5 0.0 1.0 7.0 Maybe
Haaji Ali 45 Male 4.5 1.0 0.0 0.0 7.5 No 4. Quality Issues
This dataset exhibits classic problems found in real-world, self-reported data:

Inconsistent Categorical Label: The primary issue is in the Addiction label (column y). While designed to be binary (Yes/No), a respondent has entered "Maybe". This invalid value creates a third, unintended class and must be corrected during preprocessing (e.g., by imputing a value based on other features or removing the row).

Missing Values: It is highly probable that some respondents skipped one or more questions, leading to blank (NaN) entries in various columns, especially the numerical time-based ones.

Data Validation Issues: The time-based columns (DailyUsageHours, SocialMediaHours, etc.) are susceptible to errors. For example, the sum of SocialMediaHours + GamingHours might logically be less than or equal to DailyUsageHours, but this may not hold true in the data due to reporting errors.

Self-Reporting Bias: All data is self-reported. Respondents may inaccurately estimate their usage times (often underestimating) or answer the Addiction question based on perceived social desirability rather than truth.

Potential for Outliers: There may be extreme values, such as GamingHours = 8 or SleepHours = 4, which could be legitimate but are statistical outliers that may skew a model.

5. Use Case in Machine Learning
   This dataset is ideally suited for a Supervised Learning - Binary Classification project.

ML Task: Binary Classification.

Objective: To train a model that classifies individuals into one of two categories: Addicted (Yes) or Not Addicted (No), based on their demographic and detailed smartphone usage metrics.

Potential Algorithms:

Logistic Regression: A strong baseline model to predict the probability of addiction.

Decision Tree / Random Forest: Excellent for capturing non-linear relationships between features (e.g., low SleepHours and high NightUsage might be a strong predictor of addiction).

Support Vector Machine (SVM): Could be effective in finding a clear hyperplane to separate the two classes in a high-dimensional space.

Application: A successful model could be used to:

Develop a Screening Tool: Create a simple web or mobile app where users input their habits and receive feedback on their potential risk of smartphone addiction, prompting them to seek help or use digital wellness tools.

Academic Research: Identify which specific usage behaviors (e.g., nighttime use, gaming) are the most significant correlates of self-perceived addiction.

Public Health Intervention: Help target digital wellness campaigns towards demographics and behaviors most associated with problematic usage.
