import pandas as pd
csv_path='data.csv'
df =pd.read_csv(csv_path)
df['Buyer']=df['Buyer'].replace({'yeS':'Yes'})
df['Rating']=df['Rating'].replace({'excellent':'Exc'})
df['Distance'] = df['Distance'].replace({
    r"\s*km": "",
    ">":""
    },regex=True)
df['Distance'] = df['Distance'].fillna(df['Distance'].mode()[0])
df=pd.get_dummies(df,columns=['Distance'],drop_first=False)
df['Buyer']=df['Buyer'].fillna(df['Buyer'].mode()[0])
df['NeedPharm']=df['NeedPharm'].replace({'YESSS':'Yes'})
df['NeedPharm']=df['NeedPharm'].fillna(df['NeedPharm'].mode()[0])

df['Safety']=df['Safety'].replace({'yess':'Yes'})
df['Safety'] = df['Safety'].fillna(df['Safety'].mode()[0])

df['Suitability']=df['Suitability'].replace({'suitible':'Suitable'})
df['Suitability']=df['Suitability'].fillna(df['Suitability'].mode()[0])
print(df.head(30))




