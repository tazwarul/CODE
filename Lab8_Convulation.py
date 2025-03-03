import numpy as np
import matplotlib.pyplot as plt

# Define the input signal x[n] and impulse response h[n]
x = np.array([1, 2, 3, 4, 5])  # Example input signal
h = np.array([1, -1, 2])  # Example impulse response

# Perform the convolution using numpy's convolve function
y = np.convolve(x, h, mode='full')

# Create time indices for the signals
n_x = np.arange(len(x))
n_h = np.arange(len(h))
n_y = np.arange(len(y))

# Plot the input, impulse response, and output
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.stem(n_x, x)
plt.title('Input Signal x[n]')
plt.xlabel('n')
plt.ylabel('x[n]')

plt.subplot(3, 1, 2)
plt.stem(n_h, h)
plt.title('Impulse Response h[n]')
plt.xlabel('n')
plt.ylabel('h[n]')

plt.subplot(3, 1, 3)
plt.stem(n_y, y)
plt.title('Output Signal y[n] (Convolution of x[n] and h[n])')
plt.xlabel('n')
plt.ylabel('y[n]')

plt.tight_layout()
plt.show()





# import numpy as np
# import matplotlib.pyplot as plt

# x=np.array([1,2,3,4,5])
# h=np.array([1,-1,2,])
# y=np.convolve(x,h,mode="full")

# n_x=np.arange(len(x))
# n_h=np.arange(len(h))
# n_y=np.arange(len(y))

# plt.figure(figsize=(10,5))

# plt.subplot(3,1,1)
# plt.stem(n_x,x)
# plt.title("input signal")
# plt.xlabel('x')
# plt.ylabel('x[n]')

# plt.subplot(3,1,2)
# plt.stem(n_h,h)
# plt.title("impulse signal h[n]")
# plt.xlabel('n')
# plt.ylabel('h[n]')

# plt.subplot(3,1,3)
# plt.stem(n_y,y)
# plt.title("Convolved signal y[n]")
# plt.xlabel('y')
# plt.ylabel('y[n]')

# plt.tight_layout()
# plt.show()
