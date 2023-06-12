"""
# Audio Utility
    - Some utilities used for managing the audio files
## Functions included:
### 1. `mono_converter`:
    - Get audio file and convert from stereo to mono
    - Reqired system's module: `scipy`, `soundfile`
### 2. `audio_write`:
    - Get audio file and write the data to input file
    - Required system's module: `soundfile`
    - Return new audio file
### 3. `add_noise`:
    - Get audio file and noise file, add noise to the audio file and write it back to new file
    - Required system's module: `scipy`, `numpy`
    - Return new audio file
"""
from scipy.io import wavfile
import soundfile as sf
import numpy as np

def mono_converter(path):
    """
    Mono Converter
    ===
    Function:
    ---
    - Read the input audio file and convert from stereo to mono audio

    Required Module:
    - `scipy`
    """
    rate, data = wavfile.read(path)
    data_mono = data[:,0]
    wavfile.write(path, rate, data_mono)

def audio_write(path, signal_array, frames):
    """
    Audio Write
    ===
    Function:
    ---
    - Write the input signal to input file

    Return:
    ---
    - New audio file

    Required Module:
    ---
    - `soundfile`
    """
    sf.write(path, signal_array, frames)

def add_noise(audio_path, noise_path, output_path, noise_ratio):
    """
    Add Noise
    ===
    Function:
    ---
    - Add noise to the audio file and write it back to new file

    Return:
    ---
    - New audio file

    Required Module:
    ---
    - `scipy`
    - `numpy`
    """
    
    # Read the audio file
    audio_rate, audio_array = wavfile.read(audio_path)
    noise_rate, noise_array = wavfile.read(noise_path)

    # Adjust length of the noise to match the audio
    if len(noise_array) > len(audio_array):
        noise_array = noise_array[0:len(audio_array)]
    else:
        noise_array = np.pad(noise_array, (0, len(audio_array) - len(noise_array)), 'constant')

    # Convert the audio and noise to float32
    audio_array = audio_array.astype(np.float32) / 32768.0
    noise_array = noise_array.astype(np.float32) / 32768.0

    # Normalize the amplitude of the audio and noise
    audio_array = audio_array / np.max(np.abs(audio_array))
    noise_array = noise_array / np.max(np.abs(noise_array))

    # Calculate the noise level based on the noise ratio
    noise_level = np.std(audio_array) / (np.std(noise_array) * noise_ratio)

    # Add noise to the audio
    output_array = audio_array + noise_array * noise_level

    # Write the noisy audio to new file
    sf.write(output_path, output_array, audio_rate)