import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 500)
X_t = 0.25 + 2 * np.sin(2 * np.pi * t) + np.sin(2 * np.pi * 2 * t) + 1.5 * np.sin(2 * np.pi * 20 * t) + 0.5 * np.sin(2 * np.pi * 55 * t)

X_f = np.fft.fft(X_t)
frequencies = np.fft.fftfreq(len(t), t[1] - t[0])

plt.plot(frequencies, np.abs(X_f))
plt.title("Spectrum of X(t)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()