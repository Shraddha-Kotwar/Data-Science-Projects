# -*- coding: utf-8 -*-
"""Data Analysis 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yXbDiv_gPBLPEQ0PZtiIgD90RZ3BDFOF
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Social_Network_ads.csv")
df.head()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])
df.head()

df.isnull().sum()

x = df.iloc[:,1:4]
y = df['Purchased']

from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split( x , y , test_size = 0.2)

from sklearn.linear_model import LogisticRegression
logReg = LogisticRegression()

logReg.fit(x_train,y_train)
y_pred=logReg.predict(x_test)

from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

accuracy = accuracy_score(y_test,y_pred)
precision =precision_score(y_test, y_pred,average='micro')
recall = recall_score(y_test, y_pred,average='micro')


print("Accuracy:- ",accuracy)
print("Precision:- ",precision)
print("Recall:- ",recall)

cm= confusion_matrix(y_test, y_pred)
cm

from sklearn.metrics import ConfusionMatrixDisplay
cmD = ConfusionMatrixDisplay(confusion_matrix = cm,display_labels =y.unique())
cmD.plot()

