# Digital Engagement Patterns Research

## Title & Collection Method
This dataset, titled **Digital Engagement Patterns**, explores how individuals engage with social media and mobile apps. The data was collected via a survey, where participants self-reported their age, gender, daily social media and mobile usage, favorite app, and engagement level.

## Description of Features & Labels
**Features (X):**
- Age
- Gender
- Social Media Used Hours
- Daily Mobile Use Hours
- Favorite App
- Number of Social Media Apps Used Daily

**Label (y):**
- Engagement Level (High, Medium, Low)

## Dataset Structure
The dataset contains 50 rows and 7 columns. Below is a sample of 10 rows:

| Age | Gender | Social Media Used Hours | Daily Mobile Use Hours | Favorite App | Number of Apps Used Daily | Engagement Level |
|-----|--------|------------------------|-----------------------|--------------|--------------------------|------------------|
| 22  | male   | 4h30min                | 8hrs                  | tiktok       | 3                        | High             |
| 19  | male   | 3h                     | 5hrs                  | tiktok       | 4                        | medium           |
| 24  | female | 2h24min                | 5hrs                  | facebook     | 3                        | medium           |
| 26  | male   | 6h                     | 9hrs                  | tiktok       | 4                        | High             |
| 23  | male   | 4hrs                   | 6hrs                  | facebook     | 5                        | High             |
| 22  | male   | 2                      | 3                     | youtube      | 2                        | low              |
| 21  | female | 3hrs                   | 4h30min               | instgram     | 3                        | medium           |
| 18  | male   | 3h 45m                 | 5h 30m                | tiktok       |                          | medium           |
| 33  | female | 3h 15m                 | 4h 30m                | facebook     | 2                        | medium           |
| 20  | male   | 7hrs                   | 11h40m                | tiktok       | 6                        | High             |

## Quality Issues
- **Missing Values:** Some rows have missing values (e.g., Number of Apps Used Daily).
- **Inconsistent Formats:** Time values are recorded in different formats (e.g., "4h30min", "4hrs", "2").
- **Duplicates:** No obvious duplicates in the sample, but should be checked in the full dataset.
- **Imbalance:** Engagement Level may be imbalanced (more "medium" and "High" than "low").

## Use Case
This dataset can be used for:
- **Classification:** Predicting engagement level based on usage patterns and demographics.
- **Regression:** Estimating hours spent on social media or mobile use.
- **Clustering:** Grouping users by app preferences or usage habits.

It is suitable for machine learning projects focused on understanding digital behavior, targeting app recommendations, or analyzing engagement trends.
