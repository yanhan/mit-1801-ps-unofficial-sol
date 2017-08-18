from __future__ import division
from __future__ import print_function

import os.path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

def _target(x):
    return (x * x + 1) / (x * x - 1)

def _gradient(x):
    return -4 * x / (x * x - 1)**2

def _odd_fn(x):
    return -2 * x / (x * x - 1)

def _odd_gradient(x):
    return 2 * (x * x + 1) / (x * x - 1)**2

_NR_POINTS = 1000
_MAIN_PLOT_COLOR = "blue"
_GRADIENT_PLOT_COLOR = "green"

def _main():
    x_left_limit = -5
    x_right_limit = 5
    y_lower_limit = -5
    y_upper_limit = 5
    vec_target = np.vectorize(_target)
    vec_gradient = np.vectorize(_gradient)

    plt.figure(figsize=(480/96, 360/96,), dpi=96,)
    axes = plt.gca()
    axes.set_xlim([x_left_limit, x_right_limit])
    axes.set_ylim([y_lower_limit, y_upper_limit])
    first_x_part = np.linspace(x_left_limit, -1.000001, _NR_POINTS)
    second_x_part = np.linspace(-0.999999, 0.999999, _NR_POINTS)
    third_x_part = np.linspace(1.000001, x_right_limit, _NR_POINTS)
    all_x_parts = (first_x_part, second_x_part, third_x_part,)
    for x_part in all_x_parts:
        plt.plot(x_part, vec_target(x_part), color=_MAIN_PLOT_COLOR)
        plt.plot(x_part, vec_gradient(x_part), color=_GRADIENT_PLOT_COLOR)

    plt.axhline(y=0, color="black")
    plt.axvline(x=-1, color="gray", linestyle="dashed",)
    plt.axvline(x=1, color="gray", linestyle="dashed",)
    plt.title("Graph of y = (x^2 + 1) / (x^2 - 1) and its derivative")
    plt.xlabel("x")
    plt.ylabel("y")
    main_plot_patch = mpatches.Patch(color=_MAIN_PLOT_COLOR, label="main plot",)
    derivative_plot_patch = mpatches.Patch(color=_GRADIENT_PLOT_COLOR, label="derivative",)
    plt.legend(handles=[main_plot_patch, derivative_plot_patch,])
    plt.savefig("q1_even.png", dpi=96,)

    vec_odd_fn = np.vectorize(_odd_fn)
    vec_odd_gradient = np.vectorize(_odd_gradient)
    plt.clf()
    axes = plt.gca()
    axes.set_xlim([x_left_limit, x_right_limit])
    axes.set_ylim([y_lower_limit, y_upper_limit])
    for x_part in all_x_parts:
        plt.plot(x_part, vec_odd_fn(x_part), color=_MAIN_PLOT_COLOR,)
        plt.plot(x_part, vec_odd_gradient(x_part), color=_GRADIENT_PLOT_COLOR,)
    plt.axhline(y=0, color="black")
    plt.axvline(x=-1, color="gray", linestyle="dashed",)
    plt.axvline(x=1, color="gray", linestyle="dashed",)
    plt.title("Graph of y = (-2x) / (x^2 - 1) and its derivative")
    plt.xlabel("x")
    plt.ylabel("y")
    main_plot_patch = mpatches.Patch(color=_MAIN_PLOT_COLOR, label="main plot",)
    derivative_plot_patch = mpatches.Patch(color=_GRADIENT_PLOT_COLOR, label="derivative",)
    plt.legend(handles=[main_plot_patch, derivative_plot_patch,])
    plt.savefig("q1_odd.png", dpi=96,)

if __name__ == "__main__":
    _main()
