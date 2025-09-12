In assignment 3 I applied **10-step systematic** to clean the data **car\_l3\_dataset.csv**

1. **Dataset Evaluation**
   I checked the data using **head, shape, info, MISSING VALUES and isnull** I saw that the data had many errors
2. **Price Cleaning**
   `Price` contained money signs and commas I also checked **skewness** to understand how the price distribution is skewed
3. **Categorical Component Correction**
   I changed “Subrb→Suburb” and replaced “??” with missing values.
4. **Imputation**

* I used **Median** for `Odometer_km` because there are outliers
* I used **Mode** for `Doors`, `Accidents`, and `Location` because most of the time the highest value is a reasonable choice, after that the data is not left with any gaps.

5. **Removing Consecutive Duplicates**
   Duplicates can cause machine learning errors, so I removed them
6. **Managing Outliers (IQR Capping)**
   I calculated the IQR bounds for `Price` and `Odometer_km` and then clipped them. This reduces the impact of values that are too far out of the norm, without deleting too much data.
7. **One-Hot Encoding**
   I converted `Location` to binary columns (`Location_City`, `Location_Rural`, `Location_Suburb`) This allows the model to use categorical data numerically.
8. **Creating 3 New Features**

* **CarAge = CurrentYear – Year** → to indicate the age of the car.
* **Km\_per\_year = Odometer / CarAge** → to indicate the average annual usage.
* **is\_Urban = 1 – Location\_Rural** → to indicate whether the car is in an urban area.
  I also created **log\_Price = log(Price+1)** to reduce skewness (no leakage).
* Label (target): `Price`
* Feature keys: `Odometer_km`, `Doors`, `Accidents`, `Location`, `Year` (+ engineered features)

9. **Scaling**
   I used `StandardScaler` to scale the numeric features. I left out `Price`, `log_Price`, and dummy variables (0/1) to keep them the same. This makes the numeric features the same weight, without changing the target or binary columns.
10. **Final Check & Save**
    I confirmed that there was no space, checked `describe` and saved the clean data as **car\_l3\_clean\_ready.csv**
