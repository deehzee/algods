# Uses python3


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def get_fibonacci_period(m):
    P = [0]
    prv, cur = 0, 1
    while (prv, cur) != (1, 0):
        P.append(cur)
        prv, cur = cur, (prv + cur) % m
    return P


def fibonacci_sum(n):
    # Sn = F(n+2) - F1
    P = get_fibonacci_period(10)
    return (P[(n + 2) % len(P)] - 1) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
