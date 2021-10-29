# Lab 4
# Name: Claire Minahan
# Section: CPE202-03

""" QueueArray class """

class QueueArray:
    """ circular array for storing items in the queue
    Attributes:
        arr(list): built-in list data construct
        capacity(int): the size of the array
        num_items(int): number of items in the queue
        front(int): index of the front of the queue
        rear(int): index of the back of the queue
    """

    def __init__(self, capacity=2, num_items=0, front=0, rear=0):
        self.capacity = capacity
        self.num_items = num_items
        array = [None] * (self.capacity + 1)
        self.arr = array
        self.read = front
        self.write = rear

    def __repr__(self):
        return '%s, Capacity: %d' % (self.arr, self.capacity)

    def __eq__(self, other):
        return isinstance(other, QueueArray) \
               and self.arr == other.arr \
               and self.capacity == other.capacity

    def dequeue(self):
        """ removes an item from the front of the list
        Args:
        Returns:
            int: value of removed item or,
            error: raises IndexError
        """
        if self.read == self.write:
            raise IndexError
        temp = self.arr[self.read]
        self.read += 1
        self.read %= len(self.arr)
        self.num_items -= 1
        return temp

    def enqueue(self, item):
        """ adds an item to the back of the list
        Args:
             item(int): item to be added to the list
        Returns:
            none
        """
        if self.read == (self.write + 1) % (len(self.arr)):
            raise IndexError
        self.arr[self.write] = item
        self.write += 1
        self.write %= len(self.arr)
        self.num_items += 1

    def is_empty(self):
        """ returns True if the queue is empty
        Args:
        Returns:
            bool: True if empty, False otherwise
        """
        return self.read == self.write

    def is_full(self):
        """ returns True if the queue is full
        Args:
        Returns:
            bool: True if full, False otherwise
        """
        return self.read == (self.write + 1) % (len(self.arr))

    def size(self):
        """ returns the number of items in the queue
        Args:
        Returns:
            int: number of items in the queue
        """
        return self.num_items
