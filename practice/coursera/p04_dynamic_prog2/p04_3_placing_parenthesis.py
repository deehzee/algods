# Uses python3


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False, 'Unsupported operator'


def get_max_value(dataset):
    '''Placing paretheses for maximum arithmetic values.

    Examples:
    ---------
    >>> get_max_value('1+5')
    6
    >>> get_max_value('5-8+7*4-8+9')
    200

    How to solve:
    -------------
    digits: d[0..n]
    ops: ops[0..(n-1)]  // op is one of {+, -, *}

    max(`d[0] op[0] d[1] ... op[n-1] d[n]')

    M[i][j] = max(`d[0] op[0] d[1] ... op[j-1] d[j]')
    m[i][j] = min(`d[0] op[0] d[1] ... op[j-1] d[j]')

    Initial values:
        M[i][i] = d[i]  for all 0 <= i <= n
        m[i][i] = d[i]  for all 0 <= i <= n

    Recurrence:
        M[i][j] = max_{i<=k<=j-1} (
                        M[i][k] op[k] M[k+1][j],
                        M[i][k] op[k] m[k+1][j],
                        m[i][k] op[k] m[k+1][j],
                        m[i][k] op[k] m[k+1][j]
                  )
        Smilarly, for m[i][j] replace "max" by "min".

    '''
    # Parse the input
    digits = list(map(int, dataset[::2]))
    ops = list(dataset[1::2])

    M = [[float('-inf')] * len(digits) for _ in range(len(digits))]
    m = [[float('inf')] * len(digits) for _ in range(len(digits))]

    for i in range(len(digits)):
        M[i][i] = m[i][i] = digits[i]

    # Fill up M and m diagonally up until (0, 1)
    for d in range(1, len(digits)):
        for i in range(len(digits) - d):
            j = i + d
            for k in range(i, j):
                M[i][j] = max(M[i][j],
                              evalt(M[i][k], M[k + 1][j], ops[k]),
                              evalt(M[i][k], m[k + 1][j], ops[k]),
                              evalt(m[i][k], M[k + 1][j], ops[k]),
                              evalt(m[i][k], m[k + 1][j], ops[k]))
                m[i][j] = min(m[i][j],
                              evalt(M[i][k], M[k + 1][j], ops[k]),
                              evalt(M[i][k], m[k + 1][j], ops[k]),
                              evalt(m[i][k], M[k + 1][j], ops[k]),
                              evalt(m[i][k], m[k + 1][j], ops[k]))
    return M[0][-1]


def main():
    print(get_max_value(input()))


if __name__ == "__main__":
    main()

