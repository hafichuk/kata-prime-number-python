import unittest
from primes.Naive import naive
class TestNaive(unittest.TestCase):

    def setUp(self):
        pass

    def test_primes(self):
        numbers = (
            [0, []],    
            [1, []],    
            [2, [2]],   
            [3, [3]],   
            [4, [2,2]], 
            [5, [5]],   
            [6, [2,3]], 
            [7, [7]],   
            [8, [2]*3], 
            [9, [3,3]], 
            [10, [2,5]],
            [84, [2,2,3,7]],
            [100, [2,2,5,5]],
            [2*3*5*7*11*13*17, [2,3,5,7,11,13,17]],
            [2**100, [2]*100],
            [2147483647, [2147483647]],
            [11*11*11*13*2147483647, [11,11,11,13,2147483647]]
        )

        for number in numbers:
            self.assertEquals(number[1], naive(number[0]))



