
import pandas as pd 
import numpy as np 

from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# 1 soo jiido xogta, Load the cleaned dataset
CSV_PATH = 'car_l3_clean_ready.csv'
df = pd.read_csv(CSV_PATH)


# 2 features ka x ka reeb labelska,  y waa labelska
X = df.drop(columns=["Price"])
y = df["Price"]


# 3 data u kala saar trining iyo test 80/20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 4) Train Linear Regression
# training linear & random forest
lr = LinearRegression()
rf = RandomForestRegressor(n_estimators=100, random_state=42) #estimators inte decitiontree sameyn karaa marwalbu bato waa accurancy badana
lr.fit(X_train, y_train)
rf.fit(X_train, y_train)  #fit() baro xogta training


#prediction Linear regression & random forest
lr_pred = lr.predict(X_test)
rf_pred = rf.predict(X_test)
# print(lr_pred[:10])


#fuction kuso saara metrics
def metrics(name, y, y_predict):  #name magaca model-ka, y value ga dhabta ah, y_predict values uu model-ku qiyaasayah 
  r2 = r2_score(y, y_predict)     #1 perfect
  mae = mean_absolute_error(y, y_predict)  #farqiga celcelis ee runta iyo prediction
  mse = mean_squared_error(y, y_predict)  #khaladadka labajibbaaran/squared
  rmse = np.sqrt(mse)            #xididka MSE, si loo fahmo khaladka celceliska

  #soo saar metrics kana saar format float
  print(f"predicting of {name}")
  print(f"R2: {r2:.3f}")
  print(f"MAE: {mae:,.0f}")
  print(f"MSE: {mse:,.0f}")
  print(f"RMSE: {rmse:,.0f}")

#soo saar natiijada metrics
metrics("Linear Regression", y_test, lr_pred)  
metrics("Random Forest", y_test, rf_pred)  

# kala soo bax rowga predictka 
i = 0     #wuxuu soo qaadanayaa  rowga 1 oo dhan
x_one_df = X_test.iloc[[i]] #iloc waa propert uu nasii index aan baasnay data diisu nasiin xtest waa date columns ka ahyd
y_true = y_test.iloc[i] #scalar, qiimaha dhabta ah, data caadiga ahayd

p_lr_one = float(lr.predict(x_one_df)[0])
p_rf_one = float(rf.predict(x_one_df)[0])

#natiijada
print("\nSingle-row sanity check:")
print(f"Actual Price: ${y_true:,.0f}")  #qiimaha dhabta ah
print(f"LR Pred: ${p_lr_one:,.0f}")    #waxa qiyaasay Linear Regression 
print(f"RF Pred: ${p_rf_one:,.0f}")   #waxa qiyaasay Random Forest