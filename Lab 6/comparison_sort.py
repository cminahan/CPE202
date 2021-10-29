""" Sorting functions for lab 6
Members: Claire Minahan, Nathan Kennedy, Jeremiah Lee
Course: CPE 202
"""

#import random
#import time
#start_time = time.time()
#end_time = time.time()
#sort_time = end_time - start_time
#print(sort_time)


def selection_sort(alist):
    """ Claire Minahan
    Sorts an array of integers using selection sort
    Args:
        alist(list): a list of integers
    Returns:
        int: number of comparisons
    Big O: O(n^2)
    """
    size = len(alist)
    num_comparisons = 0
    end_index = size - 1
    new_list = []
    for num in range(size):
        max_index = 0
        for index in range(size):
            num_comparisons += 1
            if alist[index] > alist[max_index] and index <= end_index:
                max_index = index
        new_list.append(alist[max_index])
        alist.pop(max_index)
        end_index -= 1
        size -= 1
    new_list.reverse()
    return num_comparisons


def merge_sort(alist):
    """ Claire Minahan
    Sorts an array of integers using merge sort
    Args:
        alist(list): a list of integers
    Returns:
        int: number of comparisons
    Big O: O(nlogn)
    """
    num_comparisons = 0
    size = len(alist)
    if size <= 1:
        return alist
    midpoint = size//2
    left = alist[:midpoint]
    right = alist[midpoint:]
    merge_sort(left)
    merge_sort(right)

    left_index = 0
    right_index = 0
    size_left = len(left)
    size_right = len(right)
    main_index = 0

    while left_index < size_left and right_index < size_right:
        num_comparisons += 1
        if left[left_index] > right[right_index]:
            alist[main_index] = right[right_index]
            right_index += 1
            num_comparisons += 1
        else:
            alist[main_index] = left[left_index]
            left_index += 1
            num_comparisons += 1
        main_index += 1

    while right_index < size_right:
        num_comparisons += 1
        alist[main_index] = right[right_index]
        main_index += 1
        right_index += 1
    while left_index < size_left:
        num_comparisons += 1
        alist[main_index] = left[left_index]
        main_index += 1
        left_index += 1
    return num_comparisons


def bubble_sort(alist):
    """function to sort an integer list using bubble sort
    Author: Nathan Kennedy
    Args:
        alist (list): a list of integers
    Returns:
        alist (list): the sorted list of integers
    Big O: O(n^2)"""
    num_comp = 0
    n = len(alist)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            num_comp += 1
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist, num_comp, n


def quick_sort(items, lo, hi, counter=0):
    """function to sort an integer list using quick sort
    Author: Nathan Kennedy
    Args:
        items (list): a list of integers
        lo (int): lowest index in the list
        hi (int): highest index in the list
        counter (int): to increment a count for number of comparisons
    Returns:
        items (list): the sorted list of integers
    Big O: O(n * log(n))"""
    if lo >= hi:
        return
    mid = (lo + hi) // 2
    pivot = items[mid]
    # items[lo], items[mid] = items[mid], items[lo]
    lt = lo
    gt = hi
    i = lt
    while i <= gt:
        if items[i] < pivot:
            items[i], items[lt] = items[lt], items[i]
            i += 1
            lt += 1
            counter += 1
        elif items[i] > pivot:
            items[i], items[gt] = items[gt], items[i]
            gt -= 1
            counter += 2
        else:
            i += 1
    quick_sort(items, lo, lt - 1)
    quick_sort(items, gt + 1, hi)
    return items, counter


def insertion_sort(alist):
    """ Jeremiah Lee
    sorts a list using insertion sort
    args:
        alist (list): unsorted list
    returns:
        comparisons (int): number of comparisons
    O(n^2) time complexity:
    """
    size = len(alist)
    comparisons = 0
    for i in range(1, size):
        j = i
        count = comparisons
        while j > 0 and alist[j - 1] > alist[j]:
            #shift over 1
            alist[j - 1], alist [j] = alist[j], alist[j - 1]
            j -= 1
            count += 1
        if count == comparisons:
            comparisons += 1
        else:
            comparisons = count
    return comparisons


def heapify(arr, n, i):
    """ Jeremiah Lee
    helper function for heap_sort()
    creates a max heap of the subtree with i = index of root
    and n = size of subtree
    args:
        arr (list)
        i (int)
        n (int)
    returns:
        count (int)
    time O(nlogn)
    """
    count = 0
    root = i  # Initialize largest as root
    left = 2 * i + 1  # left leaf of root
    right = 2 * i + 2  # right leaf of root

    # if left is greater than root, make left the root
    if left < n and arr[i] < arr[left]:
        root = left

        # if right is greater than root, make right the root
    if right < n and arr[root] < arr[right]:
        root = right

        # if root was changed, reflect that in the array
    if root != i:
        count += 1
        arr[i], arr[root] = arr[root], arr[i]
        # do recursion
        count += heapify(arr, n, root)
    return count


def heap_sort(alist):
    """sorts a given arr using heap sort
    utilized the helper functions build_heap and heapify()
    args:
        arr (list)
    returns:
        count (int)
    """
    n = len(alist)
    count = 0
    start = int(n / 2) - 1
    for i in range(start, -1, -1):  # builds the initial heap
        count += heapify(alist, n, i)
    for i in range(n - 1, 0, -1):  # prepends the root of the heap (max) to the sorted sublist
        alist[i], alist[0] = alist[0], alist[i]
        count += heapify(alist, i, 0)  # recreates the heap with the new max as root
    return count
