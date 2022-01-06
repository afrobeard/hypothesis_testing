import random

class MersenneTwister(object):
    @staticmethod
    def get_random():
        return int(random.random() * 100)


class Randu(object):
    """
    https://en.wikipedia.org/wiki/RANDU

    """
    _seed = 0
    _M = 2 ** 6
    _A = 0
    _B = 65539

    def __init__(self, seed):
        self._seed = seed

    def get_random(self):
        out = self._seed
        out = self._A + ((self._B * out) % self._M)
        self._seed = out
        return out


class MiddleSquare(object):
    def __init__(self, seed_number=4750):
        self.seed_number = seed_number
        self.number = seed_number
        self.counter = 0

    def get_random(self):
        self.counter += 1
        self.number = int(str(self.number * self.number).zfill(8)[2:6])
        return int(self.number / 100)

class CounterRandom(object):
    counter = 1
    @classmethod
    def get_random(cls):
        if cls.counter > 85:
            cls.counter = int(cls.counter / 10)
        cls.counter += 7
        return cls.counter

mersenne = MersenneTwister()
randu = Randu(10)
naive = CounterRandom()
middlesquare = MiddleSquare()

def generate(algo="mersenne"):
    if algo not in ("mersenne", "randu", "middlesquare", "naive"):
        raise ValueError("Invalid Random number generation algo")
    elif algo == "mersenne":
        generator_obj = mersenne
    elif algo == "randu":
        generator_obj = randu
    elif algo == "naive":
        generator_obj = naive
    elif algo == "middlesquare":
        generator_obj = middlesquare
    return generator_obj.get_random()

if __name__ == "__main__":
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    samples = dict()

    plt.figure(1)
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(7,7))
    i = 0
    for algo in ("mersenne", "randu", "middlesquare", "naive"):
        samples[algo] = [generate(algo=algo) for x in range(100000)]
        midpoint = int(100000/2)
        x_range = samples[algo][0:midpoint]
        y_range = samples[algo][midpoint:]

        (x,y) = divmod(i, 2)
        axs[x, y].set_title(algo)
        axs[x, y].scatter(x_range, y_range)
        i += 1

        #fig, ax = plt.subplots()
        #ax.scatter(x_range, y_range, label=algo)
        #plt.legend(loc='upper left')
        #ax.grid()
        #plt.show()

    fig.tight_layout()
    plt.show()
