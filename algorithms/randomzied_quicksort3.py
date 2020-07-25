import random


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

