import numpy as np

def snr(original, filtered):
    """Compute the SNR between two signals.

    Args:
        original (np.ndarray): Original signal.
        filtered (np.ndarray): Filtered signal.

    Returns:
        float: SNR between the two signals.
    """
    noise = original - filtered
    # calculate SNR in dB
    original_snr = 10 * np.log10(np.mean(np.power(original, 2)) / np.mean(np.power(noise, 2)))
    filtered_snr = 10 * np.log10(np.mean(np.power(filtered, 2)) / np.mean(np.power(noise, 2)))

    # calculate the percentage difference in SNR
    snr_diff = np.abs(original_snr - filtered_snr / original_snr * 100)

    # output everything
    print("Original SNR: {:.2f} dB".format(original_snr))
    print("Filtered SNR: {:.2f} dB".format(filtered_snr))
    print("SNR difference: {:.2f}%".format(snr_diff))



