# Radar Equation Calculator with Visualization

import math
import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light in m/s
pi = math.pi

# --- INPUTS ---
Pt = float(input("Enter Transmit Power (W): "))       # e.g. 100 W
G_dB = float(input("Enter Antenna Gain (dB): "))       # e.g. 30 dB
f = float(input("Enter Radar Frequency (Hz): "))       # e.g. 10e9 Hz
R = float(input("Enter Distance to Target (m): "))     # e.g. 5000 m
sigma = float(input("Enter Target RCS σ (m²): "))      # e.g. 1
L = float(input("Enter System Loss (L): "))            # e.g. 1.5

# --- CALCULATION ---
G = 10 ** (G_dB / 10)               # Convert gain from dB to linear
wavelength = c / f

# Single point calculation
Pr = (Pt * G**2 * wavelength**2 * sigma) / ((4 * pi)**3 * R**4 * L)
Pr_dBm = 10 * math.log10(Pr * 1000)  # Convert to dBm

# --- OUTPUT ---
print(f"\n Received Power at {R} m: {Pr:.4e} W")
print(f" Received Power (dBm): {Pr_dBm:.2f} dBm")

# --- VISUALIZATION ---
# Distance range for plotting
distances = np.linspace(100, 10000, 500)
received_powers = (Pt * G**2 * wavelength**2 * sigma) / ((4 * pi)**3 * distances**4 * L)
received_powers_dBm = 10 * np.log10(received_powers * 1000)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(distances, received_powers_dBm, label="Received Power (dBm)")
plt.axvline(x=R, color='red', linestyle='--', label=f"Input Distance = {R} m")
plt.axhline(y=Pr_dBm, color='green', linestyle='--', label=f"Calculated Power = {Pr_dBm:.2f} dBm")

plt.title("Radar Received Power vs Distance")
plt.xlabel("Distance (m)")
plt.ylabel("Received Power (dBm)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

