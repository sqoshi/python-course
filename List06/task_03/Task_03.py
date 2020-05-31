import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from sklearn.preprocessing import MinMaxScaler

tanh = np.tanh


def tanh_derivative(x: np.ndarray) -> np.ndarray:
    return 1.0 - x ** 2


def sigmoid(s):
    return 1 / (1 + np.exp(-s))


def sigmoid_derv(s):
    return s * (1 - s)


def softmax(s):
    exps = np.exp(s - np.max(s, axis=1, keepdims=True))
    return exps / np.sum(exps, axis=1, keepdims=True)


def relu(x):
    return x * (x > 0)


def relu_derivative(x):
    return 1. * (x > 0)


def cross_entropy(pred, real):
    print(pred)
    print(real)
    n_samples = real.shape[0]
    res = pred - real
    return res/ n_samples


class NeuralNetwork:
    def __init__(self, x, y):
        self.x = x
        neurons = 10
        self.lr = 0.02
        ip_dim = x.shape[1]
        op_dim = y.shape[1]

        self.w1 = np.random.randn(ip_dim, neurons)
        self.b1 = np.zeros((1, neurons))
        self.w2 = np.random.randn(neurons, neurons)
        self.b2 = np.zeros((1, neurons))
        self.w3 = np.random.randn(neurons, op_dim)
        self.b3 = np.zeros((1, op_dim))
        self.y = y

    def feedforward(self):
        z1 = np.dot(self.x, self.w1) + self.b1
        self.a1 = sigmoid(z1)
        z2 = np.dot(self.a1, self.w2) + self.b2
        self.a2 = relu(z2)
        z3 = np.dot(self.a2, self.w3) + self.b3
        self.a3 = softmax(z3)

    def backprop(self):
        a3_delta = cross_entropy(self.a3, self.y)  # w3
        z2_delta = np.dot(a3_delta, self.w3.T)
        a2_delta = z2_delta * sigmoid_derv(self.a2)  # w2
        z1_delta = np.dot(a2_delta, self.w2.T)
        a1_delta = z1_delta * relu_derivative(self.a1)  # w1

        self.w3 -= self.lr * np.dot(self.a2.T, a3_delta)
        self.b3 -= self.lr * np.sum(a3_delta, axis=0, keepdims=True)
        self.w2 -= self.lr * np.dot(self.a1.T, a2_delta)
        self.b2 -= self.lr * np.sum(a2_delta, axis=0)
        self.w1 -= self.lr * np.dot(self.x.T, a1_delta)
        self.b1 -= self.lr * np.sum(a1_delta, axis=0)


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
    neural_network = NeuralNetwork(x, y)
    for i in range(25000):
        neural_network.feedforward()
        neural_network.backprop()
        if i % 1000 == 0:
            x_p, y_p = x_scaled.inverse_transform(x), y_scaled.inverse_transform(y)
            speculated = y_scaled.inverse_transform(neural_network.a3)
            draw(x_p, y_p, speculated)
            print('MSE: %.3f' % (mse(y_p, speculated)))  #

    # print("Training accuracy : ", get_acc(x_train / 16, np.array(y_train)))


learn_parabolic()
