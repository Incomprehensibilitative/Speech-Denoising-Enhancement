from utils.audio_reader import audio_read
from utils.audio_utility import add_noise, audio_write, mono_converter
from spectral_subtraction.spectral_subtraction import spectral_subtraction

if __name__ == "__main__":
    # ===== Files' Path =====

    # path to the audio file
    audio = "../audio_files/audio/piano.wav"
    mono_audio = "../audio_files/audio/mono_audio.wav"

    # ----- Airport noise -----
    # path to the noise file
    noise1 = "../audio_files/noise/noise_airport.wav"
    mono_noise1 = "../audio_files/noise/mono_noise_airport.wav"

    # path to the noise added file
    noisy_audio1 = "../audio_files/noisy_audio/noisy_airport.wav"

    # path to the denoised file
    denoised1 = "../filtered_audio_files/ssm_airport.wav"

    # ----- Rainstorm noise -----
    # path to the noise file
    noise2 = "../audio_files/noise/noise_rainstorm.wav"
    mono_noise2 = "../audio_files/noise/mono_noise_rainstorm.wav"

    # path to the noise added file
    noisy_audio2 = "../audio_files/noisy_audio/noisy_rainstorm.wav"

    # path to the denoised file
    denoised2 = "../filtered_audio_files/ssm_rainstorm.wav"

    # ----- Restaurant noise -----
    # path to the noise file
    noise3 = "../audio_files/noise/noise_restaurant.wav"
    mono_noise3 = "../audio_files/noise/mono_noise_restaurant.wav"

    # path to the noise added file
    noisy_audio3 = "../audio_files/noisy_audio/noisy_restaurant.wav"

    # path to the denoised file
    denoised3 = "../filtered_audio_files/ssm_restaurant.wav"

    # ===== Main =====

    # convert audio and noise to mono
    mono_converter(audio, mono_audio) # audio
    mono_converter(noise1, mono_noise1) # noise1
    mono_converter(noise2, mono_noise2) # noise2
    mono_converter(noise3, mono_noise3) # noise3

    # add noise to the audio file -> output: noisy_audio
    add_noise(mono_audio, mono_noise1, noisy_audio1, 2)
    add_noise(mono_audio, mono_noise2, noisy_audio2, 2)
    add_noise(mono_audio, mono_noise3, noisy_audio3, 2)

    # read the noisy audio file
    noisy_array1, noisy_freq1, _, _ = audio_read(noisy_audio1)
    noisy_array2, noisy_freq2, _, _ = audio_read(noisy_audio2)
    noisy_array3, noisy_freq3, _, _ = audio_read(noisy_audio3)

    # read the noise file
    noise_array1 = audio_read(mono_noise1)[0]
    noise_array2 = audio_read(mono_noise2)[0]
    noise_array3 = audio_read(mono_noise3)[0]

    # apply spectral subtraction to the noisy audio file -> output: denoised signal_array
    denoised_array1 = spectral_subtraction(noisy_array1, noise_array1, noisy_freq1, 2)
    denoised_array2 = spectral_subtraction(noisy_array2, noise_array2, noisy_freq2, 2)
    denoised_array3 = spectral_subtraction(noisy_array3, noise_array3, noisy_freq3, 2)

    # write the denoised audio file -> output: denoised
    audio_write(denoised1, denoised_array1, noisy_freq1)
    audio_write(denoised2, denoised_array2, noisy_freq2)
    audio_write(denoised3, denoised_array3, noisy_freq3)