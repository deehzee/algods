"""
Problem
=======
Given a sorted array, return the index of the given key. Return -1 if
the given key is not found in the given array.

"""


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
