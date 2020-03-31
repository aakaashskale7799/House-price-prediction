# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:22:03 2020

@author: User
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv("train.csv")
bata=pd.read_csv("test.csv")
print("==========================")
print(data.head())
#data.shape
data["LotFrontage"]
data["LotFrontage"].mean()
data["LotFrontage"]=data["LotFrontage"].replace(np.NaN,data["LotFrontage"].mean())
data.LotFrontage.isnull().sum()
#deleting one coloumn
del data["Alley"]

data.shape

data.dropna()
data.shape
data.columns[data.isnull().sum()<2]
#data.isnull().sum()>00
#deleting columns with missing values
mis=data.columns[data.isnull().sum()>00]
mis
for i in mis:
    print("deleting column: ",i)
    del data[i]
    print(data.shape)
data.shape

data.isnull().sum()
data.notnull().sum()
target=data["SalePrice"]
datadf=pd.DataFrame(data,index=None)
print("now lableling=========")
col=datadf.columns
"""for i in col:
    #print(i)
    datadf[i]=LabelEncoder()
"""
print("===================================")

print("labelling done")

features=datadf
features


