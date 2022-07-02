import unittest

from main import fib as fib, my_genn as my_genn, FibonacciLst as FibonacciLst, FibonacciLstMax as FibonacciLstMax


class TestFibFunction(unittest.TestCase):

    def test_fib_1(self):
        self.assertEqual(fib(1), [0, 1, 1])

    def test_fib_2(self):
        self.assertEqual(fib(8), [0, 1, 1, 2, 3, 5, 8])

    def test_fib_3(self):
        self.assertEqual(fib(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        

class TestFibGen(unittest.TestCase):

    def test_gen_1(self):
        self.assertEqual(list(my_genn(1)), [0])

    def test_gen_2(self):
        self.assertEqual(list(my_genn(8)), 
                        [0, 1, 1, 2, 3, 5, 8, 13])

    def test_gen_3(self):
        self.assertEqual(list(my_genn(10)), 
                        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])


class TestFibonacci(unittest.TestCase):

    def test_FibonacciLst(self):
        self.assertEqual(list(FibonacciLst(list(range(8)))),
                        [0, 1, 1, 2, 3, 5, 8, 13])

    def test_FibonacciLstMax(self):
        self.assertEqual(list(FibonacciLstMax(list(range(9)))),
                        [0, 1, 1, 2, 3, 5, 8])
      

if __name__ == '__main__':
    unittest.main()