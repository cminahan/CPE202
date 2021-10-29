# Lab 2
# Name: Claire Minahan
# Section: CPE202-03

class Node:
    ''' A node of a list
    Attributes:
        val(int): the payload
        next(Node): the next item in the list
        prev(Node): the previous item in the list
    '''
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return "Node(%s, %s)" %(self.val, self.next)

    def __eq__(self, other):
        return isinstance(other, Node)\
            and self.val == other.val\


class OrderedList:
    ''' An ordered list
    Attributes:
         head(Node): a pointer to the head of the list
         tail(Node): a pointer to the tail of the list
         num_items(int): the number of items stored in the list
    '''
    def __init__(self, head=None, tail=None, num_items=None):
        self.head = head
        self.tail = tail
        self.num_items = num_items

    def __repr__(self):
        return "OD: num_items:%d, head:%s, tail:%s"%(self.num_items, self.head, self.tail)

    def __eq__(self, other):
        return isinstance(other, OrderedList)\
            and self.head == other.head\
            and self.tail == other.tail\
            and self.num_items == other.num_items

    def add(self, item):
        ''' Adds a new item(int) to the list making sure the order is preserved
        Args:
             item(int): the value to be added to the list
        Returns:
            None
        '''
        return self.add_helper(self.head, item)

    def add_helper(self, node, item):
        ''' a helper function for adding an item
        Args:
            node(Node): a node
        Returns:
            none(None)
        '''
        if self.num_items is None or self.num_items == 0:
            new_node = Node(item, None, None)
            self.head = new_node
            self.num_items = 1
            self.tail = new_node
            return None
        if node is self.tail and node.val < item:
            node_new = Node(item, None, node)
            node.next = node_new
            self.tail = node_new
            self.num_items += 1
            return None
        if item < node.val and node is self.head:
            new_node = Node(item, node, None)
            node.prev = new_node
            self.head = new_node
            self.num_items += 1
            return None
        if node.val < item < node.next.val:
            new_node = Node(item, node.next, node)
            node.next = new_node
            new_node.next.prev = new_node
            self.num_items += 1
            return None
        return self.add_helper(node.next, item)

    def remove(self, item):
        ''' Removes the item from the list
        Args:
             item(int): the value to be removed from the list
        Returns:
            int: position of the removed item
            error: raise ValueError
        '''
        return self.remove_helper(self.head, item, 0)

    def remove_helper(self, node, item, pos):
        ''' a helper function for removing an item
        Args:
            node(Node): a node
            int(item): a value to remove in the list
        Returns:
            int: position of the removed item, or
            error: raise ValueError
        '''
        if node.val == item:
            if self.num_items == 1:
                self.tail = None
                self.head = None
            elif self.head == node:
                node.next.prev = None
                self.head = node.next
            elif self.tail == node:
                node.prev.next = None
                self.tail = node.prev
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.num_items -= 1
            return pos
        if node.next is None:
            raise ValueError()
        return self.remove_helper(node.next, item, pos + 1)

    def search_forward(self, item):
        ''' Searches a specified item in the list starting from the head
        Args:
            item(int): the value to be searched in the list
        Returns:
            bool: True if found, False otherwise
        '''
        return self.search_forward_helper(self.head, item)

    def search_forward_helper(self, node, item):
        ''' a helper function for searching an item forward
        Args:
            node(Node): a node
            int(item): a value to search for in the list
        Returns:
            bool: True if found, False otherwise
        '''
        if node is None:
            return False
        if node.val == item:
            return True
        return self.search_forward_helper(node.next, item)

    def search_backward(self, item):
        ''' Searches a specified item in the list starting from the tail
        Args:
            item(int): the value to be searched in the list
        Returns:
            bool: True if found, False otherwise
        '''
        return self.search_backward_helper(self.tail, item)

    def search_backward_helper(self, node, item):
        ''' a helper function for searching an item backward
        Args:
            node(Node): a node
            int(item): a value to search for in the list
        Returns:
            bool:True if found, False otherwise
        '''
        if node is None:
            return False
        if node.val == item:
            return True
        return self.search_backward_helper(node.prev, item)

    def is_empty(self):
        ''' Tests to see whether the list is empty
        Args:
             none
        Returns:
            bool: True if list is empty, False otherwise
        '''
        if self.num_items is None or self.num_items == 0:
            return True
        return False

    def size(self):
        ''' Returns the number of items in the list
        Args:
            none
        Returns:
            int: number of items in the list
        '''
        if self.num_items is None:
            return 0
        return self.num_items

    def index(self, item):
        ''' Finds the position of the item in the list
        Args:
            item(int): the item to search for
        Returns:
            int: the position of the item, or
            error: raises valueError
        '''
        if self.num_items is None or self.num_items == 0:
            raise ValueError
        return self.index_helper(self.head, item, 0)

    def index_helper(self, node, item, pos):
        ''' a helper function for index
        Args:
            node(Node): a node
            int(item): the value searching for
        Returns:
            int: the position of the item, or
            error: raises valueError
        '''
        if node is self.tail and node.val is not item:
            raise ValueError()
        if node.val == item:
            return pos
        return self.index_helper(node.next, item, pos + 1)

    def pop(self, pos=None):
        ''' Removes an item from a list at position pos, or from the tail
            if no argument is passed
            Args:
                pos(int): position
            Returns:
                int(item): item in applicable position
        '''
        if pos is None:
            return self.pop_none_helper(self.tail)
        if pos >= self.num_items or self.num_items is None:
            raise IndexError()
        if pos <= self.num_items//2:
            return self.first_pops_helper(self.head, pos, 0)
        return self.second_pops_helper(self.tail, pos, self.num_items - 1)

    def pop_none_helper(self, node):
        ''' a helper function for pop, if pos is none
        Args:
            node(Node): a node
        Returns:
            int: item as last position
        '''
        if self.num_items is None or self.num_items == 0:
            raise IndexError()
        if self.num_items == 1:
            val_return = node.val
            self.head = None
            self.tail = None
            self.num_items = 0
            return val_return
        val_return = node.val
        node.prev.next = None
        self.tail = node.prev
        self.num_items -= 1
        return val_return

    def first_pops_helper(self, node, pos, node_pos):
        ''' a helper function for pops, starting at the head
        Args:
            node(Node): a node
            pos(int): a position in the list
        Returns:
            int: item at the position
        '''
        if node_pos == pos and node == self.head:
            node_return = node.val
            node.next.prev = None
            self.head = node.next
            self.num_items -= 1
            return node_return
        if node_pos == pos:
            node_return = node.val
            node.prev.next = node.next
            node.next.prev = node.prev
            self.num_items -= 1
            return node_return
        return self.first_pops_helper(node.next, pos, node_pos + 1)

    def second_pops_helper(self, node, pos, node_pos):
        ''' a helper function for pops, starting at the tail
        Args:
            node(Node): a node
            pos(int): a position in the list
        Returns:
            int: item at the position
        '''
        if node_pos == pos and node == self.tail:
            val_return = node.val
            node.prev.next = None
            self.tail = node.prev
            self.num_items -= 1
            return val_return
        if node_pos == pos:
            node_val = node.val
            node.prev.next = node.next
            node.next.prev = node.prev
            self.num_items -= 1
            return node_val
        return self.second_pops_helper(node.prev, pos, node_pos - 1)
