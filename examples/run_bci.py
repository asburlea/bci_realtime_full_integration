from src.system import RealTimeBCI
from src.classifier import OnlineLDA

clf = OnlineLDA()
# clf.train(X, y) must be done beforehand

bci = RealTimeBCI("config/config.yaml", clf)
bci.run()
