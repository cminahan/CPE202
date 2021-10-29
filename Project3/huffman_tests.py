""" Project 3: Test Cases
Name: Claire Minahan
Course: CPE202-03
Instructor: Kuboi
"""

import unittest
import filecmp
from huffman_coding import*
from huffman import*

class TestProject3(unittest.TestCase):
    def test_huffman(self):
        huff_node = HuffmanNode(3, 'd')
        huff_node2 = HuffmanNode(8, 'u')
        self.assertEqual(print(huff_node), None)
        self.assertFalse(huff_node == huff_node2)

    def test_cnt_freq(self):
        freq_list = cnt_freq("file2.txt")
        ans_list = [0]*256
        ans_list[101:116] = [1, 0, 3, 1, 0, 0, 0, 0, 0, 0, 3, 1, 0, 1, 1]
        self.assertEqual(freq_list[101:116], ans_list[101:116])

    def test_create_huff_tree(self):
        freq_list = cnt_freq("file2.txt")
        huff_tree = create_huff_tree(freq_list)
        self.assertEqual(huff_tree.left.char, 'g')
        self.assertEqual(huff_tree.freq, 14)
        self.assertEqual(huff_tree.left.freq, 6)
        left = huff_tree.left
        self.assertEqual(left.right.freq, 3)
        self.assertEqual(left.right.char, 'o')
        freq_list2 = []
        self.assertEqual(create_huff_tree(freq_list2), None)
        freq_list3 = [0]*256
        freq_list3[89] = 7
        huff_tree3 = create_huff_tree(freq_list3)
        huff_node = HuffmanNode(7, 'Y')
        self.assertEqual(create_huff_tree(freq_list3), huff_node)

    def test_create_code(self):
        freqlist = cnt_freq("file3.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('s')], '111')
        self.assertEqual(codes[ord('t')], '00')
        self.assertEqual(codes[ord('a')], '010')
        freqlist2 = cnt_freq("file1.txt")
        hufftree2 = create_huff_tree(freqlist2)
        codes2 = create_code(hufftree2)
        self.assertEqual(codes2[ord('d')], '0')
        self.assertEqual(codes2[ord('a')], '11111')
        self.assertEqual(codes2[ord('f')], '1110')

    def test_huffman_encode(self):
        self.assertRaises(FileNotFoundError, huffman_encode, "test_gibberish.txt", "gibberish.txt")
        huffman_encode("test_encode.txt", "encode_ans.txt")
        self.assertTrue(filecmp.cmp("encode_ans.txt", "encode_soln.txt"))
        huffman_encode("test_encode2.txt", "encode_ans2.txt")
        self.assertTrue(filecmp.cmp("encode_ans2.txt", "encode_soln2.txt"))

    def test_huffman_decode(self):
        self.assertRaises(FileNotFoundError, huffman_decode, "test_gibberish.txt", "gibberish.txt")
        huffman_decode("test_compressed.txt", "test_decode.txt")
        self.assertTrue(filecmp.cmp("test_decode.txt", "decode_soln.txt"))
        huffman_decode("test_compressed2.txt", "test_decode2.txt")
        self.assertTrue(filecmp.cmp("test_decode2.txt", "decode_soln2.txt"))

if __name__ == '__main__':
    unittest.main()