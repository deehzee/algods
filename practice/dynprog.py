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
    '''Discrete knapsack with repetition.

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


