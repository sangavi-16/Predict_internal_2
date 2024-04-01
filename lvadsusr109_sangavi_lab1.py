# -*- coding: utf-8 -*-
"""LVADSUSR109_Sangavi_Lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GpwHWDK88XhJ-I_NGI0-13-mqkPCTEnO
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, precision_score, f1_score, recall_score, confusion_matrix
from sklearn.preprocessing import MinMaxScaler
import time
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("/content/drive/MyDrive/Predictive/winequality-red.csv")
print(df)

df.info()

df.describe()

# check for missing values
print(df.isnull().sum())
# Fill the missing value
df['fixed acidity']=df['fixed acidity'].fillna(method='ffill')
df['volatile acidity']=df['volatile acidity'].fillna(method='bfill')
df['citric acid']=df['citric acid'].fillna(method='ffill')
df['residual sugar']=df['residual sugar'].fillna(method='ffill')
df['chlorides']=df['chlorides'].fillna(method='ffill')
df['sulphates']=df['sulphates'].fillna(method='ffill')
df['free sulfur dioxide']=df['free sulfur dioxide'].fillna(method='bfill')

# Check for null after filling the missing value
print(df.isnull().sum())

# Check for duplicate records
print(df.duplicated().sum()) # 221 duplicate records
# drop duplicates
df=df.drop_duplicates()
print(df.duplicated().sum())

# Checking Outliers
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)
print(outliers)

df1 = df[~outliers]

def map_quality(quality):
    if quality >= 3 and quality <= 6:
        return 0
    elif quality >= 7 and quality <= 8:
        return 1
    else:
        return None
df1['quality'] = df1['quality'].apply(map_quality)

quality_distribution = df1['quality'].value_counts()
print("Wine quality distribution:")
print(quality_distribution)

plt.figure(figsize=(8, 6))
quality_distribution.plot(kind='bar', color='purple')
plt.title('Wine Quality Distribution')
plt.xlabel('Quality')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# Splitting of X and Y

X = df1.drop(columns=['quality'])
y = df1['quality']
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Building
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train,Y_train)
rf_predictions = rf_classifier.predict(X_test)
rf_accuracy = accuracy_score(Y_test, rf_predictions)
print("Random Forest Classifier Accuracy:", rf_accuracy)

# Metrices
accuracy = accuracy_score(Y_test, rf_predictions)
precision = precision_score(Y_test, rf_predictions, average='weighted')
recall = recall_score(Y_test, rf_predictions, average='weighted')
f1 = f1_score(Y_test, rf_predictions, average='weighted')
conf_matrix = confusion_matrix(Y_test, rf_predictions)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Confusion Matrix:\n", conf_matrix)