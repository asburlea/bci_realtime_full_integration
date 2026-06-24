from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

class OnlineLDA:
    def __init__(self):
        self.model = LinearDiscriminantAnalysis()
        self.trained = False

    def train(self, X, y):
        self.model.fit(X, y)
        self.trained = True

    def predict(self, x):
        if not self.trained:
            return None
        return int(self.model.predict([x])[0])

