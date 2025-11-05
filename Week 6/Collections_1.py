def rotate_list(lst: list, k: int) -> list:
    '''
    Given a list of items and an integer k, rotate the list to the right by k steps.


    Arguments:
    lst: list - a list of items
    k: int - the number of steps to rotate the list to the right

    Return:
    list - the rotated list
    '''
    if not lst:
        return lst

    # Handle cases where k is larger than the list length
    n = len(lst)
    k = k % n

    # If k is 0, no rotation needed
    if k == 0:
        return lst

    # Rotate by taking the last k elements and putting them at the front
    return lst[-k:] + lst[:-k]