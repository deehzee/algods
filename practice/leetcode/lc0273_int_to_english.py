def int2words(n):
    '''
    273. Integer to English Words
    =============================
    Convert a non-negative integer to English words.
    Input constraint: n < 2 ** 31 - 1

    Examples
    --------
    >>> int2words(123)
    'One Hundred Twenty Three'

    >>> int2words(12345)
    'Twelve Thousand Three Hundred Fourty Five'

    >>> int2words(1234567)
    'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven'

    >>> out = 'One Billion Two Hundred Thirty Four Million Five Hundred' \
              'Sixty Seven Thousand Eight Hundred Ninety One'
    >>> int2words(1234567891) == out
    True

    '''
    if n == 0:
        return 'Zero'

    words = {
        0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
        6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
        15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
        19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
        50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
        90: 'Ninety'
    }

    if n < 20:
        return words[n]

    if n < 100:
        t, r = divmod(n, 10)
        if r == 0:
            return words[10 * t]
        return f'{words[10 * t]} {int2words(r)}'

    if n < 1000:
        t, r = divmod(n, 100)
        if r == 0:
            return f'{words[t]} Hundred'
        return f'{words[t]} Hundred {int2words(r)}'

    if n < 1000_000:
        t, r = divmod(n, 1000)
        if r == 0:
            return f'{int2words(t)} Thousand'
        return f'{int2words(t)} Thousand {int2words(r)}'

    if n < 1000_000_000:
        t, r = divmod(n, 1000_000)
        if r == 0:
            return f'{int2words(t)} Million'
        return f'{int2words(t)} Million {int2words(r)}'

    t, r = divmod(n, 1000_000_000)
    if r == 0:
        return f'{int2words(t)} Billion'
    return f'{int2words(t)} Billion {int2words(r)}'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

