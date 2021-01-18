"""
Description
===========
Given a string with lowercase letters only, if you are allowed to replace
no more than k letters with any letter, find the length of the longest
substring having the same letters after replacement.

Example #1
----------
Input:  s="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c's with 'b' in the substring "bccbb".

Example #2
----------
Input:  s="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' in the substring "bbcb".

Example #3
----------
Input:  s="abccde", k=1
Output: 3
Explanation: Either replace the 'b' with 'c' in the substring 'bcc' or
    replace the 'd' with 'c' in the substring 'ccd'.

"""


def longest_substr_same_letters_after_substt(s, k):
    """Find the length of the longest substring made of only one letter after
    substituting at most k letters by any letters.

    Time:  O(n)
    Space: O(1) # size of the alphabet is constant

    >>> longest_substr_same_letters_after_substt("aabccbb", 2)
    5
    >>> longest_substr_same_letters_after_substt("abbcb", 1)
    4
    >>> longest_substr_same_letters_after_substt("abccde", 1)
    3

    """
    max_len = max_repeat = 0
    win_counts = {}
    win_start = 0
    for win_end in range(len(s)):
        cur_char = s[win_end]
        win_counts[cur_char] = win_counts.get(cur_char, 0) + 1
        max_repeat = max(max_repeat, win_counts[cur_char])
        if (win_end - win_start + 1) - max_repeat > k:
            left_char = s[win_start]
            win_counts[left_char] -= 1
            win_start += 1
        else:
            max_len += 1
    return max_len


if __name__ == '__main__':
    import doctest
    doctest.testmod()

