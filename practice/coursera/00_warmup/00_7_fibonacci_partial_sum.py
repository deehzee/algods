# Uses python3


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def get_fibonacci_period(k):
    P = [0]
    a, b = 0, 1
    while (a, b) != (1, 0):
        P.append(b)
        a, b = b, (a + b) % k
    return P


def fibonacci_partial_sum(m, n):
    P = get_fibonacci_period(10)
    per = len(P)
    return (P[(n + 2) % per] - P[(m + 1) % per]) % 10


if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fibonacci_partial_sum(m, n))

