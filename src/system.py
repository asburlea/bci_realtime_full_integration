import yaml
from src.acquisition import EEGStream
from src.preprocessing import OnlineBandpass
from src.features import SlidingWindow, BandPower
from src.classifier import OnlineLDA
from src.feedback import VisualBar
from src.profiler import Profiler

class RealTimeBCI:
    def __init__(self, config_path, classifier):
        with open(config_path) as f:
            cfg = yaml.safe_load(f)

        self.eeg = EEGStream()
        self.filter = OnlineBandpass(
            cfg["sampling_rate"],
            cfg["filter"]["low"],
            cfg["filter"]["high"],
            cfg["channels"]
        )
        self.window = SlidingWindow(
            cfg["window"]["size"],
            cfg["window"]["step"]
        )
        self.features = BandPower(
            cfg["sampling_rate"],
            cfg["features"]["band"]
        )
        self.classifier = classifier
        self.feedback = VisualBar(cfg["feedback"]["smoothing"])
        self.profiler = Profiler()

    def run(self):
        while True:
            self.profiler.tic("loop")
            sample = self.eeg.pull()
            sample = self.filter.process(sample)
            win = self.window.update(sample)

            if win is not None:
                feats = self.features.compute(win)
                pred = self.classifier.predict(feats)
                if pred is not None:
                    self.feedback.update(float(pred))

            loop_time = self.profiler.toc("loop")
            print(f"Loop time: {loop_time:.4f}s")

