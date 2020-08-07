def merge(nums1, m, nums2, n):
    '''
    88. Merge Sorted Array
    ======================
    Given two arrays nums1 and nums2, merge them into nums1.
    nums1 has extra space padded with zeros.

    Example
    -------
    >>> nums1 = [1, 2, 3, 0, 0, 0]
    >>> nums2 = [2, 5, 6]
    >>> merge(nums1, nums2)
    >>> all(nums1[i] <= nums1[i + 1] for i in range(len(nums1) - 1))
    True

    '''
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
    if j >= 0:
        nums1[:k + 1] = nums2[:j + 1]
    return nums1

