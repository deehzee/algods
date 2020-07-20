#Uses python3
from functools import cmp_to_key
import random


def compare(x, y):
    for i in range(min(len(x), len(y))):
        if x[i] > y[i]:
            return -1
        elif x[i] < y[i]:
            return 1
    for i in range(min(len(x), len(y))):
        if x[-(i + 1)] > y[-(i + 1)]:
            return -1
        elif x[-(i + 1)] < y[-(i + 1)]:
            return 1
    return 0


def compare1(x, y):
    s, t = f'{x}{y}', f'{y}{x}'
    if s < t:
        return 1
    elif s > t:
        return -1
    return 0


def largest_number(a):
    res = ''
    a = sorted(a, key=cmp_to_key(compare1))
    for x in a:
        res += x
    return res


def generate_inputs():
    n = random.randint(3, 10)
    a = []
    for _ in range(n):
        k = random.randint(1, 3)  # num of digits
        x = random.randrange(10 ** k)
        a.append(str(x))
    return a


if __name__ == '__main__':
    n = int(input())
    a = input().split()
    print(largest_number(a))

    # random.seed(42)
    # for i in range(5):
        # a = generate_inputs()
        # print(a)
        # print(largest_number(a))
        # print()


