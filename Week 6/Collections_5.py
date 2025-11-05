def common_char_sorted_str(s1: str, s2: str) -> str:
    '''Returns a sorted string with unique common charecters present in the given strings.

    Arg:
        s1 (str) : Input string.
        s2 (str) : Input string.

    Returns:
        str: string of unique common charecters arranged in ascending order.

    Examples:
    >>> common_char_sorted_str('apple', 'ball')
    'al'
    >>> common_char_sorted_str('abcde', 'edfci')
    'cde'
    '''
    # Find common characters using set intersection
    common_chars = set(s1) & set(s2)

    # Sort the common characters and join them into a string
    return ''.join(sorted(common_chars))

