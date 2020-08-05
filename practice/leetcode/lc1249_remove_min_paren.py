def remove_min_paren(s):
    """
    1249. Minimum Remove to Make Valid Parentheses
    ==============================================

    Given a string s of '(', ')' and lowercase english characters, the
    task is to remove the minimum number of parentheses in any positio so
    that the resulting string has well nested parentheses.

    Examples
    --------
    >>> remove_min_paren('lee(t(c)o)de)')
    'lee(t(c)o)de'

    >>> remove_min_paren('a)b(c)d')
    'ab(c)d'

    >>> remove_min_paren('))((')
    ''

    >>> remove_min_paren('(a(b(c)d)')
    'a(b(c)d)'

    """
    delete = set()
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                delete.add(i)
        else:
            pass
    if stack:
        delete = delete.union(stack)
    return ''.join(c for i, c in enumerate(s) if i not in delete)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

