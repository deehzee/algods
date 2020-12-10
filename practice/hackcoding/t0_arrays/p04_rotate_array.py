"""
Description
===========

Given an array of integers, rotate the array by k elements where k is an
integer:

For positive values of k, perform a right rotation.
For negative values of k, perform a left rotation.

Make sure you make changes to the original array.

Example
-------
arr = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]

k = -1
output = [10, 20, 0, 59, 86, 32, 11, 9, 40, 1]

k = 2
output = [9, 40, 1, 10, 20, 0, 59, 86, 32, 11]

"""

import numpy as np


def rotate_array(arr, k):
    """Rotate an array arr by k elements.

    If k > 0, rotate to the right, otherwise, to the left.

    Time:  O(n)
    Space: O(1)
    """
    n = len(arr)
    k = k % n
    reverse(arr, 0, n)
    reverse(arr, 0, k)
    reverse(arr, k, n)


def reverse(arr, start, end):
    """Reverse an array arr between indices start and end (exclusive)."""
    while start < end:
        arr[start], arr[end - 1] = arr[end - 1], arr[start]
        start += 1
        end -= 1

