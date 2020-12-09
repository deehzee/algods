"""
Description
===========
Search for a given number in a sorted array, with unique elements,
that has been rotated by some arbitrary number. Return -1 if the
number doesn't exist.

Example
-------
arr = [17, 19, 20, 1, 4, 10, 15]
x = 19
output = 1

"""

import numpy as np


def search_rotated_array(arr, key):
    """Search for a key in a rotated sorted array arr.
    Assumption: Elements of arr are unique.

    Time:  O(log n)
    Space: O(1)
    """
    lo, hi = 0, len(arr)
    while lo < hi:
        mi = (lo + hi) // 2
        if arr[mi] == key:
            return mi
        elif arr[lo] <= key < arr[mi]:
            hi = mi
        elif arr[mi] < key <= arr[hi - 1]:
            lo = mi + 1
        elif arr[lo] >= arr[mi]:
            hi = mi
        elif arr[mi] >= arr[hi - 1]:
            lo = mi + 1
        else:
            return -1
    return -1


## Tests ##


def generate_random_input(maxlen=20, maxent=40):
    n = np.random.randint(1, maxlen + 1)
    arr = np.sort(np.random.choice(np.arange(1, maxent + 1), size=n, replace=False))
    k = np.random.randint(0, n)
    arr = np.hstack((arr[k:], arr[:k]))
    return arr


def random_tests(seed=None, maxlen=20, maxent=40):
    np.random.seed(seed)
    n = 0
    try:
        while True:
            flag = False
            arr = generate_random_input(maxlen, maxent)
            for key in range(maxent + 2):
                n += 1
                i = search_rotated_array(arr, key)
                if (i == -1 and key in arr) or (i >= 0 and arr[i] != key):
                    print(f'Test #{n}')
                    print('arr:', arr)
                    print('key:', key)
                    print(f'i={i}')
                    flag = True
                    break
            if flag:
                break
    except KeyboardInterrupt:
        print(f'\nPassed {n} tests.')


if __name__ == '__main__':
    print('Performing random tests...')
    print('Press ^C to stop.')
    random_tests(seed=42, maxlen=200, maxent=400)

