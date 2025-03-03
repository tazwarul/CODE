import matplotlib.pyplot as plt
import numpy as np

K = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 2, 11]
t0 = K.index(4)  # Assuming the bold number is 4
t = np.arange(len(K))

K_t = 2 * np.array(K) + t0 - 5 * t0 - 2 * np.array(K) * (t0 + 4)

plt.stem(t, K_t)
plt.title("Sequence K(t)")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()


# Suru
import numpy as np
import matplotlib.pyplot as plt

# Given sequence x(n)
x_n = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
n_range = np.arange(len(x_n))

# Compute y(n)
y_n = []
for n in range(len(x_n)):
    x_n_minus_5 = x_n[n-5] if 0 <= n-5 < len(x_n) else 0
    x_n_plus_4 = x_n[n+4] if 0 <= n+4 < len(x_n) else 0
    y_n.append(2*x_n_minus_5 - 3*x_n_plus_4)

# Plot the sequences
plt.stem(n_range, y_n, linefmt='r-', markerfmt='ro', basefmt='k-', label='y(n)')
plt.stem(n_range, x_n, linefmt='b-', markerfmt='bo', basefmt='k-', label='x(n)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Plot of x(n) and y(n)')
plt.legend()
plt.grid()
plt.show()