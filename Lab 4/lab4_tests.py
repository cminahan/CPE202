# Lab 4
# Name: Claire Minahan
# Section: CPE202-03

""" lab4 tests """

import unittest
from queue_linked import*
from queue_array import*

class TestLab4(unittest.TestCase):

    def test_queue_linked(self):
        queue1 = QueueLinked(4)
        self.assertTrue(queue1.is_empty())
        self.assertRaises(IndexError, queue1.dequeue)
        queue1.enqueue(90)
        self.assertEqual(print(queue1), None)
        self.assertEqual(queue1.size(), 1)
        self.assertEqual(queue1.capacity, 4)
        self.assertEqual(queue1.dequeue(), 90)
        queue1.enqueue(53)
        queue1.enqueue(8)
        self.assertFalse(queue1.is_full())
        queue1.enqueue(16)
        queue1.enqueue(7)
        self.assertEqual(queue1.dequeue(), 53)
        node1 = queue1.front
        node2 = queue1.rear
        self.assertEqual(queue1.front, node1)
        self.assertEqual(queue1.rear, node2)
        self.assertEqual(queue1.num_items, 3)
        queue1.enqueue(6)
        self.assertEqual(queue1.num_items, queue1.capacity)
        self.assertTrue(queue1.is_full())
        self.assertRaises(IndexError, queue1.enqueue, 8)

    def test_queue_array(self):
        queue2 = QueueArray(3)
        self.assertRaises(IndexError, queue2.dequeue)
        queue2.enqueue(8)
        self.assertEqual(print(queue2), None)
        queue2.enqueue(6)
        self.assertEqual(queue2.dequeue(), 8)
        self.assertEqual(queue2.size(), 1)
        self.assertFalse(queue2.is_empty())
        self.assertFalse(queue2.is_full())
        queue2.enqueue(78)
        queue2.enqueue(7)
        self.assertRaises(IndexError, queue2.enqueue, 9)

if __name__ == '__main__':
    unittest.main()