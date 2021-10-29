# lab1
# Name: Claire Minahan
# Section: CPE202-03
# Quarter: Spring 2020

# this lab practices the use of both iterative and recursive functions that do
# both similar and different tasks


def get_max(list1):
    ''' Finds the largest integer value in a list of integers
    Args:
         list1(list): a list of integers
    Returns:
        int: the largest integer value, or None if the list is empty
    '''
    if len(list1) == 0:
        return None
    max = list1[0]
    for i in list1:
        if i > max:
            max = i
    return max



def reverse(string1):
    ''' Reverses a string
    Args:
        string1(string): a random string
    Returns:
        string of the input string but backwards
    '''
    length = len(string1)
    if length == 0:
        return ''
    return string1[length - 1] + reverse(string1[0:length - 1])

def search(list1, target):
    ''' Searches for the location of an integer value in a list of integers
    Args:
        list1(list): a list of sorted integers
        target(int): the target value
    Returns:
        int: the index of target in list1, or None if target does not exist in list1
    Time Complexity: O(log(n))
    '''
    if len(list1) == 0:
        return 0
    index = len(list1)//2
    if list1[index] == target:
        return index
    lo = 0
    if list1[lo] == target:
        return lo
    hi = len(list1)-1
    if list1[hi] == target:
        return hi
    if list1[index] < target:
        return helper(index, hi, list1, target)
    elif list1[index] > target:
        return helper(lo, index, list1, target)


def helper(lo, hi, list1, target):
    ''' Determines whether the hi or lo indexes contain the target and return where they are relative to it in list
    Args:
        lo(int): first index of list1
        hi(int): highest index of list1
        list1(list): list of sorted integers
        target(int): an integer value of the number we are searching for
    Returns:
        int: the index of the integer in the list
    '''
    index = (lo + hi) // 2
    if lo == hi:
        return None
    if list1[index] == target:
        return index
    elif list1[index] < target:
        index += 1
        lo = index
    elif list1[index] > target:
        index -= 1
        hi = index
    elif list1[index] == lo:
        return lo
    elif list1[index] == hi:
        return hi
    return helper(lo, hi, list1, target)


def fib(n):
    ''' Computes the nth Fibonacci number of Fibonacci Numbers
    Args:
        n(int): an integer value
    Returns:
        an integer value of the nth number
    Time Complexity: O(2^n)
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def factorial_iter(n):
    ''' Compute the factorial of n
    Args:
        n(int): an integer value
    Returns:
        an integer value of the factorial of n
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    x = 1
    for num in range(1,n):
        x *= (num+1)
    return x


def factorial_rec(n):
    ''' Compute the factorial of n
    Args:
        n(int): an integer value
    Returns:
        an integer value of the factorial of n
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n*(factorial_rec(n-1))


