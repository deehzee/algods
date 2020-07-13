#Uses python3


def max_dot_product(a, b):
    a, b = sorted(a), sorted(b)
    ans = 0
    for x, y in zip(a, b):
        ans += x * y
    return ans


if __name__ == '__main__':
    n = int(input())
    a = [int(_) for _ in input().split()]
    b = [int(_) for _ in input().split()]
    print(max_dot_product(a, b))

