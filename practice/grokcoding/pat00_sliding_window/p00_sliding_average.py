"""
Description
===========
Given an array of numbers, find the average of all contiguous subarrays of
size k in it.

Example
-------
Input:  [1, 3, 2, 6, -1, 4, 1, 8, 2], 5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]

"""


def sliding_average(arr, k):
    """Find slinding averages of window size k for the elements of arr.

    Time:  O(n)
    Space: O(1)
    """
    averages = []
    win_start = 0
    win_sum = 0
    for win_end in range(len(arr)):
        win_sum += arr[win_end]
        if win_end >= k - 1:
            averages.append(win_sum / k)
            win_sum -= arr[win_start]
            win_start += 1
    return averages

