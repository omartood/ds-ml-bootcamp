# Research Paper: Traffic Conditions and Influencing Factors Dataset

## 1. Title & Collection Method
**Title:** Traffic Conditions in Mogadishu: Patterns and Influencing Factors

**Collection Method:**  
This dataset consists of 50 samples collected in Mogadishu at various times of the day. Data was gathered through direct observation and manual counting. Observed factors include time of day, day of the week, weather conditions, traffic events, and accidents.

---

## 2. Description of Features & Label
The dataset contains 5 features (X) and 1 target variable (y):

| Feature / Label | Description |
|-----------------|-------------|
| **Time (X1)**   | Hour of the day in AM/PM format. |
| **Day (X2)**    | Day of the week (categorical). |
| **Weather (X3)** | Weather condition during observation (e.g., Sunny, Rainy, Cloudy). |
| **Event (X4)**  | Presence of events that might affect traffic (Yes/No). |
| **Accident (X5)** | Occurrence of accidents during the observation period (Yes/No). |
| **Traffic Level (y)** | Target variable: Traffic density (categorical: Low, Medium, High). |

---

## 3. Dataset Structure
- **Rows:** 50 samples from different times and days.  
- **Columns:** 6 (5 features + 1 label).  
- **Features (X1–X5):** Time, Day, Weather, Event, Accident  
- **Label (y):** Traffic Level  

**Sample Table (10 rows):**

| No | Time  | Day      | Weather | Event | Accident | Traffic Level (y) |
|----|-------|----------|---------|-------|----------|-----------------|
| 1  | 7 AM  | Monday   | Sunny   | No    | No       | High            |
| 2  | 12 PM | Wednesday| Cloudy  | No    | No       | High            |
| 3  | 5 PM  | Friday   | Sunny   | Yes   | No       | High            |
| 4  | 8 AM  | Monday   | Rainy   | No    | No       | High            |
| 5  | 2 PM  | Thursday | Cloudy  | No    | No       | Low             |
| 6  | 4 PM  | Saturday | Sunny   | Yes   | No       | High            |
| 7  | 9 AM  | Tuesday  | Sunny   | No    | No       | Medium          |
| 8  | 12 PM | Thursday | Sunny   | No    | No       | High            |
| 9  | 7 AM  | Tuesday  | Sunny   | No    | No       | High            |
| 10 | 5 PM  | Friday   | Rainy   | Yes   | No       | High            |

---

## 4. Quality Issues
During data collection, several issues were identified that require preprocessing:  

- **Missing Values:** Some times or traffic observations were not recorded.  
- **Categorical Labels:** Traffic Level is textual (Low, Medium, High) and may need encoding (e.g., 0, 1, 2).  
- **Imbalance:** Certain traffic levels (e.g., Low) may have fewer samples.  
- **Human Error:** Possible mistakes in recording accidents or traffic events.  
- **Different Scales:** Time is categorical (AM/PM), while other features are binary or categorical; normalization may be needed for ML models.  

---

## 5. Machine Learning Use Case
**Classification:**  
Predict Traffic Level (Low, Medium, High) based on time, day, weather, events, and accidents. This dataset can be used to train machine learning models to identify patterns in traffic flow and predict congestion.

---

## 6. Conclusion
This dataset of 50 samples highlights the relationship between time, day, weather, traffic events, and accidents with observed traffic levels. Despite limitations like missing values and human error, it provides a solid foundation for machine learning models to predict traffic patterns.

The primary goal is to understand traffic flow patterns in Mogadishu, which could aid in traffic management, road safety, and urban planning.
