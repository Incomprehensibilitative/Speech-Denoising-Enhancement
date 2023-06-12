"""
# Audio Utility
    - Some utilities used for managing the audio files
## Functions included:
### 1. `mono_converter`:
    - Get audio file and convert from stereo to mono.
    - Reqired system's module: `scipy`.
### 2. `audio_write`:
    - Get the input signal array and write to new file.
    - Required system's module: `soundfile`.
"""
from scipy.io import wavfile
import soundfile as sf

def mono_converter(path):
    """
    Mono Converter
    ===
    Function:
    ---
    - Read the input audio file and convert from stereo to mono audio.

    Required Module:
    - `scipy`
    """
    rate, date = wavfile.read(path)
    data_mono = date[:,0]
    wavfile.write(path, rate, data_mono)

def audio_write(path, signal_array, frames):
    """
    Audio Write
    ===
    Function:
    ---
    - Write the input signal to new file.

    Required Module:
    ---
    - `soundfile`
    """
    sf.write(path, signal_array, frames)