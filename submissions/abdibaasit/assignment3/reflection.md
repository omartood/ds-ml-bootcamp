# Reflection

In this project I cleaned and prepared the car dataset.

### 1. Missing values
When some values are empty, I filled them.  
- For numbers like **Odometer_km**, I used the **median** (the middle value). Median is better than mean when there are very big or very small numbers that can change the average.  
- For categories like **Doors** or **Location**, I used the **mode** (the most common value). Mode is simple and shows the usual case.

### 2. Outliers
Some numbers were too big or too small compared to others.  
I used **IQR capping**. IQR looks at the middle 50% of the data and sets a lower and upper limit.  
If a value is outside the limit, I cut it (cap) to the boundary.  
This way, strange values do not confuse the model, but I still keep all rows.

### 3. New features
I created new columns to give the model more useful information:  
- **LogPrice**: I changed Price to log scale to make the numbers less skewed.  
- **IsAccident**: From the accident number, I made a simple column "1" if accidents ≥ 1 and “0” if accidents = 0.  
- **Location**: I changed location into small columns (one-hot encoding). This helps the model understand each location separately.

### 4. Scaling
I made the numeric columns (like Odometer_km) on the same scale using **StandardScaler**.  
I did not scale Price or LogPrice because they are target values.  
This step helps the model treat all numbers fairly.

---

In short, I chose median and mode because they are simple and safe.  
I used IQR to fix outliers without deleting rows.  
I made new features to give more meaning (accident, log price, location).  
I scaled numeric data so the model can learn better.
