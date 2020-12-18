"""
Description
===========
Given a list of intervals (as pairs), return merged intervals. The intervals
are sorted by their start times.

Example
-------
Input:  [(1, 5), (3, 7), (4, 6), (6, 8)]
Output: [(1, 8)]

"""

def merge_intervals(intervals):
    """Merge a list of intervals sorted by the start times.

    Time:  O(n)
    Space: O(1)
    """
    #intervals = sorted(intervals, key=lambda x: x[0])
    result = []
    cur_start, cur_end = None, None
    for interval in intervals:
        start, end = interval
        if cur_start is None:
            cur_start, cur_end = start, end
        elif start <= cur_end:
            if end > cur_end:
                cur_end = end
        else:
            result.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    if cur_start is not None:
        result.append((cur_start, cur_end))
    return result

