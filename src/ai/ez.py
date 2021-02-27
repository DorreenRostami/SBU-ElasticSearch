import numpy as np
from scipy.optimize import minimize
from sklearn import linear_model
from elastic.evaluator import evaluate

best_eval = 0
best_weights = []

def optimize(x, y):
    classifier = linear_model.SGDClassifier(loss="hinge", penalty="l2", max_iter=100)
    classifier.fit(x, y)
    x0 = np.array([1, 2, 3, 4]).reshape(4)
    minn = minimize(prediction_wrapper, x0=x0, options={"maxiter": 12, "disp": True, 'eps': 1})
    print(f'fyi_2 scikit learn finds \n{minn.x.tolist()}\n that has a map of {prediction(minn.x)}')
    print(f"best i ever saw was {best_weights} with a map of {best_eval}")


def to_list(x):
    return x.astype('int').tolist()


def prediction(x):
    return evaluate(to_list(x))["query"]["map"] * -100000


def prediction_wrapper(x):
    global best_eval
    global best_weights
    return_value = prediction(x)
    if return_value < best_eval:
        best_weights = to_list(x)
        best_eval = return_value
    return return_value
