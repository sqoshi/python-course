import os
import random
import time

import numpy as np
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def plot_(x, y, scx, scy, model):
    yhat = model.predict(x)
    x_plot = scx.inverse_transform(x)
    y_plot = scy.inverse_transform(y)
    yhat_plot = scy.inverse_transform(yhat)
    pyplot.scatter(x_plot, y_plot, label='Actual', s=90)
    pyplot.scatter(x_plot, yhat_plot, label='Predicted', edgecolors='black')
    pyplot.title('Input (x) versus Output (y)')
    pyplot.xlabel('Input Variable (x)')
    pyplot.ylabel('Output Variable (y)')
    pyplot.legend()
    pyplot.show()


def get_random_model(x, y, ep=500, acts=('tanh', 'relu', 'sigmoid'), krnl_init='he_uniform', in_dim=1, out_dim=1,
                     max_neuron_layer=10,
                     min_neuron_layer=2, layers_number=0, ls='mse', opt='adam'):
    model = Sequential()
    model.add(
        Dense(random.randint(min_neuron_layer, max_neuron_layer), input_dim=in_dim, activation=random.choice(acts),
              kernel_initializer=krnl_init))
    for i in range(layers_number):
        neurons = random.randint(min_neuron_layer, max_neuron_layer)
        model.add(
            Dense(neurons, activation=random.choice(acts),
                  kernel_initializer=krnl_init))
    model.add(Dense(out_dim))
    model.compile(loss=ls, optimizer=opt)
    model.fit(x, y, epochs=ep, batch_size=10, verbose=0)
    return model


def get_data(name):
    if 'parabolic' in name:
        x = np.linspace(-50, 50, 26)
        y = x ** 2
    elif 'sinus' in name:
        x = np.linspace(0, 2, 21)
        y = np.sin((3 * np.pi / 2) * x)
    else:
        raise NotImplementedError
    x = x.reshape((len(x), 1))
    y = y.reshape((len(y), 1))
    scale_x = MinMaxScaler()
    x = scale_x.fit_transform(x)
    scale_y = MinMaxScaler()
    y = scale_y.fit_transform(y)
    return x, y, scale_x, scale_y


def learn_parabolic(model):
    x, y, scx, scy = get_data('learn_parabolic')
    yhat = model.predict(x)
    y_plot = scy.inverse_transform(y)
    yhat_plot = scy.inverse_transform(yhat)
    print('MSE: %.3f' % mean_squared_error(y_plot, yhat_plot))
    return mean_squared_error(y_plot, yhat_plot)


def learn_sinus(model):
    x, y, scx, scy = get_data('learn_sinus')
    yhat = model.predict(x)
    y_plot = scy.inverse_transform(y)
    yhat_plot = scy.inverse_transform(yhat)
    print('MSE: %.3f' % mean_squared_error(y_plot, yhat_plot))
    return mean_squared_error(y_plot, yhat_plot)


def get_current_time():
    return int(round(time.time() * 1000))


def get_environment(x, y, n=10):
    return [get_random_model(x, y) for _ in range(n)]


def local_search(t, quality):
    end_time = get_current_time() + t * 1000
    x, y, scx, scy = get_data(quality.__name__)
    model = get_random_model(x, y)
    best_solution = model
    while get_current_time() < end_time:
        model = min(get_environment(x, y), key=quality)
        if quality(model) < quality(best_solution):
            best_solution = model
    plot_(x, y, scx, scy, best_solution)
    return best_solution


def main(t, func):
    x = local_search(t, quality=func)
    print(x.summary())
    for layer in x.layers:
        print(layer.name, str(layer.activation).split(" ")[1])


main(10, learn_sinus)
