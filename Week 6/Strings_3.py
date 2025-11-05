def is_palindrome(n: int) -> bool:
    '''Checks if an integer is a palindrome.

    Arguments:
    n: int - the integer to check

    Return:
    bool - True if the integer is a palindrome, False otherwise
    '''
    str_n = str(n)

    return str_n == str_n[::-1]
