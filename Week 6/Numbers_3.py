def arithmetic_operations(t: tuple) -> tuple:
    '''
    Given a tuple of two integers (a, b), return a tuple containing the
    sum, difference, product, and quotient (integer division) of the two numbers.

    Arguments:
    t: tuple - a tuple of two integers (a, b)

    Return:
    tuple - a tuple containing the sum, difference, product, and quotient

    Example:
    >>> arithmetic_operations((1, 2))
    (3, -1, 2, 0)
    '''
    a, b = t

    sum_result = a + b
    difference = a - b
    product = a * b
    quotient = a // b  # Integer division

    return (sum_result, difference, product, quotient)
