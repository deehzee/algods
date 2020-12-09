'''
1060. Missing Element in Sorted Array
=====================================
Given a sorted array A of unique numbers integers, find the k-th missing
number.

Examples:
---------
>>> missing(A=[4, 7, 9, 10], k=1)
5
>>> missing(A=[4, 7, 9, 10], k=3)
8
>>> missing(A=[1, 2, 4], k=3)
6

'''

import random


### Testing ###


def generate_random_input(maxlen=1000, maxdiff=10):
    print('HI')
    n = random.randint(1, maxlen)
    A = [0] * n
    prev = 0
    for i in range(n):
        A[i] = random.randint(prev + 1, prev + maxdiff)
        prev = A[i]
    k = random.randint(1, 2 * maxlen)
    return A


def verify(A, k, ans):
    i = j = 0
    while i < k:
        if A[j] == i:
            j += 1
        else:
            i += 1


def bruteforce(A, k):
    i = j = 0
    x = 1
    while i < k:
        if A[j] == x:
            j += 1
        else:
            i += 1
            x = A[j]

