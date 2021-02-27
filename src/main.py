import random
from ai.manual import manual_optimize
from ai.ez import optimize
from elastic import elastic_index
from elastic.evaluator import evaluate


def main():
    re_index = input(
    "Do you want to index or re-index documents?[Y/n] \n (Hint: if you are trying app for first time type \'y\' otherwise \'n\')")

    if re_index == ('y' or "Y"):
        print("Starting to index data ...")
        elastic_index.build_index()
        print("Indexing Completed.")

    random_theta = [1, 3, 2, 9]
    samples_count = 50
    x = []
    y = []
    for i in range(samples_count):
        x.append([int(random.random() * 10) for _ in range(4)])
    for i in range(samples_count):
        y.append(int(evaluate(x[i])['query']['map'] * 10000))
        
    print("starting ez optimization\n")
    optimize(x, y)
    print("starting manual optimization\n")
    manual_optimize(x, y, random_theta)


if __name__ == '__main__':
    main()
