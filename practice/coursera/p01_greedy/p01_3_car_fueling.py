# python3


def compute_min_refills(distance, tank, stops):
    stops = stops.copy()
    stops.insert(0, 0)
    stops.append(distance)
    n_refills = 0
    refill = 0
    cur = 0
    while cur < len(stops) - 1:
        prv = cur
        while cur < len(stops) - 1 and stops[cur + 1] <= stops[refill] + tank:
            cur += 1
        if cur == prv:
            return -1
        if cur < len(stops) - 1:
            n_refills += 1
            refill = cur
    return n_refills


if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = [int(_) for _ in input().split()]
    print(compute_min_refills(d, m, stops))

