#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 19:45:19 2022

@author: max
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy import wcs
from astropy.wcs import WCS
import astropy.convolution as conv

data,header = fits.getdata('co_mom1_test1.fits',header=True)

fig = plt.figure(figsize=(7,7))

Ny,Nx = data.shape
X = np.arange(Nx)
Y = np.arange(Ny)
XX,YY = np.meshgrid(X,Y)
ax = plt.subplot(projection='3d')
data1 = data.copy()

ra = XX.flatten()
dec = YY.flatten()
da = data1.flatten()


Nk=3
k = np.ones((Nk,Nk))/Nk**2
data_con = conv.convolve(data1,k,nan_treatment='fill',fill_value=np.nan)
ax=fig.add_subplot(projection='3d')

c=np.arange(71890)/71890
p=ax.scatter(ra,dec,da,c=plt.cm.coolwarm(1*c))
plt.xlabel('x')
plt.ylabel('y')

plt.plot(662,640,10,'ro')
plt.plot(709,633,10,'yo')
