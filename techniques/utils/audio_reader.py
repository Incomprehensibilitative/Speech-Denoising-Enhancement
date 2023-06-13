"""
Audio Reader
===

Function: 
`audio_converter`
---
    1. Read the audio file
    2. Calculate frequency (Hz) of audio (sample rate/second)
    3. Calculate the number of samples
    4. Calculate the length of audio in second (time (s))
    5. If stereo: Convert into mono channel andwrite it back to the file
    6. Get the floating ndarray of the audio

Return:
---
Tupple `[signal_array, frequency, no_of_samples, length]`

Required Module:
---
- `wave`
- `audio_utility`
- `numpy`
"""
import wave
import numpy as np
def audio_read(path):
    """
    Audio Read
    ===
    - Input: file's path
    - Output: Tupple form: `[signal_array, frequency, no_of_samples, length]`
        - [0]: signal_array (integer/float ndarray)
        - [1]: frequency
        - [2]: number of sample
        - [3]: length
    """
    file = wave.open(path, 'rb')

    # caculating the number of samples of the sound are taken per second  
    sample_freq = file.getframerate()
    # print("Sample Frequency: (Hz) ", sample_freq)

    # number of individual frames (samples)
    n_samples = file.getnframes()
    # print("Number of Samples: ", n_samples)

    # length of audio in seconds
    t_audio = n_samples/sample_freq
    # print("Length of Audio (second): ", t_audio)

    # number of channels
    n_channels = file.getnchannels()
    # if (n_channels == 2):
    #     mono_converter(path)
    # print("Number of Channels: ", n_channels)

    # amplitude of the wave at the point in time
    signal_wave = file.readframes(n_samples)
    # return type = byte (check by using type())
    # print(type(signal_wave))

    # get signal values (list of audio-frames) -> turn into integer ndarray (numpy array)

    signal_array = np.frombuffer(signal_wave, dtype=np.int16)

    # Uncomment this line to get the floating ndarray of the audio
    # signal_array = signal_array.astype(np.float32) / 32768.0

    # print("Signal Array: ", signal_array)

    # return signal in time domain
    return signal_array, sample_freq, n_samples, t_audio