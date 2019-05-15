# -*- coding: utf-8 -*-
"""
Created on Sun May  5 09:01:59 2019

@author: Pavan S Gowda
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('s.csv')

X=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,y_train)
y_pred=lr.predict(5.5)
