import pandas as pd
import numpy as np

df = pd.read_csv("student_perfor_dataset.csv")

# Clean Age


def clean_age(x):
    if '-' in str(x):
        low, high = x.split('-')
        return (int(low) + int(high) / 2)
    elif '>' in str(x):
        return int(x.replace('>', '')) + 1
    return np.nan


df['Age'] = df['Age'].apply(clean_age)


# Clean hours columns

def clean_hours(x):
    if pd.isna(x):
        return np.nan
    x = str(x).lower().replace("hrs", "").replace("hours", "").strip()
    if '-' in x:
        low, high = x.replace("<", "").replace(">", "").split('-')
        return (float(low) + float(high) / 2)
    if '<' in x:
        return 0.5 if '1' in x else 4
    if '>' in x:
        return 11 if '10' in x else 4
    return float(x) if x.isdigit() else 0


for col in ['Sleep_hours', 'AI_use_weekly_hours', 'SocialMedia_use_daily_hpurs', 'Study_hours_weekly']:
    df[col] = df[col].apply(clean_hours)

#  Encode Device
df['Device'] = df['Device'].fillna(df['Device'].mode()[0])
df = pd.get_dummies(df, columns=['Device'], drop_first=False).astype(int)

# Encode Performance
perf_map = {'Poor': 1, 'Average': 2, 'Good': 3, 'Excellent': 4}
df['Performance'] = df['Performance'].map(perf_map)

# Handle missing values in numbers
for col in ['Sleep_hours', 'AI_use_weekly_hours', 'SocialMedia_use_daily_hpurs', 'Study_hours_weekly']:
    df[col] = df[col].fillna(df[col].median())

print(df.head())

OUT_PATH = "student_perfor_dataset_ready.csv"
df.to_csv(OUT_PATH, index=False)
print(f"\nCleaned dataset saved to {OUT_PATH}")
