import datetime as dt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# 1) Loading the dataset and seeing its shape and missing values

# Path of the dataset file
IN_DATASET_PATH = 'car_l3_dataset.csv'

# Load the dataset into pandas DataFrame
df = pd.read_csv(IN_DATASET_PATH)

# Display the first 5 rows of the dataset
# print("First 5 rows of the dataset:")
# print(df.head())

# Display the shape of the dataset
# print("\Info of the dataset:")
# print(df.info())

# Check for missing values in the dataset
# print("\nInitial Missing values in the dataset:")
# print(df.isnull().sum())


# 2) Clean the target column formatting issues
df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)
# print("Missing values in the target column after cleaning:")
# print(df['Price'].isnull().sum())


# 3) Fix the categorical issues before imputation
df['Location'] = df['Location'].replace({'Subrb': 'Suburb', '??': pd.NA})
# print(df.Location.isna().sum())



# 4) Impute the missing values in the dataset
df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].median())
df['Doors'] = df['Doors'].fillna(df['Doors'].mode()[0])
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])

# print("\nMissing values after imputation:")
# print(df.isnull().sum())



# 5) Remove duplicates from the dataset
# is there any duplicates?
# print("Number of duplicate rows in the dataset:", df.duplicated().sum())
# print(df[df.duplicated(keep=False)])

before_dep = df.shape
df = df.drop_duplicates()
after_dep = df.shape
# print(f"Shape before dropping duplicates: {before_dep}, after dropping duplicates: {after_dep}")

# 6) IQR capping for outlier treatment
def iqr_capping(series, factor=1.5):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - (IQR * factor)
    upper_bound = Q3 + (IQR * factor)
    return lower_bound, upper_bound

low_odometer, high_odometer = iqr_capping(df['Odometer_km'])
low_price, high_price = iqr_capping(df['Price'])

# print(f"Odometer_km - Lower Bound: {low_odometer}, Upper Bound: {high_odometer}")
# print(f"Price - Lower Bound: {low_price}, Upper Bound: {high_price}")

df['Odometer_km'] = df['Odometer_km'].clip(lower=low_odometer, upper=high_odometer)
df['Price'] = df['Price'].clip(lower=low_price, upper=high_price)
# print(df[['Odometer_km', 'Price']].describe())



# 7) One-hot encoding for categorical columns
df = pd.get_dummies(df, columns=['Location'], drop_first=False, dtype='int')
# print(f"Shape after one-hot encoding: {df.shape}")


# 8) Feature engineering
current_year = dt.datetime.now().year
df['Car_Age'] = current_year - df['Year']
df['Km_per_Year'] = df['Odometer_km'] / df['Car_Age'].replace(0, 1)  # to avoid division by zero
df['Km_per_Year'] = df['Km_per_Year'].astype(float).round(2)
df['Accident_Rate'] = df['Accidents'] / df['Car_Age'].replace(0, 1)  # to avoid division by zero
df['Accident_Rate'] = df['Accident_Rate'].astype(float).round(2) * 100  # convert to percentage
df['Log_Price'] = np.log1p(df['Price'])
df['Is_OldCar'] = (df['Car_Age'] > 10).astype(int)
df['Is_FamilyCar'] = ((df['Doors'] >= 4) & (df['Odometer_km'] > 10000) & (df['Accidents'] == 0)).astype(int)
df['Is_UrbanCar'] = ((df['Odometer_km'] < 50000)).astype(int)


# 9) Standard scaling for numerical columns
dont_scale = ['Price', 'Log_Price']
num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
exclude_cols = [col for col in num_cols if col.startswith('Location_')]
cols_to_scale = [col for col in num_cols if col not in dont_scale and col not in exclude_cols]

scaler = StandardScaler()
df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

# Display the first 5 rows of the dataset
# print("First 5 rows of the dataset:")
# print(df.head())

# Display the shape of the dataset
# print("\info of the dataset:")
# print(df.info())

# Check for missing values in the dataset
# print("\nInitial Missing values in the dataset:")
# print(df.isnull().sum())


# 10) Save the preprocessed dataset
OUT_DATASET_PATH = 'car_l3_clean_ready.csv'
df.to_csv(OUT_DATASET_PATH, index=False)

