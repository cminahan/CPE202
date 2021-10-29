# Project1
# Name: Claire Minahan
# Section: CPE202-03

import unittest
from perm_gen_lex import*
from bear_picnic import*
from base_convert import*

class TestProject1(unittest.TestCase):

    def test_perm_gen_lex(self):
        answer_list = ['qrs', 'qsr', 'rqs', 'rsq', 'sqr', 'srq']
        self.assertEqual(perm_gen_lex('qrs'), answer_list)
        self.assertEqual(perm_gen_lex('a'), ['a'])
        self.assertEqual(perm_gen_lex(''), [])
        self.assertEqual(perm_gen_lex('xy'), ['xy', 'yx'])
        answer_list2 = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc',\
                        'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda',\
                        'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']
        self.assertEqual(perm_gen_lex('abcd'), answer_list2)

    def test_base_convert(self):
        self.assertEqual(convert(30, 4), '132')
        self.assertEqual(convert(45, 2), '101101')
        self.assertEqual(convert(316, 16), '13C')

    def test_bear_picnic(self):
        self.assertTrue(bears(42))
        self.assertFalse(bears(81))
        self.assertTrue(bears(84))
        self.assertFalse(bears(53))
        self.assertTrue(bears(1260))
        self.assertFalse(bears(41))
        self.assertFalse(bears(100))
        self.assertFalse(bears(51))

# Run the unittest
if __name__ == '__main__':
    unittest.main()

