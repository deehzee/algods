# Uses python3


def calc_fib(n):
    if (n <= 1):
        return n
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))

