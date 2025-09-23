import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
from sklearn.naive_bayes import MultinomialNB


df = pd.read_csv('mail_l7_dataset.csv')

# print(df.head())

df.loc[df["Category"].str.lower().str.strip() =='spam',"Category"] =0
df.loc[df["Category"].str.lower().str.strip() =='ham',"Category"] =1

# print(df.head())

X = df["Message"].astype(str)
y = df["Category"].astype(int)

# print(X.info())


X_train,X_test,y_train,y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# print("X train")
# print(X_train.info())
# print("X test")
# print(X_test.info())
# # print("y train")
# # print(y_train.info())

lfidf = TfidfVectorizer(min_df=1,stop_words="english",lowercase=True)

X_train_features = lfidf.fit_transform(X_train)
X_test_features = lfidf.transform(X_test)

lr = LogisticRegression(random_state=42,max_iter=1000)
rf = RandomForestClassifier(random_state=42)
nb = MultinomialNB()

lr.fit(X_train_features,y_train)
rf.fit(X_train_features,y_train)
nb.fit(X_train_features,y_train)

# print(X_test)
lr_predict = lr.predict(X_test_features)
rf_predict = rf.predict(X_test_features)
nb_predict = nb.predict(X_test_features)

def print_metrics(name,y_true,y_pred,pos_label=0):
    acc = accuracy_score(y_true,y_pred)
    prec = precision_score(y_true,y_pred,pos_label=pos_label)
    rec = recall_score(y_true,y_pred,pos_label=pos_label)
    f1 = f1_score(y_true,y_pred,pos_label=pos_label)
    print(f"{name } performentce")
    print(f"Accurance: {acc:.3f}")
    print(f"Precision: {prec:.3f} (positive = spam = {pos_label})")
    print(f"Recall: {rec:.3f} (positive = spam = {pos_label})")
    print(f"F-Score: {f1:.3f} (positive = spam = {pos_label})")
# print(lr_predict)
# print(rf_predict)
# print(nb_predict)

def confMat(name,y_true,y_pred):
    cm = confusion_matrix(y_true,y_pred,labels=[1,0])
    cm_df = pd.DataFrame(
        cm,
        index=["Accual Ham (1)","Accual Spam (0)"],
        columns=["Pred Ham (1)","Pred Spam(0)"]
    )
    print(f"{name} - Confission Matrixs:\n {cm_df}")


# print_metrics("Logistic Regression",y_test,lr_predict)
# print_metrics("Random Forest ",y_test,rf_predict)
# print_metrics("Naive Bayes ",y_test,nb_predict)
# confMat("Logistic Regression",y_test,lr_predict)
# confMat("Random Forest ",y_test,rf_predict)
# confMat("Naive Bayes ",y_test,nb_predict)

i = 16
# sample_text = "Dear User,You have been selected as the lucky winner of a $1,000 Amazon Gift Card! 🛒💳To claim your reward, simply click the link below and complete a short survey.👉 Claim your prize now before it expires in 24 hours! Thank you for being a valued customer. Sincerely, The Rewards Team"#X_test.iloc[i]
sample_text ="Congratulations! You have won a $1,000 gift card"
true_label = 0#y_test.iloc[i]

lr_pred_one = int(lr.predict(lfidf.transform([sample_text]))[0])
rf_pred_one = int(rf.predict(lfidf.transform([sample_text]))[0])
nb_pred_one = int(nb.predict(lfidf.transform([sample_text]))[0])

def label2str(r):
    return "Spam (0)" if r ==0 else "Ham (1)"

print("Sanity Check")
print("Sample text: "+sample_text)
print(f"Accual: {label2str(true_label)}")
print(f"LR Predict: {label2str(lr_pred_one)}")
print(f"RF Predict: {label2str(rf_pred_one)}")
print(f"NB Predict: {label2str(nb_pred_one)}")
