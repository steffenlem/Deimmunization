from operator import itemgetter

before = [[108, 26], [109, 26], [48, 24], [49, 24], [118, 24], [107, 23], [110, 23], [119, 21], [102, 19], [103, 19],
          [104, 19], [105, 19], [106, 19], [113, 19], [114, 19], [115, 19], [47, 18], [117, 18], [42, 17], [43, 17],
          [44, 17], [45, 17], [46, 17], [111, 17], [112, 17], [26, 16], [27, 16], [28, 16], [29, 16], [30, 16],
          [31, 16],
          [32, 16], [33, 16], [125, 16], [116, 15], [120, 14], [121, 14], [50, 13], [92, 12], [93, 12], [94, 12],
          [95, 12], [96, 12], [122, 12], [123, 12], [124, 12], [41, 11], [88, 11], [89, 11], [90, 11], [91, 11],
          [7, 10],
          [8, 10], [9, 10], [10, 10], [11, 10], [12, 10], [25, 10], [126, 10], [53, 8], [54, 8], [55, 8], [4, 8],
          [5, 8],
          [6, 8], [65, 8], [66, 8], [67, 8], [68, 8], [69, 8], [70, 8], [51, 7], [52, 7], [56, 7], [63, 7], [64, 7],
          [34, 6],
          [101, 6], [71, 5], [131, 5], [132, 5], [133, 5], [127, 4], [128, 4], [129, 4], [130, 4], [62, 3], [13, 2],
          [14, 2],
          [15, 2], [72, 1], [73, 1], [97, 1], [98, 1], [99, 1], [100, 1], [57, 1], [58, 1], [59, 1], [60, 1], [61, 1],
          [134, 1], [135, 1], [136, 1], [137, 1], [138, 1], [139, 1]]

after = [[26, 16], [27, 16], [28, 16], [29, 16], [30, 16], [31, 16], [32, 16], [33, 16], [118, 15], [125, 14],
         [111, 13],
         [112, 13], [119, 12], [42, 11], [43, 11], [44, 11], [45, 11], [46, 11], [47, 11], [48, 11], [49, 11], [88, 11],
         [89, 11], [90, 11], [91, 11], [92, 11], [93, 11], [94, 11], [95, 11], [96, 11], [110, 11], [7, 10], [8, 10],
         [9, 10], [10, 10], [11, 10], [12, 10], [25, 10], [113, 10], [114, 10], [115, 10], [117, 10], [120, 10],
         [121, 10],
         [122, 10], [123, 10], [124, 10], [126, 9], [4, 8], [5, 8], [6, 8], [65, 8], [66, 8], [67, 8], [68, 8], [69, 8],
         [70, 8], [107, 8], [108, 8], [109, 8], [63, 7], [64, 7], [34, 6], [50, 6], [41, 5], [71, 5], [116, 5],
         [131, 5],
         [132, 5], [133, 5], [127, 4], [128, 4], [129, 4], [130, 4], [62, 3], [104, 3], [105, 3], [106, 3], [13, 2],
         [14, 2],
         [15, 2], [72, 1], [73, 1], [53, 1], [54, 1], [55, 1], [56, 1], [57, 1], [58, 1], [59, 1], [60, 1], [61, 1],
         [134, 1],
         [135, 1], [136, 1], [137, 1], [138, 1], [139, 1]]

width = 0.5  # gives histogram aspect to the bar diagram

import matplotlib.pyplot as plt

import numpy as np


def plot_epitope_spread(epitopes_per_index_before, epitopes_per_index_after):
    """
    plots the epitope spread as a barplot with an additional lineplot
    :param epitopes_per_index_before: expected to be sorted by epitope count!
    :param epitopes_per_index_after: expected to be sorted by epitope count!
    """
    highest_epitope_count = max(epitopes_per_index_before[0][1], epitopes_per_index_after[0][1])

    # fill any missing values for both sets
    epitopes_per_index_before = fill_missing_val_epitope_pred(epitopes_per_index_before)
    epitopes_per_index_after = fill_missing_val_epitope_pred(epitopes_per_index_after)

    # sort both sets according to the index
    sorted_epitopes_before_np = sort_epitope_pred_per_index(epitopes_per_index_before)
    sorted_epitopes_after_np = sort_epitope_pred_per_index(epitopes_per_index_after)

    # extract X and y data points
    X_before, y_before = sorted_epitopes_before_np[:, :-1], sorted_epitopes_before_np[:, -1]
    X_after, y_after = sorted_epitopes_after_np[:, :-1], sorted_epitopes_after_np[:, -1]

    # create plots for both sets
    plt = create_epitope_pred_plot(X_before, y_before, 1, highest_epitope_count)
    plt = create_epitope_pred_plot(X_after, y_after, 2, highest_epitope_count)

    plt.show()  # shows both plots in separate windows


def keep_only_nth_label(ax):
    # Keeps every nth label
    n = 10
    [l.set_visible(False) for (i, l) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]


def sort_epitope_pred_per_index(epitopes_per_index):
    epitopes_per_index_before_np = np.array(epitopes_per_index)
    sorted_epitopes_per_index = sorted(epitopes_per_index_before_np, key=lambda x: x[0])
    sorted_epitopes_np = np.array(sorted_epitopes_per_index)
    return sorted_epitopes_np


def fill_missing_val_epitope_pred(epitopes_per_index):
    sorted_epitope_per_index = sorted(epitopes_per_index, key=itemgetter(0))  # sort per index

    # fill in missing values
    i = 1
    prev_val = 1
    for val in sorted_epitope_per_index:
        if val[0] != i:
            for j in range(val[0] - prev_val):
                epitopes_per_index.append([j + prev_val, 0])
        i = val[0] + 1
        prev_val = val[0]

    return epitopes_per_index


def create_epitope_pred_plot(X, y, plot_number, highest_epitope_count):
    # plot before
    pos = np.arange(len(y))

    ax = plt.axes()
    ax.set_xticks(pos)
    ax.set_xticklabels(X, fontsize=6)

    keep_only_nth_label(ax)

    plt.figure(plot_number)
    plt.plot(pos, y, color='b')
    plt.bar(pos, y, width, color='r')
    plt.ylim(top=highest_epitope_count + 2)

    return plt


plot_epitope_spread(before, after)
