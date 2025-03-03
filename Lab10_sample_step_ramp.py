import numpy as np
import matplotlib.pyplot as plt

# Unit sample sequence
unit_sample = np.zeros(10)
unit_sample[5] = 1

# Unit step signal
unit_step = np.heaviside(np.arange(10), 1)

# Unit ramp signal
unit_ramp = np.arange(10)

plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.stem(unit_sample)
plt.title("Unit Sample Sequence")

plt.subplot(3, 1, 2)
plt.stem(unit_step)
plt.title("Unit Step Signal")

plt.subplot(3, 1, 3)
plt.stem(unit_ramp)
plt.title("Unit Ramp Signal")

plt.tight_layout()
plt.show()