# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:52:14 2020

@author: Yannic Sommer
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.optimize import curve_fit

# Das Model kann mit den folgenden Funktionen modelliert werden
# Wir haben uns dazu entschlossen, besonders für den Beginn der Epidemie
# einen exponentiellen Verlauf anzunehmen.


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


# Die Namen der Landkreise könne aus der "data.csv" ermittelt werden
# Es soll später noch eine Loop über die Werte gelaufen werden, um automatisch
# die Parameter für alle Landkreise zu bestimmen.
# Mit Strg + 1 kann aus  und einkommentiert werden, um die verschiedenen
# Landkreise zu betrachten
df = df[df['Landkreis'] == "LK Kleve"]
# df = df[df['Landkreis'] == "SK Kaiserslautern"]
# df = df[df['Landkreis'] == "SK Leipzig"]
# df = df[df['Landkreis'] == "SK Nürnberg"]
# df = df[df['Landkreis'] == "SK Berlin Mitte"]
# df = df[df['Landkreis'] == "SK München"]

# Hier werden die Daten für die Landkreise nach den Daten sortiert
df['Meldedatum'].map(
    lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%f%z').date())
df.sort_values("Meldedatum", inplace=True)

# Hier wird über alle verschiedenen Klassen summiert.
df_sum = df.groupby(["Meldedatum"]).sum()

# Ein array zur hilfe der Visualierung
arr = np.arange(len(df_sum))
# Die kummulierte Summe der Datan, um die absolute Anzahl der Infizierten zu
# erhalten
df_sum = df_sum.cumsum()


# the fit is performed here
# Es handelt sich hier um einen Least-Squares fit
popt, pcov = curve_fit(func, arr, df_sum['AnzahlFall'])

# Huer wird die Basisreproduktionsrate berechnet.
base = np.round(np.exp(popt[1]), decimals=3)

# Hier werden die Plots zur Visualisierung erstellt.
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
