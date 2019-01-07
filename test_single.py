# -*- coding: utf-8 -*-
"""
TESTING MAKEPLOT() Function
"""

import numpy as np
import matplotlib.pyplot as plt

from make_plot import make_plot

x = np.arange(0, 2*np.pi, 0.01)
y1 = np.sin(x)
y2 = np.sin(2*x)
y3 = np.cos(x)
y4 = np.random.random(len(x))



make_plot(data={'y1': [x, y1],
          'y2': [x, y2]},
          color='color',
          plottype='line',

          title='Graph title',
          ).savefig('single.png')
