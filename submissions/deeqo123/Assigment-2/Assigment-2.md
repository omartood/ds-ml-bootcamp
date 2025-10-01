# Impact of Daily Phone Usage on Personal Productivity

## 1. Title & Collection Method
**Title:** Impact of Daily Phone Usage on Personal Productivity  

**Collection Method:**  
This dataset was collected by manually tracking daily screen usage and productivity for a period of 7 days.  
The data was recorded using smartphone screen-time reports and a self-assessed productivity score (rated from 1 to 10).  
I recorded the total screen time, time spent on social media apps, time spent studying, and hours of sleep.  
The productivity score was self-evaluated at the end of each day based on how much meaningful work I completed.  

---

## 2. Description of Features & Labels
**Input variables (features x):**
- **Screen Time Hours:** Total screen time per day (in hours).
- **Social Media Hours:** Time spent on social media apps.
- **Study Hours:** Time spent studying or doing productive work.
- **Sleep Hours:** Hours of sleep.

**Output variable (label y):**
- **Productivity Score:** A subjective rating of productivity on a scale of 1 (low) to 10 (high).  

---

## 3. Dataset Structure
The dataset contains **50 rows and 6 columns** (5 features and 1 label).  

### Sample Table:
| Row | Screen Time | Social Media | Study Hours | Sleep Hours | Productivity |
|-----|-------------|--------------|-------------|-------------|--------------|
| 1   | 6.5         | 2.0          | 2.5         | 7.0         | 7            |
| 2   | 5.5         | 1.5          | 3.5         | 8.0         | 8            |
| 3   | 8.0         | 3.5          | 1.0         | 6.0         | 4            |
| 4   | 4.8         | 1.0          | 4.0         | 7.5         | 9            |
| 5   | 5.5         | 2.0          | 2.0         | 6.5         | 6            |  

---

## 4. Quality Issues
- The productivity score is subjective, so it may vary based on mood or perception.  
- Screen time measurements are rounded to the nearest 0.1 hour, which may reduce precision.  
- Only 5 data points (rows) were collected, which may be too small for real machine learning training.  
- Some missing values occurred when the phone battery died or sleep time wasn’t recorded.  

---

## 5. Use Case (Machine Learning)
- This dataset could be used to train a **regression model** that predicts daily productivity based on behavioral patterns such as screen time, study habits, and sleep.  
- Alternatively, the productivity score could be converted into **categories** (e.g., Low, Medium, High) and used for a **classification model**.  
- This could help in developing apps that recommend better digital habits.    
