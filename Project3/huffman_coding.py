""" Project 3: Huffman Encoding
Name: Claire Minahan
Course: CPE202-03
Instructor: Kuboi
"""

from min_pq import*
from huffman import*
from huffman_bit_writer import*
from huffman_bit_reader import*

def cnt_freq(filename):
    """ opens a text file and counts the frequency of all occurrences of characters within the file
    Args:
        filename(file): a text file
    Returns:
        list: 256 item list with counts of occurrences
    """
    counts = [0]*256
    fin = open(filename, 'r')
    counts[0] = 1
    for line in fin:
        for char in line:
            counts[ord(char)] += 1
    fin.close()
    return counts

def create_huff_tree(list_of_freqs):
    """ creates a huffman tree of a list of frequencies
    Args:
        list_of_freqs(list): a list of frequencies for each character
    Returns:
        node: the root huffman node
    """
    min_pq = MinPQ()
    for index in range(len(list_of_freqs)):
        if list_of_freqs[index] != 0:
            huffman_node = HuffmanNode(list_of_freqs[index], chr(index))
            min_pq.insert(huffman_node)
    if len(min_pq.arr) == 0:
        return None
    if len(min_pq.arr) == 1:
        return min_pq.arr[0]
    while min_pq.num_items > 1:
        huffman_1 = min_pq.del_min()
        huffman_2 = min_pq.del_min()
        parent_freq = huffman_1.freq + huffman_2.freq
        if ord(huffman_1.char) < ord(huffman_2.char):
            parent_char = huffman_1.char
        else:
            parent_char = huffman_2.char
        parent_node = HuffmanNode(parent_freq, parent_char, huffman_1, huffman_2)
        min_pq.insert(parent_node)
    return min_pq.arr[0]

def create_code(root_node):
    """ traverses the tree and returns an array of strings
    Args:
        root_node(node): a HuffmanNode
    Returns:
        list: a list of strings
    """
    code_array = ['']*256
    code_helper(root_node, '', code_array)
    return code_array

def code_helper(node, code, list_code):
    """ a helper function for create_code
    Args:
        node(node): a Huffman node
        list_code(list): list of codes
        code(str): the code to reach the char in the tree
    """
    if node.left is None and node.right is None:
        list_code[ord(node.char)] = code
    else:
        code_helper(node.left, code + '0', list_code)
        code_helper(node.right, code + '1', list_code)

def huffman_encode(in_file, out_file):
    """ reads an input text file and writes to an output file
    Args:
         in_file():
         out_file():
    """
    fin = open(in_file, 'r')
    fout = open(out_file, 'w', newline='')
    freq_list = cnt_freq(in_file)
    tree = create_huff_tree(freq_list)
    code = create_code(tree)
    header = create_header(freq_list)
    write = ''
    for line in fin:
        for item in line:
            write += code[ord(item)]
    fout.write(header)
    fout.write(write)
    new_out_file = out_file[: len(out_file)-4]
    new_out_file += '_compressed'
    new_out_file += out_file[len(out_file) - 4:len(out_file)]
    bit_writer = HuffmanBitWriter(new_out_file)
    bit_writer.write_str(header)
    bit_writer.write_code(write)
    bit_writer.write_code(code[0])
    fin.close()
    fout.close()
    bit_writer.close()

def create_header(list_of_freqs):
    """ creates the header
    Args:
        list_of_freqs(list): list of frequencies of characters
    Returns:
        str: header
    """
    header = ''
    for index in range(len(list_of_freqs)):
        if list_of_freqs[index] != 0:
            header += str(index)
            header += ' '
            header += str(list_of_freqs[index])
            header += ' '
    header += "\n"
    return header

def huffman_decode(encoded_file, decode_file):
    """ reads an encoded text file
    Args:
        encoded_file(str): file
        decode_file(str): file
    """
    fout = open(decode_file, "w")
    bit_reader = HuffmanBitReader(encoded_file)
    list_freq = parse_header(bit_reader.read_str())
    huff_tree = create_huff_tree(list_freq)
    new_string = ''
    sum_freq = 0
    for num in list_freq:
        sum_freq += int(num)
    sum_freq -= 1
    while sum_freq > 0:
        char = decode_helper(bit_reader, huff_tree)
        new_string += char
        sum_freq -= 1
    fout.write(new_string)
    fout.close()
    bit_reader.close()

def decode_helper(bit_reader, tree):
    """ a helper function for huffman_decode
    Args:
         bit_reader(node): a HuffmanBitReader object
         tree(node): a HuffmanTree object
    Returns:
        str: a character
    """
    while tree.left is not None and tree.right is not None:
        bit = bit_reader.read_bit()
        if bit is False:
            left = tree.left
            return decode_helper(bit_reader, left)
        right = tree.right
        return decode_helper(bit_reader, right)
    return tree.char

def parse_header(header_string):
    """ creates a header for huffman_decode
    Args:
        header_string(str): a string
    Returns:
        str: the header
    """
    header = header_string.decode('utf8')
    head = header.split()
    new_array = [0]*256
    for index in range(len(head) - 1):
        if index % 2 == 0:
            array_index = int(head[index])
            array_input = int(head[index + 1])
            new_array[array_index] = array_input
    return new_array
