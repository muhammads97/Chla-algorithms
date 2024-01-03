#
# Copyright (c) 2024 Muhammad Salah msalah.29.10@gmail.com
# Licensed under AGPL-3.0-or-later.
# Refer to LICENSE for the AGPL license.
# All rights reserved.
# This project is developed as part of my research in the Remote Sensing Laboratory
# in Kyoto University of Advanced Science towards my Master's Degree course.
#

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


def get_fit_line(X, Y):
    """calculate fitting line for the scatter plots"""
    X[X <= 0] = 0.01
    x = np.log10(X)
    Y[Y <= 0] = 0.01
    y = np.log10(Y)
    fit_x = x.reshape((x.shape[0], 1))
    model = LinearRegression()
    model.fit(fit_x, y)
    a0 = model.intercept_
    a1 = model.coef_[0]
    x1 = 0.01
    x2 = 1000
    y1 = a0 + a1 * np.log10(x1)
    y2 = a0 + a1 * np.log10(x2)
    y1 = np.power(10, y1)
    y2 = np.power(10, y2)
    return [x1, x2], [y1, y2]


def hex_to_rgb(value):
    value = value.lstrip("#")
    lv = len(value)
    return tuple(int(value[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb


def darken(hex):
    """darken a color dynamically for the scatter border"""
    rgb = hex_to_rgb(hex)
    factor = 0.6
    rgb = list(rgb)
    rgb[0] = int(factor * rgb[0])
    rgb[1] = int(factor * rgb[1])
    rgb[2] = int(factor * rgb[2])
    rgb = tuple(rgb)
    return rgb_to_hex(rgb)


def get_classes_colors(classes, color):
    """for scatter plots, dynamically calculated colors to get different classes suitable colors from an initial color"""
    rgb = hex_to_rgb(color)
    add = 128
    colors = []
    for c in classes:
        colors.append(rgb_to_hex(rgb))
        rgb = list(rgb)
        rgb[0] = np.abs(add - rgb[0])
        rgb[1] = np.abs(add - rgb[1])
        rgb[2] = np.abs(add - rgb[2])
        rgb = tuple(rgb)
        add = (add + 127) % 256
    return colors


def scatter_plot(
    x,
    y,
    legend_dict=None,
    title="",
    x_axis="",
    y_axis="",
    color="#0177B6",
    classes=None,
):
    """
    scatter plot function
    arguments:
        - x (estimated)
        - y (actual)
        - legend_dict (aditional data to display in the legend (key value pairs))
        - plot title
        - x_axis title
        - y_axis title
        - initial scatter color
        - classes (optional: list of classes for the scatter plot)
    """
    legend_pos = "lower right"
    if classes == None:
        classes = [[y.min() - 1, y.max() + 1]]
    colors = get_classes_colors(classes, color)
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    cl = 0
    # ax.plot([], [], ' ', label=title)
    for c in classes:
        x_c = x[(x > c[0]) & (x <= c[1])]
        y_c = y[(x > c[0]) & (x <= c[1])]
        # print(x_c, y_c, colors[cl])
        ax.scatter(
            x_c,
            y_c,
            alpha=0.5,
            facecolor=colors[cl],
            marker="o",
            edgecolor=darken(colors[cl]),
        )
        cl += 1
    fit_x, fit_y = get_fit_line(x, y)
    ax.set_yscale("log")
    ax.set_xscale("log")
    ax.set_yticks([0.01, 0.1, 1, 10, 100, 1000])
    ax.set_yticklabels([0.01, 0.1, 1, 10, 100, 1000])
    ax.set_xticks([0.01, 0.1, 1, 10, 100, 1000])
    ax.set_xticklabels([0.01, 0.1, 1, 10, 100, 1000])
    ax.set_ylim([0.01, 1000])
    ax.set_xlim([0.01, 1000])
    ax.plot([0.01, 1000], [0.01, 1000], "k--")

    ax.plot(fit_x, fit_y, color="black", alpha=0.5)
    plt.rc("axes", labelsize=14)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_title(title)

    for k in legend_dict.keys():
        ax.plot([], [], " ", label="%s: %.2f" % (k, legend_dict[k]))
    plt.legend(loc=legend_pos, fontsize="13")
    plt.show()
