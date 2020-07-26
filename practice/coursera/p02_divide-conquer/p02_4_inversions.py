# Uses python3
import sys


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    mid = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, mid)
    number_of_inversions += get_number_of_inversions(a, b, mid, right)
    number_of_inversions += merge(a, b, left, mid, right)
    return number_of_inversions


def merge(a, b, left, mid, right):
    i, j, k = left, mid, left
    n_invs = 0
    while i < mid and j < right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
            n_invs += mid - i
        k += 1
    while i < mid:
        b[k] = a[i]
        i += 1
        k += 1
    while j < right:
        b[k] = a[j]
        j += 1
        k += 1
    for _ in range(left, right):
        a[_] = b[_]
    return n_invs


def main():
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))


if __name__ == '__main__':
    main()

