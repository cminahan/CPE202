""" Lab 8: Implementing Hash Tables with
    different Collision Resolutions
Name: Claire Minahan
Course: CPE202-03
Instructor: Kuboi
"""

from linked_list import*

class HashTableSepchain:
    """ implements separate chaining
    Attributes:
        slots(int): the size of the table
        table(list): the Hash table
        num_collisions(int): the number of collisions
        num_items(int): number of items in the table
    """
    def __init__(self, table_size=11):
        self.slots = table_size
        self.table = [None]*table_size
        self.num_collisions = 0
        self.num_items = 0

    def __repr__(self):
        return '%s  Collisions: %d'%(self.table, self.num_collisions)

    def __eq__(self, other):
        return isinstance(other, HashTableSepchain) and\
                self.slots == other.slots and\
                self.table == other.table and\
                self.num_collisions == other.num_collisions and\
                self.num_items == other.num_items

    def __getitem__(self, key):
        """ for getting a value with [] """
        return self.get(key)

    def __setitem__(self, key, val):
        """ for enabling value assignment with [] """
        return self.put(key, val)

    def __contains__(self, key):
        """ for enabling in operator in our Hash Tables """
        return self.contains(key)

    def put(self, key, data):
        """ insert key-value pair into the hash table
        Args:
            key(str): a key
            data(str): an item
        """
        if self.load_factor() >= 1.5:
            self.resize(self.table)
        pair = LinkedList(key, data)
        hash_idx = hash_string(key, self.slots)
        if self.table[hash_idx] is None:
            self.table[hash_idx] = pair
            self.num_items += 1
            return
        self.num_collisions += 1
        link = self.table[hash_idx]
        while link.next is not None and link.key != key:
            link = link.next
        if link.key == key:
            link.val = data
            return
        self.num_items += 1
        link.next = pair
        return

    def resize(self, table):
        """ enlarge the size of the table
        Args:
            table(list): hash table
        Returns:
            list: new hash table with more space
        """
        new_array = [None]*(len(table)*2 + 1)
        self.slots = len(new_array)
        self.table = new_array
        self.num_items = 0
        self.num_collisions = 0
        for item in table:
            if item is not None:
                node = item
                while node:
                    self.put(node.key, node.val)
                    node = node.next

    def get(self, key):
        """ takes a key and returns a value from the hash table
            associated with the key
        Args:
            key(str): a key
        Returns:
            any: value associated with the key
        Raises:
            KeyError: if key does not exist in list
        """
        for item in self.table:
            if item is not None:
                node = item
                while node is not None:
                    if node.key == key:
                        return node.val
                    node = node.next
        raise KeyError

    def contains(self, key):
        """ returns True if the key exists in the table,
            otherwise False
        Args:
            key(str): a key
        Returns:
            bool: True if exists, False otherwise
        """
        hash_idx = hash_string(key, self.slots)
        item = self.table[hash_idx]
        while item is not None:
            if item.key == key:
                return True
            item = item.next
        return False

    def remove(self, key):
        """ removes and returns the key-value pair from the hash table
        Args:
            key(str): a key
        Returns:
            str: the key-value pair removed
        Raises:
            KeyError(KeyError): if no key exists in the table
        """
        if self.contains(key) is False:
            raise KeyError
        hash_idx = hash_string(key, self.slots)
        item = self.table[hash_idx]
        num = 0
        self.num_items -= 1
        while item is not None:
            if item.key == key:
                return_val = Node(item.key, item.val)
                if num == 0:
                    self.table[hash_idx] = item.next
                    return return_val
            prev = item
            item = item.next
        prev.next = item.next
        return return_val

    def size(self):
        """ returns the number of key-value pairs stored
            in the hash table
        Returns:
            int: number of key-value pairs
        """
        return self.num_items

    def load_factor(self):
        """ returns the current load factor of the hash table
        Returns:
            int: the load factor of the hash table
        """
        load = round(self.num_items/self.slots, 2)
        return load

    def collisions(self):
        """ returns the number of collisions that have occurred
            during insertions with the hash table
        Returns:
            int: number of collisions
        """
        return self.num_collisions

