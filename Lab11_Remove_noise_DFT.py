import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate a pure sine wave (440 Hz)
fs = 1000  # Sampling frequency in Hz
t = np.linspace(0, 1, fs, endpoint=False)  # 1-second time vector
f = 440  # Frequency of the sine wave (Hz)
pure_signal = np.sin(2 * np.pi * f * t)  # Generate sine wave

# Step 2: Add random noise
noise = np.random.randn(len(pure_signal)) * 0.5  # Gaussian noise
noisy_signal = pure_signal + noise  # Add noise to signal

# Step 3: Apply DFT (Discrete Fourier Transform)
dft_signal = np.fft.fft(noisy_signal)  # Compute DFT
freqs = np.fft.fftfreq(len(noisy_signal), 1/fs)  # Frequency axis

# Step 4: Remove high-frequency noise (simple low-pass filter)
cutoff = 500  # Frequency threshold (keep low frequencies)
dft_signal[np.abs(freqs) > cutoff] = 0  # Set high frequencies to zero

# Step 5: Apply Inverse DFT to recover cleaned signal
cleaned_signal = np.fft.ifft(dft_signal).real  # Take only real part

# Plot Results
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, pure_signal, label="Pure Signal (440 Hz)")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, noisy_signal, label="Noisy Signal", color='r')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, cleaned_signal, label="Cleaned Signal (Filtered)", color='g')
plt.legend()

plt.xlabel("Time (s)")
plt.show()
