#Uses python3

import sys


def lcs2(a, b):
    '''Longest common subsequence of two arrays

    Examples:
    ---------
    >>> lcs2([2, 7, 5], [2, 5])
    2
    >>> lcs2([7], [1, 2, 3, 4])
    0
    >>> lcs2([2, 7, 8, 3], [5, 2, 8, 7])
    2

    '''
    # Substructure:
    # LCS(i, j) <- lcs between A[:i], B[:j]
    # LCS(i, j) = 1 + LCS(i-1, j-1) if A[i-1] == B[j-1]
    #    = max(LCS(i-1, j), LCS(i, j-1)) if A[i-1] != B[j-1]
    T = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                T[i][j] = 1 + T[i - 1][j - 1]
            else:
                T[i][j] = max(T[i][j - 1], T[i - 1][j])
    return T[-1][-1]


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))


if __name__ == '__main__':
    main()

