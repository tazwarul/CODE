import numpy as np
import matplotlib.pyplot as plt

def signal_operations():
    n = np.arange(-10, 11)  # Create time index from -10 to 10
    x = np.sin(0.2 * np.pi * n)  # Example signal (sine wave)
    y=np.sin(0.5*np.pi*n)
   
    signal_ad=x+y

    # Shift right by 3 positions, and handle the boundary values
    # x_shifted = np.roll(x, 3)  # Initialize with zeros
    # x_shifted[:3] = 0  # Set the first 3 elements to zero # Shift the signal right by 3, leave zeros at the start

    x_shifted = np.sin(0.2 * np.pi * (n - 2))  # Right shift by 2
    x_shifted[:3] = 0
    # x_shifted = np.sin(0.2 * np.pi * (n + 2))  # Left shift by 2


    
    # Time reversal (folding the signal)
    x_folded = np.flip(x)  # Reverse the signal

    # Plotting the results
    plt.figure(figsize=(10, 8))

    # Original signal plot
    plt.subplot(4, 1, 1)
    plt.stem(n, x)
    plt.title("Original Signal")
    plt.xlabel("n")
    plt.ylabel("x[n]")

    plt.subplot(4, 1, 2)
    plt.plot(signal_ad)
    plt.title("Signal Add")
    plt.xlabel("n")
    plt.ylabel("x[n] and Y[n]")
    # Shifted signal plot
    plt.subplot(4, 1, 3)
    plt.stem(n, x_shifted)
    plt.title("Shifted Signal (Right by 3)")
    plt.xlabel("n")
    plt.ylabel("x[n]")

    # Folded signal plot
    plt.subplot(4, 1, 4)
    plt.stem(n, x_folded)
    plt.title("Folded Signal")
    plt.xlabel("n")
    plt.ylabel("x[n]")


    # Adjust layout to avoid overlap
    plt.tight_layout()
    plt.show()

# Run the function to see the result
signal_operations()
