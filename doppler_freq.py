# Doppler Simulation - Frequency Shift due to Target Movement

import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)
f0 = float(input("Enter transmitted radar frequency (Hz): "))  # e.g. 10e9 for 10 GHz
v = float(input("Enter target velocity (m/s): "))              # e.g. 30 m/s

# Doppler frequency shift
fd = (2 * v * f0) / c

print(f"\n📡 Doppler Shift: {fd:.2f} Hz")

# Simulate transmitted and received signal
t = np.linspace(0, 1e-3, 1000)  # 1 ms duration
tx_signal = np.cos(2 * np.pi * f0 * t)                # Transmitted signal
rx_signal = np.cos(2 * np.pi * (f0 + fd) * t)         # Received with Doppler shift

# Plot both signals
plt.figure(figsize=(10, 5))
plt.plot(t[:200], tx_signal[:200], label='Transmitted Signal')
plt.plot(t[:200], rx_signal[:200], label='Received Signal (Doppler Shifted)', linestyle='--')
plt.title("Doppler Simulation: Transmitted vs Received Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
