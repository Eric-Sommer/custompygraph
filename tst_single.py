# -*- coding: utf-8 -*-
"""
TESTING MAKEPLOT() Function
"""

import numpy as np
import matplotlib.pyplot as plt

from make_plot import make_plot

x = np.arange(0, 2*np.pi, 0.5)
y1 = np.sin(x)
y2 = np.sin(2*x)
y3 = np.cos(x)
y4 = np.random.random(len(x))

plt.style.use('default')

for pt in ['scatter']:
    make_plot(data={'y1': [x, y1],
              'y2': [x, y2]},            
              color='bw',
              plottype=pt,
              xaxis_grid=False,
              yaxis_grid=True,
              title='Graph title',
              hline=(0, 0.2),
              ).savefig('single.png')

