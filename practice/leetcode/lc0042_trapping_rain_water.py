def trap(heights):
    '''
    42. Trapping Rain Water
    =======================

    Given n non-negative integers representing an elevation map
    where the width of each bar is 1, compute how much water it
    is able to trap after raining

    Example:
    --------
    >>> trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    6

    '''
    if not heights:
        return 0
    fmax = heights[0]
    bmax = heights[-1]
    fmaxs = [0] * len(heights)
    bmaxs = [0] * len(heights)
    fmaxs[0] = fmax
    bmaxs[-1] = bmax
    for i in range(1, len(heights)):
        fmax = max(fmax, heights[i])
        bmax = max(bmax, heights[-(i + 1)])
        fmaxs[i] = fmax
        bmaxs[-(i + 1)] = bmax
    total = sum(min(f, b) for f, b in zip(fmaxs, bmaxs))
    water = total - sum(heights)
    return water


if __name__ == '__main__':
    import doctest
    doctest.testmod()

