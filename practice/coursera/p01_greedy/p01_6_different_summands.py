# Uses python3


def optimal_summands(n):
    summands = []
    cur = 0
    while n > 0:
        prv, cur = cur, cur + 1
        if cur >= n - cur:
            cur = n
        summands.append(cur)
        n -= cur
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
    print()

