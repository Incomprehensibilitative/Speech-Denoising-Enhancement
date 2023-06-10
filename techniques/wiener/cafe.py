import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from techniques.wiener.wiener_filtering import wiener_filter

# Load the WAV file
sample_rate, data = wavfile.read('../../audio_files/cafe.wav')

# Extract the channels
channel_1 = data[:, 0]
channel_2 = data[:, 1]

# Apply the Wiener filter to the input signal
filtered_channel_2 = np.fft.ifft(wiener_filter(channel_1, channel_2) * np.fft.fft(channel_2)).real

# Combine the filtered channel with the reference channel
filtered_data = np.column_stack((channel_1, filtered_channel_2))

# Save the filtered data to a new WAV file
path = '../../filtered_audio_files/' + 'wf_cafe.wav'
wavfile.write(path, sample_rate, filtered_data.astype(np.int16))


# Plot the original and filtered signals

# Create a time array for plotting
time = np.arange(len(channel_2)) / sample_rate

# Create a figure and axes
fig, ax = plt.subplots(figsize=(8, 4))

# Plot the original signal
ax.plot(time, channel_2, label='Original')

# Plot the filtered signal
ax.plot(time, filtered_channel_2, label='Filtered')

# Add a title and axis labels
ax.set_title('Original vs Filtered Signal')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')

# Add a legend
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()
