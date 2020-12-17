"""
Description
===========
Given an interger array, move all elements that are 0 to the left while
maintaining the order of other elements in the array. The array has to be
modified in-place.

Example
-------
arr = [1, 10, 20, 0, 59, 63, 0, 88, 0]
output = [0, 0, 0, 1, 10, 20, 59, 63, 88]

"""

def move_zeros_to_left(arr):
    """Given an array, move all zeros to the left (in-place).

    Time:  O(log n)
    Space: O(1)
    """
    read_head = write_head = len(arr) - 1
    while read_head >= 0:
        if arr[read_head] == 0:
            read_head -= 1
        elif read_head == write_head:
            read_head -= 1
            write_head -= 1
        else:
            arr[write_head] = arr[read_head]
            read_head -= 1
            write_head -= 1
    while write_head >= 0:
        arr[write_head] = 0
        write_head -= 1

