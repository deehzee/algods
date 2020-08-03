# Uses python3


def edit_distance(s, t):
    '''Find edit distance - insertion, deletion, substitution

    Examples:
    >>> edit_distance('short', 'ports')
    3
    >>> edit_distance('editing', 'distance')
    5

    '''
    T = [[float('inf')] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(len(s) + 1):
        T[i][0] = i
    for j in range(len(t) + 1):
        T[0][j] = j
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            T[i][j] = min(
                T[i - 1][j] + 1,
                T[i][j - 1] + 1,
                T[i - 1][j - 1] + (s[i - 1] != t[j - 1]),
            )
    return T[-1][-1]


def main():
    print(edit_distance(input(), input()))


if __name__ == '__main__':
    main()

