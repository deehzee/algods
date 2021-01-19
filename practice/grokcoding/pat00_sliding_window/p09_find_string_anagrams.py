"""
Problem
=======
Given a string and a pattern, find all anagrams of the pattern in the given
string.

Example #1
----------
Input: s="ppqp", pattern="pq"
Output: [1, 2]
Explanation: Thw two anagrams are 'pq' and 'qp' appearing at indices 1 and 2.

Example #2
----------
Input: s="abbcabc",
k = "abc"
Output: [2, 3, 4]
Explanation: The three anagrams are "bca", "cba" and "abc" at indices 1, 3 and
4 respectively.

"""

def find_string_anagrams(s, pattern):
    """Find all anagrams of pattern in the given string, s.

    >>> find_string_anagrams("ppqp", "pq")
    [1, 2]

    >>> find_string_anagrams("abbcabc", "abc")
    [2, 3, 4]


    """
    results = []
    k = len(pattern)
    if k > len(s):
        return results
    counts = {}
    for c in pattern:
        counts[c] = counts.get(c, 0) + 1
    matched = 0
    win_start = 0
    for win_end, next_char in enumerate(s):
        if next_char in counts:
            counts[next_char] -= 1
            if counts[next_char] == 0:
                matched += 1
        if win_end >= k - 1:
            if matched == len(counts):
                results.append(win_start)
            first_char = s[win_start]
            if first_char in counts:
                if counts[first_char] == 0:
                    matched -= 1
                counts[first_char] += 1
            win_start += 1
    return results


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

