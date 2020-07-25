# Uses python3
from collections import Counter
import random
import sys


def get_majority_element1(a, left, right):
    if left == right:
        return -1
    elif left + 1 == right:
        return left
    half = (right - left) // 2
    mid = (left + right) // 2
    i = get_majority_element1(a, left, mid)
    if i != -1 and sum(a[i] == x for x in a[left:right]) > half:
        return i
    j = get_majority_element1(a, mid, right)
    if j != -1 and sum(a[j] == x for x in a[left:right]) > half:
        return j
    return -1


def get_majority_element2(a, left, right):
    counts = Counter(a)
    half = (right - left) // 2
    for x in counts:
        if counts[x] > half:
            return 1
    return -1


def generate_random_input(maxlen=10, maxnum=20):
    n = random.randint(1, maxlen)
    if random.random() < 0.5:
        # Generate inpute with majority element
        k = random.randint(n // 2 + 1, n)
        x = random.randint(1, maxnum)
        a1 = ([x for _ in range(k)])
        a2 = [random.randrange(1, maxnum + 1) for _ in range(n - k)]
        a = a1 + a2
        random.shuffle(a)
    else:
        a = [random.randrange(1, maxnum) for _ in range(n)]
    return a


def random_tests(seed=None, maxlen=10, maxnum=20):
    if seed is not None:
        random.seed(seed)
    n = 0
    try:
        while True:
            n += 1
            a = generate_random_input(maxlen=maxlen, maxnum=maxnum)
            ans1 = (get_majority_element1(a, 0, len(a)) != -1)
            ans2 = (get_majority_element2(a, 0, len(a)) != -1)
            if ans1 != ans2:
                print(f'Test[{n}]: {a}')
                print(f'ans1 = {ans1}')
                print(f'ans2 = {ans2}')
                break
    except KeyboardInterrupt:
        print(f'Passed: {n}')


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element1(a, 0, n) != -1:
        print(1)
    else:
        print(0)
    # random_tests(seed=42)

