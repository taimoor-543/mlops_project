import pytest
from src.model import MLModel

def test_model_training():
    model = MLModel()
    X_train = [[0], [1], [2], [3]]
    y_train = [0, 0, 1, 1]
    model.train(X_train, y_train)
    assert model.predict([[2]]) == [1]

if __name__ == "__main__":
    pytest.main()
