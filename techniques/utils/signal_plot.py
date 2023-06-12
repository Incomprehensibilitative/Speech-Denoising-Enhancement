"""
Signal Plot
===
- Plot the signal in 3 forms
## Function:
`signal_plot`
## Required Module:
- `audio_reader`
- `scipy`
- `numpy`
"""

from audio_reader import audio_read
import numpy as np
from scipy.fft import fft

def signal_plot(path):
    """
    Signal Plot
    ===
    - Input: file's path
    - Plot the signal of the input file in these form:
        - Amplitide - Time
        - Spectrum - Time
        - Frequency - Time
    """

    # ===== Opening a WAV File =====    
    signal = audio_read(path)
    # signal_array must be integer ndarray

    # caculating the time at which each sample is taken
    times = np.linspace(0, signal[3], num=signal[2])

    # ===== Plotting the Signal Amplitude
    import matplotlib.pyplot as plt

    plt.figure(figsize=(15,5))
    plt.plot(times ,signal[0])
    plt.title("Amplitude - Time")
    plt.ylabel('Signal Value')
    plt.xlabel('Time (s)')
    plt.xlim(0, signal[3])
    plt.show()

    # ===== Plotting the Frequency Spectrum =====
    plt.figure(figsize=(15, 5))
    plt.specgram(signal[0], Fs=signal[1], vmin=-20, vmax=50)
    plt.title('Spectrum - Time')
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.xlim(0, signal[3])
    plt.colorbar()
    plt.show()

    # ===== Plotting the Frequency =====
    plt.figure(figsize=(15,5))
    signal_time = np.sin(signal[0])
    signal_freq = np.fft.fft(signal_time)
    plt.plot(times,signal_freq)
    plt.title('Frequency - Time')
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.xlim(0, signal[3])
    plt.show()