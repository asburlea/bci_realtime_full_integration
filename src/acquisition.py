from pylsl import StreamInlet, resolve_stream

class EEGStream:
    def __init__(self):
        streams = resolve_stream("type", "EEG")
        self.inlet = StreamInlet(streams[0])

    def pull(self):
        sample, _ = self.inlet.pull_sample()
        return sample
