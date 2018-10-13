
def write_plot_as_png(plot, title):
    if title.endswith('01.png'):
        plot.savefig('data/plots/difference_figure/' + title)
    elif title.endswith('02.png'):
        plot.savefig('data/plots/pred_and_test_plot_figure/' + title)
    elif title.endswith('03.png'):
        plot.savefig('data/plots/pred_and_test_point_figure/' + title)
