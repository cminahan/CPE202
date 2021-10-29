""" Lab 8: Implementing Hash Tables with different Collision Resolutions
Name: Claire Minahan
Course: CPE202-03
Instructor: Kuboi
"""

import unittest
from hashtables import *


class TestLab8(unittest.TestCase):

    def test_separate_chaining(self):
        hash_sep = HashTableSepchain()
        hashtable = import_stopwords("stop_words.txt", hash_sep)
        self.assertEqual(hashtable.slots, 383)
        self.assertEqual(hashtable.num_items, 305)
        ht = HashTableSepchain()
        self.assertFalse(ht == hashtable)
        self.assertEqual(print(hashtable), None)
        node = LinkedList('eleven', 'eleven')
        self.assertEqual(hashtable.get('eleven'), node.val)
        self.assertRaises(KeyError, hashtable.get, 'unicorn')
        self.assertTrue(hashtable.contains('thereafter'))
        self.assertEqual(hashtable.__getitem__('under'), 'under')
        self.assertFalse(hashtable.contains('championship'))
        node_1 = Node('whereby', 'whereby')
        self.assertEqual(hashtable.remove('whereby'), node_1)
        self.assertRaises(KeyError, hashtable.remove, 'computer')
        hashtable.remove('done')
        hashtable.remove('go')
        hashtable.remove('also')
        self.assertFalse(hashtable.contains('whereby'))
        self.assertEqual(hashtable.size(), 301)
        self.assertEqual(hashtable.load_factor(), 0.79)
        self.assertEqual(hashtable.collisions(), 89)
        self.assertEqual(hashtable.put('microphone', 'microphone'), None)
        hashtable.__setitem__('guitar', 'guitar')
        self.assertTrue(hashtable.__contains__('guitar'))
        sep_table = HashTableSepchain()
        for i in range(34):
            sep_table.put(chr(i), i)
        self.assertEqual(sep_table.put(chr(20), 20), None)
        self.assertEqual(sep_table.size(), 34)
        node_2 = Node('everyone', 'everyone')
        self.assertEqual(hashtable.remove('everyone'), node_2)

    def test_linear_probing(self):
        hash_lin = HashTableLinear()
        hashtable = import_stopwords("stop_words.txt", hash_lin)
        self.assertEqual(print(hashtable), None)
        lin_table = HashTableLinear()
        lin_table.__setitem__('train', 7)
        self.assertFalse(hashtable == lin_table)
        self.assertEqual(hashtable.__getitem__('moreover'), 'moreover')
        self.assertEqual(hashtable.num_items, 305)
        self.assertEqual(hashtable.slots, 767)
        self.assertEqual(hashtable.get('often'), 'often')
        self.assertRaises(KeyError, hashtable.get, 'donkey')
        self.assertFalse(hashtable.contains('wizard'))
        self.assertTrue(hashtable.contains('twenty'))
        self.assertTrue(lin_table.__contains__('train'))
        node = Node('throughout', 'throughout')
        self.assertEqual(hashtable.remove('throughout'), node)
        self.assertFalse(hashtable.contains('throughout'))
        self.assertEqual(hashtable.size(), 304)
        self.assertRaises(KeyError, hashtable.remove, 'diamond')
        load = hashtable.num_items / hashtable.slots
        self.assertEqual(hashtable.load_factor(), load)
        self.assertEqual(hashtable.put('throughout', 'dog'), None)
        self.assertEqual(hashtable.get('throughout'), 'dog')
        self.assertEqual(hashtable.collisions(), hashtable.num_collisions)
        hashtable.remove('former')
        hashtable.remove('if')
        hashtable.remove('beyond')

    def test_quadratic_probing(self):
        hash_quad = HashTableQuadratic()
        hashtable = import_stopwords("stop_words.txt", hash_quad)
        prob_table = HashTableQuadratic()
        self.assertEqual(print(prob_table), None)
        self.assertTrue(prob_table != hashtable)
        self.assertEqual(hashtable.num_items, 305)
        self.assertTrue(hashtable.slots == 543)
        self.assertEqual(hashtable.get('hereupon'), 'hereupon')
        self.assertRaises(KeyError, hashtable.get, 'university')
        self.assertTrue(hashtable.contains('while'))
        node = Node('while', 'while')
        self.assertEqual(hashtable.remove('while'), node)
        self.assertRaises(KeyError, hashtable.remove, 'while')
        self.assertEqual(hashtable.size(), 304)
        self.assertFalse(hashtable.contains('while'))
        self.assertFalse(hashtable.contains('university'))
        self.assertEqual(hashtable.__getitem__('last'), 'last')
        load = hashtable.num_items / hashtable.slots
        self.assertEqual(hashtable.load_factor(), load)
        self.assertEqual(hashtable.collisions(), hashtable.num_collisions)
        self.assertEqual(hashtable.__setitem__('honey', 'honey'), None)
        self.assertTrue(hashtable.__contains__('honey'))


if __name__ == '__main__':
    unittest.main()
