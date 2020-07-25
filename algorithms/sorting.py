import random


def randomized_quicksort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    # m1, m2 = partition3(a, l, r)
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
    m1, m2 = j, k

    randomized_quicksort3(a, l, m1 - 1);
    randomized_quicksort3(a, m2 + 1, r);


def test_randomized_quicksort3(maxlen=20, maxnum=20, seed=42):
    n = 0
    try:
        while True:
            n += 1
            a = [random.randint(1, maxnum) for _
                    in range(random.randint(0, maxlen))]
            x = sorted(a)
            y = a.copy()
            randomized_quicksort3(y, 0, len(a) - 1)
            if x != y:
                print(f'Failed test#{n}\n{a}\n{x}\n{y}')
                break
    except KeyboardInterrupt:
        print(f'Passed: {n}')


if __name__ == '__main__':
    test_randomized_quicksort3()

