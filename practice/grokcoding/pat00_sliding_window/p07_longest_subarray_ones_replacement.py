"""
Problem
=======
Given an array of 0s and 1s, if you are allowed to replace no more than 'k'
0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example #1
----------
Input: A=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace 0s with 1s at indices 5 and 8.

Example #2
----------
Input: A=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace 0s with 1s at indices 6, 9 and 10.

"""


def len_longest_subarray(A, k):
    """Find the length of the longest subarray with all 1s after replacing
    at most k 0s.

    >>> len_longest_subarray(A=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2)
    6
    >>> len_longest_subarray(A=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3)
    9

    """
    max_len = num_ones = 0
    win_start = 0
    for win_end in range(len(A)):
        if A[win_end] == 1:
            num_ones += 1
        if (win_end - win_start + 1) - num_ones > k:
            if A[win_start] == 1:
                num_ones -= 1
            win_start += 1
        else:
            max_len += 1
    return max_len


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

