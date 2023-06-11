import numpy as np

def spectral_subtraction(audio_signal, noise_signal,frames, alpha):

    # audio_signal = audio_signal.astype(np.float32) / 32768.0
    # noise_signal = noise_signal.astype(np.float32) / 32768.0

    # initialize the filtered_signal
    filtered_signal = np.zeros_like(audio_signal)

    # Frame the signal (Devide the nosie into short overlapping frames)
    # Typical frame sizes range from 20-40 ms with 50% overlap
    frame_size = int(frames * 0.02) # 20ms frame size
    ovlp_size = int(frames * 0.01) # 10ms opverlapping size (50% of origin frame)

    # Perfroming Fast Fourier Transform to each frame to convert from time domain to freqeuncy domain
    for i in range(0, len(audio_signal) - frame_size, ovlp_size):
        frame = audio_signal[i:i+frame_size]
        frame_spectrum = np.fft.fft(frame)
        noise_spectrum = np.fft.fft(noise_signal[i:i+frame_size])

        # Estimate the noise spectrum from each frame
        noise_magnitude = np.abs(noise_spectrum)
        noise_power = noise_magnitude ** 2

        # Gain function (type: )
        gain = np.maximum(1 - alpha * (noise_power / (np.abs(frame_spectrum) ** 2 )), 0)

        # Apply gain funciton to frame spectrum
        filtered_spectrum = frame_spectrum * gain

        # Perform inverse Fast Fourier Transform to convert back to time domain
        filtered_frame = np.fft.ifft(filtered_spectrum).real
        
        # apply to each frame
        filtered_signal[i:i+frame_size] += filtered_frame

    return filtered_signal # return filtered signal in time domain