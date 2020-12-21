"""
Description
===========
Given an array with characters where each character represents a fruit
tree, you are given two baskets, and your goal is to put maximum number
of fruits in each basket. The only restriction is that each basket can
have only one type of fruit.

You can start with any tree, but you can't skip any tree once you have
started. You will pick one fruit from each tree until you cannot, i.e.,
you you'll stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the
baskets.

Example #1
----------
Input:  fruits=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: The optimal sequence is ['C', 'A', 'C']

Example #2
----------
Input:  fruits=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: The optimal sequence is ['B', 'C', 'B', 'B', 'C']

"""

def fruit_into_baskets(fruits):
    """Find the maximum contiguous fruits that can be picked with two baskets.

    Time:  O(n)
    Space: O(1)

    >>> fruit_into_baskets(['A', 'B', 'C', 'A', 'C'])
    3
    >>> fruit_into_baskets(['A', 'B', 'C', 'B', 'B', 'C', 'A'])
    5

    """
    fruit_counts = {}
    max_fruits = 0
    win_start = 0
    for win_end in range(len(fruits)):
        last_fruit = fruits[win_end]
        fruit_counts[last_fruit] = fruit_counts.get(last_fruit, 0) + 1
        if len(fruit_counts) > 2:
            first_fruit = fruits[win_start]
            fruit_counts[first_fruit] -= 1
            if fruit_counts[first_fruit] == 0:
                del fruit_counts[first_fruit]
            win_start += 1
        max_fruits = max(max_fruits, win_end - win_start + 1)
    return max_fruits


if __name__ == '__main__':
    import doctest
    doctest.testmod()
