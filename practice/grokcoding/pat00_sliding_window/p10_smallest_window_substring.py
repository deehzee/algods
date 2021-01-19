"""
Problem
=======
Given a string and a pattern, find the smallest substring in the given string
which has all the characters of the given pattern.

Example #1
----------
Input: s="aabdec", pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is
    "abdec".

Example #2
----------
Input: s="abdbcs", pattern="abc"
Output: "bca"

Example #3
----------
Input: s="adcad", pattern="abc"
Output: ""

"""


def find_substring(s, pattern):
    """Given a string and a pattern, find the smallest substring in the given
    string which has all the characters of the given pattern.

    >>> find_substring(s="aabdec", pattern="abc")
    'abdec'
    >>> find_substring(s="abdbca", pattern="abc")
    'bca'
    >>> find_substring(s="adcad", pattern="abc")
    ''

    """
    k = len(pattern)
    pattern_chars = set(pattern)
    counts = {}
    matched = 0
    min_len = 0
    substr = ""
    win_start = 0
    for win_end, next_char in enumerate(s):
        if next_char in pattern_chars and counts.get(next_char, 0) == 0:
            matched += 1
        counts[next_char] = counts.get(next_char, 0) + 1
        first_char = s[win_start]
        while first_char not in pattern_chars or counts[first_char] > 1:
            counts[first_char] -= 1
            win_start += 1
            first_char = s[win_start]
        if matched == len(pattern_chars):
            min_len = min(min_len, win_end - win_start + 1)
            substr = s[win_start:win_end + 1]
    return substr



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

