import unittest
from primes.Naive import naive
class TestNaive(unittest.TestCase):

    def setUp(self):
        pass

    def test_0(self):
        n = 0
        primes = []
        self.assertEquals(primes, naive(n))

    def test_1(self):
        n = 1
        primes = []
        self.assertEquals(primes, naive(n))

    def test_2(self):
        n = 2
        primes = [2]
        self.assertEquals(primes, naive(n))

    def test_3(self):
        n = 3
        primes = [3]
        self.assertEquals(primes, naive(n))

    def test_4(self):
        n = 4
        primes = [2,2]
        self.assertEquals(primes, naive(n))

    def test_5(self):
        n = 5
        primes = [5]
        self.assertEquals(primes, naive(n))

    def test_6(self):
        n = 6
        primes = [2,3]
        self.assertEquals(primes, naive(n))

    def test_7(self):
        n = 7
        primes = [7]
        self.assertEquals(primes, naive(n))