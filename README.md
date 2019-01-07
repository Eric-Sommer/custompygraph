# Custompygraph
Custompygraph is a wrapper for matplotlib creating two-dimensional line plots which saves you the hassle of specifying each 
and every option everytime you create the plot.
Everything is supposed to work through one call of `make_plot()`, which might be appended with `.show()` or `.savefig()`. For subplots, the settings is slightly more complicated (see below)
The legend is put below the plot area instead of within, mimicking Stata style.

## Arguments

* **data** the data expects a dictionary where each entry contains the label, and the x and y data as a list. The dictionary key 
    will appear in the graph legend

    Example:
    ```python
    data = {'label1': [x1data, y1data], 'label2': [x2data, y2data]}
    ```
     `x` and `y` data can be lists, numpy arrays, panda series or whatever matplotlib accepts as input.

* **xlab, ylab** are strings defining the label for the respective axes
* **title** is the string for the plot title
* **fs** specifies the basic font size applying to xlab and ylab. Legend labels will be a little smaller as well as tick labels.
    Titles will be slightly larger.
* **plottype** either 'line' ( *default* ) or 'scatter'

## Optional Arguments     
* **xlim_low, xlim_high, ylim_low, ylim_high** are integers specifying the limits of the two axes, respectively.
* **lw** specifies the linewidth
* **color** `=['bw', 'color']` specifies whether lines will be black or colored ( *default: bw* ). In the former case, lines will differ by linestyle (solid, dashed, dotted, ...)
* **showlegend** 
* **figs** specifies a tuple with the figure size.
* **style** is a string defining one of the styles from `print(plt.style.available)`
* **subplot**: If True, the function will return only the axis, not the whole plot. Requires **subnum**. See for *subplots* below
* **subnum**: An integer specifying the position of the subplot. See for *subplots* below

### Subplots

If you want to combine several subplots in one figure, you need to
1. Initialize the figure first as a subplot and give the number of rows and columns.
2. define each axis with make_plot, with subplot = True and subnum specified.
3. Do whatever you like with the figure (show, savefig, etc.)

Example for a 1x2 Figure:
```python
import matplotlib.pyplot as plt
from make_plot import make_plot

# 1. Initialize the plot
fig, (ax1, ax2) = plt.subplots(1,2)
# 2. Produce the axes
ax1 = make_plot(data=...,                
                title='Left Plot',
                subplot= True,
                subnum= 121
                )

ax2 = make_plot(data=...,                      
                title='Right Plot',
                subplot=True,
                subnum = 222
                )
# 3. Output
fig.show()
```

## Future extensions

* allow an indefinite number of plots
