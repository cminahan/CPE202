# lab1
# Name: Claire Minahan
# Section: CPE202-03


import unittest
from lab1 import*

class TestLab1(unittest.TestCase):

    def test_get_max(self):
        self.assertEqual(get_max([1, -3, 4, 7]), 7)
        self.assertEqual(get_max([2, -23, 89, 23, 78, 0]), 89)
        self.assertEqual(get_max([0, 0, 12, 14, -9, 14]), 14)

    def test_reverse(self):
        self.assertEqual(reverse('banana'), 'ananab')
        self.assertEqual(reverse('!hell0 w*rLd'), 'dLr*w 0lleh!')
        self.assertEqual(reverse('racecar'), 'racecar')

    def test_search(self):
        self.assertEqual(search([1, 2, 4, 6, 8], 6),3)
        self.assertEqual(search([3, 6, 9, 12, 15], 9), 2)
        self.assertEqual(search([-1, 0, 4, 7, 12], 0), 1)
        self.assertEqual(search([1, 2, 3, 4, 5], 6), None)
        self.assertEqual(search([ ], 9), 0)

    def test_fib(self):
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(9), 34)

    def test_factorial_iter(self):
        self.assertEqual(factorial_iter(4), 24)
        self.assertEqual(factorial_iter(9), 362880)

    def test_factorial_rec(self):
        self.assertEqual(factorial_rec(3), 6)
        self.assertEqual(factorial_rec(7), 5040)


# Run the unittest
if __name__ == '__main__':
    unittest.main()
