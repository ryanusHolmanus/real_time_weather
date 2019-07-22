#   Dark Sky API key
#   a7e68689cf67de5251f639f19ef23601

#https://api.darksky.net/forecast/a7e68689cf67de5251f639f19ef23601/46.2044,6.1432

#from darksky import forecast
#gen = forecast(a7e68689cf67de5251f639f19ef23601, 46.2044, 6.1432)
#gen['currently']

#GET https://api.darksky.net/forecast/a7e68689cf67de5251f639f19ef23601/46.2044,6.1432?exclude=minutely,hourly,daily,alerts,flags | sed 's/,/\n/g' | tr -d } | tr -d { | sed 's/"//g'

import matplotlib
matplotlib.use("TKAgg")
import pylab

import requests
import sys
import numpy as np
import os
import subprocess
import json
import pandas as pp
from pandas.io.json import json_normalize
import time
#import matplotlib.pyplot as plt

#iterate
x=[]
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
y6=[]
y7=[]
matplotlib.pyplot.ion()

#data = subprocess.check_output('GET https://api.darksky.net/forecast/a7e68689cf67de5251f639f19ef23601/46.2044,6.1432?exclude=minutely,hourly,daily,alerts,flags',shell=True)
r = requests.get("https://api.darksky.net/forecast/a7e68689cf67de5251f639f19ef23601/46.2044,6.1432?exclude=minutely,hourly,daily,alerts,flags")
data = r.text
jdata = json.loads(data)
df = pp.DataFrame.from_dict(json_normalize(jdata), orient='columns')
temp = df["currently.temperature"][0]
pres = df["currently.pressure"][0]
hum = df["currently.humidity"][0]
tim = df["currently.time"][0]
ozo = df["currently.ozone"][0]
wind = df["currently.windSpeed"][0]
precInt = df["currently.precipIntensity"][0]
precProb = df["currently.precipProbability"][0]
a = [tim, temp, pres, hum, ozo, wind, precInt, precProb]
print(a)
fig = matplotlib.pyplot.figure(num=None,figsize=(10,10),dpi=80)
ax1=fig.add_subplot(811)
ax2=fig.add_subplot(812)
ax3=fig.add_subplot(813)
ax4=fig.add_subplot(814)
ax5=fig.add_subplot(815)
ax6=fig.add_subplot(816)
ax7=fig.add_subplot(817)
x.append(tim)
y1.append(temp)
y2.append(pres)
y3.append(hum)
y4.append(ozo)
y5.append(wind)
y6.append(precInt)
y7.append(precProb)
ax1.plot(x,y1)
ax2.plot(x,y2)
ax3.plot(x,y3)
ax4.plot(x,y4)
ax5.plot(x,y5)
ax6.plot(x,y6)
ax7.plot(x,y7)
ax1.title.set_text('Temperature, F')
ax2.title.set_text('Pressure, ')
ax3.title.set_text('Humidity, %')
ax4.title.set_text('Ozone, ')
ax5.title.set_text('Wind Speed, ')
ax6.title.set_text('Prec Intensity, ')
ax7.title.set_text('Prec Probability, ')
matplotlib.pyplot.tight_layout()
#fig.show()
#fig.canvas.draw()

while(True):
    #data = subprocess.check_output('GET https://api.darksky.net/forecast/a7e68689cf67de5251f639f19ef23601/46.2044,6.1432?exclude=minutely,hourly,daily,alerts,flags',shell=True)
    r = requests.get("https://api.darksky.net/forecast/a7e68689cf67de5251f639f19ef23601/46.2044,6.1432?exclude=minutely,hourly,daily,alerts,flags")
    data = r.text
    jdata = json.loads(data)
    df = pp.DataFrame.from_dict(json_normalize(jdata), orient='columns')
    temp = df["currently.temperature"][0]
    pres = df["currently.pressure"][0]
    hum = df["currently.humidity"][0]
    tim = df["currently.time"][0]
    ozo = df["currently.ozone"][0]
    wind = df["currently.windSpeed"][0]
    precInt = df["currently.precipIntensity"][0]
    precProb = df["currently.precipProbability"][0]
    a = [tim, temp, pres, hum, ozo, wind, precInt, precProb]
    print(a)
    x.append(tim)
    y1.append(temp)
    y2.append(pres)
    y3.append(hum)
    y4.append(ozo)
    y5.append(wind)
    y6.append(precInt)
    y7.append(precProb)
    astr=str(tim)+","+str(temp)+","+str(pres)+","+str(hum)+","+str(ozo)+","+str(wind)+","+str(precInt)+","+str(precProb)
    print(astr)
    with open('rtw.csv','a') as ff:
        ff.write(astr+"/n")
    ff.close()
    ax1.plot(x, y1)
    ax2.plot(x, y2)
    ax3.plot(x, y3)
    ax4.plot(x, y4)
    ax5.plot(x, y5)
    ax6.plot(x, y6)
    ax7.plot(x, y7)
    #matplotlib.pyplot.tight_layout()
    #fig.canvas.draw()
    time.sleep(87)
#append to file)
#plot realtime
