# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:52:14 2020

@author: Yannic Sommer
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime
# from datetime import timedelta
from scipy.optimize import curve_fit


# exponential function for the fit (with offset)
def func(x, a, b, c):
    return a * np.exp(b*x) + c

# # exponential function for the fit (without offset)
# def func(x, a, b):
#     return a * np.exp(b*x)

# # sigmoid function for the fit
# def func(x, a, b, c):
#     return a / (1. + np.exp(-b*(x - c)))


# import csv file as pandas DataFrame
df = pd.read_csv("data.csv")
# df = df[df[:, 2] == "SK Magdeburg"]
# df = df.loc("SK Magdeburg")

# convert it to numpy array
# arr = df.to_numpy()

# df = df[df['Landkreis'] == "LK Kleve"]
# df = df[df['Landkreis'] == "SK Kaiserslautern"]
# df = df[df['Landkreis'] == "SK Leipzig"]
# df = df[df['Landkreis'] == "SK Nürnberg"]
df = df[df['Landkreis'] == "SK Berlin Mitte"]
# df = df[df['Landkreis'] == "SK München"]

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
base = np.round(np.exp(popt[1]), decimals=3)

plt.figure(figsize=(12, 8))
plt.grid()
plt.title(df["Landkreis"][df.index[0]], fontsize=20)
plt.xlabel(u"Tag $x$ seit Beginn der Erfassung", fontsize=16)
plt.ylabel("Anzahl der Infizierten", fontsize=16)
plt.plot(arr, df_sum['AnzahlFall'], "o", label="data")
plt.plot(arr, func(arr, *popt),
         label = u"fit: f(x)=%.3f$\cdot\exp(%.3f \cdot x)$\n Geschätzte Basisreproduktionszahl: %.3f"%(popt[0], popt[1], base))
# textstr = "".join((r'$a=%.3f$' %(popt[1])))
# plt.text(1., popt[0], textstr, fontsize=10, verticalalignment='top')
plt.legend(fontsize=16)
plt.show()

"""
Diese ist natürlich deutlich geringer als der wahre Wert, da die
Dunkelziffer komplett vernachlässigt wird.
"""
# print("Geschätzte Basisreproduktionszahl", np.round(np.exp(popt[1]), decimals=5))

# def fermi(x):
#     return 1 / (np.exp(-x)+1)

# x = np.linspace(-10., 10., 1000)

# plt.figure()
# plt.grid()
# plt.plot(x + 10, fermi(x))
# plt.show()
