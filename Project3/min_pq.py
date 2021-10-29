""" Project 3 -- Minimum Priority Queue
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
        self.num_items = len(self.arr)
        idx = index_parent(self.capacity - 1)
        while -1 < idx:
            self.shift_down(idx)
            idx -= 1

    def insert(self, item):
        """ inserts an item to the queue
            Args:
                item(any): an item to be inserted to the queue
        """
        if self.num_items == self.capacity:
            self.enlarge()
        if self.num_items == 0:
            self.arr[0] = item
            self.num_items += 1
            return
        self.arr[self.num_items] = item
        self.num_items += 1
        self.shift_up(self.num_items - 1)
        return

    def del_min(self) -> any:
        """ deletes the minimum item in the queue
            Returns:
                any: item removed from the queue
            Raises:
                IndexError: when queue is empty
        """
        if self.num_items == 0:
            raise IndexError
        min_item = self.arr[0]
        self.arr[0] = self.arr[self.num_items - 1]
        self.num_items -= 1
        self.shift_down(0)
        return min_item

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
        idx_parent = index_parent(idx)
        if idx_parent < 0 or self.arr[idx_parent] < self.arr[idx]:
            return None
        self.arr[idx_parent], self.arr[idx] = self.arr[idx], self.arr[idx_parent]
        return self.shift_up(idx_parent)

    def shift_down(self, idx):
        """ shifts down an item in the queue using tail recursion
        Args:
            idx(int): the index of the item to be shifted down in the array
        """
        end = self.num_items - 1
        if end - 1 < idx:
            return None
        min_index = index_minchild(self.arr, idx, end)

        if min_index is None or min_index < 0 or self.arr[idx] < self.arr[min_index]:
            return None
        self.arr[idx], self.arr[min_index] = self.arr[min_index], self.arr[idx]
        return self.shift_down(min_index)

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


def index_parent(index):
    """ computes the index of the parent node
    Args:
        index(int): index of the child node
    Returns:
        int: index of the parent node
    """
    return (index - 1) // 2


def index_left(index):
    """ computes the index of the left child
    Args:
        index(int): index of the node
    Returns:
        int: index of the left node
    """
    return (2*index) + 1


def index_right(index):
    """ computes the index of the right child
    Args:
        index(int): index of the node
    Returns:
        int: index of the right child
    """
    return (2*index) + 2


def index_minchild(items, index, end):
    """ computes the index of the child node with the min key value
    Args:
        items(list): a list of key values
        index(int): index of the node
        end(int): the last index of the heap
    Returns:
        int: index of the node with the min value
    """
    left = index_left(index)
    right = index_right(index)
    if left > end or left < 0:
        return None
    if right > end or right < 0:
        return left
    if items[left] < items[right]:
        return left
    return right
