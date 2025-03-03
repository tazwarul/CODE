import numpy as np
import matplotlib.pyplot as plt

# Auto-Correlation Function
def auto_correlation(signal):
    correlation = np.correlate(signal, signal, mode='full')
    return correlation[correlation.size // 2:]  # Only non-negative lags

# Cross-Correlation Function
def cross_correlation(signal1, signal2):
    correlation = np.correlate(signal1, signal2, mode='full')
    return correlation[correlation.size // 2:]  # Only non-negative lags

# Example signals
t = np.linspace(0, 1, 500, endpoint=False)
signal1 = np.sin(2 * np.pi * 5 * t)  # A sine wave with 5 Hz frequency
signal2 = np.sin(2 * np.pi * 5 * t + np.pi / 4)  # A sine wave with a phase shift

# signal=signal1*signal2 #(add signal)

# Compute auto-correlation and cross-correlation
auto_corr_signal1 = auto_correlation(signal1)
cross_corr = cross_correlation(signal1, signal2) 

# Plotting the results
plt.figure(figsize=(12, 6))

# Auto-correlation plot
plt.subplot(1, 2, 1)
plt.plot(auto_corr_signal1)
plt.title('Auto-Correlation of Signal 1')
plt.xlabel('Lag')
plt.ylabel('Correlation')

# Cross-correlation plot
plt.subplot(1, 2, 2)
plt.plot(cross_corr)
plt.title('Cross-Correlation between Signal 1 and Signal 2')
plt.xlabel('Lag')
plt.ylabel('Correlation')

plt.tight_layout()
plt.show()







# import numpy as np
# import matplotlib.pyplot as plt

# def auto_correlation(signal):
#     correlation=np.correlate(signal,signal,mode='full')
#     return correlation[correlation.size //2:]
# def cross_correlation(signal1,signal2):
#     correlation=np.correlate(signal1,signal2,mode='full')
#     return correlation[correlation.size //2:]

# t=np.linspace(1,0,500,endpoint=False)
# signal1=np.sin(2*np.pi*5*t)
# signal2=np.sin(2*np.pi*5*t+np.pi/4)

# auto_corr_signal1=auto_correlation(signal1)
# cros_correlat=cross_correlation(signal1,signal2)

# plt.figure(figsize=(10,8))

# plt.subplot(1,2,1)
# plt.plot(auto_corr_signal1)
# plt.title("Auto_correlation of signal1 ")
# plt.xlabel("lag")
# plt.ylabel("correlation")

# plt.subplot(1,2,2)
# plt.plot(cros_correlat)
# plt.title("crross_correlation of signal1 and signal2 ")
# plt.xlabel("lag")
# plt.ylabel("correlation")

# plt.tight_layout()
# plt.show()