class HashTableLinear:
    """ implements linear probing
    Attributes:
        slots(int): the size of the table
        table(list): the Hash table
        num_collisions(int): the number of collisions
        num_items(int): number of items in the table
    """
    def __init__(self, table_size=11):
        self.slots = table_size
        self.table = [None]*table_size
        self.num_collisions = 0
        self.num_items = 0

    def __repr__(self):
        return '%s  Collisions: %d'%(self.table, self.num_collisions)

    def __eq__(self, other):
        return isinstance(other, HashTableLinear) and \
               self.slots == other.slots and \
               self.table == other.table and \
               self.num_collisions == other.num_collisions and \
               self.num_items == other.num_items

    def __getitem__(self, key):
        """ for getting a value with [] """
        return self.get(key)

    def __setitem__(self, key, val):
        """ for enabling value assignment with [] """
        return self.put(key, val)

    def __contains__(self, key):
        """ for enabling in operator in our Hash Tables """
        return self.contains(key)

    def put(self, key, data):
        """ insert key-value pair into the hash table
        Args:
            key(str): a key
            data(str): an item
        """
        if self.load_factor() > 0.75:
            self.resize(self.table)
        hash_idx = hash_string(key, self.slots)
        while self.table[hash_idx] is not None and self.table[hash_idx].key != key:
            hash_idx = (hash_idx + 1) % self.slots
            self.num_collisions += 1
        if self.table[hash_idx] is None:
            self.table[hash_idx] = Node(key, data)
        else:
            self.table[hash_idx].val = data
        self.num_items += 1

    def resize(self, table):
        """ enlarge the size of the table
        Args:
            table(list): hash table
        Returns:
            list: new hash table with more space
        """
        new_array = [None]*(len(table) * 2 + 1)
        self.slots = len(new_array)
        self.table = new_array
        self.num_items = 0
        self.num_collisions = 0
        for item in table:
            if item is not None:
                self.put(item.key, item.val)

    def get(self, key):
        """ takes a key and returns a value from the hash table
            associated with the key
        Args:
            key(str): a key
        Returns:
            str: key-value pair
        """
        hash_idx = hash_string(key, self.slots)
        while self.table[hash_idx] is not None and key != self.table[hash_idx].key:
            hash_idx = (hash_idx + 1) % self.slots
        if self.table[hash_idx] is not None and self.table[hash_idx].key == key:
            return self.table[hash_idx].val
        raise KeyError

    def contains(self, key):
        """ returns True if the key exists in the table, otherwise False
        Args:
            key(str): a key
        Returns:
            bool: True if exists, False otherwise
        """
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def remove(self, key):
        """ removes and returns the key-value pair from the hash table
        Args:
            key(str): a key
        Returns:
            str: the key-value pair removed
        Raises:
            KeyError(KeyError): if no key exists in the table
        """
        if self.contains(key) is False:
            raise KeyError
        hash_idx = hash_string(key, self.slots)
        while key != self.table[hash_idx].key:
            hash_idx = (hash_idx + 1) % self.slots
        return_val = self.table[hash_idx]
        self.table[hash_idx] = None
        hash_idx = hash_idx + 1
        while True:
            if self.table[hash_idx] is None:
                break
            node = self.table[hash_idx]
            self.table[hash_idx] = None
            self.put(node.key, node.val)
            hash_idx += 1
        self.num_items -= 1
        return return_val

    def size(self):
        """ returns the number of key-value pairs stored in the hash table
        Returns:
            int: number of key-value pairs
        """
        return self.num_items

    def load_factor(self):
        """ returns the current load factor of the hash table
        Returns:
            int: the load factor of the hash table
        """
        return self.num_items / self.slots

    def collisions(self):
        """ returns the number of collisions that have occurred
            during insertions with the hash table
        Returns:
            int: number of collisions
        """
        return self.num_collisions

class Dummy:
    """ dummy object used as special marker """
    def __init__(self):
        pass

