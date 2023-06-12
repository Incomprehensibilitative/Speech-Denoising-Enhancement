from utils import audio_reader as ar
from utils import audio_utility as au
from utils import signal_plot as sp
from spectral_subtraction import spectral_subtraction as ss

if __name__ == "__main__":
    
    # path to the audio file
    audio = 

    # path to the noise file
    noise = 

    # path to the denoise file
    denoise =

    # read the audio file
    signal_array, freq, n_samples, length = ar.audio_read(audio)

    # read the noise file
    noise_array = ar.audio_read(noise)[0]

    # denoise the audio file
    filtered_signal = ss.spectral_subtraction(signal_array, noise_array, freq, 2)

    # create and write the denoise file
    au.audio_write(denoise, filtered_signal, freq)

    # plot the audio file
    sp.signal_plot(audio)

    # plot the noise file
    sp.signal_plot(denoise)