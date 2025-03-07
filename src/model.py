from sklearn.linear_model import LogisticRegression
import pickle

class MLModel:
    def __init__(self):
        self.model = LogisticRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save_model(self, filepath="model.pkl"):
        with open(filepath, "wb") as f:
            pickle.dump(self.model, f)

if __name__ == "__main__":
    print("Model file created")
