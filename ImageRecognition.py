# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 22:19:17 2018

@author: magda
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import functools as ft

def threshold(imageArray) :
    balanceAr = []
    newAr = imageArray

    
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = ft.reduce((lambda x, y: int(x) + int(y)), eachPix[:3])/len(eachPix[:3])
            balanceAr.append(avgNum)
    balance = ft.reduce((lambda x, y: int(x) + int(y)), balanceAr)/len(balanceAr)      
      
    for eachRow in newAr:
        for eachPix in eachRow:
           if ft.reduce((lambda x, y: int(x) + int(y)), eachPix[:3])/len(eachPix[:3]) > balance:
               eachPix[0] = 255
               eachPix[1] = 255
               eachPix[2] = 255
               'eachPix[3] = 255'
           else:
               eachPix[0] = 0
               eachPix[1] = 0
               eachPix[2] = 0
               'eachPix[3] = 255'
    return newAr
               
i0 = Image.open('img/num0.jpg')
iar0 = np.array(i0)

i1 = Image.open('img/num4.jpg')
iar1 = np.array(i1)

i2 = Image.open('img/num2.jpg')
iar2 = np.array(i2)

i3 = Image.open('img/num3.jpg')
iar3 = np.array(i3)

threshold(iar0)
threshold(iar1)
threshold(iar2)
threshold(iar3)

fig = plt.figure()
ax0 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
ax1 = plt.subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8, 6), (0, 4), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8, 6), (4, 4), rowspan=4, colspan=3)

ax0.imshow(iar0)
ax1.imshow(iar1)
ax2.imshow(iar2)
ax3.imshow(iar3)

plt.show()