import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

df=pd.read_csv('LR single variable/income.csv')
print(df.head(5))

# x=[1,2,3,4,5,6]
# y=[1.2,2.3,4.6,1.2,7.4,5.3]
# initialize linear regression object
reg=linear_model.LinearRegression()
# fit the object 
reg.fit(df[['year']],df.income)

# predction of income in 2025
print(reg.predict([[2025]]))
# print(reg.coef_,reg.intercept_).....y=mx+c

# plot the scatterplot

plt.xlabel('Year')
plt.ylabel('per capita income(US$)')
plt.scatter(df.year,df.income,color='red',marker='*')
plt.plot(df.year,reg.predict(df[['year']]),color='blue')
plt.show()