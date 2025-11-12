def number_of_unique_common_digits(n1: int, n2: int) -> int:
    '''
    Given two integers, return the number of unique digits that are common in both numbers.
    Eg, 287498,295424 - 2, 4 and 9 are common to both nums so answer is 3
    Arguments:
    n1: int - the first number
    n2: int - the second number
    Return:
    int - the number of unique common digits.
    '''
    # Convert numbers to strings to get individual digits
    digits_n1 = set(str(abs(n1)))
    digits_n2 = set(str(abs(n2)))
    
    # Find intersection of the two sets and return its length
    return len(digits_n1 & digits_n2)