class HashTableQuadratic:
    """ implements quadratic probing
    Attributes:
        slots(int): the size of the table
        table(list): the Hash table
        num_collisions(int): the number of collisions
        num_items(int): number of items in the table
    """
    def __init__(self, table_size=16):
        self.slots = table_size
        self.table = [None]*table_size
        self.num_items = 0
        self.num_collisions = 0
        self.deleted = Node(Dummy(), Dummy())

    def __repr__(self):
        return '%s  Collisions: %d' % (self.table, self.num_collisions)

    def __eq__(self, other):
        return isinstance(other, HashTableQuadratic) and \
               self.slots == other.slots and \
               self.table == other.table and \
               self.num_collisions == other.num_collisions and \
               self.num_items == other.num_items

    def __getitem__(self, key):
        """ for getting a value with [] """
        return self.get(key)

    def __setitem__(self, key, val):
        """ for enabling value assignment with [] """
        return self.put(key, val)

    def __contains__(self, key):
        """ for enabling in operator in our Hash Tables """
        return self.contains(key)

    def put(self, key, data):
        """ insert key-value pair into the hash table
        Args:
            key(str): a key
            data(str): an item
        """
        if self.load_factor() >= 0.75:
            self.resize(self.table)
        hash_idx = hash_string(key, self.slots)
        num = 1
        while self.table[hash_idx] and self.table[hash_idx] != self.deleted\
            and self.table[hash_idx].key != key:
            hash_idx = (hash_idx + num*num) % self.slots
            self.num_collisions += 1
            num += 1
        self.table[hash_idx] = Node(key, data)
        self.num_items += 1

    def resize(self, table):
        """ enlarge the size of the table
        Args:
            table(list): hash table
        Returns:
            list: new hash table with more space
        """
        new_array = [None] * (len(table) * 2 + 1)
        self.slots = len(new_array)
        self.table = new_array
        self.num_items = 0
        self.num_collisions = 0
        for item in table:
            if item is not None:
                self.put(item.key, item.val)

    def get(self, key):
        """ takes a key and returns a value from the hash table
            associated with the key
        Args:
            key(str): a key
        Returns:
            str: key-value pair
        """
        hash_idx = hash_string(key, self.slots)
        num = 1
        while self.table[hash_idx] is not None and key != self.table[hash_idx].key:
            hash_idx = (hash_idx + num * num) % self.slots
            num += 1
        if self.table[hash_idx] is not None and key == self.table[hash_idx].key:
            return self.table[hash_idx].val
        raise KeyError

    def contains(self, key):
        """ returns True if the key exists in the table, otherwise False
        Args:
            key(str): a key
        Returns:
            bool: True if exists, False otherwise
        """
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def remove(self, key):
        """ removes and returns the key-value pair from the hash table
        Args:
            key(str): a key
        Returns:
            str: the key-value pair removed
        Raises:
            KeyError(KeyError): if no key exists in the table
        """
        hash_idx = hash_string(key, self.slots)
        num = 1
        while self.table[hash_idx] and self.table[hash_idx].key != key:
            hash_idx = (hash_idx + num*num) % self.slots
            num += 1
        if self.table[hash_idx] is None:
            raise KeyError
        return_val = self.table[hash_idx]
        self.table[hash_idx] = self.deleted
        self.num_items -= 1
        return return_val

    def size(self):
        """ returns the number of key-value pairs stored in the hash table
        Returns:
            int: number of key-value pairs
        """
        return self.num_items

    def load_factor(self):
        """ returns the current load factor of the hash table
        Returns:
            int: the load factor of the hash table
        """
        return self.num_items / self.slots

    def collisions(self):
        """ returns the number of collisions that have occurred
            during insertions with the hash table
        Returns:
            int: number of collisions
        """
        return self.num_collisions

def hash_string(string, size):
    """ finds the index for the key value
    Args:
        string(str): a key
        size(int): the size of the list
    Returns:
        int: the index for the key
    """
    hash_idx = 0
    for letter in str(string):
        hash_idx = (hash_idx*31 + ord(letter)) % size
    return hash_idx

def import_stopwords(filename, hashtable):
    """ returns a hashtable object of the file
    Args:
        filename(str): name of the file containing stop words
        hashtable(object): HashTable
    """
    fin = open(filename, 'r')
    for line in fin:
        line = line.split()
        for word in line:
            word = str(word)
            hashtable.put(word, word)
    fin.close()
    return hashtable
