# Research Paper: Transport Habits Dataset

## 1. Title & Collection Method
**Title:** Transport Habits and Travel Patterns  

**Collection Method:**  
The dataset was collected using a Google Form survey shared with friends and classmates. Respondents were asked about their daily trips, including distance, mode of transport, waiting time, trip duration, cost, and whether they arrived on time.

## 2. Description of Features & Label

**Features (X):**  
1. **Distance (km):** The length of the trip.  
2. **Transport Mode:** Type of transport (Bus, Taxi, Car, Bajaj, Walk, Bicycle).  
3. **Waiting Time (minutes):** Time spent waiting before starting the trip.  
4. **Trip Duration (minutes):** Total minutes spent on the trip.  
5. **Cost ($):** Amount spent on the trip.  

**Label (y):**  
- **On-Time Arrival:** Whether the traveler arrived on time (Yes/No).

## 3. Dataset Structure
The dataset contains **50 rows (samples)** and **6 columns (5 features + 1 label)**.  

**Sample Table (10 rows):**

| Distance (km) | Transport Mode | Waiting Time (min) | Trip Duration (min) | Cost ($) | On-Time Arrival |
|---------------|----------------|------------------|-------------------|----------|----------------|
| 7.6           | Bus            | 10               | 50                | 1        | Yes            |
| 5             | Bajaj          | 5                | 23                | 2        | Yes            |
| 13            | Taxi           | 15               | 45                | 5        | No             |
| 3             | Walk           | 0                | 13                | 0        | Yes            |
| 4.6           | Bajaj          | 7                | 15                | 0        | No             |
| 8             | Bajaj          | 0                | 16                | 3        | Yes            |
| 12.7          | Bus            | 30               | 60                | 0.9      | No             |
| 0             | Walk           | 0                | 18                | 0        | No             |
| 1             | Walk           | 0                | 16                | 0        | Yes            |
| 30            | Car            | 2                | 40                | 5        | Yes            |

## 4. Quality Issues
- **Missing Values:** Some distances are missing (e.g., “?”).  
- **Outliers:** Very large trips (e.g., 120 km, 90 minutes waiting time).  
- **Mixed Formats:** Some costs recorded as whole numbers, others as decimals.  
- **Imbalance:** More Bajaj and Bus trips compared to Taxi, Bicycle, or Walk.  

## 5. Use Case
This dataset can be applied in Machine Learning:  
- **Classification:** Predict if a traveler will arrive on time (Yes/No).  
- **Regression:** Predict trip duration or cost based on distance and mode.  
- **Clustering:** Group travelers by transport habits (e.g., walkers vs. bus riders).  

## 6. Conclusion
This study on transport habits provides useful insights into how distance, mode of transport, waiting time, trip duration, and cost affect punctuality. By analyzing these features, educators, city planners, or policymakers can identify common travel challenges and design better solutions. Furthermore, with the help of machine learning models, it is possible to predict travel outcomes and support data-driven decision-making for improving daily commuting efficiency.
