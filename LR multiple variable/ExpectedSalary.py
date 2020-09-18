import pandas as pd
from sklearn import linear_model
from word2number import w2n
import math
df=pd.read_csv('LR multiple variable/hiring.csv')

# Filling empty values and converting to int
df.experience=df.experience.fillna('zero')
print(df.experience)
df.experience = df.experience.apply(w2n.word_to_num)

# Filling empty values
median_score=math.floor(df.test_score.median())

df.test_score=df.test_score.fillna(median_score)

# Creating linear regression object
reg=linear_model.LinearRegression()
reg.fit(df[['experience','test_score','interview_score']],df.salary)

print(reg.coef_,reg.intercept_)
print(reg.predict([[2,9,6]]))
print(reg.predict([[12,10,10]]))