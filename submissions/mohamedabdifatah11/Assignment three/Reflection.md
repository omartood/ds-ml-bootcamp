# Reflection – Lesson 3 Data Preprocessing

For missing values, I used the median for Odometer because it is less affected by extreme values. For categorical columns like Doors, Accidents, and Location, I used the mode since it represents the most common category.

I handled outliers in Price and Odometer with IQR capping. This avoids throwing away useful data while reducing the impact of extreme values.

For feature engineering, I created CarAge (since age strongly affects value), Km_per_year (to capture usage intensity), and Is_Urban (urban vs. non-urban effect). I also added LogPrice as an alternative target to reduce skewness.

Scaling was applied only to continuous features (Odometer_km, CarAge, Km_per_year), leaving categorical dummies untouched. This keeps the data consistent and ready for modeling.

The final dataset is complete, with no missing values and balanced features, saved as car_l3_clean_ready.csv.
