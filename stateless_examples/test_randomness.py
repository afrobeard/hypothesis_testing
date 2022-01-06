import unittest
import statistics
from randomness import generate

algos = ("mersenne", "randu", "middlesquare", "naive")
#algo = algos[-4]
algo = algos[0]

class TestMersenne(unittest.TestCase):
    def setUp(self):
        if not hasattr(self, "algo"):
            self.algo = "mersenne"
        self.samples = [generate(algo=self.algo) for x in range(100000)]

    def test_repetition(self):
        seen = set()
        for i in range(1000):
            selection = self.samples[i:i+1000]
            new_hash = hash(tuple(selection))
            assert new_hash not in seen
            seen.add(new_hash)

    def test_median(self):
        assert 45 <= statistics.median(self.samples) <= 55

    def test_1d_uniformity(self):
        for ref, actual in zip(range(10, 100, 10), statistics.quantiles(self.samples, n=10)):
            assert (ref - 2.5) <= actual <= (ref +2.5)

    """
    def test_nd_uniformity(self):
        pass  # Long term goal
    """

class TestRandu(TestMersenne):
    algo = "randu"

class TestMiddleSquare(TestMersenne):
    algo = "middlesquare"

class TestNaive(TestMersenne):
    algo = "naive"

if __name__ == "__main__":
    unittest.main()
