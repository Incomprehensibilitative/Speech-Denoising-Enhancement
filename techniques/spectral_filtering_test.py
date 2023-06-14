import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from spectral_filtering.spectral_filtering import spectral_filtering


def spectral_filtering(channel_1, channel_2):
    # Compute the FFT of signal
    fhat = np.fft.fft(channel_2)

    # Power spectrum
    psd = fhat * np.conj(fhat) / channel_1

    # Create x-axis of freq
    freq = (1 / (0.01 * channel_1)) * (channel_1)

    # Find the large power freq (Make spectral vector = PSD > const)
    # to check element and if <100 element equals to 0. Otherwise equals to 1
    indices = psd > 100

    # Zero down small fourier coeffs
    psd_clean = psd * indices
    fhat = indices * fhat

    # Inverse FFT for filtered time signal
    spectral_filtering = np.fft.ifft(fhat)

    return spectral_filtering

# Load the WAV file
sample_rate1, data1 = wav.read(r'..\audio_files\airport.wav')
dis1 = r'..\audio_files\airport.wav'

sample_rate2, data2 = wav.read(r'..\audio_files\cafe.wav')
dis2 = r'..\audio_files\cafe.wav'

sample_rate3, data3 = wav.read(r'..\audio_files\rainstorm.wav')
dis3 = r'..\audio_files\rainstorm.wav'

# Extract the channels
channel1_1 = data1[:, 0]
channel1_2 = data1[:, 1]

channel2_1 = data2[:, 0]
channel2_2 = data2[:, 1]

channel3_1 = data3[:, 0]
channel3_2 = data3[:, 1]

# Find filtered by spectral filtering def
filtered_channel1_2 = spectral_filtering(channel1_1, channel1_2)

filtered_channel2_2 = spectral_filtering(channel2_1, channel2_2)

filtered_channel3_2 = spectral_filtering(channel3_1, channel3_2)

# Save the filtered data to a new WAV file
path1 = r'..\filtered_audio_files/' + 'sf_airport.wav'
wav.write(path1, sample_rate1, filtered_channel1_2.astype(np.int16))

path2 = r'..\filtered_audio_files/' + 'sf_cafe.wav'
wav.write(path2, sample_rate1, filtered_channel2_2.astype(np.int16))

path3 = r'..\filtered_audio_files/' + 'sf_rainstorm.wav'
wav.write(path3, sample_rate1, filtered_channel3_2.astype(np.int16))

# Create a time array for plotting
time = np.arange(len(channel1_2)) / sample_rate1


def plot(channel, filtered_channel, a):
    # Create figure for plotting
    plt.figure(num=a, figsize=(15, 10))

    # Plot the original signal
    plt.subplot(3, 1, 1)
    plt.plot(channel)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Original')

    # Plot the filtered signal
    plt.subplot(3, 1, 2)
    plt.plot(filtered_channel)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Filtered')

    # Plot both original and filtered signal
    plt.subplot(3, 1, 3)
    plt.plot(channel, label='Original')
    plt.plot(filtered_channel, label='Filtered')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Original and Filtered')
    plt.legend()

    # Show plot
    plt.show()
    # Close figure
    plt.close()


# Plotting all
plot(channel1_2, filtered_channel1_2, 'Airport')
plot(channel2_2, filtered_channel2_2, 'Cafe')
plot(channel3_2, filtered_channel3_2, 'Rainstorm')