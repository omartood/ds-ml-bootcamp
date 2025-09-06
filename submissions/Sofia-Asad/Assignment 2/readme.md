# Research Paper: Transportation & Commute Dataset

## Title & Collection Method

## **Title:** Student Transportation and Commute Dataset

**Collection Method:** i designed a short **Survey questionare** and collected responses from  51 students at my university large group whatsapp about their daily commuting habits. Each student provided information about their mode of transport, daily commute time, cost of commute, and departute time.

---

## Description of Features & Labels

* **Features (X):**

  1. **Age of the Student** (numeric, 19-25)
  2. **Mode of Transport**  (categorical: Walking, Bajaj, Bus, Car)
  3. **Travel Time (minutes)** (numeric, 10–40 minutes)
  4. **Cost ($)** (numeric,0-1 dollars)
  5. **departure time** (categorical: Morning, Noon, Evening)

* **Label (y):**

  * **Travel Time (minutes) (numeric, 10–40 minutes)t** 

This makes the problem a **a regression task** (predicting exact travel time based on transport mode).

---

## Dataset Structure

* **Rows:** 51 students (samples)
* **Columns:** 5 features + 1 label

### Sample Table (10 rows)

| Age | TransportMode | DailyCost($) | DepartureTime | Travel Time(minute)
| --- | ------------- | ------------ | ------------  | ------------------- | 
| 22  | bus           | 0.15         | morning       | 15-35               | 
| 19  | bajaj         | 0.25         | morning       | 10-25               | 
| 20  | bajaj         | 0.25         | morning       | 10-25               | 
| 21  | walk          | 0            | noon          | 20-40               | 
| 23  | bus           | 0.15         | morning       | 15-35               | 
| 25  | car           | 1            | noon          | 8-20                | 
| 24  | car           | 1            | noon          | 8-20                | 
| 20  | walk          | 0            | morning       | 20-40               | 
| 22  | bajaj         | 0.25         | noon          | 10-25               | 
| 21  | bajaj         | 0.25         | noon          | 10-25               | 

---

## Quality Issues

* **Missing values:** Some students may not report exact travel time.
* **Categorical text:** Transportmode and DepartureTime must be encoded for ML.
* **Data inconsistency** Some students may over/underestimate travel time.
* **Self-report bias:** Dataset depends on honesty and accuracy of students’ responses.

---

## Use Case

This dataset can be used to train a **regression model** to predict **travel time** for students based on their mode of transport, cost, and departure time.


## Possible
* **Regression**: Predict exact travel time (minutes).
* **Clustering**: Group students by commute patterns (e.g., fast commuters, budget commuters).
* **Feature analysis**: Evaluate how **transport mode** and **cost** affect travel time.