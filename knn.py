from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
irisData = load_iris()
print("Features:\n", irisData.data)
print("\nTarget:\n", irisData.target)
x = irisData.data
y = irisData.target
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train, y_train)
print("\nPredictions on test data:\n", knn.predict(x_test))
print("\nAccuracy:", knn.score(x_test, y_test))