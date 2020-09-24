# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:11:56 2020

@author: Sergey
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:24:20 2020

@author: Sergey
"""

import matplotlib.pyplot as plt
import numpy as np

def psiE(x, n):
    return (np.sqrt(2)*np.sin(x*np.pi*n), n**2)  # Прямоугольная одномерная потенциальная яма с бесконечно высокими стенками

vpsiE = np.vectorize(psiE)
x = np.arange(0, 1, 0.001)
fig, ax = plt.subplots(1,2)
for i in range(5):
    psi, E = vpsiE(x, i + 1)
    ax[0].plot(x, E + psi)
    ax[0].plot(x, E, 'k-')
    ax[1].plot(x, E + psi**2)
    ax[1].plot(x, E, 'k-')
pity = np.arange(0, 30, 0.01)
pitx_left = 0*np.ones([len(pity)])
pitx_right = 1*np.ones([len(pity)])
for _ax in ax:
    _ax.set_xticks([])
    _ax.set_yticks([])
    _ax.set_frame_on(False)
    _ax.plot(pitx_left, pity, 'k-', lw =4)
    _ax.plot(pitx_right, pity, 'k-', lw =4)
    _ax.set_xlim(-0.2, 1.2)
    _ax.set_ylim(0, 30)
#ax.set_xlabel(r'$x/l$')
#ax.set_ylabel(r'$E_n + \psi_n(x)$')
#ax.yaxis.set_major_locator(plt.MaxNLocator(8))
#ax.xaxis.set_major_locator(plt.MaxNLocator(5))
#ax.grid(True, linestyle=':')
#ax.set_ylim(0, 1.8)
plt.show()