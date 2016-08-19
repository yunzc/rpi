# -*- coding: utf-8 -*-
"""
Created on Sun Feb 07 21:58:10 2016

@author: Dell
"""

from urllib2 import urlopen
from json import load 
import matplotlib.pyplot as plt

lsl = []
maxtemp = []
for sol in range(200,1300):
    apiUrl = "http://marsweather.ingenology.com/v1"
    apiParamlatest = "/latest/?"
    outputFormat = "format=json"
    apiParamarchive = "/archive/?sol="+str(sol)+"&"

    response = urlopen(apiUrl+apiParamarchive+outputFormat)

    json_obj = load(response)

    for aspect in json_obj['results']:
        print "ls:", aspect['ls'], "min:", aspect['min_temp'], "C", "max:", aspect['max_temp'], "C"
        lsl.append(aspect['ls'])
        maxtemp.append(float(aspect['max_temp']))

plt.plot(lsl,maxtemp)