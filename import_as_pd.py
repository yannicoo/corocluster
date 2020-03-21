# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:52:14 2020

@author: Yannic Sommer
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# import csv file as pandas DataFrame
df = pd.read_csv("data.csv")
# df = df[df[:, 2] == "SK Magdeburg"]
# df = df.loc("SK Magdeburg")

# convert it to numpy array
# arr = df.to_numpy()

df = df[df['Landkreis'] == "LK Heinsberg"]
# plt.plot(arr[:,5])
# arr = arr.sort(axis=8)
df['Meldedatum'].map(lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%f%z').date())
df.sort_values("Meldedatum", inplace=True)

plt.plot(df["Meldedatum"], df['AnzahlFall'])

# a = []
# i = 0
# while(arr[i, 2]=="SK Flensburg"):
#     a.append(arr[i, :])
#     i+=1

# a = np.array(a)

# def fermi(x):
#     return 1 / (np.exp(-x)+1)

# x = np.linspace(-10., 10., 1000)

# plt.figure()
# plt.grid()
# plt.plot(x + 10, fermi(x))
# plt.show()

