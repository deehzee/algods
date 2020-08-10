'''
215. kth Largest Element in an Array
====================================

'''

import heapq
import random


def sortselect(nums, k):
    '''
    Examples
    --------
    >>> sortselect([3, 2, 1, 5, 6, 4], 2)
    5
    >>> sortselect([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    4

    '''
    # Sort and return the kth element: O(n log n)
    return sorted(nums)[len(nums) - k]


def heapselect1(nums, k):
    '''
    Examples
    --------
    >>> heapselect1([3, 2, 1, 5, 6, 4], 2)
    5
    >>> heapselect1([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    4

    '''
    # Maintain a min heap of size k: O(n log k)
    q = []
    for n in nums:
        heapq.heappush(q, n)
        if len(q) > k:
            heapq.heappop(q)
    return q[0]


def heapselect2(nums, k):
    '''
    Examples
    --------
    >>> heapselect2([3, 2, 1, 5, 6, 4], 2)
    5
    >>> heapselect2([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    4

    '''
    # Build a maxheap from nums and pull out k times: O(n + k log n)
    q = [x for x in nums]
    heapq.heapify(q)
    for _ in range(len(nums) - k + 1):
        x = heapq.heappop(q)
    return x


def quickselect(nums, k):
    '''
    Examples
    --------
    >>> quickselect([3, 2, 1, 5, 6, 4], 2)
    5
    >>> quickselect([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    4

    '''
    n = len(nums)
    assert n > 0
    assert 0 < k <= n

    if n < 2:
        return nums[0]

    # partiton based on `<=`.
    pivot = randomized_partition(nums, 0, len(nums))
    if n - k == pivot:
        return nums[pivot]
    elif n - k < pivot:
        return quickselect(nums[:pivot], k - n + pivot)
    else:
        return quickselect(nums[pivot + 1:], k)


def randomized_partition(nums, left, right):
    assert right > left
    if right - left == 1:
        return left
    pivot_idx = random.randint(left, right - 1)
    pivot = nums[pivot_idx]
    nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]
    pivot_idx = left
    for i in range(left + 1, right):
        if nums[i] <= pivot:
            pivot_idx += 1
            nums[i], nums[pivot_idx] = nums[pivot_idx], nums[i]
    nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]
    return pivot_idx


### Testing ###


def generate_random_input(maxnum=1000, maxlen=10000):
    n = random.randint(1, maxlen)
    k = random.randint(1, n)
    nums = [random.randint(1, maxnum) for _ in range(n)]
    return nums, k


def verify(nums, k, ans):
    return ans == sorted(nums)[len(nums) - k]


def random_tests(func, maxnum=100, maxlen=1000, n_tests=None, seed=42):
    if seed is not None:
        random.seed(seed)
    n = 1
    try:
        while True:
            if n_tests is not None and n >= n_tests:
                break
            nums, k = generate_random_input(maxnum=maxnum, maxlen=maxlen)
            ans = func(nums, k)
            if not verify(nums, k, ans):
                print(f'Failed test #{n}')
                print('nums =', nums)
                print('k =', k)
                print('ans =', ans)
                print()
                break
            n += 1
    except KeyboardInterrupt:
        print('Passed:', n)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

