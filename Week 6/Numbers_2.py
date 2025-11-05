def is_ten_digit_even(n):
    '''Checks if a number is a 10 digit even number.

    Also account for negative numbers discarding the sign.

    Args:
        n (int): The given number.

    Returns:
        bool : result as True or False.

    Examples:
    >>> is_ten_digit_even(8769473839)
    False
    >>> is_ten_digit_even(928948)
    False
    >>> is_ten_digit_even(9289479278)
    True
    >>> is_ten_digit_even(-9289479278)
    True
    '''
    

    #write your code below :-


    abs_n = abs(n)
    if abs_n < 1000000000 or abs_n > 9999999999:
        return False
    return abs_n % 2 == 0
