import numpy as np
import matplotlib.pyplot as plt

def DFT(x):
    """Compute the Discrete Fourier Transform (DFT) of a 1D signal."""
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

def IDFT(X):
    """Compute the Inverse Discrete Fourier Transform (IDFT) of a 1D signal."""
    N = len(X)
    x = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
    return x / N  # Normalize

# Create sample signal (two sine waves)
Fs = 1000  # Sampling rate
T = 1 / Fs  # Sampling interval
t = np.linspace(0, 1, Fs, endpoint=False)  # 1 second duration
f1, f2 = 50, 120
signal = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Compute DFT
dft_output = DFT(signal)
freqs = np.fft.fftfreq(len(dft_output), T)  # Frequency bins

# Compute IDFT
reconstructed_signal = IDFT(dft_output)

# Print frequency bins
print("Frequency Bins:")
print(freqs[:Fs//2])  # Single-sided frequencies

# Plot signals
plt.figure(figsize=(10, 6))

# Plot magnitude spectrum
plt.subplot(2,1,1)
plt.plot(freqs[:Fs//2], np.abs(dft_output[:Fs//2]))  # Single-sided spectrum
plt.title("DFT Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()


plt.subplot(2,1,2)
plt.plot(t, signal, label="Original Signal", linestyle="dashed")
plt.plot(t, reconstructed_signal.real, label="Reconstructed Signal", alpha=0.7)
plt.title("Original vs Reconstructed Signal (IDFT)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()



plt.tight_layout()
plt.show()
