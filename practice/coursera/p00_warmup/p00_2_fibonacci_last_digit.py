# Uses python3


def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % 10
    return b


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))

