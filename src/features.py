import numpy as np
from scipy.signal import welch

class SlidingWindow:
    def __init__(self, size, step):
        self.size = size
        self.step = step
        self.buffer = []
        self.counter = 0

    def update(self, sample):
        self.buffer.append(sample)
        self.counter += 1
        if len(self.buffer) > self.size:
            self.buffer.pop(0)
        if len(self.buffer) == self.size and self.counter % self.step == 0:
            return np.array(self.buffer)
        return None


class BandPower:
    def __init__(self, fs, band):
        self.fs = fs
        self.band = band

    def compute(self, window):
        freqs, psd = welch(window, fs=self.fs, axis=0)
        idx = (freqs >= self.band[0]) & (freqs <= self.band[1])
        return psd[idx].mean(axis=0)
