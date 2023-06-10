import numpy as np


def wiener_filter(channel_1, channel_2):
    # Compute the cross-power spectral density
    cpsd = np.abs(np.fft.fft(channel_1) * np.conj(np.fft.fft(channel_2)))

    # Compute the auto-power spectral density of the reference channel
    apsd_ref = np.abs(np.fft.fft(channel_1)) ** 2

    # Compute the Wiener filter
    wiener_filter = cpsd / (cpsd + apsd_ref)

    return wiener_filter
