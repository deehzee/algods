"""
Problem
=======
Given a large array of integers and a window of size ww, find the current
maximum value in the window as the window slides through the entire array.

Example
-------
a = [-4, 2, -5, 3, 6]
k = 3 (window size)
expected output: [2, 3, 6]

"""

from collections import deque
import numpy as np


# Time: O(n)
# Space: O(k)
def max_in_sliding_window(arr, width):
    acc = []
    win = deque()

    for i, a in enumerate(arr):
        #insert
        while win and arr[win[-1]] <= a:
            win.pop()
        win.append(i)
        # max
        if i >= width - 1:
            acc.append(arr[win[0]])
        # remove
        if win[0] <= i - width + 1:
            win.popleft()

    if len(arr) < width:
        acc.append(arr[win[0]])

    return acc


## Testing ##


def generate_random_input(seed=None, maxlen=20, maxent=30):
    n = np.random.randint(0, maxlen)
    arr = np.random.randint(1, maxent + 1, n)
    return arr


def check(acc, arr, width):
    ans = True
    for i in range(len(arr) - width + 1):
        if acc[i] != max(arr[i:i + width]):
            ans = False
            break
    return ans


def random_tests(seed=None, maxlen=20, maxent=30):
    try:
        n = 0
        while True:
            flag = False
            arr  = generate_random_input(seed, maxlen, maxent)
            for width in range(1, len(arr) + 1):
                n += 1
                acc = max_in_sliding_window(arr, width)
                if not check(acc, arr, width):
                    print(f'Test #{n}')
                    print('arr:', arr)
                    print('width:', width)
                    flag = True
                    break
            if flag:
                break
    except KeyboardInterrupt:
        print(f'\nPassed {n} tests.')


if __name__ == '__main__':
    print('Performing random tests...')
    print('Press ^C to stop.')
    random_tests(42, 100, 150)

