from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

width = 0.5  # gives histogram aspect to the bar diagram


def plot_epitope_spread(epitopes_per_index_before, epitopes_per_index_after, protein_length):
    """
    plots the epitope spread as a barplot with an additional lineplot -> shows the plots
    :param epitopes_per_index_before: expected to be sorted by epitope count!
    :param epitopes_per_index_after: expected to be sorted by epitope count!
    """
    highest_epitope_count = max(epitopes_per_index_before[0][1], epitopes_per_index_after[0][1])

    # fill any missing values for both sets
    epitopes_per_index_before = fill_missing_val_epitope_pred(epitopes_per_index_before, protein_length)
    epitopes_per_index_after = fill_missing_val_epitope_pred(epitopes_per_index_after, protein_length)

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
    """
    hides all labels except the nth
    :param ax:
    :return:
    """
    n = 10
    [l.set_visible(False) for (i, l) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]


def sort_epitope_pred_per_index(epitopes_per_index):
    """
    sorts epitopes per index lists per index
    :param epitopes_per_index:
    :return:
    """
    epitopes_per_index_before_np = np.array(epitopes_per_index)
    sorted_epitopes_per_index = sorted(epitopes_per_index_before_np, key=lambda x: x[0])
    sorted_epitopes_np = np.array(sorted_epitopes_per_index)
    return sorted_epitopes_np


def fill_missing_val_epitope_pred(epitopes_per_index, protein_length):
    """
    any missing values are added with an epitope count of 0
    :param epitopes_per_index:
    :param protein_length:
    :return:
    """
    sorted_epitope_per_index = sorted(epitopes_per_index, key=itemgetter(0))  # sort per index

    # fill in missing values from index 1 to the currently already included amino acids
    i = 1
    prev_val = 1
    for val in sorted_epitope_per_index:
        if val[0] != i:
            for j in range(val[0] - prev_val):
                epitopes_per_index.append([j + prev_val, 0])
        i = val[0] + 1
        prev_val = val[0] + 1

    # add any additionally missing values from the end to the protein length
    if epitopes_per_index[len(epitopes_per_index) - 1][0] < protein_length:
        for index in range(protein_length - len(epitopes_per_index)):
            epitopes_per_index.append([index + protein_length, 0])

    return epitopes_per_index


def create_epitope_pred_plot(X, y, plot_number, highest_epitope_count):
    """
    creates a barplot including a lineplot
    :param X:
    :param y:
    :param plot_number:
    :param highest_epitope_count:
    :return:
    """
    pos = np.arange(len(y))

    ax = plt.axes()
    ax.set_xticks(pos)
    ax.set_xticklabels(X, fontsize=6)

    keep_only_nth_label(ax)

    plt.figure(plot_number)
    plt.xlabel("Amino Acid")
    plt.ylabel("Epitope Count")
    plt.plot(pos, y, color='r')
    plt.bar(pos, y, width, color='r')
    plt.ylim(top=highest_epitope_count + 2)

    return plt

# plot_epitope_spread(before, after, 140)
