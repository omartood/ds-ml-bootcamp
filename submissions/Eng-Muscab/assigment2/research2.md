Research Paper: Dataset on Smartphone Usage and Addiction

Author: Moscab Bashir Hassan

1. Title & Collection Method

Title: Behavioral Dataset Linking Smartphone Application Usage to Self-Reported Addiction

Collection Method:
This dataset was collected using a custom-designed digital survey created via Google Forms. The survey was distributed anonymously through social media platforms and personal networks to gather responses from a diverse demographic. The survey aimed to quantify time spent on different smartphone activities (e.g., social media, gaming), usage during critical periods (e.g., nighttime), and directly capture respondents’ self-perceived level of smartphone addiction.

2. Description of Features & Labels

This dataset is structured for binary classification in machine learning, aiming to predict whether a respondent believes they are addicted to their smartphone based on usage patterns and demographic factors.

Features (Input Variables X):
Feature Type Description
Name Categorical (to be removed) Unique identifier for respondent privacy. This feature will be removed during preprocessing as it does not contribute to prediction.
Age Numerical (continuous) Respondent's age in years.
Sex Categorical (binary) Biological sex of the respondent (Male/Female).
DailyUsageHours Numerical (continuous) Total self-reported average daily screen time in hours.
SocialMediaHours Numerical (continuous) Average daily hours spent on social media apps.
GamingHours Numerical (continuous) Average daily hours spent on mobile games.
NightUsage Numerical (continuous) Self-reported smartphone usage after 10:00 PM in hours.
SleepHours Numerical (continuous) Average total sleep per night in hours.
Label (Output Variable y):
Label Type Description
Addiction Categorical (binary) Target variable based on the question: "Do you believe you are addicted to your smartphone?" Values: Yes/No.

Note: Any entries like “Maybe” should be cleaned or removed to maintain a binary classification.

3. Dataset Structure

The collected dataset consists of 63 samples (rows) and 9 original variables (columns): 8 features and 1 label. After removing the Name column, the dataset prepared for ML will have 62 samples and 8 columns.

Sample Table (First 5 Rows):

Age Sex DailyUsageHours SocialMediaHours GamingHours NightUsage SleepHours Addiction
22 Female 7.5 4.0 0.5 2.0 6.0 Yes
19 Male 5.0 2.0 2.0 1.5 7.5 No
34 Male 3.0 1.5 0.0 0.5 8.0 No
17 Female 9.0 5.5 1.0 3.0 5.0 Yes
28 Female 6.0 3.5 0.0 1.0 7.0 Maybe (to be cleaned) 4. Data Quality Issues

Inconsistent Labels: The Addiction label should be binary (Yes/No). Some entries, e.g., “Maybe,” need to be corrected or removed.

Missing Values: Some respondents may have skipped questions, resulting in NaN entries.

Validation Issues: The sum of SocialMediaHours + GamingHours might exceed DailyUsageHours due to self-reporting errors.

Self-Reporting Bias: Respondents may under- or overestimate usage or respond based on social desirability.

Outliers: Extreme values (e.g., GamingHours = 8, SleepHours = 4) may exist, which are valid but could skew models.

5. Use Case in Machine Learning

Task: Binary Classification – predicting whether a person is addicted to their smartphone.

Objective: Train a model to classify individuals as Addicted (Yes) or Not Addicted (No) using demographic and smartphone usage features.

Potential Algorithms:

Logistic Regression: Strong baseline for predicting probability of addiction.

Decision Tree / Random Forest: Captures non-linear relationships (e.g., low SleepHours + high NightUsage → addiction).

Support Vector Machine (SVM): Effective for finding hyperplanes separating classes in feature space.

Applications:

Screening Tool: Build a web/mobile app for users to input habits and receive feedback on addiction risk.

Academic Research: Identify usage behaviors most strongly correlated with addiction.

Public Health: Target digital wellness campaigns to behaviors and demographics at highest risk.
