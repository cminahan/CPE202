# Lab 4
# Name: Claire Minahan
# Section: CPE202-03

""" QueueLinked class """

from node import*

class QueueLinked:
    """ a linked structure to implement Queue ADT
    Attributes:
        capacity(int): number of items the queue can hold
        num_items(int): number of items in the Queue
        front(Node): points to the front of the queue
        rear(Node): points to the back of the queue
    """

    def __init__(self, capacity=2, num_items=0, front=None, rear=None):
        self.capacity = capacity
        self.num_items = num_items
        self.front = front
        self.rear = rear

    def __repr__(self):
        return 'Items: %d, Front: %s, Rear: %s' % (self.num_items, self.front, self.rear)

    def __eq__(self, other):
        return isinstance(other, QueueLinked) \
               and self.capacity == other.capacity \
               and self.num_items == other.num_items \
               and self.front == other.front \
               and self.rear == other.rear

    def dequeue(self):
        """ Removes an item(Node) from the front of the list
        Args:
        Returns:
            val(int): value of the removed node or,
            error: raise IndexError
        """
        if self.num_items == 0:
            raise IndexError
        if self.num_items == 1:
            temp = self.front.val
            self.front = None
            self.rear = None
        else:
            temp = self.front.val
            self.front = self.front.next
        self.num_items -= 1
        return temp

    def enqueue(self, item):
        """ Adds an item to the back of the list
        Args:
            item(int): the value to be added
        Returns:
            none or,
            raises IndexError
        """
        if self.capacity == self.num_items:
            raise IndexError
        new_node = Node(item)
        if self.num_items == 0:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.num_items += 1

    def is_empty(self):
        """ returns True if the queue is empty
        Args:
        Returns:
            bool: True if empty, False otherwise
        """
        return self.num_items == 0

    def is_full(self):
        """ returns True if the queue if full
        Args:
        Returns:
            bool: True if full, False otherwise
        """
        return self.num_items == self.capacity

    def size(self):
        """ returns the number of items in the queue
        Args:
        Returns:
            int: number of items in the list
        """
        return self.num_items
