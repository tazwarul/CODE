import numpy as np
import matplotlib.pyplot as plt

# Define X(n) = 2δ(n+2) - δ(n-4)
def X(n):
    return 2 * (1 if n == -2 else 0) - (1 if n == 4 else 0)

# Define the range of n for X(n)
n_X = np.arange(-7, 7)  # Indices for X(n): -7 to 7
x_values = np.array([X(n) for n in n_X])

# Plot X(n)
plt.figure(figsize=(10, 5))
plt.stem(n_X, x_values)  # Removed use_line_collection=True
plt.title('Sequence X(n)')
plt.xlabel('n')
plt.ylabel('X(n)')
plt.grid(True)
plt.show()