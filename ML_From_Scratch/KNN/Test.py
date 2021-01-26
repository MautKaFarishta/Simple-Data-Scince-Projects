from KNN import KNN
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np

# Simple accuracy function 
def accuracy(true, pred):
    accuracy = np.sum(true == pred) / len(true)
    return accuracy

iris = datasets.load_iris()
X, y = iris.data, iris.target

# Splitting the data to train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)
KNNmodel = KNN(K=5)
KNNmodel.fit(X_train, y_train)
predictions = KNNmodel.predict(X_test)
print("Accuracy-", accuracy(y_test, predictions))