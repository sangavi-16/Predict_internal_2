# -*- coding: utf-8 -*-
"""LVADSUSR109_Sangavi_Lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IFuh6sNHntIIMURxwL_WBnc3JcfdlZQw
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/content/drive/MyDrive/Predictive/Mall_Customers.csv")
print(df)

df.info()

df.describe()

# check for missing values
print(df.isnull().sum()) # 10 missing values in Annual income
# Fill the missing value
df['Annual Income (k$)']=df['Annual Income (k$)'].fillna(method='ffill')
# Check for null after filling the missing value
print(df.isnull().sum())
# Check for duplicate records
print(df.duplicated().sum()) # No duplicate records

# Encoding categorical values
encoder=LabelEncoder()
df['Gender']=encoder.fit_transform(df['Gender'])
print(df.head())

# Normalization of the variables
scaler = MinMaxScaler()
scaler.fit(df[['Annual Income (k$)']])
df['Annual Income (k$)'] = scaler.transform(df[['Annual Income (k$)']])
scaler.fit(df[['Spending Score (1-100)']])
df['Spending Score (1-100)'] = scaler.transform(df[['Spending Score (1-100)']])
print(df.head())
plt.scatter(df['Spending Score (1-100)'],df['Annual Income (k$)'])

# Elbow Method
sse = [] # The sum of Squared Errors =SSE
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['Spending Score (1-100)','Annual Income (k$)']])
    sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)

# n_cluster=5 according to the elbow method
km = KMeans(n_clusters=5)
y_predicted = km.fit_predict(df[['Spending Score (1-100)','Annual Income (k$)']])
df['cluster']=y_predicted
df.head(25)
print(km.cluster_centers_)

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
df4 = df[df.cluster==3]
df5 = df[df.cluster==4]

Mean_cluster1=df1['Spending Score (1-100)'].mean()
Mean_cluster2=df2['Spending Score (1-100)'].mean()
Mean_cluster3=df3['Spending Score (1-100)'].mean()
Mean_cluster4=df4['Spending Score (1-100)'].mean()
Mean_cluster5=df5['Spending Score (1-100)'].mean()

plt.scatter(df1['Spending Score (1-100)'],df1['Annual Income (k$)'],color='pink')
plt.scatter(df2['Spending Score (1-100)'],df2['Annual Income (k$)'],color='yellow')
plt.scatter(df3['Spending Score (1-100)'],df3['Annual Income (k$)'],color='blue')
plt.scatter(df4['Spending Score (1-100)'],df4['Annual Income (k$)'],color='cyan')
plt.scatter(df5['Spending Score (1-100)'],df5['Annual Income (k$)'],color='green')

plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='black',marker='o',label='centroid')
plt.xlabel('Spending Score (1-100)')
plt.ylabel('Annual Income (k$)')
plt.legend()

# Cluster Analysis
sns.barplot([Mean_cluster1,Mean_cluster2,Mean_cluster3,Mean_cluster4,Mean_cluster5])
plt.xlabel('Clusters')
plt.ylabel('Mean of Spending Score ')

plt.show()
# My comparing the mean of the Spending score we can see how the clusters are distributed
# How the cluster 1 is distributed to all the values can be seen clearly
df1.head().plot(kind="bar")

Mean_cluster1=df1['Annual Income (k$)'].mean()
Mean_cluster2=df2['Annual Income (k$)'].mean()
Mean_cluster3=df3['Annual Income (k$)'].mean()
Mean_cluster4=df4['Annual Income (k$)'].mean()
Mean_cluster5=df5['Annual Income (k$)'].mean()
sns.barplot([Mean_cluster1,Mean_cluster2,Mean_cluster3,Mean_cluster4,Mean_cluster5])
plt.xlabel('Clusters')
plt.ylabel('Mean of Annual Income ')

# Strategy
'''
We can infer from the bar graph plotted that cluster 1 and cluster 2 have higher average
'''