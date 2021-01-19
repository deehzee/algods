def twosum_sorted(A, target):
    """Given an array A and a target value, return a two indices such that the
    corresponding sum equals the target.

    [LC-0001]

    Examples:

    >>> twosum_sorted([2, 7, 11, 15], target=9)
    [0, 1]

    >>> twosum_sorted([1, 2, 3, 4, 6], target=6)
    [1, 3]

    >>> twosum_sorted([2, 5, 9, 11], target=11)
    [0, 2]

    """
    left, right = 0, len(A) - 1
    while left < right:
        s = A[left] + A[right]
        if s < target:
            left += 1
        elif s > target:
            right -= 1
        else:
            return [left, right]
    return []


def remove_duplicates_sorted(A):
    """Remove all duplicates in-place from a sorted array, ruturn the new
    length.

    [LC-0026]

    Examples:

    >>> remove_duplicates_sorted([1, 1, 2])
    2

    >>> remove_duplicates_sorted([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    5

    >>> remove_duplicates_sorted([2, 3, 3, 3, 6, 9, 9])
    4

    >>> remove_duplicates_sorted([2, 2, 2, 11])
    2

    """
    read_head = write_head = 0
    prv = None
    while read_head < len(A):
        cur = A[read_head]
        if cur != prv:
            A[write_head] = A[read_head]
            prv = cur
            write_head += 1
        read_head += 1
    return write_head


def square_sorted(A):
    """Given a sorted array, return a new array sorted by the squares of the
    the elements.

    [LC-977]

    Example:

    >>> square_sorted([-4, -1, 0, 3, 10])
    [0, 1, 9, 16, 100]

    >>> square_sorted([-7, -3, 2, 3, 11])
    [4, 9, 9, 49, 121]

    >>> square_sorted([-2, -1, 0, 2, 3])
    [0, 1, 4, 4, 9]

    >>> square_sorted([-3, -1, 0, 1, 2])
    [0, 1, 1, 4, 9]

    """
    left, right = 0, len(A) - 1
    results = [0 for _ in A]
    write_head = len(A) - 1
    while left <= right:
        left_squared = A[left] ** 2
        right_squared = A[right] ** 2
        if left_squared > right_squared:
            results[write_head] = left_squared
            left += 1
        else:
            results[write_head] = right_squared
            right -= 1
        write_head -= 1
    return results


def threesum_zero(A):
    """Given an array of unsorted numbers, find all unique triplets that
    sum up to zero.

    [LC-0015]

    >>> threesum_zero([-3, 0, 1, 2, -1, 1, -2])
    [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]

    >>> threesum_zero([-5, 2, -1, -2, 3])
    [[-5, 2, 3], [-2, -1, 3]]

    >>> threesum_zero([-1, 0, 1, 2, -1, -4])
    [[-1, -1, 2], [-1, 0, 1]]

    >>> threesum_zero([])
    []

    >>> threesum_zero([0])
    []

    """
    A = sorted(A)
    results = []
    for left in range(len(A) - 2):
        if left > 0 and A[left - 1] == A[left]:
            continue
        mid, right = left + 1, len(A) - 1
        while mid < right:
            s = A[left] + A[mid] + A[right]
            if s < 0:
                mid += 1
            elif s > 0:
                right -= 1
            else:
                results.append([A[left], A[mid], A[right]])
                mid += 1
                right -= 1
    return results


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

