"""Contains starter code for lab 5
CPE202
Instructions:
    Complete this file by writing python3 code.
"""
import random

#implement BSTNode class and get,contains,insert,delete functions in bst.py
import bst

#classmate.py is implemented for you
from classmate import classmate_factory 

class TreeMap:
    """class for TreeMap
    Attributes:
        tree(list): tree
        num_items(int): number of items in the tree
    """
    def __init__(self):
        self.tree = None
        self.num_items = 0

    def __repr__(self):
        #Complete this method
        return "Tree: [%s]" %self.tree

    def __eq__(self, other):
        #Complete this method
        return isinstance(other, TreeMap)\
                and self.tree == other.tree\
                and self.num_items == other.num_items

    def __getitem__(self, key):
        """implementing this method enables getting an item with [] notation
        This function calls your get method.
        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            any : the value associated with the key
        Raises:
            KeyError : it raises KeyError because the get function in bst.py raises the error.
        """
        return self.get(key)

    def __setitem__(self, key, val):
        """implementing this method enables setting a key value pair with [] notation
        This function calls your put method.
        Args:
            key (any) : a key which is compareable by <,>,==
            val (any): the value associated with the key
        """
        self.put(key, val)

    def __contains__(self, key):
        """implementing this method enables checking if a key exists with in notaion
        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False 
        """
        return self.contains(key)

    def get(self, key):
        """put a key value pair into the map
        Calls insert function in bst.py
        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            any : the value associated with th key
        Raises:
            KeyError : if the key does not exist
        """
        #this method is already written for you
        return bst.get(self.tree, key)

    def put(self, key, val):
        """put a key value pair into the map
        Calls insert function in bst.py and increments num_items by 1
        Args:
            key (any) : a key which is compareable by <,>,==
            val (any): the value associated with the key
        """
        #---- to do ----
        #call a function in the bst module
        # and increment self.num_items by 1
        #---------------
        self.num_items += 1
        self.tree = bst.insert(self.tree, key, val)

    def contains(self, key):
        """ given a key, check if the tree contains it
        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False 
        """
        #---- to do ----
        #call a function in the bst module
        #---------------
        return bst.contains(self.tree, key)

    def delete(self, key):
        """ removes a key value pair from the tree
        Args:
            key (any) : a key which is compareable by <,>,==
        Raises:
            KeyError : if the key does not exist
        """
        #---- to do ----
        #call a function in the bst module
        #and decrement the num_items
        #---------------
        if self.num_items == 0:
            raise KeyError
        self.num_items -= 1
        return bst.delete(self.tree, key)

    def size(self):
        """returns the number of items in the map
        Returns:
            int : the number of items in the map
        """
        return self.num_items

    def find_min(self)->(any, any):
        """ return the key and value associated with the smallest key in the tree
        Returns:
            key(any): key
            val(any): value associated with key
        Raises:
            ValueError
        """
        #---- to do ----
        # complete this method by calling bst.find_min()
        # return the key and the value associated with the smallest key in the tree
        # raise ValueError if the tree is empty
        #---------------
        if self.num_items == 0:
            raise ValueError
        return bst.find_min(self.tree)

    def find_max(self)->(any, any):
        """Return the key and the value associated with the largest key in the tree
        Returns:
            key(any): key
            val(any): value associated with key
        Raises:
            ValueError
        """
        #---- to do ----
        # complete this method by calling bst.find_max()
        # return the key and the value associated with the largest key in the tree 
        # raise ValueError if the tree is empty
        #---------------
        if self.num_items == 0:
            raise ValueError
        return bst.find_max(self.tree)

    def inorder_list(self)->list:
        """ return a list of BST keys representing inorder traversal of BST
        Returns:
            list: list of BST keys
        """
        #---- to do ----
        # complete this method by calling bst.inorder_list()
        # return a list of BST keys representing inorder traversal of BST
        #---------------
        return bst.inorder_list(self.tree, accum=[])

    def preorder_list(self)->list:
        """ return a list of BST keys representing preorder traversal of BST
        Returns:
            list: a list of BST keys
        """
        #---- to do ----
        # complete this method by calling bst.preorder_list()
        # return a list of BST keys representing preorder traversal of BST
        #---------------
        return bst.preorder_list(self.tree, accum=[])

    def tree_height(self)->int:
        """ return the height of the tree
        Returns:
            height(int): the height of the tree
            -1 if empty
        """
        #---- to do ----
        # complete this method by calling bst.tree_height()
        # return the height of the tree
        # return -1 if the tree is empty
        #---------------
        if self.num_items == 0:
            return -1
        return bst.tree_height(self.tree)

    def range_search(self, low, high)->list:
        """ returns a list of (key, value) whose keys fall within the given range
        Args:
            low(any): low end of range
            high(any): high end of range, exculsive
        Returns:
            list(list): list of (key, value)
        """
        #---- to do ----
        # complete this method by calling bst.range_search()
        # return a list of (key,value) whose keys fall within the given range
        #---------------
        return bst.range_search(self.tree, low, high, accum=[])

def import_classmates(filename):
    """Imports classmates from a tsv file
    Design Recipe step 4 (Templating) is done for you.
    Complete this function by following the template.
    Args:
        filename (str) : the file name of a tsv file containing classmates
    Returns:
        TreeMap : return an object of TreeMap containing classmates.
    """
    #create an object of TreeMap
    tree_map = TreeMap()
    #create an empty list for classmates
    classmates = []
    #---- to do ----
    # complete this function by following the comments below
    #open the file whose name is passed as the argument filename
    # with python builtin open() function.
    #read all lines in the file and assign it to variable lines
    #for each line in lines
        #split the line at tabs (\t) and assign it to a variable tokens
        #classmate = classmate_factory(tokens)
        #append the classmate to a list classmates
    #---------- ----
    file_name = open(filename, "r")
    for line in file_name:
        tokens = line.split('\t')
        classmate = classmate_factory(tokens)
        classmates.append(classmate)
    #shuffle the classmates
    random.seed(2)
    random.shuffle(classmates)
    #---- to do ----
    # complete this function by following the comments below
    #for each classmate in classmates
        #put the classmate into the tree_map using its sid as the key
    #---------- ----
    for student in classmates:
        tree_map.put(student.sid, student)
    return tree_map

def search_classmate(tmap, sid):
    """Searches a classmate in a TreeMap using the sid as a key
    Args:
        tmap (TreeMap) : an object of TreeMap
        sid (int) : the id of a classmate
    Returns:
        Classmate : a Classmate object
    Raises:
        KeyError : if a classmate with the id does not exist
    """
    #---- to do ----
    # complete this function 
    #---------------
    if tmap.contains(sid):
        return tmap.get(sid)
    raise KeyError
