# Lab 3
# Name: Claire Minahan
# Section: CPE202-03

class StackArray:
    """ an array
    Attributes:
        arr(list): a list of items
        capacity(int): number of spots in arr
        num_items(int): number of items stored in the list
    """

    def __init__(self, arr=[None] * 2, capacity=2, num_items=0):
        self.arr = arr
        self.capacity = capacity
        self.num_items = num_items

    def __repr__(self):
        return "Stack: %s, Capacity: %d, Items: %d" % (self.arr, self.capacity, self.num_items)

    def __eq__(self, other):
        return isinstance(other, StackArray) \
               and self.arr == other.arr \
               and self.capacity == other.capcity \
               and self.num_items == other.num_items

    def enlarge(self):
        """ enlarges the size of the list by 2
        Args:
            none
        Returns:
            none
        """
        self.capacity = self.capacity * 2
        new_array = [None] * self.capacity
        new_num_items = 0
        for index in range(self.num_items):
            new_array[index] = self.arr[index]
            new_num_items += 1
        self.arr = new_array
        self.num_items = new_num_items
        return None

    def shrink(self):
        """ reduce the size of the array by a factor of 2
        Args:
        Returns:
            none
        """
        self.capacity = self.capacity // 2
        new_array = [None] * self.capacity
        new_num_items = 0
        for index in range(self.num_items):
            new_array[index] = self.arr[index]
            new_num_items += 1
        self.arr = new_array
        self.num_items = new_num_items
        return None

    def pop(self):
        """ removes the top item from the stack
        Args:
        Returns:
            item(int): the item removed from the array, or
            error: raise IndexError
        """
        if self.is_empty():
            raise IndexError
        if self.capacity / self.num_items >= 4:
            self.shrink()
        removed_item = self.arr[self.num_items - 1]
        self.arr[self.num_items - 1] = None
        self.num_items -= 1
        return removed_item

    def push(self, item):
        """ adds a new item to the top of the stack
        Args:
            int(item): the item to be added to the stack
        Returns:
            none
        """
        if self.capacity == self.num_items:
            self.enlarge()
        index = self.num_items
        self.arr[index] = item
        self.num_items += 1
        return None

    def peek(self):
        """ returns the top item from the stack but does not remove it
        Args:
        Returns:
            item(int): the item from the top of the stack
        """
        if self.num_items == 0:
            raise IndexError
        return self.arr[self.num_items - 1]

    def is_empty(self):
        """ tests to see whether the stack is empty
        Args:
        Returns:
            bool: True if empty, False otherwise
        """
        return self.num_items == 0

    def size(self):
        """ returns the number of items in the stack
        Args:
        Returns:
            num_items(int): number of items in the list
        """
        return self.num_items
