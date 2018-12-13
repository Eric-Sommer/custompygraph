# Custompygraph
Custompygraph is a wrapper for matplotlib creating two-dimensional line plots which saves you the hassle of specifying each 
and every option everytime you create the plot.
Everything is supposed to work through one call of `makeplot()`, which might be appended with `.show()` or `.savefig()`.
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

### Optional Arguments     
* **xlim_low, xlim_high, ylim_low, ylim_high** are integers specifying the limits of the two axes, respectively.
* **lw** specifies the linewidth
* **color** `=['bw', 'color']` specifies whether lines will be black or colored. In the former case, lines will differ by linestyle (solid, dashed, dotted, ...)
* **showlegend** 
* **figs** specifies a tuple with the figure size.
* **style** is a string defining on of the styles from `print(plt.style.available)`

## Future extensions

* allow further plot types
* allow an indefinite number of plots
