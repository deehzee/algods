# Uses python3


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_period(m):
    P = [0]
    prv, cur = 0, 1
    while (prv, cur) != (1, 0):
        P.append(cur)
        prv, cur = cur, (prv + cur) % m
    return P


def get_fibonacci_huge(n, m):
    P = get_fibonacci_period(m)
    return P[n % len(P)]


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n, m))

