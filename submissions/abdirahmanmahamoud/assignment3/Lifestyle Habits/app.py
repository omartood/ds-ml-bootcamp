import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = '../../assignment2/data.csv'
df = pd.read_csv(CSV_PATH)


df["HealthStatus"] = df["HealthStatus"].str.strip()

df["Age"] = df["Age"].fillna(df["Age"].median())
df["SleepHours"] = df["SleepHours"].fillna(df["SleepHours"].median())
df["TeaCoffeePerDay"] = df["TeaCoffeePerDay"].fillna(0)
df["ExerciseDays"] = df["ExerciseDays"].fillna(0)
df["HealthyMeals"] = df["HealthyMeals"].fillna(df["HealthyMeals"].median())
df["MealsPerDay"] = df["MealsPerDay"].fillna(df["MealsPerDay"].mode()[0])
df["HealthStatus"] = df["HealthStatus"].fillna("Average")

before = df.shape
df = df.drop_duplicates()
after = df.shape


def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_age, high_age = iqr_fun(df["Age"])
low_sleep, high_sleep = iqr_fun(df["SleepHours"])
low_tea, high_tea = iqr_fun(df["TeaCoffeePerDay"])
low_exercise, high_exercise = iqr_fun(df["ExerciseDays"])
low_meals, high_meals = iqr_fun(df["HealthyMeals"])
low_mealsDay, high_mealsDay = iqr_fun(df["MealsPerDay"])


status_map = {"Poor": 0, "Average": 1, "Good": 2}
df["HealthStatusEncoded"] = df["HealthStatus"].map(status_map)

df["Meals_to_SleepRatio"] = df["MealsPerDay"] / df["SleepHours"].replace(0, np.nan)
df["Exercise_to_AgeRatio"] = df["ExerciseDays"] / df["Age"].replace(0, np.nan)
df["Caffeine_to_Meals"] = df["TeaCoffeePerDay"] / df["MealsPerDay"].replace(0, np.nan)

dont_scale = {"HealthStatusEncoded"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])


OUT_PATH = "Health_Clean.csv"
df.to_csv(OUT_PATH, index=False)
