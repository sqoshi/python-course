import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def softmax(s):
    exps = np.exp(s - np.max(s, axis=1, keepdims=True))
    return exps / np.sum(exps, axis=1, keepdims=True)


def sigmoid_derv(x):
    return x * (1.0 - x)


def cross_entropy(pred, real):
    n_samples = real.shape[0]
    res = pred - real
    return res / n_samples


def error(pred, real):
    n_samples = real.shape[0]
    logp = - np.log(pred[np.arange(n_samples), real.argmax(axis=1)])
    loss = np.sum(logp) / n_samples
    return loss


def scale_data(data: np.ndarray, target_range=(0, 1)) -> np.ndarray:
    scaler = MinMaxScaler(target_range)
    return scaler.fit_transform(data)


class NeuralNetwork:
    def __init__(self, x, y):
        self.x = x
        neurons = 10
        self.lr = 0.5
        ip_dim = x.shape[1]
        op_dim = y.shape[1]
        self.w1 = np.random.randn(ip_dim, neurons)  # weights
        self.b1 = np.zeros((1, neurons))  # biases
        self.w2 = np.random.randn(neurons, op_dim)
        self.b2 = np.zeros((1, op_dim))
        self.y = y

    def feedforward(self):
        z1 = np.dot(self.x, self.w1) + self.b1
        self.a1 = sigmoid(z1)
        z2 = np.dot(self.a1, self.w2) + self.b2
        self.a2 = softmax(z2)

    def backprop(self):
        loss = error(self.a2, self.y)
        print('Error :', loss)
        a2_delta = cross_entropy(self.a2, self.y)  # w3
        z1_delta = np.dot(a2_delta, self.w2.T)
        a1_delta = z1_delta * sigmoid_derv(self.a1)  # w1

        self.w2 -= self.lr * np.dot(self.a1.T, a2_delta)
        self.b2 -= self.lr * np.sum(a2_delta, axis=0, keepdims=True)
        self.w1 -= self.lr * np.dot(self.x.T, a1_delta)
        self.b1 -= self.lr * np.sum(a1_delta, axis=0)

    def predict(self, data):
        self.x = data
        self.feedforward()
        return self.a2


def learn_function(training_data_x, training_data_y, test_data_x, test_data_y, nn: NeuralNetwork = None):
    training_data_x = training_data_x.reshape((-1, 1))
    training_data_y = training_data_y.reshape((-1, 1))
    test_data_x = test_data_x.reshape((-1, 1))
    test_data_y = test_data_y.reshape((-1, 1))
    # preprocess data for nn
    scaler_x = MinMaxScaler((0, 1))
    scaler_y = MinMaxScaler((0, 1))
    scaled_x_train = scaler_x.fit_transform(training_data_x)
    scaled_y_train = scaler_y.fit_transform(training_data_y)
    scaled_x_test = scaler_x.fit_transform(test_data_x)
    # learning
    nn = NeuralNetwork(scaled_x_train, scaled_y_train)
    draw = 10000
    for i in range(100):
        nn.feedforward()
        nn.backprop()

        if i % draw == 0:
            pr = nn.predict(scaled_x_test)
            print('p', pr, len(pr))

            plt.scatter(test_data_x, test_data_y, 14)
            plt.scatter(test_data_x, scaler_y.inverse_transform(pr), 14)
            plt.show()

        plt.scatter(test_data_x, test_data_y)
        plt.title(f'Function')
        plt.show()

        pr = nn.predict(scaled_x_test)
        plt.scatter(test_data_x, scaler_y.inverse_transform(pr))
        plt.title(f'End, Error: '
                  f'{np.square(test_data_y - scaler_y.inverse_transform(pr)).mean()}')
        plt.show()


def learn_parabolic():
    training_data = np.linspace(-50, 50, 26)
    labels = training_data ** 2
    test_data = np.linspace(-50, 50, 101)
    expected_from_test = test_data ** 2
    learn_function(training_data, labels, test_data, expected_from_test)


learn_parabolic()
"""
if __name__ == '__main__':
    x = np.array(np.linspace(-50, 50, 26))
    y = x ** 2
    neural_network = NeuralNetwork(x, y)
    for _ in range(10000):
        neural_network.feedforward()
        neural_network.backprop()
    np.set_printoptions(precision=3, suppress=True)
    print(neural_network.a2)
    print(neural_network.w1)
    print(neural_network.w2)
"""
