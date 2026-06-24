"""
Compare offline and online filtering
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from src.filters import OnlineBandpass

FS = 250
N_CHANNELS = 1

signal = np.random.randn(FS * 5, N_CHANNELS)

b, a = butter(4, [8, 30], fs=FS, btype="band")
offline = filtfilt(b, a, signal[:, 0])

online_filt = OnlineBandpass(FS, 8, 30, N_CHANNELS)
online = [online_filt.process([s])[0] for s in signal[:, 0]]

plt.plot(offline, label="offline (filtfilt)")
plt.plot(online, label="online (causal)")
plt.legend()
plt.title("Offline vs Online Filtering")
plt.show()

