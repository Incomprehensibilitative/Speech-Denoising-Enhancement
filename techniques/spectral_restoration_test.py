import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from spectral_restoration.spectral_restoration import spectral_restoration

# Load the WAV file
sample_rate, data = wav.read(r'...\audio_files\airport.wav or cafe.wav or rainstorm.wav')
dis = r'...\airport.wav or cafe.wav or rainstorm.wav'

# Extract the channels
channel_1 = data[:, 0]
channel_2 = data[:, 1]

# Find filtered by spectral restoration def
filtered_channel_2 = spectral_restoration(channel_1, channel_2)

# Save the filtered data to a new WAV file
path = r'...\filtered_audio_files/' + 'sr_airport.wav or sr_cafe.wav or sr_rainstorm.wav'
wav.write(path, sample_rate, filtered_channel_2.astype(np.int16))

# Create a time array for plotting
time = np.arange(len(channel_2)) / sample_rate

# Create figure for plotting
plt.figure(figsize=(18, 15))

# Plot the original signal
plt.subplot(4, 1, 1)
plt.plot(channel_2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Original')

# Plot the filtered signal
plt.subplot(4, 1, 2)
plt.plot(filtered_channel_2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Filtered')

# Plot both original and filtered signal
plt.subplot(4, 1, 3)
plt.plot(channel_2, label = 'Original')
plt.plot(filtered_channel_2, label = 'Filtered')

plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Original and Filtered')

# Show plot
plt.show()
