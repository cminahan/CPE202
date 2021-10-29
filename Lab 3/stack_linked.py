# Lab 3
# Name: Claire Minahan
# Section: CPE202-03

from node import*

class StackLinked:
    ''' a stackedLinked list
    Attributes:
        top(node): the node at the top of the stack
        num_items(int): number of nodes in the stack
    '''
    def __init__(self, top=0, num_items=0):
        self.top = top
        self.num_items = num_items

    def __repr__(self):
        return "top: %s, items: %d" %(self.top, self.num_items)

    def __eq__(self, other):
        return isinstance(other, StackLinked)\
            and self.top == other.top\
            and self.num_items == other.num_items

    def push(self, item):
        ''' adds a new node to the top of the stack
        Args:
            item(int): the val of the node to be added to the stack
        Returns:
            none
        '''
        new_node = Node(item)
        if self.num_items == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.num_items += 1
        return None

    def pop(self):
        ''' removes the top node from the stack
        Args:
            none
        Returns:
            node(Node): the node removed, or
            raise: IndexError
        '''
        if self.is_empty():
            raise IndexError
        return_val = self.top.val
        self.top = self.top.next
        self.num_items -= 1
        return return_val

    def peek(self):
        ''' returns the top item from the stack without removing it
        Args:
            none
        Returns:
            node(Node): the top item from the stack, or
            raise: IndexError
        '''
        if self.is_empty():
            raise IndexError
        return self.top.val

    def is_empty(self):
        ''' tests to see whether the stack is empty
        Args:
            none
        Returns:
            bool: True if empty, False otherwise
        '''
        return self.num_items == 0

    def size(self):
        ''' returns the number of items in the stack
        Args:
            none
        Returns:
            num_items(int): the number of items in the stack
        '''
        return self.num_items
