def binary_search(a, x):
    left, right = 0, len(a)
    while left < right:
        mid = (left + right) // 2
        if x < a[mid]:
            right = mid
        elif x > a[mid]:
            left = mid + 1
        else:
            return mid
    return -1

