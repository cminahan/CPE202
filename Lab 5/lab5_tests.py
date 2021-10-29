# Lab 5 Tests
# Claire Minahan
# CPE202

import unittest
from classmate import*
from bst import*
from tree_map import*

class TestLab5(unittest.TestCase):

    def test_bst(self):
        pass

    def test_tree_map(self):
        thing = BSTNode(4, 'happy', None, None)
        self.assertEqual(print(thing), None)
        class_treeMap = import_classmates("classmates.tsv")
        self.assertEqual(class_treeMap.num_items, 52)
        student1 = class_treeMap.get(32)
        self.assertRaises(KeyError, search_classmate, class_treeMap, 87)
        self.assertEqual(search_classmate(class_treeMap, 32), student1)
        treeMap = TreeMap()
        self.assertFalse(treeMap == class_treeMap)
        self.assertEqual(treeMap.num_items, 0)
        self.assertRaises(KeyError, treeMap.delete, 13)
        self.assertRaises(ValueError, treeMap.find_max)
        self.assertRaises(ValueError, treeMap.find_min)
        self.assertEqual(treeMap.tree_height(), -1)
        treeMap.__setitem__(8, 'dog')
        treeMap.__setitem__(9, 'alligator')
        self.assertEqual(treeMap.size(), 2)
        treeMap.__setitem__(4, 'cat')
        treeAnswer = TreeMap()
        treeAnswer.__setitem__(8, 'dog')
        treeAnswer.__setitem__(4, 'cat')
        self.assertEqual(treeMap.__getitem__(4), 'cat')
        treeAnswer.__setitem__(1, 'hop')
        self.assertEqual(treeMap.delete(9), treeAnswer.delete(1))
        treeMap.__setitem__(12, 'bird')
        treeAnswer.put(4, 'kangaroo')
        self.assertEqual(treeAnswer.get(4), 'kangaroo')
        self.assertEqual(treeMap.num_items, 3)
        self.assertTrue(treeMap.__contains__(12))
        self.assertFalse(treeMap.__contains__(1))
        self.assertEqual(treeMap.get(4), 'cat')
        self.assertRaises(KeyError, treeMap.get, 5)
        self.assertEqual(treeMap.get(8), 'dog')
        self.assertEqual(treeMap.get(12), 'bird')
        self.assertEqual(treeMap.inorder_list(), [4, 8, 12])
        self.assertEqual(treeMap.preorder_list(), [8, 4, 12])
        treeMap.put(10, 'snake')
        treeMap.put(6, 'rat')
        treeMap.put(14, 'bunny')
        treeMap.put(2, 'fish')
        self.assertEqual(treeMap.find_min(), (2, 'fish'))
        self.assertEqual(treeMap.find_max(), (14, 'bunny'))
        self.assertEqual(treeMap.tree_height(), 2)
        list_answer = [(6, 'rat'), (8, 'dog'), (10, 'snake')]
        self.assertEqual(treeMap.range_search(6, 12), list_answer)
        new_tree = treeMap

if __name__ == '__main__':
    unittest.main()