# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:06:16 2020

@author: Yannic Sommer
"""


import requests
import os


"File to init Github"

"""Dieser File dient dazu, die Daten von
https://opendata.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0.csv
herunterzuladen.
Die Daten werden als CSV file herunrtergeladen.
"""


url = "https://opendata.arcgis.com/datasets/"
url2 = "917fc37a709542548cc3be077a786c17_0.csv"
url = url+url2
r = requests.get(url, allow_redirects=True)

with open(os.path.join("data.csv"), "wb") as f:
    f.write(r.content)
