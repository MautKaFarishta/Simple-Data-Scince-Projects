from KNN import KNN
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np

def accuracy(true, pred):
    accuracy = np.sum(true == pred) / len(true)
    return accuracy

iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
k = 3
clf = KNN(K=k)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print("Accuracy", accuracy(y_test, predictions))