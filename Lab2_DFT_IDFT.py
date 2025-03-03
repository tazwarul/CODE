import numpy as np
import matplotlib.pyplot as plt

def DFT(x):
    """
    Compute the Discrete Fourier Transform (DFT) of a 1D signal.
    """
    N = len(x)
    X = np.zeros(N, dtype=complex)  # Output array (complex numbers)

    for k in range(N):  # Loop over frequency bins
        for n in range(N):  # Loop over time samples
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    
    return X
def IDFT(X):
    """
    Compute the Inverse Discrete Fourier Transform (IDFT) of a 1D signal.
    """
    N = len(X)
    x = np.zeros(N, dtype=complex)  # Output array (complex numbers)

    for n in range(N):  # Loop over time samples
        for k in range(N):  # Loop over frequency bins
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
    
    return x / N  # Normalize by N


# Create a sample signal (two sine waves)
Fs = 1000  # Sampling rate
T = 1 / Fs  # Sampling interval
t = np.linspace(0, 1, Fs, endpoint=False)  # 1 second duration

# Signal: Combination of 50 Hz and 120 Hz sine waves
f1, f2 = 50, 120
signal = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Compute DFT
dft_output = DFT(signal)

# Compute frequency bins
freqs = np.fft.fftfreq(len(dft_output), T)

# Compute IDFT to reconstruct the original signal
reconstructed_signal = IDFT(dft_output)

plt.figure(figsize=(10, 5))

# Verify: Plot the original and reconstructed signals
plt.subplot(2,1,2)
plt.plot(t, signal, label="Original Signal", linestyle="dashed")
plt.plot(t, reconstructed_signal.real, label="Reconstructed Signal", alpha=0.7)
plt.title("Original vs Reconstructed Signal (IDFT)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")


# Plot magnitude spectrum (single-sided)
plt.subplot(2,1,1)
plt.plot(freqs[:Fs//2], np.abs(dft_output[:Fs//2]))  # Single-sided spectrum
plt.title("DFT Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")


plt.tight_layout()
plt.show()
