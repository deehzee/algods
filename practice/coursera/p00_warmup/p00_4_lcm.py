# Uses python3


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    d = gcd(a, b)
    return (a // d) * b


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

