# Reflection 

This reflection explains the reasoning behind each major decision I made while cleaning and transforming 13_car dataset. It includes the approaches for handling missing values, outliers, feature engineering, and encoding categorical variables.

---

## 1. Handling Missing Values

- **Odometer_km**:  
  I used the **median**  because the odometer readings are highly skewed due to extreme values (e.g., cars with 5,000 km vs. cars with 395,000 km). The median is more robust against such outliers, ensuring that missing values were imputed with a representative central value.

- **Doors**:  
  For missing door counts, I used the **mode**. Since the number of doors is categorical in nature (2, 3, 4, 5), the mode preserves realistic values without introducing decimals.

- **Location**:  
  Missing locations were filled with the **mode**, because location is a categorical feature and using the most frequent class is a simple and reliable approach.

---

## 2. IQR capping

- **Price** and **Odometer_km** contained unrealistic extreme values.  
  I applied **IQR capping**  instead of removing rows. This allowed me to limit extreme outliers to a reasonable range while keeping as much data as possible.  
  - Example: Prices like `$135,000` or `$120,000` were capped down because they were inconsistent with the majority of the dataset.

---

## 3. Feature Engineering

I engineered several new features to enrich the dataset:

- **CarAge** = Current year – Year of car  
  - Reason: Car age is a stronger predictor of price than the raw manufacturing year. A 20-year-old car conveys more meaning than simply saying “2003.”

- **Km_per_year** = Odometer_km ÷ CarAge  
  - Reason: This normalizes mileage by the car’s age. A 200,000 km car that is 20 years old is very different from a 200,000 km car that is 5 years old.

- **LogPrice** = log(Price)  
  - Reason: Prices were right-skewed. Applying a log transformation stabilized variance and made the data more suitable for modeling.

- **Location Encoding**:  
  - I applied **one-hot encoding** to convert `Location` into three binary features: `Location_City`, `Location_Rural`, and `Location_Suburb`.  
  - Additionally, I created a derived feature **Is_Rural** to quickly distinguish between urban and rural cars, as location strongly influences resale value.

---

