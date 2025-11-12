def delete_first_three(l: list) -> None:
    '''
    Given a list, delete the first three elements in the list.
    Arguments:
    l: list - a list of elements.
    Return: None - the list is modified in place.
    '''
    if len(l) < 3:
        l.clear()

    else :
        del l[:3]