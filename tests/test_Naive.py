import unittest
from primes.Naive import naive
class TestNaive(unittest.TestCase):

    def setUp(self):
        pass

    def test_0(self):
        primes = []
        self.assertEquals(primes, naive(0))