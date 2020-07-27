# Uses python3

'''
Input: m segments and n points.
Output: For each point, find the number of segments containing the point.

'''
from bisect import bisect_left, bisect_right
from collections import namedtuple
import random
import sys


### Solution 0: Naive ###
# O(mn) time

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


### Solutiom 1: Sort everything ###
# O((m + n)*log(m + n))

Entity = namedtuple('Entity', ['value', 'type', 'idx'])


def fast_count_segments1(starts, ends, points):
    counts = [0 for _ in range(len(points))]
    entities = []
    for i, (s, e) in enumerate(zip(starts, ends)):
        entities.append(Entity(s, '0_start', i))
        entities.append(Entity(e, '2_end', i))
    for j, p in enumerate(points):
        entities.append(Entity(p, '1_point', j))
    entities = sorted(entities)
    n_seg = 0
    for entity in entities:
        if entity.type == '0_start':
            n_seg += 1
        elif entity.type == '1_point':
            counts[entity.idx] = n_seg
        elif entity.type == '2_end':
            n_seg -= 1
    return counts


### Solution 2: Binary search ###
# O((m + n) * log m)


def fast_count_segments2(starts, ends, points):
    counts = [len(starts) for _ in range(len(points))]
    starts = sorted(starts)
    ends = sorted(ends)
    for i, p in enumerate(points):
        counts[i] -= bisect_left(ends, p)
        counts[i] -= len(starts) - bisect_right(starts, p)
    return counts


def bisect_left(a, x):
    left, right = 0, len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


def bisect_right(a, x):
    left, right = 0, len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] > x:
            right = mid
        else:
            left = mid + 1
    return left


### Tests ###


def random_input(maxnsegs=10, maxnpts=10, maxnum=30):
    n_segs = random.randint(1, maxnsegs)
    n_pts = random.randint(1, maxnpts)
    starts, ends, points = [], [], []
    for _ in range(n_segs):
        s = random.randint(0, maxnum)
        e = random.randint(s, maxnum)
        starts.append(s)
        ends.append(e)
    for _ in range(n_pts):
        p = random.randint(0, maxnum)
        points.append(p)
    return starts, ends, points


def run_tests(func1, func2, seed=42):
    random.seed(seed)
    n = 0
    try:
        while True:
            n += 1
            starts, ends, points = random_input()
            ans1 = func1(starts, ends, points)
            ans2 = func2(starts, ends, points)
            if ans1 != ans2:
                print(f'Failed test#{n}:')
                print(f'starts={starts}')
                print(f'ends={ends}')
                print(f'points={points}')
                print(f'ans1={ans1}')
                print(f'ans2={ans2}')
                break
    except KeyboardInterrupt:
        print(f'Passed: {n}')


### Main ###

count_segments = fast_count_segments1


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')


if __name__ == '__main__':
    main()

