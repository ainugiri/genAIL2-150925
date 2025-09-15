import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
# logistic Classification algo
from sklearn.linear_model import LogisticRegression

df = load_iris(as_frame=True).frame
print(df.head())
print(df.describe())
print(df.info())


model = LogisticRegression()
X = df.drop(columns=['target'])
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

u_s_len = float(input("Enter the sepal length (cm): ").strip())
u_s_wid = float(input("Enter the sepal width (cm): ").strip())
u_p_len = float(input("Enter the petal length (cm): ").strip())
u_p_wid = float(input("Enter the petal width (cm): ").strip())

prediction = model.predict(np.array([[u_s_len, u_s_wid, u_p_len, u_p_wid]]))[0]
species = df['target'].unique()[prediction]
print('w.r.t species', species)
# print setosa, versicolor, virginica
if species == 0:
    print("The predicted species is: Setosa")
elif species == 1:
    print("The predicted species is: Versicolor")
elif species == 2:
    print("The predicted species is: Virginica")
else:
    print("Unknown species")