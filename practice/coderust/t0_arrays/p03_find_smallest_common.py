"""
Description
===========

You are given three positive integer arrays which are sorted in ascending order.

You have to find the smallest number that is common in all three arrays. Return
-1 if the smallest common number is not found.

Example:
-------
a = [6, 7, 10, 25, 30, 63, 64]
b = [0, 4, 5, 6, 7, 8, 50]
c = [1, 6, 10, 14]
Output = 6

"""

import numpy as np


def find_least_common_number(a, b, c):
    """Find least common number in the three given sorted array.
    Return -1 if there is no common number.

    Time:  O(n)
    Space: O(1)
    """
    i = j = k = 0
    while i < len(a) and j < len(b) and k < len(c):
        x, y, z = a[i], b[j], c[k]
        if x == y == z:
            return x
        m = max(x, y, z)
        if x < m:
            i += 1
        if y < m:
            j += 1
        if z < m:
            k += 1
    return -1


## Testing ##

def generate_random_input(maxlen=20, maxent=30):
    p, q, r = np.random.randint(0, maxlen, 3)
    a = np.sort(np.random.randint(1, maxent + 1, p))
    b = np.sort(np.random.randint(1, maxent + 1, q))
    c = np.sort(np.random.randint(1, maxent + 1, r))
    return a, b, c


def check(ans, a, b, c):
    a, b, c = set(a), set(b), set(c)
    common = a & b & c
    if ans == -1:
        return not bool(common)
    if ans != -1:
        return bool(common) and min(common) == ans
    return False


def random_tests(seed=None, maxlen=20, maxent=30):
    np.random.seed(seed)
    n = 0
    try:
        while True:
            n += 1
            a, b, c = generate_random_input(maxlen, maxent)
            ans = find_least_common_number(a, b, c)
            if not check(ans, a, b, c):
                print(f'Test #{n} failed!')
                print('a:', a)
                print('b:', b)
                print('c:', c)
                print(f'ans={ans}')
                break
    except KeyboardInterrupt:
        print(f'\nPassed {n} tests.')


if __name__ == '__main__':
    print('Performing random tests...')
    print('Press ^C to stop.')
    random_tests(seed=42, maxlen=200, maxent=300)

