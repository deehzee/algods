"""
Description
===========
Given a string, find the length of the longest substring with no more than
k distinct characters.

Example #1
----------
Input:  s='araaci', k=2
Output: 4
Explanation: The longest substring with <= 2 distinct characters is "araa".

Example #2
----------
Input:  s="araaci", k=1
Output: 2
Explanation: The longest substring with <= 1 distinct characters is "aa".

Example #3
----------
Input:  s="cbbebi", k=3
Output: 5
Explanation: Longest substrings with <= 3 distinct characters are "cbbeb"
    and "bbebi".

"""

def longest_substring_with_k_distinct(s, k):
    """Find the length of the longest substr with less than or equal to
    k distinct characters.

    Time:  O(n)
    Space: O(k)

    >>> longest_substring_with_k_distinct("araaci", 2)
    4
    >>> longest_substring_with_k_distinct("araaci", 1)
    2
    >>> longest_substring_with_k_distinct("cbbebi", 3)
    5

    """
    char_counts = {}
    max_len = 0
    win_start = 0
    for win_end in range(len(s)):
        last_char = s[win_end]
        char_counts[last_char] = char_counts.get(last_char, 0) + 1
        while len(char_counts) > k:
            first_char = s[win_start]
            char_counts[first_char] -= 1
            if char_counts[first_char] == 0:
                del char_counts[first_char]
            win_start += 1
        max_len = max(max_len, win_end - win_start + 1)
    return max_len


if __name__ == '__main__':
    import doctest
    doctest.testmod()

