# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 19:49:06 2019

@author: Work Is Fun
"""

import pandas as pd
from sklearn.linear_model import LinearRegression


df = pd.read_excel("linear_reg_tut1.xls")       # Read the dataset
print(df.describe())

X_train = df["Horsepower"][:-100]
Y_train = df["Price"][:-100]

X_test = df["Horsepower"][-100:]
Y_test = df["Price"][-100:]

reg = LinearRegression()
reg.fit([X_train,Y_train], Y_train)      # Train Model

#Print the coefficients
print("Slope = "+reg.coef_+"\n Intercept = "+reg.intercept_)

#reg.score(X_train)

