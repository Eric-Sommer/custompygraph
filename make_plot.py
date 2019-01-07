# -*- coding: utf-8 -*-
"""
# Make Plot

@author: Eric Sommer, ericsomm@gmx.de
"""

import matplotlib.pyplot as plt


def make_plot(data,
              xlab='',
              ylab='',
              title='',
              fs=14,
              color='bw',
              showlegend=True,
              figs=(5*1.618, 5),
              style='seaborn-whitegrid',
              plottype='line',
              **kwargs
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
             'color': ['b-', 'r-', 'g-', 'c-', 'm-', 'b-', 'r-', 'g-', 'c-']
             }
    colors = {'bw': ['black' for i in range(0, 9)],
              'color': ['navy',
                        'maroon',
                        'forestgreen',
                        'darkmagenta',
                        'lightskyblue',
                        'darkorange']
             }

    markers = {'bw': ['.', ',', 'o', 's', 'D', 'v', '+'],
               'color': ['o' for i in range(0, 9)]
               }

    fillstyles = {'bw': 'none',
                  'color': 'full'}
    # If limits are not given, they are set automatically
    firstkey = list(data.keys())[0]

    if not isinstance(data[firstkey][0].min(), (int, float)):
        raise Exception('Invalid entry data')
    #type(data[firstkey][0]).__module__ not in ['numpy', 'pandas.core.series']:
    #   raise Exception('Only Numpy array or Panda Series allowed as data input')

    # Optional arguments
    color = kwargs.get('color', 'bw')
    xlim_low = kwargs.get('xlim_low', data[firstkey][0].min() * 1.1)
    xlim_high = kwargs.get('xlim_high', data[firstkey][0].max() * 1.1)
    ylim_low = kwargs.get('ylim_low', data[firstkey][1].min() * 1.1)
    ylim_high = kwargs.get('ylim_high', data[firstkey][1].max() * 1.1)
    xaxis_grid = kwargs.get('xaxis_grid', False)
    yaxis_grid = kwargs.get('yaxis_grid', True)
    subplot = kwargs.get('subplot', False)
    subnum = kwargs.get('subnum')

    # check whether subnum is specified
    if subplot:
        assert subnum, "Subplot is True, but no subnum is defined"

    lw = kwargs.get('lw', 2)
    # Switch off grid lines?
    plt.gca().xaxis.grid(xaxis_grid)
    plt.gca().yaxis.grid(yaxis_grid)

    # Start plotting
    if not subplot:
        plt.clf()
        fig = plt.figure(figsize=figs)
        ax = fig.add_subplot(111)
    if subplot:
        ax = plt.subplot(subnum)

    ax.tick_params(axis='both',
                   which='major',
                   labelsize=fs-2)

    # Set limits
    try:
        ax.set_ylim(ylim_low, ylim_high)
    except ValueError:
        raise Exception('Invalid limits for y axis. You may need to specify them yourself.')
    try:
        ax.set_xlim(xlim_low, xlim_high)
    except ValueError:
        raise Exception('Invalid limits for x axis. You may need to specify them yourself.')

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
    axlist = []
    for l, plotdata in data.items():
        if plottype == 'line':
            ax.plot(plotdata[0],
                    plotdata[1],
                    lines[color][count],
                    c=colors[color][count],
                    label=l,
                    linewidth=lw
                    )
        if plottype == 'scatter':
            ax.scatter(plotdata[0],
                       plotdata[1],
                       marker=markers[color][count],
                       c=colors[color][count],
                       # fillstyle=fillstyles[color],
                       label=l
                    )
        count += 1

    if showlegend:
        ax.legend(loc='upper center',
                  fontsize=fs,
                  bbox_to_anchor=(0.48, -0.15),
                  ncol=2)

    if subplot:
        return ax
    if not subplot:
        return fig
