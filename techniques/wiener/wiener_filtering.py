import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt


def wiener_filter(channel_1, channel_2):
    # Compute the cross-power spectral density
    cpsd = np.abs(np.fft.fft(channel_1) * np.conj(np.fft.fft(channel_2)))

    # Compute the auto-power spectral density of the reference channel
    apsd_ref = np.abs(np.fft.fft(channel_1)) ** 2

    # Compute the Wiener filter
    wiener_filter = cpsd / (cpsd + apsd_ref)

    return wiener_filter


def apply_wiener_filter(input_file, output_file):
    # Load the WAV file
    sample_rate, data = wavfile.read(input_file)

    # Extract the channels
    channel_1 = data[:, 0]
    channel_2 = data[:, 1]

    # Apply the Wiener filter to the input signal
    filtered_channel_2 = np.fft.ifft(wiener_filter(channel_1, channel_2) * np.fft.fft(channel_2)).real

    # Combine the filtered channel with the reference channel
    filtered_data = np.column_stack((channel_1, filtered_channel_2))

    # Save the filtered data to the output WAV file
    wavfile.write(output_file, sample_rate, filtered_data.astype(np.int16))

    # Plot the original and filtered signals in the time domain
    time = np.arange(len(channel_2)) / sample_rate
    plt.plot(time, channel_2, label='Original')
    plt.plot(time, filtered_channel_2, label='Filtered')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Original vs Filtered Signal (Time Domain)')
    plt.legend()

    # Show the plot
    plt.show()

    # Clear the figure
    plt.clf()

    # Perform FFT on the signals
    fft_channel_2 = np.fft.fft(channel_2)
    fft_filtered_channel_2 = np.fft.fft(filtered_channel_2)

    # Plot the original and filtered signals in the frequency domain
    freq = np.fft.fftfreq(len(channel_2), d=1 / sample_rate)
    plt.plot(freq, np.abs(fft_channel_2), label='Original')
    plt.plot(freq, np.abs(fft_filtered_channel_2), label='Filtered')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Original vs Filtered Signal (Frequency Domain)')
    plt.legend()

    # Show the plot
    plt.show()



