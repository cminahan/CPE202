# Lab 3
# Name: Claire Minahan
# Section: CPE202-03

import unittest
from stack_array import*
from stack_linked import*
from node import*

class TestLab3(unittest.TestCase):

    def test_stack_array(self):
        arr1 = StackArray()
        arr1.push(3)
        arr1.push(4)
        arr1.push(2)
        self.assertEqual(arr1.arr, [3, 4, 2, None])
        self.assertEqual(arr1.num_items, 3)
        self.assertEqual(arr1.capacity, 4)
        arr1.push(18)
        self.assertEqual(arr1.size(), 4)
        self.assertEqual(arr1.pop(), 18)
        self.assertFalse(arr1.is_empty())
        self.assertEqual(arr1.size(), 3)
        arr2 = StackArray()
        self.assertTrue(arr2.is_empty)
        self.assertRaises(IndexError, arr2.pop)
        arr1.push(28)
        arr1.push(34)
        arr1.push(2)
        arr1.push(5)
        arr1.pop()
        arr1.pop()
        arr1.pop()
        self.assertEqual(arr1.peek(), 28)
        arr1.pop()
        arr1.pop()
        self.assertEqual(arr1.pop(), 4)
        self.assertEqual(arr1.num_items, 1)
        self.assertEqual(arr1.capacity, 4)

    def test_node(self):
        node1 = Node(1)
        node2 = Node(4, node1)
        self.assertEqual(node1.val, 1)
        self.assertEqual(node2.next, node1)

    def test_stack_linked(self):
        node1 = Node(8)
        node2 = Node(3, node1)
        node3 = Node(7, node2)
        stack1 = StackLinked(node3, 3)
        self.assertEqual(stack1.top, node3)
        self.assertEqual(stack1.num_items, 3)
        stack1.pop()
        self.assertEqual(stack1.size(), 2)
        stack1.pop()
        self.assertEqual(stack1.pop(), 8)
        self.assertRaises(IndexError, stack1.pop)
        self.assertTrue(stack1.is_empty())
        stack1.push(24)
        stack1.push(6)
        stack1.push(98)
        self.assertFalse(stack1.is_empty())
        self.assertEqual(stack1.peek(), 98)

if __name__ == '__main__':
    unittest.main()
