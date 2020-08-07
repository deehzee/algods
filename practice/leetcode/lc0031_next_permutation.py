def next_permutation1(nums):
    '''
    31. Next Permutation
    ====================
    Find the next permutation in lexicographic order.

    Examples
    --------
    >>> next_permutation1([1, 2, 3])
    [1, 3, 2]
    >>> next_permutation1([3, 2, 1])
    [1, 2, 3]
    >>> next_permutation1([1, 1, 5])
    [1, 5, 1]
    >>> next_permutation1([4, 2, 0, 2, 3, 2, 0])
    [4, 2, 0, 3, 0, 2, 2]

    '''
    for i in reversed(range(len(nums) - 1)):
        for j in reversed(range(i + 1, len(nums))):
            if nums[i] < nums[j]:
                break
        if nums[i] < nums[j]:
            break
    else:
        nums.sort()
        return nums
    nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = sorted(nums[i + 1:])
    return nums


def next_permutation2(nums):
    '''
    31. Next Permutation
    ====================
    Find the next permutation in lexicographic order.

    Examples
    --------
    >>> next_permutation2([1, 2, 3])
    [1, 3, 2]
    >>> next_permutation2([3, 2, 1])
    [1, 2, 3]
    >>> next_permutation2([1, 1, 5])
    [1, 5, 1]
    >>> next_permutation2([4, 2, 0, 2, 3, 2, 0])
    [4, 2, 0, 3, 0, 2, 2]

    '''
    # Idea:
    # Find the smalest largest i, such that A[i] < A[i + 11]
    # Find the largest j > i, such that A[i] < A[j]
    # Swap A[i] <-> A[j]
    # Reverse A[(i + 1):(j + 1)]
    #
    for i in reversed(range(len(nums) - 1)):
        if nums[i] < nums[i + 1]:
            break
    else:
        reverse(nums, 0, len(nums))
        return nums
    for j in reversed(range(i + 1, len(nums))):
        if nums[i] < nums[j]:
            break
    nums[i], nums[j] = nums[j], nums[i]
    reverse(nums, i + 1, len(nums))
    return nums


def reverse(nums, i, j):
    left, right = i, j - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


if __name__ == '__main__':
    import doctest
    doctest.testmod()

