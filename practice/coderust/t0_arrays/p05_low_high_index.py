"""
Description
===========

Given a sorted array of integers, return the low and high index of the given
key. You must return -1 if the indexes are not found.

Example
-------

arr = [1, 2, 2, 5, 5, 5, 5, 7]

key = 1
output: low, high = 0, 0

key = 2
output: low, high = 1, 2

key = 5
output: low, high = 3, 6

key = 6
output: low, high = -1, -1

"""

import numpy as np


def find_low_index1(arr, key):
    """Find the low index of the key in the array arr.

    Time:  O(log n)
    Space: O(1)
    """
    lo, hi = 0, len(arr)
    while lo < hi:
        mi = (lo + hi) // 2
        if arr[mi] < key:
            lo = mi + 1
        elif arr[mi] >= key:
            hi = mi
    if hi < len(arr) and arr[hi] == key:
        return hi
    return -1


def find_high_index1(arr, key):
    """Find the high index of the key in the array arr.

    Time:  O(log n)
    Space: O(1)
    """
    lo, hi = 0, len(arr)
    while lo < hi:
        mi = (lo + hi) // 2
        if arr[mi] <= key:
            lo = mi + 1
        elif arr[mi] > key:
            hi = mi
    if lo > 0 and arr[lo - 1] == key:
        return lo - 1
    return -1


def find_low_index(arr, key):
    """Find the low index of the key in the array arr.

    Time:  O(log n)
    Space: O(1)
    """
    lo, hi = 0, len(arr)
    while lo < hi:
        mi = (lo + hi) // 2
        if arr[mi] < key:
            lo = mi + 1
        elif arr[mi] == key and (mi == 0 or arr[mi - 1] < key):
            return mi
        else:
            hi = mi
    return -1


def find_high_index(arr, key):
    """Find the high index of the key in the array arr.

    Time:  O(log n)
    Space: O(1)
    """
    lo, hi = 0, len(arr)
    while lo < hi:
        mi = (lo + hi) // 2
        if arr[mi] > key:
            hi = mi
        elif arr[mi] == key and (mi + 1 == len(arr) or arr[mi + 1] > key):
            return mi
        else:
            lo = mi + 1
    return -1


## Testing ##


def generate_random_input(maxlen=20, maxent=20):
    n = np.random.randint(0, maxlen + 1)
    arr = np.sort(np.random.randint(1, maxent + 1, n))
    return arr


def check_low(arr, key, lo):
    if lo == -1:
        return key not in arr
    return 0 <= lo < len(arr) and arr[lo] == key and (lo == 0 or arr[lo - 1] < key)


def check_high(arr, key, hi):
    if hi == -1:
        return key not in arr
    return 0 <= hi < len(arr) and arr[hi] == key and (hi == len(arr) - 1 or arr[hi + 1] > key)


def random_tests(seed=None, maxlen=20, maxent=20):
    np.random.seed(seed)
    n = 0
    try:
        while True:
            n += 1
            flag = False
            arr = generate_random_input(maxlen, maxent)
            for key in range(maxent + 1):
                lo = find_low_index(arr, key)
                hi = find_high_index(arr, key)
                if not check_low(arr, key, lo) or not check_high(arr, key, hi):
                    print(f'Test #{n} falied...')
                    print('arr:', arr)
                    print('key:', key)
                    print(f'lo={lo}, hi={hi}')
                    flag = True
                    break
            if flag: break
    except KeyboardInterrupt:
        print(f'\nPassed {n} tests.')


if __name__ == '__main__':
    print('Performing random tests...')
    print('Press ^C to stop.')
    random_tests(maxlen=100, maxent=100)


