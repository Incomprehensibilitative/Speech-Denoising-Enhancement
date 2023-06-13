from utils.signal_plot import signal_plot

if __name__ == "__main__":
    # Plot the noisy audio at airport
    signal_plot("../audio_files/noisy_audio/noisy_airport.wav", "Airport Noise")

    # Plot the denoised audio at airport
    signal_plot("../filtered_audio_files/ssm_airport.wav", "Airport Noise")

    # Plot the noisy audio at rainstorm
    signal_plot("../audio_files/noisy_audio/noisy_rainstorm.wav", "Rainstorm Noise")

    # Plot the denoised audio at rainstorm
    signal_plot("../filtered_audio_files/ssm_rainstorm.wav", "Rainstorm Noise")

    # Plot the noisy audio at restaurant
    signal_plot("../audio_files/noisy_audio/noisy_restaurant.wav", "Restaurant Noise")

    # Plot the denoised audio at restaurant
    signal_plot("../filtered_audio_files/ssm_restaurant.wav", "Restaurant Noise")