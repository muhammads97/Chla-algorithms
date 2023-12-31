import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def get_fit_line(X, Y, log=False):
    '''calculate fitting line for the scatter plots (with log or without)'''
    if log:
        X[X <= 0] = 0.01
        x = np.log10(X)
        Y[Y <= 0] = 0.01
        y = np.log10(Y)
    else:
        x = X
        y = Y
    fit_x = x.reshape((x.shape[0], 1))
    model = LinearRegression()
    model.fit(fit_x, y)
    a0 = model.intercept_
    a1 = model.coef_[0]
    if log:
        x1 = 0.01
        x2 = 1000
        y1 = a0 + a1 * np.log10(x1)
        y2 = a0 + a1 * np.log10(x2)
        y1 = np.power(10, y1)
        y2 = np.power(10, y2)
    else:
        x1 = 0
        x2 = 300
        y1 = a0 + a1 * x1
        y2 = a0 + a1 * x2
    return [x1, x2], [y1, y2]


def scatter_plot(x, y, legend_dict=None, title="", log=False, x_axis="", y_axis=""):
    '''
    scatter plot function
    arguments:
        - x (estimated)
        - y (actual)
        - legend_dict (aditional data to display in the legend (key value pairs))
        - plot title
        - log scale or not
        - x_axis title
        - y_axis title
        - initial scatter color
        - edge color (not used, replaced by the dynamic calculation)
        - classes (optional: list of classes for the scatter plot)
    a pdf of the plot is also saved with the plot title in the relative location
    '''
    color="#0177B6"
    edgecolor="#00B4D8"
    legend_pos="lower right"
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.scatter(x, y, label=title, alpha=0.5, facecolor=color, marker='o', edgecolor=edgecolor)
    fit_x, fit_y = get_fit_line(x, y, log=log)
    if log:
        ax.set_yscale("log")
        ax.set_xscale("log")
        ax.set_yticks([0.01, 0.1, 1, 10, 100, 1000])
        ax.set_yticklabels([0.01, 0.1, 1, 10, 100, 1000])
        ax.set_xticks([0.01, 0.1, 1, 10, 100, 1000])
        ax.set_xticklabels([0.01, 0.1, 1, 10, 100, 1000])
        ax.set_ylim([0.01, 1000])
        ax.set_xlim([0.01, 1000])
        ax.plot([0.01, 1000], [0.01, 1000], "k--")
    else:
        plt.ylim([0, x.max()])
        plt.xlim([0, x.max()])
        ax.plot([0, 300], [0, 300], "k--")

    ax.plot(fit_x, fit_y, color="black", alpha=0.5)
    plt.rc('axes', labelsize=14)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    for k in legend_dict.keys():
        ax.plot([], [], ' ', label="%s: %.2f" % (k, legend_dict[k]))
    plt.legend(loc=legend_pos, fontsize="13")
    plt.show()