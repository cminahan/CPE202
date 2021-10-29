""" Lab 7 -- Minimum Priority Queue
Name: Claire Minahan
Course: CPE202-03
Instructor: Kuboi
"""


class MinPQ:
    """ Minimum Priority Queue
    Attributes:
        capacity(int): the capacity of the queue
                       the default capacity is 2, but will be increased automatically
        num_items(int): the number of items in the queue
                        this also points to the position where a new item will be added
            arr(list): an array which contains the items in the queue
    """

    def __init__(self, arr=None):
        if arr is None:
            self.arr = [None] * 2
            self.capacity = 2
            self.num_items = 0
        else:
            self.arr = arr
            self.heapify()

    def heapify(self):
        """ convert the array, self.arr, into a min heap """
        self.capacity = len(self.arr)
        self.num_items = len(self.arr) - 1
        new_pq = MinPQ()
        for item in self.arr:
            new_pq.insert(item)
        self.arr = new_pq.arr
        self.num_items = self.capacity

    def insert(self, item):
        """ inserts an item to the queue
        Args:
            item(any): an item to be inserted to the queue
        """
        if self.num_items == self.capacity:
            self.enlarge()
        if self.num_items == 0:
            self.arr[0] = item
        else:
            new_array = [None] * self.capacity
            new_array[0] = item
            for index in range(self.num_items):
                new_array[index + 1] = self.arr[index]
            self.arr = new_array
            self.shift_up(0)
        self.num_items += 1

    def del_min(self) -> any:
        """ deletes the minimum item in the queue
        Returns:
            any: item removed from the queue
        Raises:
            IndexError: when queue is empty
        """
        if self.num_items == 0:
            raise IndexError
        return_value = self.arr[0]
        self.shift_down(0)
        if self.capacity > 2 and self.num_items and self.capacity >= self.num_items * 4:
            self.shrink()
        self.num_items -= 1
        return return_value

    def min(self) -> any:
        """ returns the minimum item in the queue without deleting it
        Returns:
            any: the minimum item in the queue
        Raises:
            IndexError: when the queue is empty
        """
        if self.num_items == 0:
            raise IndexError
        return self.arr[0]

    def is_empty(self) -> bool:
        """ checks if the queue is empty
        Returns:
             bool: True if empty, False otherwise
        """
        return self.num_items == 0

    def size(self) -> int:
        """ returns the number of items in the queue
        Returns:
            int: self.num_items
        """
        return self.num_items

    def shift_up(self, idx):
        """ shifts up an item in the queue using tail recursion
        Args:
            idx(int): the index of the item to be shifted up in the array
        """
        if idx == self.num_items:
            return
        temp = self.arr[idx]
        if self.arr[idx + 1] < temp:
            self.arr[idx] = self.arr[idx + 1]
            self.arr[idx + 1] = temp
            self.shift_up(idx + 1)

    def shift_down(self, idx):
        """ shifts down an item in the queue using tail recursion
        Args:
             idx(int): the index of the item to be shifted down in the array
        """
        if idx < self.num_items - 1:
            self.arr[idx] = self.arr[idx + 1]
            self.shift_down(idx + 1)

    def enlarge(self):
        """ enlarges the array """
        self.capacity *= 2
        new_array = [None] * self.capacity
        for index in range(self.num_items):
            new_array[index] = self.arr[index]
        self.arr = new_array

    def shrink(self):
        """ shrinks the array """
        self.capacity //= 2
        new_array = [None] * self.capacity
        for index in range(self.num_items):
            new_array[index] = self.arr[index]
        self.arr = new_array
