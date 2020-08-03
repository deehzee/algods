# Uses python3
import sys
import itertools


def partition3_dynprog(A):
    '''Is it possible to partition the given values into 3 equal piles?

    Examples:
    >>> partition3([3, 3, 3, 3])
    0
    >>> partition3([40])
    0
    >>> partition3([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59])
    1
    >>> partition3([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25])
    1

    '''
    # Let S = sum(A)
    #
    # T[i][s][t] = whether A[0..(i-1)] can be divided into three parts
    #              with the sum of the first part s, and the second
    #              part t (the remaining is the thrid part with sum
    #              S - s -t).
    #
    # Recurrent relation:
    # T[s][t][i] = OR(T[s - A[i - 1]][t][i],  // Case 1
    #                 T[s][t - A[i - 1]][i],  // Case 2
    #                 T[s][t][i - 1])         // Case 3
    #
    # Where,
    #   Case j: Add A[i - 1] to the j-th part
    #
    # Initial conditions:
    #   T[0][0][i] = 1
    #
    tot = sum(A)
    tgt = tot // 3
    if tot % 3 != 0 or len(A) < 3:
        return 0
    T = [[[0] * (len(A) + 1) for _ in range(tgt + 1)]
         for _ in range(tgt + 1)]
    for i in range(len(A) + 1):
        T[0][0][i] = 1
    for s in range(0, tgt + 1):
        for t in range(0, tgt + 1):
            if s + t == 0: continue
            for i in range(1, len(A) + 1):
                T[s][t][i] = T[s][t][i - 1]
                if A[i - 1] <= s:
                    T[s][t][i] = T[s][t][i] or T[s - A[i - 1]][t][i - 1]
                if A[i - 1] <= t:
                    T[s][t][i] = T[s][t][i] or T[s][t - A[i - 1]][i - 1]
    return T[-1][-1][-1]


def partition3_bruteforce(A):
    '''Is it possible to partition the given values into 3 equal piles?

    Examples:
    >>> partition3([3, 3, 3, 3])
    0
    >>> partition3([40])
    0
    >>> partition3([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59])
    1
    >>> partition3([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25])
    1

    '''
    # Bruteforce
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1
    return 0


partition3 = partition3_dynprog


def main():
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))


if __name__ == '__main__':
    main()

