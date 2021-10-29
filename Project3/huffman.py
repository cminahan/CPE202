""" Project 3: Huffman Encoding
Name: Claire Minahan
Course: CPE202-03
Instructor: Kuboi
"""

class HuffmanNode:
    """ a leaf or internal node of a Huffman tree
    Attributes:
        char(char): for storing a character
        freq(int): the character's frequency
        left(node): pointer to the left node
        right(node): pointer to the right node
    """

    def __init__(self, frequency, char=None, left=None, right=None):
        self.char = char
        self.freq = frequency
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Char: %s, Freq: %d, Left: %s, Right: %s'\
               %(self.char, self.freq, self.left, self.right)

    def __eq__(self, other):
        return isinstance(other, HuffmanNode) and\
                self.char == other.char and\
                self.freq == other.freq and\
                self.left == other.left and\
                self.right == other.right

    def __lt__(self, other):
        """ returns True if self should come before other
        when added to the Min Priority Queue, and False otherwise
        Args:
            other(node): a HuffmanNode
        Returns:
            bool: true if self should come before other, false otherwise
        """
        if self.freq < other.freq:
            return True
        if other.freq < self.freq:
            return False
        if ord(self.char) < ord(other.char):
            return True
        return False
