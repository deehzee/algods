"""
Description
===========
Given a string, find the length of the longest substring with no repeating
characters.

Example #1
----------
Input:  s="aabccbb"
Output: 3
Explantion: The longest such substring is "abc".

Example #2
----------
Input:  s="abbbb"
Output: 2
Explanation: The longest such substring is "ab".

Example #3
----------
Input:  s="abccde"
Output: 3
Explanation: Longest substrings with no repeating characters are "abc"
    and "cde".

"""


def non_repeat_substring(s):
    """Find the length of the longest substring with no repeating characters.

    Time:  O(n)
    Space: O(1) // size of the alphabet for the set

    >>> non_repeat_substring("")
    0
    >>> non_repeat_substring("a")
    1
    >>> non_repeat_substring("aabccbb")
    3
    >>> non_repeat_substring("abbbb")
    2
    >>> non_repeat_substring("abccde")
    3

    """
    win_start = 0
    chars = set()
    max_len = 0
    for win_end in range(len(s)):
        last_char = s[win_end]
        while last_char in chars:
            first_char = s[win_start]
            chars.remove(first_char)
            win_start += 1
        chars.add(last_char)
        max_len = max(max_len, len(chars))
    return max_len


def non_repeat_substring1(s):
    """Find the length of the longest substring with no repeating characters.

    Time:  O(n)
    Space: O(1) // size of the alphabet for the set

    >>> non_repeat_substring1("")
    0
    >>> non_repeat_substring1("a")
    1
    >>> non_repeat_substring1("aabccbb")
    3
    >>> non_repeat_substring1("abbbb")
    2
    >>> non_repeat_substring1("abccde")
    3

    """
    win_start = 0
    char_index = {}
    max_len = 0
    for win_end in range(len(s)):
        last_char = s[win_end]
        if last_char in char_index:
            win_start = max(win_start, char_index[last_char] + 1)
        char_index[last_char] = win_end
        max_len = max(max_len, win_end - win_start + 1)
    return max_len


if __name__ == '__main__':
    import doctest
    doctest.testmod()

