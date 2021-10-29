# Lab 2
# Name: Claire Minahan
# Section: CPE202-03

import unittest
from ordered_list import*

class TestLab2(unittest.TestCase):

    def test_Node(self):
        node1 = Node(0, None, None)
        node2 = Node(1, None, node1)
        node1.next = node2
        self.assertEqual(node1.val, 0)
        self.assertEqual(node2.val, 1)
        self.assertEqual(node1.next, node2)
        self.assertEqual(node2.next, None)
        self.assertEqual(node1.prev, None)
        self.assertEqual(node2.prev, node1)
        self.assertEqual(print(node1), None)

    def test_ordered_list(self):
        node1 = Node(0, None, None)
        node2 = Node(1, None, node1)
        node1.next = node2
        orderList1 = OrderedList(node1, node2, 2)
        self.assertEqual(orderList1.tail, node2)
        self.assertEqual(orderList1.head, node1)
        self.assertEqual(orderList1.num_items, 2)
        self.assertEqual(print(orderList1), None)

        order_list = OrderedList()
        order_list.add(9)
        self.assertEqual(order_list.head.val, 9)
        self.assertEqual(order_list.tail.val, 9)
        order_list.add(12)
        order_list.add(11)
        self.assertEqual(order_list.head.val, 9)
        self.assertEqual(order_list.tail.val, 12)
        order_list.add(3)
        order_list.add(27)
        self.assertEqual(order_list.num_items, 5)
        self.assertFalse(orderList1 == order_list)

        # testing remove
        self.assertEqual(order_list.remove(9), 1)
        self.assertEqual(order_list.remove(3), 0)
        self.assertEqual(order_list.remove(27), 2)
        self.assertRaises(ValueError, order_list.remove, 15)

        # testing search methods
        order_list.add(17)
        order_list.add(4)
        self.assertTrue(order_list.search_forward(11))
        self.assertFalse(order_list.search_forward(27))
        self.assertFalse(order_list.search_backward(2))
        self.assertTrue(order_list.search_backward(12))

        # testing empty and size
        orderList1.remove(0)
        orderList1.remove(1)
        orderList3 = OrderedList()
        self.assertFalse(order_list.is_empty())
        self.assertTrue(orderList1.is_empty())
        self.assertEqual(orderList1.size(), 0)
        self.assertEqual(orderList3.size(), 0)
        self.assertEqual(order_list.size(), 4)

        # testing index
        self.assertEqual(order_list.index(4), 0)
        self.assertEqual(order_list.index(12), 2)
        order_list.add(8)
        self.assertEqual(order_list.index(17), 4)
        self.assertRaises(ValueError, order_list.index, 19)
        self.assertRaises(ValueError, orderList1.index, 12)

        # testing pop
        self.assertEqual(order_list.pop(), 17)
        self.assertEqual(order_list.num_items, 4)
        self.assertEqual(order_list.tail.val, 12)
        order_list.add(1)
        self.assertEqual(order_list.pop(4), 12)
        self.assertEqual(order_list.pop(2), 8)
        self.assertEqual(order_list.pop(0), 1)
        self.assertRaises(IndexError, orderList1.pop)
        self.assertRaises(IndexError, order_list.pop, 2)
        orderList3.add(78)
        self.assertEqual(orderList3.pop(), 78)
        orderList3.add(1)
        orderList3.add(2)
        orderList3.add(3)
        orderList3.add(9)
        orderList3.add(7)
        self.assertEqual(orderList3.pop(3), 7)

if __name__ == '__main__':
    unittest.main()
    