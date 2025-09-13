# Reflection on Lesson 3 Data Preprocessing Assignment 

In this assignment, I focused on cleaning and preparing a messy car price dataset for analysis and modeling. Below are the key decisions I made in each major step:

---

### **1. Imputation Choices: Median vs Mode**

For the numeric column `Odometer_km`, I used the **median** to impute missing values because it is robust to outliers and provides a better central measure when the data is skewed.

For `Doors`, `Accidents`, and `Location`, I used the **mode**. Although `Doors` and `Accidents` are stored as numeric types, they represent **discrete values** rather than continuous measurements. For example, the number of doors is typically 2, 3, 4, or 5, and these values function more like categorical choices. Using the mode ensures the most frequent, sensible category fills in the missing values.

---

### **2. IQR Capping for Outliers**

To handle outliers in `Price` and `Odometer_km`, I applied **Interquartile Range (IQR) capping**. This clips extreme values beyond 1.5 times the IQR from the lower and upper quartiles. It reduces the influence of outliers without removing valuable data or distorting the distribution entirely.

---

### **3. Feature Engineering**

I created several new features to enrich the dataset and support better modeling:

* `CarAge`: The age of the vehicle, since newer and older cars differ in value and condition.
* `Km_per_year`: The average usage per year, giving context to the odometer reading.
* `Accident_Rate`: Number of accidents per year, to normalize accident counts by age.
* `Is_OldCar`: A binary flag for cars older than 15 years.
* `Is_Urban`: Based on the `Location_City` dummy, identifying whether a car is urban.
* `LogPrice`: A log-transformed version of price to reduce skewness and stabilize variance.

These features provide more context and help models generalize better.

---

### **4. Additional Decisions**

* I kept `Price`, `LogPrice`, and dummy variables (like `Location_*`) **unscaled**, since scaling is unnecessary for target variables and has no meaningful effect on binary indicators.
* I used **one-hot encoding** for `Location` to convert text categories into numeric features, which are required by most machine learning models.
* I **removed duplicates** to avoid redundant or repeated data that could bias training or analysis.

---

### **Conclusion**

Overall, my preprocessing pipeline focused on making the data clean, consistent, and informative. The choices I made—such as using median for skewed data, mode for discrete categories, and IQR for outliers—were grounded in best practices and the nature of the dataset. The resulting data is now well-structured and ready for modeling in a reproducible and explainable way.