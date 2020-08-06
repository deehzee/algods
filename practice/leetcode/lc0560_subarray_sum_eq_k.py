'''
560. Subarray Sum Equals k
==========================
Given an array of integers A and an integer k, find the total number
of contiguous subarrays whose sum is equal to k.

Input Constraints
-----------------
1. 1 <= len(A) <= 20000
2. -1e3 <= a[i] <= 1e3
3. -1e7 <= k <= 1e7

Examples:
---------
# >>> get_num_subarrays([1, 1, 1], 2)
# 2

'''

def sol2(nums, k):
    # Modified bruteforce O(n^2)
    #
    # cumsum[i] = sums(nums[:i], 0 <= i <= len(nums)
    # sum(a[i:j]) == cumsum[j] - cumsum[i]
    #
    cumsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        cumsum[i] = cumsum[i - 1] + nums[i - 1]
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            count += (cumsum[j] - cumsum[i] == k)
    return count


def sol3(nums, k):
    # Eliminate cumsum, same as above, O(n^2)
    count = cumsum_i = 0
    for i in range(len(nums)):
        cumsum_j = cumsum_i
        for j in range(i + 1, len(nums) + 1):
            cumsum_j += nums[j - 1]
            count += (cumsum_j - cumsum_i == k)
        cumsum_i += nums[i]
    return count


def sol4(nums, k):
    # Modify sol3 using dict, O(n)
    # seen[cumsum_i] = times cumsum seen so far
    seen = {}
    count = 0
    cumsum = 0
    for x in nums:
        seen[cumsum] = seen.get(cumsum, 0) + 1
        cumsum += x
        count += seen.get(cumsum - k, 0)
    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()

