def reverse_first_half(t: tuple) -> tuple:
    '''
    Given an even-length tuple, return a new tuple where the first half 
    is reversed, and the second half remains unchanged.
    Arguments:
    t: tuple - an even-length tuple.
    Return: tuple - a new tuple with the first half reversed.
    '''
    mid_point = len(t) // 2
    first_half = t[:mid_point]
    second_half = t[mid_point:]
    
    # Reverse the first half and combine with unchanged second half
    return first_half[::-1] + second_half