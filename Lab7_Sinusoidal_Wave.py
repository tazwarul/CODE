import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 500)
frequencies = [1, 5, 10]

plt.figure(figsize=(12, 6))
for f in frequencies:
    plt.plot(t, np.sin(2 * np.pi * f * t), label=f"{f} Hz")

plt.legend()
plt.title("Sinusoidal Waves")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()