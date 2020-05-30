import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1.0 - x)


def relu(x):
    return x * (x > 0)


def relu_derivative(x):
    return 1. * (x > 0)


class NeuralNetwork:
    def __init__(self, x, y, func1=relu, func2=relu):
        np.random.seed(17)
        self.f1 = func1
        self.f2 = func2
        self.der2 = relu_derivative if func2.__name__ == 'relu' else sigmoid_derivative
        self.der1 = relu_derivative if func1.__name__ == 'relu' else sigmoid_derivative
        self.input = x
        self.weights1 = np.random.rand(4, self.input.shape[1])
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = 0.01

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
`

if __name__ == '__main__':
    X = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])
    y = np.array([[0], [1], [1], [0]])
    history = []
    neural_network = NeuralNetwork(X, y, func1=sigmoid, func2=relu)
    r = 20000
    for _ in range(r):
        neural_network.feedforward()
        neural_network.backprop()
        history.append(neural_network.output)
    np.set_printoptions(precision=3, suppress=True)
    errors = []
    for h in history:
        errors.append(sum([abs(h1[0] - z1) for h1, z1 in zip(h, [0, 1, 1, 0])]) / len(h))  # error
    plt.scatter(np.linspace(0, r, r), errors, 0.2)
    plt.show()
    print(neural_network.output)
    print(neural_network.weights1)
    print(neural_network.weights2)
