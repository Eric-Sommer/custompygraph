#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:19:09 2019

@author: eric
"""

import matplotlib.pyplot as plt
from make_plot import make_plot
import numpy as np


plt.close("all")
x = np.arange(0, 2*np.pi, 0.01)
y1 = np.sin(x)
y2 = np.sin(2*x)
y3 = np.cos(x)


# 1. Initialize the plot
fig, (ax1, ax2) = plt.subplots(1,2)
# 2. Create the axes
ax1 = make_plot(data={'y1': [x, y1]},
                title='Left Plot',
                subplot = True,
                subnum = 221
                )

ax2 = make_plot(data={'y3': [x, y3]},
                title='Right Plot',
                subplot=True,
                xaxis_grid=False,
                subnum = 222
                )
# 3. Output
fig.savefig('combined.png')