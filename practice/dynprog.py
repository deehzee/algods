'''Dynamic programming examples'''

### Longest Increasoing Subsequence ###


def lis(A):
    '''Longest increasing subsequence

    Example:
        >>> lis([7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3])
        5
    '''
    T = [1] * len(A)
    maxlen = 0
    for i in range(len(A)):
        for j in range(i):
            if A[j] < A[i]:
                T[i] = max(T[i], T[j] + 1)
        maxlen = max(maxlen, T[i])
    return maxlen


def lis_bruteforce(A, seq_len, last_index):
    if last_index == -1:
        last_element = float('-inf')
    else:
        last_element = A[last_index]
    result = seq_len
    for i in range(last_index + 1, len(A)):
        if A[i] > last_element:
            result = max(result, lis(A, seq_len + 1, i))
    return result


def lis_demo1(A):
    '''Longest increasing subsequence - returns the length, the
    indices, and the values of a longest common subsequence.

    Example:
        >>> lis_demo([7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3])
        (5, [1, 3, 5, 9, 11], [2, 3, 4, 6, 9])
    '''
    T = [1] * len(A)
    prev = [-1] * len(A)
    maxlen = 0
    end = -1
    for i in range(len(A)):
        for j in range(i):
            if A[j] < A[i] and T[j] + 1 > T[i]:
                T[i] = T[j] + 1
                prev[i] = j
        if T[i] > maxlen:
            maxlen = T[i]
            end = i
    cur = end
    ilis = []
    while cur >= 0:
        ilis.append(cur)
        cur = prev[cur]
    ilis = list(reversed(ilis))
    lis = [A[i] for i in ilis]
    return maxlen, ilis, lis


def lis_demo2(A):
    '''Longest increasing subsequence - returns the length, the
    indices, and the values of a longest common subsequence.

    Example:
        >>> lis_demo([7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3])
        (5, [2, 3, 5, 10, 11], [1, 3, 4, 5, 9])
    '''
    T = [1] * len(A)
    maxlen = 0
    for i in range(len(A)):
        for j in range(i):
            if A[j] < A[i] and T[j] + 1 > T[i]:
                T[i] = T[j] + 1
        if T[i] > maxlen:
            maxlen = T[i]
    ilis = []
    last = maxlen
    for i in reversed(range(len(A))):
        if T[i] == last:
            ilis.append(i)
            last -= 1
    ilis = list(reversed(ilis))
    lis = [A[i] for i in ilis]
    return maxlen, T, ilis, lis


### Edit Distance ###


def edit_distance(s, t):
    '''Find edit distance of two strings.

    Example:
        >>> eidt_distance('editing', 'distnace')
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
                T[i-1][j] + 1, #delettion
                T[i][j-1] + 1, #insertion
                T[i-1][j-1] + (s[i-1] != t[j-1]) #substitution or match
            )
    return T[-1][-1]


def knapsack_w_rep(capacity, weights, values):
    '''Discrete knapsack with repetition.

    Example:
        >>> knapsack_w_rep(10, [6, 3, 4, 2], [30, 14, 16, 9]):
        48

    '''
    assert len(weights) == len(values)
    T = [0] * (capacity + 1)
    for u in range(1, capacity + 1):
        for i in range(len(weights)):
            if weights[i] <= u:
                T[u] = max(T[u], T[u - weights[i]] + values[i])
    return T[-1]


def knapsack_w_rep_bruteforce(capacity, weights, values, items):
    weight = sum(weights[i] for i in items)
    value = sum(values[i] for i in items)
    for i in range(len(weights)):
        if weight + weights[i] <= capacity:
            value = max(value, knapsack(capacity, weights, values, items + [i]))
    return value


def knapsack_wo_rep(capacity, weights, values):
    '''Discrete knapsack without repetition.

    Example:
        >>> knapsack_wo_rep(10, [6, 3, 4, 2], [30, 14, 16, 9]):
        46

    '''
    T = [[0] * (len(weights) + 1) for _ in range(capacity + 1)]
    for u in range(1, capacity + 1):
        for i in range(1, len(weights) + 1):
            T[u][i] = T[u][i - 1]
            if weights[i - 1] <= u:
                T[u][i] = max(
                    T[u][i],
                    T[u - weights[i - 1]][i - 1] + values[i - 1],
                )
    return T[-1][-1]


def knapsack_wo_rep_bruteforce(capacity, weights, values, items, last):
    weight = sum(weight[i] for i in items)
    if last == len(weights) - 1:
        return sum(values[i] for i in items)
    value = knapsack_wo_rep_bruteforce(
        capacity, weights, values, items, last + 1)
    if weight + weights[last + 1] <= capacity:
        value = max(value, knapsack_wo_rep_bruteforce(
            capacity, weights, values, items + [last + 1], last + 1))
    return value


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


def lcs3(a, b, c):
    '''Longest common subsequence of three sequences

    Examples
    --------
    >>> lcs3([1, 2, 3], [2, 1, 3], [1, 3, 5])
    2
    >>> lcs3([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7])
    3

    '''
    T = [[[0] * (len(c) + 1) for _ in range(len(b) + 1)]
         for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(c) + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    T[i][j][k] = 1 + T[i - 1][j - 1][k - 1]
                else:
                    T[i][j][k] = max(
                        T[i][j][k - 1], T[i][j - 1][k], T[i - 1][j][k]
                    )
    return T[-1][-1][-1]


def partition2(A):
    '''Is it possible to divide the values into two eaual piles?

    Examples:
    ---------
    >>> partition2([1, 1, 2])
    1
    >>> partition2([1, 1, 4])
    0
    >>> partition2([3, 1, 1, 2, 2, 1])
    1

    '''
    tot = sum(A)
    tgt = tot // 2
    if tot % 2 != 0 or len(A) < 2:
        return 0
    T = [[0] * (len(A) + 1) for _ in range(tgt + 1)]
    for i in range(len(A) + 1):
        T[0][i] = 1
    for s in range(1, tgt + 1):
        for i in range(1, len(A) + 1):
            T[s][i] = T[s][i - 1]
            if A[i - 1] <= s:
                T[s][i] = T[s][i] or T[s - A[i - 1]][i - 1]
    return T[-1][-1]


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


def partition3_dynprog(A):
    '''Is it possible to partition the given values into 3 equal piles?

    Examples:
    >>> partition3_dynprog([3, 3, 3, 3])
    0
    >>> partition3_dynprog([40])
    0
    >>> partition3_dynprog([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59])
    1
    >>> partition3_dynprog([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25])
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


