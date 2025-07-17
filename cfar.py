import numpy as np
import matplotlib.pyplot as plt

# Radar Parameters
c = 3e8               # Speed of light
f0 = 77e9             # Starting frequency (77 GHz typical for automotive radar)
B = 300e6             # Bandwidth of the chirp (300 MHz)
T_chirp = 100e-6      # Chirp duration (100 microseconds)
sweep_slope = B / T_chirp
Fs = 5e6              # Sampling rate (5 MHz)

# Signal Generation
N = int(T_chirp * Fs)
t = np.linspace(0, T_chirp, N)

# True target ranges in meters
ranges_true = [50, 90, 130]

# Transmitted signal
tx = np.cos(2 * np.pi * (f0 * t + 0.5 * sweep_slope * t**2))

# Received signal with delay per target
rx = np.zeros_like(t)
for R in ranges_true:
    tau = 2 * R / c
    t_delay = t - tau
    rx += np.cos(2 * np.pi * (f0 * t_delay + 0.5 * sweep_slope * t_delay**2))

# Add controlled noise
rx += 0.4 * np.random.randn(N)

# Mixer (Beat signal)
mix = tx * rx

# Zero-padding and FFT
N_fft = 4 * N  # zero-padding for higher resolution
fft_out = np.fft.fft(mix, N_fft)
fft_mag = np.abs(fft_out[:N_fft // 2])
fft_freqs = np.fft.fftfreq(N_fft, 1 / Fs)[:N_fft // 2]
range_axis = (c * fft_freqs) / (2 * sweep_slope)

# CFAR Parameters
T, G, offset = 24, 12, 5  # Training cells, Guard cells, Threshold scaling factor
cfar_output = np.zeros(len(fft_mag))

# CFAR Detection Loop
for i in range(T + G, len(fft_mag) - T - G):
    training_cells = np.concatenate((fft_mag[i - T - G:i - G], fft_mag[i + G + 1:i + G + T + 1]))
    threshold = offset * np.mean(training_cells)
    if fft_mag[i] > threshold:
        cfar_output[i] = 1

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(range_axis, fft_mag, label='FFT Magnitude')
plt.plot(range_axis, cfar_output * np.max(fft_mag), 'r--', label='CFAR Detection')
plt.title("FMCW Beat Signal Spectrum with CFAR Target Detection")
plt.xlabel("Range (m)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.legend()
plt.xlim(0, 200)
plt.tight_layout()
plt.show()



