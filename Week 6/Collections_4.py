
def unique_vowels(s: str) -> set:
    '''
    Given a string, return a set of unique vowels present in the string.

    Arguments:
    s: str - the input string

    Return:
    set - a set of unique vowels present in the string

    Examples:
    >>> unique_vowels('banana treat')
    {'a', 'e'}
    >>> unique_vowels('apple lolipop')
    {'a', 'e', 'i', 'o'}
    >>> unique_vowels('Ian Avinkov')
    {'I','A','a','i','o'}
    '''
    vowels = set('aeiouAEIOU')
    return {char for char in s if char in vowels}
