# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:52:14 2020

@author: Yannic Sommer
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
# from datetime import timedelta
from scipy.optimize import curve_fit


# exponential functino for the fit
def func(x, a, b, c):
    return a * np.exp(b*x) + c


# import csv file as pandas DataFrame
df = pd.read_csv("data.csv")
# df = df[df[:, 2] == "SK Magdeburg"]
# df = df.loc("SK Magdeburg")

# convert it to numpy array
# arr = df.to_numpy()

df = df[df['Landkreis'] == "LK Heinsberg"]
# plt.plot(arr[:,5])
# arr = arr.sort(axis=8)
df['Meldedatum'].map(
    lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%f%z').date())
df.sort_values("Meldedatum", inplace=True)
df_sum = df.groupby(["Meldedatum"]).sum()

# array with same length as datapoints

# df_sum = df.sum("Meldedatum")

arr = np.arange(len(df_sum))
df_sum = df_sum.cumsum()


# the fit is performed here
popt, pcov = curve_fit(func, arr, df_sum['AnzahlFall'])

plt.figure()
plt.grid()
plt.xlabel("Tag seit Erfassung")
plt.ylabel("Anzahl der Infizierten")
plt.plot(arr, df_sum['AnzahlFall'], "o", label="data")
plt.plot(arr, func(arr, *popt), label="fit")
plt.legend()
plt.show()


# def fermi(x):
#     return 1 / (np.exp(-x)+1)

# x = np.linspace(-10., 10., 1000)

# plt.figure()
# plt.grid()
# plt.plot(x + 10, fermi(x))
# plt.show()
