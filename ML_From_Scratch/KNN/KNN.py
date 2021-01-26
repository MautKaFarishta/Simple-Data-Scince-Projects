import numpy as np
from collections import Counter

def dist(a,b):
   return np.sqrt(np.sum((a-b)**2))

class KNN:
   def __init__(self,K=5):
      super().__init__()
      self.K=K

   def fit(self,X,y):
      self.XTrain=X
      self.yTrain=y

   def predict(self,X):
      predicted=[]
      for single_X in X:
         #Gives minimum K distances i.e. indices of K nearest neighbours
         distances=[dist(single_X,tP) for tP in self.XTrain]
         minimum=np.argsort(distances)[:self.K]
         # gets the majority of class labels K neighbours from K nearest neighbours
         labels=[self.yTrain[i] for i in minimum]
         predicted.append(Counter(labels).most_common()[0][0])

      return predicted


   
