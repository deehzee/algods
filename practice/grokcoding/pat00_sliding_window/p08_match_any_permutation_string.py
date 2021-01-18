"""
Problem:
========
Given a string and a patter, find out if the string contains sny permutation
of the pattern.

Example #1
----------
Input: s="oidbcaf", p="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of "abc".

Example #2
----------
Input: s="odicf", p="dc"
Output: false
Explanation: No permutation of "dc" is present in "odicf" as a substring.

Example #3
----------
Input: s="bcdxabcdy", p="bcdyabcdx"
Output: true
Explanation: The string and the pattern are a permutation of each other.

Example #4
----------
Input: "aaacb", p="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of "abc".

"""


def find_permutation(s,  pattern):
    """Find presence of any permutation of pattern in the text as a substring.

    >>> find_permutation("oidbcaf", "abc")
    True

    >>> find_permutation("odicf", "dc")
    False

    >>> find_permutation("bcdxabcdy", "bcdxabcdy")
    True

    >>> find_permutation("aaacb", "abc")
    True

    """
    k = len(pattern)
    if k > len(s):
        return False
    count = {}
    for c in pattern:
        count[c] = count.get(c, 0) + 1

    matches = 0
    win_start = 0
    for win_end, next_char in enumerate(s):
        if next_char in count:
            count[next_char] -= 1
            if count[next_char] == 0:
                matches += 1
        if win_end >= k - 1:
            if matches == len(count):
                return True
            first_char = s[win_start]
            if first_char in count:
                if count[first_char] == 0:
                    matches -= 1
                count[first_char] += 1
            win_start += 1
    return False


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

