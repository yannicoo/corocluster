# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:06:16 2020

@author: Yannic Sommer
"""


import requests
import numpy as np


"File to init Github"

"""Dieser File dient dazu, die Daten von
https://npgeo-corona-npgeo-de.hub.arcgis.com/ herunterzuladen"""


url = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/"
url2 = "RKI_Landkreisdaten/FeatureServer/0/query?where=1%3D1&outFields="
url3 = "*&outSR=4326&f=json"
url = url + url2 + url3
r = requests.get(url, allow_redirects=True)
open("data", "wb").write(r.content)
data = np.genfromtxt("data", delimiter=",")
data.reshape((36, data.size/36))
