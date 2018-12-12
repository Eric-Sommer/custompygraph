# -*- coding: utf-8 -*-
"""
# Make Plot

@author: Eric Sommer, ericsomm@gmx.de
"""

import matplotlib.pyplot as plt
import pandas as pd

def makeplot(data,
             xlim_low=0,
             xlim_high=1,
             ylim_low=0,
             ylim_high=1,
             xlab='',
             ylab='',
             title='',
             fs=14,
             lw=2,
             color='bw',
             showlegend=True,
             figs=(10,5),
             style='seaborn-whitegrid'
             ):
    '''
    Wrapper for matplotlib plots, avoiding the hassle of specifying the look each and every time
	
	data is a dictionary, where each entry contains the label, and the x and y data as a list.
	
	Example:
    data = {'label1': [x1data, y1data]
			'label2': [x2data, y2data]}	
    '''	
			   
    plt.style.use(style)

    lines = {'bw': ['k-', 'k--', 'k:', 'k-.', 'k-', 'k--', 'k:', 'k-.'],
             'color': ['b-', 'r-', 'g-', 'c-', 'm-']
             }

    plt.clf()
    fig = plt.figure(figsize=figs)
    ax = fig.add_subplot(111)
    # Switch off vertical lines
    plt.gca().xaxis.grid(False)
    ax.tick_params(axis='both',
                   which='major',
                   labelsize=fs-2)


    # Set limints
    ax.set_ylim(ylim_low, ylim_high)
    ax.set_xlim(xlim_low, xlim_high)
    # Title
    ax.set_title(title, size=fs+2)
    # X Axis Label
    ax.set_xlabel(xlab,
                  size=fs)
    # Y axis label
    ax.set_ylabel(ylab,
		  size=fs)   
    # legend
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.2,
                     1.05 * box.width, 1.05 * (box.height * 0.85)])
    count = 0
    for l, plotdata in data.items():
        ax.plot(plotdata[0],
                plotdata[1],
                lines[color][count],
                label=l,
                linewidth=lw
                )
        count += 1
    if showlegend:
        ax.legend(loc='upper center',
                  fontsize=fs,
                  bbox_to_anchor=(0.48, -0.15),
                  ncol=2)
    # Return the Plot
    return plt
