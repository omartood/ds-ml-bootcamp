import pandas as pd
csv_path='data.csv'
df =pd.read_csv(csv_path)
df['Buyer']=df['Buyer'].replace({'yeS':'Yes'})
# print(df['Buyer'])
df['Rating']=df['Rating'].replace({'excellent':'Exc'})
# print(df['Rating'])
#Feeling nun value
#/s removes 0 or more spaces if you want to recognise km as lettes use "" not ['']
df['Distance'] = df['Distance'].replace({
    r"\s*km": "",
    ">":""
    },regex=True)
df['Distance'] = df['Distance'].fillna(df['Distance'].mode()[0])
df=pd.get_dummies(df,columns=['Distance'],drop_first=False)
df['Buyer']=df['Buyer'].fillna(df['Buyer'].mode()[0])
# print(df['NeedPharm'].value_counts(dropna=False))
df['NeedPharm']=df['NeedPharm'].replace({'YESSS':'Yes'})
df['NeedPharm']=df['NeedPharm'].fillna(df['NeedPharm'].mode()[0])
# safety colum
df['Safety']=df['Safety'].replace({'yess':'Yes'})
df['Safety'] = df['Safety'].fillna(df['Safety'].mode()[0])
# Outlier detection function
# def iqr_fun(series, k=1.5):
#     q1, q3 = series.quantile([0.25, 0.75])
#     iqr = q3 - q1
#     lower = q1 - k * iqr
#     upper = q3 + k * iqr
#     return lower, upper




# Get bounds
df['Suitability']=df['Suitability'].replace({'suitible':'Suitable'})
df['Suitability']=df['Suitability'].fillna(df['Suitability'].mode()[0])
print(df.head(30))




