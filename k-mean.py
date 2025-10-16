import numpy as np
import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/jiss-sngce/CO_3/main/jkcars.csv')
df.head()
df.shape
df.dtypes
df.isnull().sum()
new_df = df[['Volume','Weight','CO2']]
new_df.head()

from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

sil_scores = []
clusters = range(2,11)

for k in clusters:
    kmeans_k = KMeans(n_clusters = k, random_state=10)
    kmeans_k.fit(new_df)
    cluster_labels = kmeans_k.predict(new_df)
    sil_scores.append(silhouette_score(new_df,cluster_labels))

sil_data = pd.DataFrame({'K value':clusters,'silhouette_score':sil_scores})
sil_data
import matplotlib.pyplot as plt
plt.figure(figsize=(14,5))
plt.plot(clusters,sil_scores)
plt.xlabel("K value")
plt.ylabel("silhouette_score")
plt.xticks(range(2,11))
plt.grid()
plt.show()

wcss = []
clusters = range(2,11)
for k in clusters:
    kmeans_k = KMeans(n_clusters = k, random_state=10)
    kmeans_k.fit(new_df)
    wcss.append(kmeans_k.inertia_)

plt.figure(figsize=(14,5))
plt.plot(clusters,wcss)
plt.xlabel("K value")
plt.ylabel("wcss")
plt.xticks(range(2,11))
plt.grid()
plt.show()

from sklearn.cluster import KMeans
kmeans_model=KMeans(n_clusters=3,random_state=10)
kmeans_model.fit(new_df)
cluster_labels=pd.Series(kmeans_model.predict(new_df))
cluster_labels.value_counts()
df2=pd.concat([df,cluster_labels],axis=1)

df2.columns=list(df.columns)+['label']
df2
