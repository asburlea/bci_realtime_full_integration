"""
Visualize filtered EEG in real time
"""

import matplotlib.pyplot as plt
from pylsl import StreamInlet, resolve_stream
from src.filters import OnlineBandpass

FS = 250
N_CHANNELS = 8

streams = resolve_stream("type", "EEG")
inlet = StreamInlet(streams[0])
filt = OnlineBandpass(FS, 8, 30, N_CHANNELS)

plt.ion()
fig, ax = plt.subplots()

data = []

while True:
    sample, _ = inlet.pull_sample()
    sample = filt.process(sample)
    data.append(sample)

    if len(data) > FS:
        data.pop(0)

    ax.clear()
    ax.plot(data)
    ax.set_title("Filtered EEG (8–30 Hz)")
    plt.pause(0.01)
