"""
Problem
=======
Given two nonnegative numbers `num1` and `num2` represented as strings,
return the sum of the two as a string.

* Both numbers only contain digits 0-9.
* Don't use any built-in big-integer or convert input strings to integer
  directly.

Examples:
---------
>>> add_strings('1', '9')
'10'

>>> add_strings('123', '7')
'130'

>>> add_strings('2994', '49832')
'52826'

"""


def add_strings(num1, num2):
    res = []
    carry = 0
    i1, i2 = len(num1) - 1, len(num2) - 1
    while i1 >= 0 or i2 >= 0:
        d1 = ord(num1[i1]) - ord('0') if i1 >= 0 else 0
        d2 = ord(num2[i2]) - ord('0') if i2 >= 0 else 0
        carry, digit = divmod(d1 + d2 + carry, 10)
        res.append(digit)
        i1, i2 = i1 - 1, i2 - 1
    if carry > 0:
        res.append(carry)
    return ''.join(str(d) for d in res[::-1])


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

