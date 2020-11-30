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

DBG = print


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
