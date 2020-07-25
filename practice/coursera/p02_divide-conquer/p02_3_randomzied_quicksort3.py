# Uses python3
import sys
import random


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quicksort2(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quicksort2(a, l, m - 1);
    randomized_quicksort2(a, m + 1, r);


def partition3(a, l, r):
    x = a[l]
    j = k = l
    # invariance: a[l..(j-1)] < x, a[j..k] == x, a[(k+1)..i] > x
    for i in range(l + 1, r + 1):
        if a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]
        elif a[i] < x:
            k += 1
            a[i], a[j], a[k] = a[k], a[i], a[j]
            j += 1
    return j, k


def randomized_quicksort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quicksort3(a, l, m1 - 1);
    randomized_quicksort3(a, m2 + 1, r);


def generate_random_input(maxnum=3, maxlen=15):
    n = random.randint(1, maxlen)
    a = [random.randint(1, maxnum) for _ in range(n)]
    return a


def test_partition2(a, m):
    x = a[m]
    return (
        all(a[i] <= x for i in range(m + 1)) and
        all(a[i] > x for i in range(m + 1, len(a)))
    )


def test_partition3(a, m1, m2):
    x = a[m1]
    return (
        all(a[i] < x for i in range(m1)) and
        all(a[i] == x for i in range(m1, m2 + 1)) and
        all(a[i] > x for i in range(m2 + 1, len(a)))
    )


def random_tests_partition2(seed=None, maxnum=3, maxlen=15):
    if seed is not None:
        random.seed(seed)
    n = 0
    try:
        while True:
            n += 1
            a = generate_random_input(maxnum=maxnum, maxlen=maxlen)
            a1 = a.copy()
            m = partition2(a1, 0, len(a1) - 1)
            if not test_partition2(a1, m):
                print(a)
                print(a1)
                print(m)
                print()
                break
    except KeyboardInterrupt:
        print(f'Passed: {n}')


def random_tests_partition3(seed=None, maxnum=3, maxlen=15):
    if seed is not None:
        random.seed(seed)
    n = 0
    try:
        while True:
            n += 1
            a = generate_random_input(maxnum=maxnum, maxlen=maxlen)
            a1 = a.copy()
            m1, m2 = partition3(a1, 0, len(a1) - 1)
            if not test_partition3(a1, m1, m2):
                print(a)
                print(a1)
                print(m1, m2)
                print()
                break
    except KeyboardInterrupt:
        print(f'Passed: {n}')


def random_tests_quicksort2(seed=None, maxnum=3, maxlen=15):
    if seed is not None:
        random.seed(seed)
    n = 0
    try:
        while True:
            n += 1
            a = generate_random_input(maxnum=maxnum, maxlen=maxlen)
            a1 = a.copy()
            randomized_quicksort2(a1, 0, len(a1) - 1)
            if a1 != sorted(a):
                print(a)
                print(a1)
                print()
                break
    except KeyboardInterrupt:
        print(f'Passed: {n}')


def random_tests_quicksort3(seed=None, maxnum=3, maxlen=15):
    if seed is not None:
        random.seed(seed)
    n = 0
    try:
        while True:
            n += 1
            a = generate_random_input(maxnum=maxnum, maxlen=maxlen)
            a1 = a.copy()
            randomized_quicksort3(a1, 0, len(a1) - 1)
            if a1 != sorted(a):
                print(a)
                print(a1)
                print()
                break
    except KeyboardInterrupt:
        print(f'Passed: {n}')


def main():
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    n = len(a)
    randomized_quicksort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')


if __name__ == '__main__':
    main()
    # random_tests_partition3(seed=42, maxnum=2, maxlen=3)
    # random_tests_quicksort2(seed=42, maxlen=15)

