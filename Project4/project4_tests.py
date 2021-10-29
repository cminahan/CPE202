""" Project 4:
Name: Claire Minahan
Course: CPE202-03
Instructor: Kuboi
"""

import unittest
from project4 import*

class TestProject4(unittest.TestCase):

    def test_project(self):
        stop_words = import_stopwords('stop_words.txt')
        shrek = SearchEngine('shrek', stop_words)
        self.assertEqual(shrek.read_file('shrek/shrek.txt'), ['Shrek', 'is', 'amaZing!'])
        self.assertEqual(shrek.parse_words(['Shrek', 'is', 'amaZing!']), ['shrek', 'amazing'])
        self.assertEqual(shrek.parse_words(['Get out of my swamp!!!']), ['swamp'])
        hey = [('shrek\\fairy_godmother_song.txt', 0.008547008547008548), ('shrek\\all_star.txt', 0.015552735058989069)]
        self.assertEqual(shrek.search('hey'), hey)
        self.assertTrue(shrek.term_freqs.contains('funkytown'))


if __name__ == '__main__':
    unittest.main()