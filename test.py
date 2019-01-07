# -*- coding: utf-8 -*-
"""
TESTING MAKEPLOT() Function
"""

import numpy as np

from makegraph import make_plot, combine_subplots

x = np.arange(0, 2*np.pi, 0.01)
y1 = np.sin(x)
y2 = np.sin(2*x)
y3 = np.cos(x)


fig1, ax1 = make_plot(data={'y1': [x, y1],
                            'y2': [x, y2]},
                      color='color',
                      plottype='line',
                      title='Test Plot'
                      )

fig2, ax2 = make_plot(data={'y3': [x, y3]},
                      color='color',
                      plottype='line',
                      ylim_low=-1
                      )

fig1.savefig('fig1.png')
fig2.savefig('fig2.png')



fig3 = plt.figure()
ax2 = fig3.add_subplot(122)

fig3.savefig('combine.png')

