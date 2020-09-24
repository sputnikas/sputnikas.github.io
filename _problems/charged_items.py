# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:24:20 2020

@author: Sergey
"""

import matplotlib.pyplot as plt
import numpy as np

def phi(x):
    return 1./x if x > 1 else 1.0  # сфера
    #return 1./x if x > 1 else (3 - x**2)/2  # шар

def E(x):
    return 1./x**2 if x > 1 else 0.0  # сфера
    #return 1./x**2 if x > 1 else x          # шар

vphi = np.vectorize(phi)
vE = np.vectorize(E)
x = np.arange(0, 5, 0.001)
fig, ax = plt.subplots(2)
ax[0].plot(x, vphi(x))
ax[0].set_ylabel(r'$\varphi/\varphi_0$')
ax[0].set_ylim(0, 1.8)
ax[1].plot(x, vE(x))
ax[1].set_ylabel(r'$E_r/E_0$')
ax[1].set_ylim(0, 1.5)
for _ax in ax:
    _ax.set_xlim(0, 5)
    #_ax.set_ylim(0, 1.5)
    _ax.set_xlabel(r'$r/a$')
    _ax.grid(True, linestyle=':')
    _ax.yaxis.set_major_locator(plt.MaxNLocator(8))
    _ax.xaxis.set_major_locator(plt.MaxNLocator(5))

plt.show()