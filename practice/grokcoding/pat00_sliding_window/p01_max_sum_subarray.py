"""
Description
===========
Given an array of positive numbers and a postive number k, find the maximum
sum of any contiguous subarry of size k.

Example #1
----------
Input:  arr=[2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example #2
----------
Input:  arr=[2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4]

"""


def max_sum_subarray(arr, k):
    """Find maximum sum of any contiguous subarray of size k.

    Time:  O(n)
    Space: O(1)
    """
    max_sum = win_sum = 0
    win_start = 0
    for win_end in range(len(arr)):
        win_sum += arr[win_end]
        if win_end >= k - 1:
            max_sum = max(max_sum, win_sum)
            win_sum -= arr[win_start]
            win_start += 1
    return max_sum

