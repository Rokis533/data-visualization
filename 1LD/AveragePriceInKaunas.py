# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 22:58:40 2022

@author: Rokas
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

area = []
price = []
data= pd.read_csv("Data.csv", sep=';')
print(data.Area)
                

df = pd.DataFrame({'Area': data.Area,'Average prices': data.Price})
mean_df = df.groupby('Area').mean().reset_index()
print(mean_df)
mean_df.plot(x ='Area', y='Average prices', kind = 'bar')
plt.show()