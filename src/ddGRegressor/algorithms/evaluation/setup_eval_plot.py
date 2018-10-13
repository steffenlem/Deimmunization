import logging
import numpy as np
import matplotlib.pyplot as plt

from src.ddGRegressor.io.writer.plot_file_writer import write_plot_as_png

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Draw plots and compute PPC")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def setup_evaluation_plot(prediction, ddG_test, classifier_tool, inputfilepath):
    title = inputfilepath.split('/')[len(inputfilepath.split('/')) - 1].replace('.csv', '').replace('.txt', '') + '_' + classifier_tool
    differences = [abs(ddG_test.values.tolist()[i] - prediction[i]) for i in range(len(prediction))]

    LOG.info("Start drawing plots")
    # figure 1: difference_figure
    plot_difference_figure(differences, title)

    # figure 2: pred_and_test_plot_figure
    plot_pred_and_test_plot_figure(prediction, ddG_test, title)

    # figure 3: pred_and_test_point_figure
    plot_pred_and_test_point_figure(prediction, ddG_test, title)
    LOG.info("Finished drawing plots")
    LOG.info("Compute PPC")
    ppc = ((prediction * ddG_test).mean() - (prediction.mean() * ddG_test.mean()))/(prediction.std() * ddG_test.std())
    LOG.info("Finished computing PPC")
    LOG.info(" PPC = "+str(ppc))


def plot_difference_figure(differences, title):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 1, 1)
    plt.plot(differences, '-b', label='difference (mean=' + str(round(np.array(differences).mean(), 2)) + ')')
    plt.legend(loc='upper right')
    plt.ylabel('ddG')
    write_plot_as_png(plt, title + '01.png')


def plot_pred_and_test_plot_figure(pred_val, test_val, title):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 1, 1)
    plt.plot(pred_val, '-b', label='pred_value')
    plt.plot(test_val.values.tolist(), '-r', label='test_value')
    plt.legend(loc='upper right')
    plt.ylabel('ddG')
    write_plot_as_png(plt, title + '02.png')


def plot_pred_and_test_point_figure(pred_val, test_val, title):
    interval = [test_val.min(), test_val.max()]
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 1, 1)
    plt.plot(pred_val, test_val.values.tolist(), '.', label='')
    plt.plot(interval, interval, '--', label='id')
    plt.legend(loc='upper right')
    plt.xlabel('pred_val')
    plt.ylabel('test_val')
    write_plot_as_png(plt, title + '03.png')
