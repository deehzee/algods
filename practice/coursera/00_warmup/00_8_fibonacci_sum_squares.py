# Uses python3


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def pisano_period(k):
    P = [0]
    a, b = 0, 1
    while (a, b) != (1, 0):
        P.append(b)
        a, b = b, (a + b) % k
    return P


def fibonacci_sum_squared(n):
    P = pisano_period(10)
    per = len(P)
    return (P[n % per] * P[(n + 1) % per]) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squared(n))

