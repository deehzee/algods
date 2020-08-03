# Uses python3
from collections import deque
import sys


### Solution 0: Bruteforce ###


def optimal_sequence_recursive(n):
    if n == 1:
        return [1]
    n_ops = n + 1
    if n % 3 == 0:
        seq = optimal_sequence_recursive(n // 3)
        if len(seq) + 1 < n_ops:
            n_ops = 1 + len(seq)
            opt_seq = seq
    if n % 2 == 0:
        seq = optimal_sequence_recursive(n // 2)
        if len(seq) + 1 < n_ops:
            n_ops = 1 + len(seq)
            opt_seq = seq
    if n > 1:
        seq = optimal_sequence_recursive(n - 1)
        if len(seq) + 1 < n_ops:
            n_ops = len(seq) + 1
            opt_seq = seq
    opt_seq.append(n)
    return opt_seq


### Solution 2: Memoization ###


def memoize(func):
    res = {}
    def memoized_func(n):
        if n not in res:
            print('calculating', n)
            res[n] = func(n)
        return res[n]
    return memoized_func


# optimal_sequence_memoize = memoize(optimal_sequence_recursive)
@memoize
def optimal_sequence_memoize(n):
    if n == 1:
        return [1]
    n_ops = n + 1
    if n % 3 == 0:
        seq = optimal_sequence_memoize(n // 3)
        if len(seq) + 1 < n_ops:
            n_ops = 1 + len(seq)
            opt_seq = seq
    if n % 2 == 0:
        seq = optimal_sequence_memoize(n // 2)
        if len(seq) + 1 < n_ops:
            n_ops = 1 + len(seq)
            opt_seq = seq
    if n > 1:
        seq = optimal_sequence_memoize(n - 1)
        if len(seq) + 1 < n_ops:
            n_ops = len(seq) + 1
            opt_seq = seq
    opt_seq.append(n)
    return opt_seq


### Solutino 3: Dynamic Programming ###


def optimal_sequence_dynprog(n):
    nops = [n + 1] * (n + 1)
    nops[0] = 0
    nops[1] = 0
    for i in range(2, n + 1):
        if i % 3 == 0 and nops[i // 3] + 1 < nops[i]:
            nops[i] = 1 + nops[i // 3]
        if i % 2 == 0 and nops[i // 2] + 1 < nops[i]:
            nops[i] = 1 + nops[i // 2]
        if nops[i - 1] + 1 < nops[i]:
            nops[i] = 1 + nops[i - 1]
    seq = unwind(nops)
    return seq


def unwind(nops):
    seq = []
    i = len(nops) - 1
    while i > 0:
        seq.append(i)
        if i % 3 == 0 and nops[i // 3] + 1 == nops[i]:
            i //= 3
        elif i % 2 == 0 and nops[i // 2] + 1 == nops[i]:
            i //= 2
        elif nops[i - 1] + 1 == nops[i] or i == 1:
            i -= 1
    return reversed(seq)


### Main ###

optimal_sequence = optimal_sequence_dynprog


def main():
    n = int(input())
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
    print()


if __name__ == '__main__':
    main()

