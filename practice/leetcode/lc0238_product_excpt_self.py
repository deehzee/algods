def product_except_self(A):
    '''
    238. Product of Array Except Self
    =================================
    Given an array A of n integers (n > 1), return an array where the i-th
    element is the product of all but the i-th element of A.

    Restrictions:
    -------------
    1. Don't use division
    2. Use constant extra space.

    Example:
    --------
    >>> product_except_self([1, 2, 3, 4])
    [24, 12, 8, 6]

    '''
    out = [1] * len(A)
    # Backward pass: out[-(i + 1)] = prod(A[-1]..A[-i])
    for i in range(1, len(A)):
        out[-(i + 1)] = out[-i] * A[-i]
    # Forward pass
    lprod = 1
    for i in range(1, len(A)):
        lprod *= A[i - 1]
        out[i] *= lprod
    return out

