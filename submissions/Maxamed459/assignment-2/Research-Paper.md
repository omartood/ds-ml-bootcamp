# Short Research Paper: Movie Dataset Analysis

## Title & Collection Method

**Title:** Movie Metadata Dataset with Viewer Interest

**Collection Method:**  
This dataset contains metadata for 50 movies, collected from publicly available sources such as TMDb (The Movie Database) using API calls. Features include popularity, average user ratings, vote counts, genre, and runtime. An additional column, `is_boring`, represents whether a movie is considered boring (`1`) or interesting (`0`), based on user surveys and reviews. This makes the dataset suitable for classification tasks.

---

## Description of Features & Labels

**Input Features (X):**

- **popularity** – Numerical score representing the movie’s popularity.
- **vote_average** – Average rating from users.
- **vote_count** – Total number of votes received.
- **genre** – Categorical variable representing movie genres, e.g., “Action, Comedy, Thriller.”
- **runtime** – Duration of the movie (hours and minutes).

**Output Label (y):**

- **is_boring** – Binary variable indicating viewer interest: `1` = boring, `0` = interesting.

This dataset is suitable for **classification tasks**, predicting whether a movie will be boring based on its features.

---

## Dataset Structure

The dataset contains **50 rows** and **6 columns**. Each row represents a single movie.

**Sample Table (5 rows):**

| popularity | vote_average | vote_count | genre                     | runtime | is_boring |
| ---------- | ------------ | ---------- | ------------------------- | ------- | --------- |
| 654.6075   | 4.316        | 482        | Sci-Fi, Thriller          | 1h 31m  |           |
| 442.7621   | 6.787        | 409        | Action, Comedy, Crime     | 1h 25m  |           |
| 466.4149   | 7.256        | 248        | Action, Thriller          | 1h 29m  |           |
| 325.6567   | 7.8          | 1866       | Action, Drama             | 2h 36m  |           |
| 306.1502   | 7.526        | 2925       | Sci-Fi, Adventure, Action | 2h 10m  |           |

---

## Quality Issues

1. **Missing Values:** `is_boring` column is empty and needs labeling.
2. **Inconsistent Genre Formatting:** Some genres use inconsistent separators, e.g., `"Action,Crime,Thriller"` vs `"Action, Crime, Thriller"`.
3. **Runtime Format Variability:** Durations appear in multiple formats (e.g., `1h 31m`, `15m`), requiring normalization.
4. **Class Imbalance:** Certain genres such as Action and Drama dominate the dataset.
5. **Potential Duplicates:** Similar movies may appear multiple times.

---

## Use Case

This dataset can be used in multiple machine learning scenarios:

1. **Classification:** Predict if a movie is boring (`is_boring`) based on features like popularity, ratings, genre, and runtime.
2. **Recommendation Systems:** Suggest movies likely to engage viewers by filtering out movies predicted as boring.
3. **Clustering & Segmentation:** Group movies based on similarity in genres, ratings, and runtime, to find patterns in viewer preferences.

**Example Project:**  
A classification model could predict whether a movie will be boring using features such as popularity, vote counts, ratings, genre, and runtime. Streaming platforms could use such predictions to improve content curation and provide personalized recommendations.

---

## Conclusion

This dataset provides a rich resource for classification and recommendation system projects in machine learning. Despite minor quality issues such as missing labels and inconsistent formatting, it supports predictive modeling, clustering, and exploratory data analysis, helping to understand patterns in viewer engagement.
