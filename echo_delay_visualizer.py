# Echo Delay Visualizer - Pulse Radar Simulation

import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)
pulse_width = 1e-6  # 1 microsecond pulse
R = float(input("Enter distance to target (m): "))  # e.g. 1500 m

# Calculate echo delay
delay_time = 2 * R / c
print(f"\n Echo Delay Time: {delay_time*1e6:.2f} µs")

# Time axis
t = np.linspace(0, 10e-6, 1000)  # 10 µs window

# Generate transmitted pulse
tx_pulse = np.where(t <= pulse_width, 1, 0)

# Generate received echo (delayed pulse)
rx_pulse = np.where((t >= delay_time) & (t <= delay_time + pulse_width), 1, 0)

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(t * 1e6, tx_pulse, label="Transmitted Pulse")
plt.plot(t * 1e6, rx_pulse, label="Received Echo", linestyle='--')
plt.title("Echo Delay Simulation")
plt.xlabel("Time (µs)")
plt.ylabel("Signal Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
