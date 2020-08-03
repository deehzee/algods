# Uses python3
import sys


def knapsack_wo_rep(capacity, weights, values):
    '''Discrete knapsack without repetition.

    Example:
        >>> knapsack_wo_rep(10, [6, 3, 4, 2], [30, 14, 16, 9]):
        46

    '''
    # T[i][u] = opt value of knapasack with capacity u and first i items
    T = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):
        for u in range(1, capacity + 1):
            T[i][u] = T[i - 1][u]
            if weights[i - 1] <= u:
                T[i][u] = max(
                    T[i][u],
                    T[i - 1][u - weights[i - 1]] + values[i - 1],
                )
    return T[-1][-1]


def optimal_weight1(capacity, weights):
    '''Take the maximum number of gold bars possible.

    Example:
    --------
    >>> optimal_weight1(10, [1, 4, 8])
    9

    '''
    return knapsack_wo_rep(capacity, weights, weights)


def optimal_weight0(W, w):
    # Greedy apprach: Doesn't work
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


optimal_weight = optimal_weight1


def main():
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))


if __name__ == '__main__':
    main()

