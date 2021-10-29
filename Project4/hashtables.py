""" Project 4
Name: Claire Minahan
Course: CPE202-03
Instructor: Kuboi
"""

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
        return '%s' %(self.table)

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

    def keys(self):
        """ provides a list of all the keys in a hashtable
        Returns:
            a list of keys
        """
        keys = []
        for item in self.table:
            if item is not None:
                keys.append(item.key)
        return keys

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

def import_stopwords(filename, hashtable=HashTableLinear()):
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
