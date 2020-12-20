"""
Description
===========
Given an array of postive numbers and a postive number s, find the length
of the smallest contiguous subarray whose sum is greater than or equal to s.
Return 0 if no such subarray exists.

Example #1
----------
Input:  arr=[2, 1, 5, 2, 3, 2], s=7
Output: 2
Explanation: The smallest subarray with a sum >= 7 is [5, 2].

Example #2
----------
Input:  arr=[2, 1, 5, 2, 8], s=7
Output: 1
Explanation: The smallest subarray with a sum >=7 is [8].

Example #3
----------
Input:  arr=[3, 4, 1, 1, 6], s=8
Output: 3
Explanation: Smallest subarray with a sum >= 8 are [3, 4, 1] and [1, 1, 6]

"""


def smallest_subarray_with_given_sum(arr, s):
    """Find the length of the smallest subarray whose sum is >= s.

    Time:  O(n)
    Space: O(1)

    >>> smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7)
    2

    >>> smallest_subarray_with_given_sum([2, 1, 5, 2, 8], 7)
    1

    >>> smallest_subarray_with_given_sum([3, 4, 1, 1, 6], 8)
    3

    """
    win_sum = 0
    win_start = 0
    min_len = 0
    for win_end in range(len(arr)):
        win_sum += arr[win_end]
        while win_sum >= s:
            cur_len = win_end - win_start + 1
            if min_len == 0 or cur_len < min_len:
                min_len = cur_len
            win_sum -= arr[win_start]
            win_start += 1
    return min_len


if __name__ == '__main__':
    import doctest
    doctest.testmod()

