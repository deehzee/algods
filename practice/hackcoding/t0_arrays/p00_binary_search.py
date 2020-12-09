"""
Problem
=======
Given a sorted array, return the index of the given key. Return -1 if
the given key is not found in the given array.

"""

import numpy as np


# Time: O(log n)
# Space: O(1)
def binary_search(a, key):
    lo, hi = 0, len(a)
    while lo < hi:
        mi = (lo + hi) // 2
        if a[mi] < key:
            lo = mi + 1
        elif a[mi] > key:
            hi = mi
        else:
            return mi
    return -1


# Implementation from Standard library:
# bisect.bisect_left(a, x, lo=0, hi=len(a))
# bisect.bisect_right(a, x, lo=0, hi=len(a))
# bisect.bisect(a, x, lo=0, hi=len(a)) # same as bisect_right

## Testing ##

def generate_random_sorted_array(maxlen=10, maxent=20):
    n = np.random.randint(0, maxlen + 1)
    arr = np.random.randint(1, maxent, n)
    return np.sort(arr)


def random_tests(seed=None, maxlen=10, maxent=20):
    np.random.seed(seed)
    n = 0
    try:
        while True:
            n += 1
            flag = False
            arr = generate_random_sorted_array(maxlen, maxent)
            for key in range(0, maxent + 1):
                i = binary_search(arr, key)
                if ((-1 < i < len(arr) and arr[i] != key) or (i == -1 and key in arr)):
                    print(f'Test #{n}')
                    print('arr: ', arr)
                    print('key: ', key)
                    print('i: ', i)
                    flag = True
                    break
            if flag:
                break
    except KeyboardInterrupt:
        print(f'\nPassed {n} tests.')


if __name__ == '__main__':
    print('Performing random tests...')
    print('Press ^C to stop.')
    random_tests(seed=42, maxlen=100, maxent=200)

