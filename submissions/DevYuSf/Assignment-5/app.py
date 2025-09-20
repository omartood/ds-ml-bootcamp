import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.ensemble import RandomForestRegressor

CSV_PATH = 'Housing_Clean.csv'
df = pd.read_csv(CSV_PATH)

# print(df.shape)
x = df.drop(columns=["Price","LogPrice"])
y = df['Price']

X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

lr = LinearRegression()
rf = RandomForestRegressor(n_estimators=100,random_state=42)

lr.fit(X_train,y_train)
rf.fit(X_train,y_train)

lr_Pred = lr.predict(X_test)
rf_Pred = rf.predict(X_test)

# print(lr_Pred[:10])

def print_metrics(name,y,y_pred):
    r2 = r2_score(y,y_pred)
    mae = mean_absolute_error(y,y_pred)
    mse = mean_squared_error(y,y_pred)
    rmse = np.sqrt(mse)
    print(f"Prediction of {name}")
    print(f"R2: {r2:.3f}")
    print(f"MAE: {mae:,.0f}")
    print(f"MSE: {mse:,.0f}")
    print(f"RMSE: {rmse:,.0f}")

# print_metrics("LR",y_test,lr_Pred)
# print_metrics("LF",y_test,lf_Pred)



i = 3
x_one_df = X_test.iloc[[i]]
y_true = y_test.iloc[i]

p_lr_one = float(lr.predict(x_one_df)[0])
p_rf_one = float(rf.predict(x_one_df)[0])

print("Single raw Sanity check")

print(f"Actual Price ${y_true:,.0f}")
print(f"LR Prediction ${p_lr_one:,.0f}")
print(f"RF Prediction ${p_rf_one:,.0f}")