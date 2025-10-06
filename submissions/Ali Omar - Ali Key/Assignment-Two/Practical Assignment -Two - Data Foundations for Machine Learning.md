# Daily Transportation Costs of University Students in Mogadishu
> **Author: Ali Omar Abdi**  

## 1. Collection Method
This dataset was created by surveying **100 university students in Mogadishu** about their daily transportation habits. Each student answered questions about:
- **Age**
- **Distance** from home to university (in kilometers)
- **Mode of transport** (Bajaj, Bus, Walking, Taxi, Motorcycle)
- **Travel time** (in minutes)
- **Days per week** they attend classes
- **Daily cost of transport** (in USD)

Some cost data was verified by checking typical fares in the city.

---

## 2. Features and Label

- **Features (X):**
  1. **Age** – Student’s age in years
  2. **Distance (km)** – How far they travel to university
  3. **Mode of Transport** – Type of transport used
  4. **Travel Time (min)** – Minutes spent traveling
  5. **Days per Week** – Number of days attending classes

- **Label (y):**
  - **Daily Cost (USD)** – Average amount spent per day on transport

---

## 3. Dataset Structure

- **Rows:** 100 students
- **Columns:** 6 (5 features + 1 label)

**Sample (7 rows):**

1| Age | Distance (km) | Mode of Transport | Travel Time (min) | Days/Week | Daily Cost (USD) |
 |-----|---------------|------------------|-------------------|-----------|------------------|
2| 28  | 1.3           | Walking          | 25                | 4         | 0.00             |
3| 20  | 6.0           | Motorcycle       | 15                | 7         | 1.28             |
4| 24  | 0.7           | Bajaj            | 23                | 4         | 1.07             |
5| 26  | 5.0           | Motorcycle       | 22                | 7         | 1.20             |
6| 24  | 2.2           | Motorcycle       | 27                | 3         | 0.98             |
7| 20  | 5.7           | Walking          | 27                | 4         | 0.00             |
8| 21  | 7.7           | Walking          | 16                | 3         | 0.00             |

---

## 4. Data Quality Issues

This dataset includes some real-world challenges:
- **Missing values:** Some students did not know their exact distance.
- **Mixed formats:** Distance sometimes reported in minutes instead of kilometers.
- **Spelling mistakes:** For example, “Baj” instead of “Bajaj.”
- **Imbalanced classes:** More students use Walking and Bajaj than Taxi.
- **Currency conversion:** Some costs were converted from Somali Shillings to USD.

These issues will be addressed in the data cleaning lesson.

---

## 5. Machine Learning Use Cases

This dataset can be used for:
- **Regression:** Predicting daily transport cost based on student features.
- **Classification:** Grouping students into Low, Medium, or High spenders.
- **Clustering:** Discovering patterns, such as “long-distance bus users” vs. “short-distance walkers.”

This information can help students, universities, and policymakers understand and improve transportation for students in Mogadishu.