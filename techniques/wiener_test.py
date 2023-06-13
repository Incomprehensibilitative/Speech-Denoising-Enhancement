from wiener.wiener_filtering import apply_wiener_filter
# List all WAV files in the folder
input_files = '../../audio_files/audio/airport.wav', '../../audio_files/audio/cafe.wav', '../../audio_files/audio' \
                                                                                         '/rainstorm.wav'
# Specify the output folder path
output_dir = '../../filtered_audio_files/'

# Process each input file
for input_file in input_files:
    # Extract the file name from the input_file path
    name_of_file = input_file.split('/')[-1]

    # Create the output file path with the desired prefix and directory
    output_file = f"{output_dir}wf_{name_of_file}"

    # Apply Wiener filter and save the filtered audio
    apply_wiener_filter(input_file, output_file)
