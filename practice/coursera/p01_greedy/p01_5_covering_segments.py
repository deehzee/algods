# Uses python3
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    segments = sorted(segments, key=lambda s: s.end)
    points = set()
    i, n = 0, len(segments)
    while i < n:
        p = segments[i].end
        points.add(p)
        while i < n and segments[i].start <= p:
            i += 1
    return points


if __name__ == '__main__':
    n = int(input())
    segments = []
    for _ in range(n):
        segments.append(Segment(*map(int, input().split())))
    points = optimal_points(segments)
    print(len(points))
    for point in points:
        print(point, end=' ')
    print()

