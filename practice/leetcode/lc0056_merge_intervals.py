"""
56. Merge Intervals
===================
Given a collection of intervals, merge all overlapping ones.

Examples
--------
1. Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
  Output: [[1, 6], [8, 10], [15, 18]]

2. Input: [[1, 4], [4, 5]]
  Output: [[1, 5]]

"""

def merge_intervals(intervals):
    intervals = sorted(intervals)
    merged  = []    # set of merged intervals
    current = None  # current merged intrval
    for start, end in intervals:
        if not merged or start > current[1]:
            current = [start, end]
            merged.append(current)
        else:
            current[1] = max(current[1], end)
    return merged

