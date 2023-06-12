import matplotlib.pyplot as plt
import numpy as np

def plot_compare_in_time_domain(fig_name, d1, d2):
    """
    Plot the time domain signal before and after the apply the filters
    - fig_name: figure name
    - d1, d2: data before and after the apply the filters
    - example: compare_plot('Fig.12: Spectral Restoration - Audio 1 ', original_data, filtered_data)
    """
    plt.figure(fig_name)
    plt.plot(d1)
    plt.plot(d2)
    plt.tight_layout()
    plt.show()

def plot_compare_in_freq_domain(fig_name, d1, d2, ns):
    """
    Plot the frequency domain signal before and after the apply the filters
    - fig_name: figure name
    - d1, d2: data before and after the apply the filters
    - ns: number of samples
    - example: compare_plot('Fig.12: Spectral Restoration - Audio 1 ', original_data, filtered_data, 1024)
    """
    plt.figure(fig_name)
    plt.plot(np.fft.fft(d1)[0:ns], color='C0')
    plt.plot(np.fft.fft(d2)[0:ns], color='C1')
    plt.tight_layout()
    plt.show()

