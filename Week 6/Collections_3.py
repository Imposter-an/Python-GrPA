def in_exactly_one(l1: list, l2: list) -> set:
    '''
    Given two lists, return a list containing the items
    that are present in either list but not in both.

    Arguments:
    l1: list - the first list
    l2: list - the second list

    Return:
    set - a set containing the items present in either list 1 or list 2 but not in both

    Example:
    >>> in_exactly_one([1, 2, 3], [3, 4, 5])
    {1, 2, 4, 5}
    '''
    set1 = set(l1)
    set2 = set(l2)

    # Return the symmetric difference (items in either set but not in both)
    return set1 ^ set2
