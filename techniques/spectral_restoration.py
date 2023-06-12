import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from IPython.display import Audio
from scipy.io import wavfile

# Load the WAV file
sample_rate, data = wav.read(r'...\audio_files\airport.wav or cafe.wav or rainstorm.wav')
dis = r'...\audio_files\airport.wav or cafe.wav or rainstorm.wav'

# Extract the channels
channel_1 = data[:, 0]
channel_2 = data[:, 1]


def spectral_restoration(channel_1, channel_2):
    # Compute the cross-power spectral density
    cpsd = np.abs(np.fft.fft(channel_1) * np.conj(np.fft.fft(channel_2)))

    # Compute the auto-power spectral density of the reference channel
    apsd_ref = np.abs(np.fft.fft(channel_1)) ** 2

    # Compute the Spectral Restoration
    spectral_restoration = cpsd / (2 * (cpsd + apsd_ref))

    return spectral_restoration


# Apply the Spectral Restoration to the input signal
filtered_channel_2 = np.fft.ifft(spectral_restoration(channel_1, channel_2) * np.fft.fft(channel_2)).real

# Save the filtered data to a new WAV file
path = r'...\filtered_audio_files/' + 'sr.airport.wav or sr.cafe.wav or sr.rainstorm.wav'
wavfile.write(path, sample_rate, filtered_channel_2.astype(np.int16))

# Display original and filtered audio
display(Audio(dis, autoplay=False))

display(Audio(path, autoplay=False))

# Create a time array for plotting
time = np.arange(len(channel_2)) / sample_rate

# Create figure for plotting
plt.figure(figsize=(18, 15))

# Plot the original signal
plt.subplot(3, 1, 1)
plt.plot(channel_2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Original')

# Plot the filtered signal
plt.subplot(3, 1, 2)
plt.plot(filtered_channel_2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Filtered')

# Plot both original and filtered signal
plt.subplot(3, 1, 3)
plt.plot(channel_2, label='Original')
plt.plot(filtered_channel_2, label='Filtered')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Original and Filtered')

plt.legend()

# Show plot
plt.show()