import numpy as np
from elastic.evaluator import evaluate


def manual_optimize(x, y, random_theta):
    good_theta = minibatch_gradient_descent(x, y, random_theta)
    extremum = Extremum(good_theta)
    for i, sample in enumerate(x):
        if i % 2:
            print('\t', end='')
        print(f'  map[{sample}] = {evaluate(sample)["query"]["map"]}')
        if i % 2:
            print('\t', end='')
        print(f'guess {sample} is {extremum.f(sample)}')


def minibatch_gradient_descent(x, y, theta, learning_rate=0.01, iterations=10, batch_size=20):
    m = len(y) 
    x = np.array(x)
    y = np.array(y)
    for it in range(iterations): 
        indices = np.arange(m)
        np.random.shuffle(indices)
        x = x[indices]
        y = y[indices]
        for i in range(0, m, batch_size):
            x_i = np.array(x[i: i + batch_size])
            y_i = np.array(y[i: i + batch_size])
            prediction = np.dot(x_i, theta)
            theta = theta - (1 / m) * learning_rate * x_i.T.dot(np.subtract(prediction, y_i))
    return theta.tolist()  


class Extremum:
    def __init__(self, theta):
        self.theta = np.array(theta)
        self.initial_x = [1, 1, 1, 1]
        self.iterations = 10
        self.learning_rate = 0.1

    def f(self, weights):
        return self.theta.dot(weights)

    def find_extremum(self):
        x = self.initial_x
        for i in range(self.iterations):
            new_x = x + self.learning_rate * self.theta
            if min(new_x) < 0:
                break
            x = new_x
        return self.f(x)