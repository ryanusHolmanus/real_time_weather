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
from numpy import genfromtxt
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

fig = matplotlib.pyplot.figure(num=None,figsize=(10,10),dpi=80)
ax1=fig.add_subplot(811)
ax2=fig.add_subplot(812)
ax3=fig.add_subplot(813)
ax4=fig.add_subplot(814)
ax5=fig.add_subplot(815)
ax6=fig.add_subplot(816)
ax7=fig.add_subplot(817)
ax1.title.set_text('Temperature, F')
ax2.title.set_text('Pressure, ')
ax3.title.set_text('Humidity, %')
ax4.title.set_text('Ozone, ')
ax5.title.set_text('Wind Speed, ')
ax6.title.set_text('Prec Intensity, ')
ax7.title.set_text('Prec Probability, ')
matplotlib.pyplot.tight_layout()
fig.show()
fig.canvas.draw()
ini=os.stat('rtw.csv').st_mtime
print(ini)


while(True):
    ini2=os.stat('rtw.csv').st_mtime
    print(ini,ini2)
    if ini2 > ini:
        ad = genfromtxt('rtw.csv', delimiter=',')
        ax1.plot(ad[0], ad[1])
        ax2.plot(ad[0], ad[2])
        ax3.plot(ad[0], ad[3])
        ax4.plot(ad[0], ad[4])
        ax5.plot(ad[0], ad[5])
        ax6.plot(ad[0], ad[6])
        ax7.plot(ad[0], ad[7])
        matplotlib.pyplot.tight_layout()
        fig.canvas.draw()
        ini=ini2
    time.sleep(30)
