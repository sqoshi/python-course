import sys

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from sklearn.preprocessing import MinMaxScaler

tanh = np.tanh


def tanh_derivative(x: np.ndarray) -> np.ndarray:
    return 1.0 - x ** 2


def relu(x):
    return x * (x > 0)


def relu_derivative(x):
    return 1. * (x > 0)


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1.0 - x)


class NeuralNetwork:
    def __init__(self, x, y, eta=0.05, func1=relu, func2=relu, der1=relu_derivative, der2=relu_derivative, in_neurons=1,
                 neurons=10, out_neurons=1):
        np.random.seed(17)
        self.f1 = func1
        self.f2 = func2
        self.der2 = der2  # relu_derivative if func1.__name__ == 'relu' else sigmoid_derivative
        self.der1 = der1  # relu_derivative if func1.__name__ == 'relu' else sigmoid_derivative
        self.input = x
        self.weights1 = np.random.rand(neurons, in_neurons)
        self.weights2 = np.random.rand(out_neurons, neurons)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = eta

    def feedforward(self):
        self.layer1 = self.f1(np.dot(self.input, self.weights1.T))
        self.output = self.f2(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        delta2 = (self.y - self.output) * self.der2(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)

        delta1 = np.dot(delta2, self.weights2) * self.der1(self.layer1)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def learn(self):
        self.feedforward()
        self.backprop()


def draw(x_normal, y_normal, speculated):
    plt.scatter(x_normal, speculated, label='learned')
    plt.scatter(x_normal, y_normal, label='original')
    plt.show()


def learn_parabolic():
    x = np.linspace(-50, 50, 101)
    y = x ** 2
    x, y = x.reshape((len(x), 1)), y.reshape((len(y), 1))
    x_scaled, y_scaled = MinMaxScaler(), MinMaxScaler()
    x, y = x_scaled.fit_transform(x), y_scaled.fit_transform(y)
    neural_network = NeuralNetwork(x, y,
                                   func1=sigmoid, func2=sigmoid,
                                   der1=sigmoid_derivative, der2=sigmoid_derivative)
    for i in range(5000):
        neural_network.feedforward()
        neural_network.backprop()
        if i % 150 == 0:
            x_p, y_p = x_scaled.inverse_transform(x), y_scaled.inverse_transform(y)
            speculated = y_scaled.inverse_transform(neural_network.output)
            draw(x_p, y_p, speculated)
            print('MSE: %.3f' % (mse(y_p, speculated) / 10 ** 5))  # scaled mse


def learn_sinus():
    x = np.linspace(0, 2, 161)
    y = np.sin((3 * np.pi / 2) * x)
    x, y = x.reshape((len(x), 1)), y.reshape((len(y), 1))
    x_scaled, y_scaled = MinMaxScaler(), MinMaxScaler()
    x, y = x_scaled.fit_transform(x), y_scaled.fit_transform(y)
    neural_network = NeuralNetwork(x, y, eta=0.0001,
                                   func1=tanh, func2=tanh,
                                   der1=tanh_derivative, der2=tanh_derivative)
    for i in range(100000):
        neural_network.feedforward()
        neural_network.backprop()
        if i % 5000 == 0:
            x_p, y_p = x_scaled.inverse_transform(x), y_scaled.inverse_transform(y)
            speculated = y_scaled.inverse_transform(neural_network.output)
            draw(x_p, y_p, speculated)
            print('MSE: %.5f' % mse(y_p, speculated))


if __name__ == '__main__':
    learn_parabolic() if '--parabolic' in sys.argv else learn_sinus()
