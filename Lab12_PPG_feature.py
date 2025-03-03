import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Step 1: Generate a synthetic PPG signal
fs = 100  # Sampling frequency (Hz)
t = np.linspace(0, 10, 10 * fs)  # 10 seconds of signal
ppg_signal = np.sin(2 * np.pi * 1 * t) + 0.5 * np.sin(2 * np.pi * 2 * t) + 0.2 * np.random.normal(0, 1, len(t))

# Step 2: Detect systolic peaks
peaks, _ = find_peaks(ppg_signal, height=0.5, distance=fs//2)  # Adjust height and distance as needed

# Step 3: Detect diastolic points (troughs between peaks)
inverted_ppg = -ppg_signal
troughs, _ = find_peaks(inverted_ppg, distance=fs//2)

# Step 4: Calculate heart rate
peak_times = t[peaks]
heart_rate = 60 / np.mean(np.diff(peak_times))  # Beats per minute (BPM)

# Create subplots
plt.figure(figsize=(12, 8))

# Subplot 1: Original PPG signal
plt.subplot(3, 1, 1)
plt.plot(t, ppg_signal, label="PPG Signal", color="blue")
plt.title("Original PPG Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

# Subplot 2: PPG signal with systolic peaks
plt.subplot(3, 1, 2)
plt.plot(t, ppg_signal, label="PPG Signal", color="blue")
plt.plot(t[peaks], ppg_signal[peaks], "x", label="Systolic Peaks", color="red")
plt.title(f"PPG Signal with Systolic Peaks (Heart Rate: {heart_rate:.2f} BPM)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

# Subplot 3: PPG signal with diastolic points
plt.subplot(3, 1, 3)
plt.plot(t, ppg_signal, label="PPG Signal", color="blue")
plt.plot(t[troughs], ppg_signal[troughs], "o", label="Diastolic Points", color="green")
plt.title("PPG Signal with Diastolic Points")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

# Adjust layout and display
plt.tight_layout()
plt.show()

# Output the heart rate
print(f"Heart Rate: {heart_rate:.2f} BPM")