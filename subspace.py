import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load the noisy speech signal
noisy_audio, sr = librosa.load('cafe.wav', sr=None)
#noise, sr = librosa.load('noise.wav', sr=None)

# Define frame duration and hop length
frame_duration = 0.025  # 25 milliseconds
hop_length = int(frame_duration * sr)

# Convert the noisy speech signal into frames
frames = librosa.util.frame(noisy_audio, frame_length=hop_length, hop_length=hop_length).T

# Apply window function to each frame
window = np.hamming(hop_length)
frames_windowed = frames * window

# Select a specific segment of the noise signal
noise_start = 0  # Starting index of the noise segment
noise_end = 48000  # Ending index of the noise segment
noise_segment = noisy_audio[noise_start:noise_end]

# Convert the noise segment into frames
noise_frames = librosa.util.frame(noise_segment, frame_length=hop_length, hop_length=hop_length).T

# Apply window function to each noise frame
noise_frames_windowed = noise_frames * window

# Compute the covariance matrix of the noise signal frames
noise_cov_matrix = np.cov(noise_frames_windowed.T)
eigenvalues, eigenvectors = np.linalg.eig(noise_cov_matrix)

# Perform PCA on the covariance matrix to obtain the eigenvectors and eigenvalues
pca = PCA()
pca.fit(noise_cov_matrix)

sorted_eigenvalues = np.sort(eigenvalues)[::-1]  # Sort eigenvalues in descending order

# Calculate the cumulative sum of eigenvalues
cumulative_sum = np.cumsum(sorted_eigenvalues)

# Calculate the ratio of each eigenvalue with the total sum of eigenvalues
eigenvalue_ratio = sorted_eigenvalues / cumulative_sum[-1]

# Find the index where the ratio exceeds a threshold (e.g., 0.95)
threshold_index = np.argmax(eigenvalue_ratio >= 0.95)

# Estimate the eigenvalue threshold as the eigenvalue at the threshold index
eigenvalue_threshold = sorted_eigenvalues[threshold_index]

# Retrieve the eigenvectors corresponding to the noise subspace
noise_subspace = eigenvectors[:, eigenvalues < eigenvalue_threshold]

# Project the noisy speech signal onto the noise subspace
projected_signal = np.dot(frames_windowed, noise_subspace)

# Reconstruct the denoised speech signal by projecting it back to the original feature space
denoised_audio = np.dot(projected_signal, noise_subspace.T) / window

# Concatenate the denoised speech frames
denoised_signal = np.concatenate(denoised_audio, axis=0)
#sf.write('denoised_speech.wav', denoised_signal, sr)

time = np.arange(len(noisy_audio)) / sr

# Plot the denoised signal and the noisy audio in time domain
plt.figure(figsize=(10, 4))
plt.plot(noisy_audio, label='Noisy Audio')
plt.plot(denoised_signal, label='Denoised Signal')
plt.title('Comparison of Noisy Audio and Denoised Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

