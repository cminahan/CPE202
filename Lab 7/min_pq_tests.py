""" Lab 7 Tests
Name: Claire Minahan
Course: CPE202-03
Instructor: Kuboi
"""

import unittest
from min_pq import*

class TestLab7(unittest.TestCase):

    def test_case_1(self):
        pq = MinPQ()
        self.assertRaises(IndexError, pq.min)
        self.assertRaises(IndexError, pq.del_min)
        pq.insert(1)
        pq.insert(9)
        self.assertTrue(pq.num_items == 2)
        self.assertTrue(pq.capacity == 2)
        pq.insert(7)
        pq.insert(5)
        pq.insert(2)
        pq.insert(6)
        self.assertEqual(pq.del_min(), 1)
        self.assertEqual(pq.del_min(), 2)
        self.assertEqual(pq.del_min(), 5)
        self.assertEqual(pq.min(), 6)
        self.assertEqual(pq.del_min(), 6)
        self.assertEqual(pq.del_min(), 7)
        self.assertFalse(pq.is_empty())
        self.assertEqual(pq.size(), 1)

        pq2 = MinPQ([7, 6, 5, 3, 4, 8, 1, 2])
        self.assertEqual(pq2.size(), 8)
        self.assertEqual(pq2.min(), 1)

if __name__ == '__main__':
    unittest.main()