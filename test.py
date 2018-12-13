# -*- coding: utf-8 -*-
"""
TESTING MAKEPLOT() Function
"""

import numpy as np
from makegraph import makeplot

x = np.arange(0, 2*np.pi, 0.5)
y1 = np.sin(x)
y2 = np.sin(2*x)

makeplot(data={'y1': [x, y1],
               'y2': [x, y2]},
               color='color',
               plottype='scatter',
               ).show()

