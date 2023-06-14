# Members
GROUP 9
- BI12-076 Mai Hải Đăng (Leader)
- BI12-074 Đoàn Đình Đăng
- BI12-074 Trần Hải Đăng
- BI12-040 Trần Ngọc Ánh
- BI12-099 Nguyễn Thanh Đức

# Denoising Techniques
- All techniques are stored in the folder "techniques"
- All original audio files are stored in "audio_files"
- All clean audio files are stored in "audio_files/audio"
- All noise files are stored in "audio_files/noise"
- All noisy files are stored in "audio_files/noisy_audio"
- All denoised files are stored in "filtered_audio_files"
- All plotting images are stored in "plotting_image"

## Spectral Subtraction
BI12-074 Đoàn Đình Đăng
TO DO:
- [x] Add noise to piano song
- [x] Use *Spectral Subtraction* for denoising
- [x] Return new filtered audio files after denoising
- [x] Plotting spectrum for comparison

### Denoising
Run "spectral_subtraction_method.py" will do these task:

1. Get **audio file** from "audio_files/audio/" and add 3 **noises** form 3 files in "audio_files/noise" then return the **noisy files** in folder "audio_files/noisy_audio".

2. Read the **noisy files** in "audio_files/noisy_audio/" and start denoising using "Spectral Subtraction" techniques -> Return **filtered signal_array**.

3. Write the **filtered signal_array** to new files and store in folder "filtered_audio_files" in this form "ssm_*file_name*.wav".

### Plotting
Run "spectral_subtraction_plot.py" will do these task:

1. Read the **noisy audio** in "audio_files/noisy_audio/" and **filtered audio**

2. Plot **noisy audio** with corresponding **filtered audio** in 3 forms:
    - Amplitude - Time
    - Frequency - Time
    - Spectrum - Time

