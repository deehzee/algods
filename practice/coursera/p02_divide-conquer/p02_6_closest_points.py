#Uses python3
from collections import namedtuple
from datetime import timedelta
import functools
import math
import random
import sys
import time

Point = namedtuple('Point', 'x y')

### Solution 0: Brute-force ###
# O(n^2)


def sq_dist(p, q):
    return (p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y)


def __min_sq_dist_brute_force(points):
    d_min = float('inf')
    for i, p in enumerate(points):
        for q in points[i + 1:]:
            d_min = min(d_min, sq_dist(p, q))
    return d_min


def min_distance_brute_force(points):
    return math.sqrt(__min_sq_dist_brute_force(points))


### Solution 1: Divide and Conquer ###
# O(n log n)


def min_distance_divide_conquer(points):
    Px = sorted(points, key=lambda p: p.x)
    Py = sorted(points, key=lambda p: p.y)
    m = __closest_pair_sq_dist(Px, Py)
    return math.sqrt(m)


def __closest_pair_sq_dist(Px, Py):
    if len(Px) <= 4:
        return __min_sq_dist_brute_force(Px)
    Qx, Rx = Px[:len(Px) // 2], Px[len(Px) // 2:]
    sQx = set(Qx)
    Qy, Ry = [], []
    for p in Py:
        if p in sQx:
            Qy.append(p)
        else:
            Ry.append(p)
    d1 = __closest_pair_sq_dist(Qx, Qy)
    d2 = __closest_pair_sq_dist(Rx, Ry)
    d = min(d1, d2)
    d3 = __closest_split_pair_sq_dist(Px, Py, d)
    return min(d, d3)


def __closest_split_pair_sq_dist(Px, Py, d):
    x0 = max(p.x for p in Px[:len(Px) // 2])
    Sy = [q for q in Py if x0 - d <= q.x <= x0 + d]
    d_min = d
    # Sp = [q for q in Sy if q.x == x0]
    # for q1, q2 in zip(Sp[:-1], Sp[1:]):
        # d_min = min(d_min, sq_dist(q1, q2))
    for j in range(1, 8):
        for q1, q2 in zip(Sy[:-j], Sy[j:]):
            d_min = min(d_min, sq_dist(q1, q2))
    return d_min


### Random Test ###


def timer(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        start_t = time.perf_counter()
        value = func(*args, **kwargs)
        end_t = time.perf_counter()
        run_t = end_t - start_t
        return run_t, value
    return wrapped_func


def random_input(maxlen=20, maxnum=20):
    n = random.randint(1, maxlen)
    points = [
        Point(random.randint(1, maxnum), random.randint(1, maxnum))
        for _ in range(n)
    ]
    return points


def run_tests(maxlen=10, maxnum=10, seed=42):
    random.seed(seed)
    brute_force = timer(min_distance_brute_force)
    divide_conquer = timer(min_distance_divide_conquer)
    bf_t = dc_t = 0
    n  = 0
    try:
        while True:
            n += 1
            P = random_input(maxlen=maxlen, maxnum=maxnum)
            t1, ans1 = brute_force(P)
            t2, ans2 = divide_conquer(P)
            bf_t += t1
            dc_t += t2
            if abs(ans1 - ans2) > 1e-9:
                print(f'Failed test#{n}')
                print(P)
                print(f'ans1={ans1}\nans2={ans2}')
                break
    except KeyboardInterrupt:
        print(f'Passed: {n}')
        bf_t, dc_t = timedelta(seconds=bf_t), timedelta(seconds=dc_t)
        print(f'Time taken by brute force:    {bf_t}')
        print(f'Time taken by divide conquer: {dc_t}')


### Main ###


minimum_distance = min_distance_divide_conquer


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    xs = data[1::2]
    ys = data[2::2]
    points = [Point(x, y) for x, y in zip(xs, ys)]
    print("{0:.9f}".format(minimum_distance(points)))


if __name__ == '__main__':
    main()

