"""Module for BST
CPE202
Contains the data definition of BST,
and functions (not class member methods) on BST.
Functions defined here need to be recusrive functions,
and will be used by other classes such as TreeMap as
helper functions.
Author:
    Claire Minahan
"""

class BSTNode:
    """ Binary Search Tree is one of
    - None
    - BSTNode
    Attributes:
        key (any): key
        val (any): value associated with the key
        left (BSTNode): left subtree of Binary Search Tree
        right (BSTNode): right subtree of Binary Search Tree
    """
    # ---- to do ----
    # implement __init__, __eq__ and __repr__
    # ---------------
    def __init__(self, key, val, left, right):
        self.key = key
        self.val = val
        self.right = right
        self.left = left

    def __repr__(self):
        return "[Key: %s, Right: %s, Left: %s]" %(self.key, self.right, self.left)

    def __eq__(self, other):
        return isinstance(other, BSTNode) \
               and self.key == other.key \
               and self.val == other.val \
               and self.right == other.right \
               and self.left == other.left

# ---- to do ----
# implement the following recursive top-level functions
# (they do not belong to a class)
# write a docstring for each function
#
def get(tree, key) -> any:
    """ given a key, return the value stored in the map
    Args:
        tree(node): a node
        key(any): key
    Returns:
        val(any): value associated with key or,
        None
    """
    if tree is None:
        raise KeyError
    if tree.key == key:
        return tree.val
    if tree.key > key:
        return get(tree.left, key)
    return get(tree.right, key)

def contains(tree, key) -> bool:
    """ given a key, returns True if it is in the tree, False otherwise
    Args:
        tree(node): node
        key(any): key
    Returns:
        bool(bool): True if in tree, False otherwise
    """
    if tree is None:
        return False
    if tree.key == key:
        return True
    if key < tree.key:
        return contains(tree.left, key)
    return contains(tree.right, key)

def insert(tree, key, val) -> BSTNode:
    """ inserts a key value pair in the tree
    Args:
        tree(node): a node
        key(any): key
        val(any): value associated with key
    Returns:
        tree(node): a node
    """
    if tree is None:
        return BSTNode(key, val, None, None)
    if key == tree.key:
        tree.val = val
    if key < tree.key:
        tree.left = insert(tree.left, key, val)
    else:
        tree.right = insert(tree.right, key, val)
    return tree

def delete(tree, key) -> BSTNode:
    """ removes a key value pair from a tree
    Args:
        tree(node): a node
        key(any): key
    Returns:
        tree(node): a node
    """
    if tree.key == key:
        if not(tree.left and tree.right):
            return None
        if tree.right and tree.left:
            replacement = delete_helper(tree.right)
            tree = delete(tree.right, replacement.key)
            tree.key = replacement.key
            return tree
        if tree.left:
            return tree.left
        return tree.right
    if tree.key > key:
        tree.left = delete(tree.left, key)
    else:
        tree.right = delete(tree.right, key)
    return tree

def delete_helper(tree) -> BSTNode:
    """ a helper function for delete
    Args:
        tree(node): a node
    Returns:
        tree(node): a node
    Raises:
        ValueError
    """
    if tree is None:
        raise KeyError
    if tree.left is None:
        return tree
    return delete_helper(tree.left)

def find_min(tree) -> (any, any):
    """ return the key and value associated with the smallest key value
    Args:
        tree(node): a node
    Returns:
        key(any): key
        val(any): value associated with key
    Raises:
        ValueError
    """
    if tree.left is None:
        return (tree.key, tree.val)
    return find_min(tree.left)

def find_max(tree) -> (any, any):
    """ return the key and value associated with the largest key value
    Args:
        tree(node): a node
    Returns:
        key(any): key
        val(any): value associated with key
    Raises:
        ValueError
    """
    if tree.right is None:
        return (tree.key, tree.val)
    return find_max(tree.right)

def inorder_list(tree, accum):
    """ returns a list of BST keys representing inorder traversal of BST
    Args:
        tree(node): a node
        accum(list):
    Returns:
        list: list of BST keys
    """
    if tree is not None:
        inorder_list(tree.left, accum)
        accum.append(tree.key)
        inorder_list(tree.right, accum)
    return accum

def preorder_list(tree, accum):
    """ returns a list of BST keys representing preorder traversal of BST
    Args:
        tree(node): a node
        accum(list):
    Returns:
        list: list of BST keys
    """
    if tree is not None:
        accum.append(tree.key)
        preorder_list(tree.left, accum)
        preorder_list(tree.right, accum)
    return accum

def tree_height(tree) -> int:
    """ returns the height of the tree
    Args:
        tree(node): a node
    Returns:
        int: height of the tree
    """
    if tree is None:
        return -1
    left_height = tree_height(tree.left)
    right_height = tree_height(tree.right)
    if right_height > left_height:
        return right_height + 1
    return left_height + 1

def range_search(tree, low, high, accum):
    """ return a list of (key, value) whose keys fall within the given range
    Args:
        tree(node): a node
        low(any): low range, inclusive
        high(any): hi range, exclusive
        accum(list): list of (key, value)
    Returns:
        list(list): a list of (key, value) whose keys fall within the given range
    """
    if low <= tree.key < high:
        if tree.left is not None:
            accum.append(range_search(tree.left, low, high, accum))
        accum.append((tree.key, tree.val))
        if tree.right is not None:
            accum.append(range_search(tree.right, low, high, accum))
    elif tree.key < low and tree.right is not None:
        accum.append(range_search(tree.right, low, high, accum))
    elif tree.key >= high and tree.left is not None:
        accum.append(range_search(tree.left, low, high, accum))
    new_list = []
    for item in accum:
        if isinstance(item, tuple):
            new_list.append(item)
    return new_list
