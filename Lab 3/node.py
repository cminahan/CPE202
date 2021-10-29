# Lab 3
# Name: Claire Minahan
# Section: CPE202-03

class Node:
    ''' A Linked List is one of
    - None or
    - Node(val, next): A Linked list
    Attributes:
        val(any): the payload of any type
        next(Node): a Linked List
    '''

    def __init__(self, val, nxt=None):
        self.val = val #the payload
        self.next = nxt #a reference to the next node

    def __repr__(self):
        return "(%s, %s)" %(self.val, self.next)

    def __eq__(self, other):
        return isinstance(other, Node)\
            and self.val == other.val\
            and self.next == other.next
