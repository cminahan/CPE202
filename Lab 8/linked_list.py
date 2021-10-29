""" Lab 8: Implementing Hash Tables with different collision resoultions
Name: Claire Minahan
Course: CPE202-03
Instructor: Kuboi
"""

class LinkedList:
    ''' A Linked List is one of
    - None or
    - Node(val, next): A Linked list
    Attributes:
        val(any): the payload of any type
        next(Node): a Linked List
        key(any): a key
    '''

    def __init__(self, key, val, nxt=None):
        self.val = val
        self.key = key
        self.next = nxt

    def __repr__(self):
        return "(Key-val: %s-%s, Next: %s)" %(self.key, self.val, self.next)

    def __eq__(self, other):
        return isinstance(other, LinkedList)\
            and self.val == other.val\
            and self.next == other.next\
            and self.key == other.key


class Node:
    """ A Node
    Attributes:
        key(any): a key
        val(any): a value associated with the key
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __repr__(self):
        return "Key: %s, Val: %s"%(self.key, self.val)

    def __eq__(self, other):
        return isinstance(other, Node)\
                and self.key == other.key\
                and self.val == other.val
