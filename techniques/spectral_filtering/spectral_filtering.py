import numpy as np

def spectral_filtering(channel_1, channel_2):
    # Compute the FFT of signal
    fhat = np.fft.fft(channel_2)

    # Power spectrum
    PSD = fhat * np.conj(fhat) / channel_1

    # Create x-axis of freq
    freq = (1 / (0.01 * channel_1)) * (channel_1)

    # Find the large power freq (Make spectral vector = PSD > const)
    # to check element and if <100 element equals to 0. Otherwise equals to 1
    indices = PSD > 100

    # Zero down small fourier coeffs
    PSDclean = PSD * indices
    fhat = indices * fhat

    # Inverse FFT for filtered time signal
    spectral_filtering = np.fft.ifft(fhat)

    return spectral_filtering
