import numpy as np
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1.0 - x)


class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        neurons = 10
        ip_dim = x.shape[1]
        op_dim = y.shape[1]
        self.weights1 = np.random.randn(ip_dim, neurons)  # weights
        self.weights2 = np.random.randn(neurons, op_dim)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = 0.5

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1.T))
        self.output = sigmoid(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        delta2 = (self.y - self.output) * sigmoid_derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)

        delta1 = np.dot(delta2, self.weights2) * sigmoid_derivative(self.layer1)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def predict(self, data):
        self.x = data
        self.feedforward()
        return self.y.argmax()


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
