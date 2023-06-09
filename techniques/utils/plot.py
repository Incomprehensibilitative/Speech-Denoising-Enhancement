import matplotlib.pyplot as pyplot
import numpy as np

def plot_in_time_domain(fig_name, title, data):
    """
    Plot the data in time domain
    - fig_name: figure name
    - title: title of the figure
    - data: data to be plotted
    """
    pyplot.figure(fig_name)
    pyplot.title(title)
    pyplot.plot(data)
    pyplot.show()

def plot_in_frequency_domain(fig_name, title, data):
    """
    Plot the data in frequency domain
    - fig_name: figure name
    - title: title of the figure
    - data: data to be plotted
    """
    pyplot.figure(fig_name)
    pyplot.title(title)
    pyplot.plot(np.fft.fft(data))
    pyplot.show()
